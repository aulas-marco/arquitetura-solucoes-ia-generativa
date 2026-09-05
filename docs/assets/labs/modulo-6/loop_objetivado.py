"""Loop objetivado: roda ate o verificador aprovar, com orcamento e sandbox de arquivos."""

from __future__ import annotations

import argparse
import ast
import re
import subprocess
import sys
from pathlib import Path

from langchain_ollama import ChatOllama

MODELO = "qwen2.5-coder:7b"
PASTA = Path("loop-sandbox")
SOLUCAO = PASTA / "solucao.py"
TESTES = PASTA / "test_solucao.py"
MODULOS_PERMITIDOS = {"re"}
NOMES_PROIBIDOS = {"exec", "eval", "open", "__import__", "compile", "input", "globals", "locals"}

ESPECIFICACAO = """\
Escreva a funcao Python `normalizar_pedido(texto: str) -> dict` com este contrato:

- entrada: uma linha no formato "PED-<numero> | item <sku> | qtd <inteiro>";
- o separador pode ter espacos a mais e as palavras podem vir em maiusculas ou minusculas;
- o trecho "qtd <inteiro>" e opcional; quando ausente, a quantidade e 1;
- saida: {"pedido": "<numero como texto>", "item": "<sku em maiusculas>", "quantidade": <int>};
- se a linha nao contiver "PED-<numero>" e "item <sku>", levante ValueError.

Responda SOMENTE com o codigo Python da funcao, dentro de um bloco ```python. \
Nao escreva testes, explicacoes ou exemplos de uso. Pode usar apenas o modulo re.\
"""

SUITE = '''\
import pytest

from solucao import normalizar_pedido


def test_linha_completa():
    assert normalizar_pedido("PED-845 | item P20 | qtd 2") == {
        "pedido": "845", "item": "P20", "quantidade": 2}


def test_espacos_extras_e_caixa_baixa():
    assert normalizar_pedido("  ped-846   |   item p30   |   qtd 5 ") == {
        "pedido": "846", "item": "P30", "quantidade": 5}


def test_quantidade_ausente_vale_um():
    assert normalizar_pedido("PED-847 | item P40") == {
        "pedido": "847", "item": "P40", "quantidade": 1}


def test_sku_alfanumerico():
    assert normalizar_pedido("PED-848 | item ab12 | qtd 3") == {
        "pedido": "848", "item": "AB12", "quantidade": 3}


def test_linha_invalida_levanta_erro():
    with pytest.raises(ValueError):
        normalizar_pedido("pedido sem formato nenhum")
'''

PROMPT_SISTEMA_TESTES = (
    "Voce escreve funcoes Python pequenas e corretas a partir de uma especificacao "
    "e do relatorio de falha dos testes. Responda sempre so com o bloco de codigo."
)

PROMPT_SISTEMA_MODELO = (
    "Voce escreve funcoes Python pequenas e corretas a partir de uma especificacao. "
    "Responda com o bloco de codigo e, na ultima linha, escreva PRONTO quando considerar "
    "a funcao terminada e correta."
)


def extrair_codigo(resposta: str) -> str:
    bloco = re.search(r"```(?:python)?\s*(.*?)```", resposta, re.DOTALL)
    bruto = (bloco.group(1) if bloco else resposta).strip()
    linhas = [linha for linha in bruto.splitlines() if linha.strip().upper() != "PRONTO"]
    return "\n".join(linhas).strip()


def guarda_estatica(codigo: str) -> str:
    """Devolve o motivo da recusa, ou string vazia quando o codigo e aceitavel."""
    try:
        arvore = ast.parse(codigo)
    except SyntaxError as erro:
        return f"o codigo nao compila: {erro.msg} na linha {erro.lineno}"
    for no in ast.walk(arvore):
        if isinstance(no, ast.Import):
            for alias in no.names:
                if alias.name.split(".")[0] not in MODULOS_PERMITIDOS:
                    return f"import proibido no laboratorio: {alias.name}"
        elif isinstance(no, ast.ImportFrom):
            if (no.module or "").split(".")[0] not in MODULOS_PERMITIDOS:
                return f"import proibido no laboratorio: {no.module}"
        elif isinstance(no, ast.Name) and no.id in NOMES_PROIBIDOS:
            return f"chamada proibida no laboratorio: {no.id}"
        elif isinstance(no, ast.Attribute) and no.attr.startswith("__"):
            return f"acesso proibido no laboratorio: {no.attr}"
    if "normalizar_pedido" not in {
        no.name for no in ast.walk(arvore) if isinstance(no, ast.FunctionDef)
    }:
        return "o codigo nao define a funcao normalizar_pedido"
    return ""


def rodar_testes() -> tuple[int, int, str]:
    processo = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-rf", "--tb=line", "test_solucao.py"],
        cwd=PASTA, capture_output=True, text=True, timeout=120,
    )
    saida = processo.stdout + processo.stderr
    passaram = int(m.group(1)) if (m := re.search(r"(\d+) passed", saida)) else 0
    falharam = int(m.group(1)) if (m := re.search(r"(\d+) (?:failed|error)", saida)) else 0
    linhas = [linha.strip() for linha in saida.splitlines() if linha.startswith("FAILED")][:6]
    return passaram, falharam, "\n".join(linhas) or saida.strip()[-400:]


def preparar() -> None:
    PASTA.mkdir(exist_ok=True)
    TESTES.write_text(SUITE, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parada", choices=("testes", "modelo"), default="testes")
    parser.add_argument("--max-iteracoes", type=int, default=8)
    parser.add_argument("--modelo", default=MODELO)
    args = parser.parse_args()

    preparar()
    total_testes = SUITE.count("def test_")
    sistema = PROMPT_SISTEMA_TESTES if args.parada == "testes" else PROMPT_SISTEMA_MODELO
    realimentacao = ""
    realimentacao_anterior = ""
    codigo_anterior = ""
    temperatura = 0.0
    tokens = 0
    parada = "orcamento_esgotado"
    iteracao = 0

    print(f"MODELO: {args.modelo}")
    print(f"CONDICAO_DE_PARADA: {args.parada}")
    print(f"ORCAMENTO: {args.max_iteracoes} iteracoes")
    print(f"VERIFICADOR: pytest com {total_testes} casos, em {TESTES}")
    print()

    for iteracao in range(1, args.max_iteracoes + 1):
        pedido = f"{ESPECIFICACAO}\n\nA suite que decide a parada e esta:\n```python\n{SUITE}```" if not realimentacao else (
            f"{ESPECIFICACAO}\n\nA suite que decide a parada e esta:\n```python\n{SUITE}```"
            f"\n\nSua versao anterior foi esta:\n```python\n{codigo_anterior}\n```"
            f"\n\nEla foi recusada pelo verificador. Relatorio:\n{realimentacao}"
            "\n\nCorrija a funcao e devolva a versao completa."
        )
        modelo = ChatOllama(model=args.modelo, temperature=temperatura)
        resposta = modelo.invoke([("system", sistema), ("human", pedido)])
        tokens += (resposta.usage_metadata or {}).get("total_tokens", 0)
        codigo = extrair_codigo(resposta.content)
        codigo_anterior = codigo

        recusa = guarda_estatica(codigo)
        if recusa:
            realimentacao = f"guarda estatica: {recusa}"
            print(f"ITER {iteracao} | GUARDA: recusado | TESTES: nao executados | "
                  f"TOKENS_ACUM: {tokens}")
            print(f"  MOTIVO: {recusa}")
            continue

        SOLUCAO.write_text(codigo, encoding="utf-8")
        passaram, falharam, detalhe = rodar_testes()
        estagnado = detalhe == realimentacao_anterior
        realimentacao_anterior = detalhe
        realimentacao = detalhe
        if estagnado:
            temperatura = min(temperatura + 0.4, 0.8)
            realimentacao += (
                "\nO verificador devolveu exatamente a mesma falha da iteracao anterior. "
                "Mude a abordagem em vez de repetir a mesma implementacao."
            )
        autodeclarou = "PRONTO" in resposta.content.upper()
        print(f"ITER {iteracao} | GUARDA: aceito | TESTES: {passaram}/{total_testes} | "
              f"AUTODECLAROU_PRONTO: {autodeclarou} | TEMPERATURA: {temperatura:.1f} | "
              f"TOKENS_ACUM: {tokens}")
        if estagnado:
            print("  ESTAGNACAO: mesma falha da iteracao anterior; o arnes diversificou a "
                  f"temperatura para {temperatura:.1f}")
        if detalhe and passaram < total_testes:
            print(f"  PRIMEIRA_FALHA: {detalhe.splitlines()[0][:160]}")

        if args.parada == "testes" and falharam == 0 and passaram == total_testes:
            parada = "meta_atingida"
            break
        if args.parada == "modelo" and autodeclarou:
            parada = "autodeclarada_pelo_modelo"
            break

    passaram, _, _ = rodar_testes() if SOLUCAO.exists() else (0, 0, "")
    print()
    print(f"PARADA: {parada}")
    print(f"ITERACOES: {iteracao}")
    print(f"TOKENS_TOTAIS: {tokens}")
    print(f"VERDADE_FINAL: {passaram}/{total_testes} testes passando")


if __name__ == "__main__":
    main()
