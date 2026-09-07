"""Comparacao de arneses: o mesmo modelo local sob quatro arneses diferentes."""

from __future__ import annotations

import argparse
import re
from typing import TypedDict

from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph

MODELO = "llama3.2:3b"

CATALOGO_AMPLO = {
    "consultar_pedido": "",
    "consultar_pedido_v2": "",
    "buscar_pedido_por_cliente": "",
    "consultar_estoque": "",
    "consultar_estoque_regional": "",
    "reservar_item": "",
    "reservar_item_expresso": "",
    "cancelar_pedido": "",
    "cancelar_item": "",
    "alterar_endereco": "",
    "alterar_entrega": "",
    "abrir_chamado": "",
}

CATALOGO_MINIMO = {
    "consultar_pedido": "devolve a situacao atual de um pedido; nao altera nada",
    "reservar_item": "separa uma unidade de um item para um pedido ja existente",
    "cancelar_pedido": "encerra um pedido inteiro a pedido do cliente",
    "abrir_chamado": "registra uma reclamacao para tratamento humano",
}

PEDIDOS_CONHECIDOS = {"845", "846"}
PEDIDOS_JA_DESPACHADOS = {"845"}

CASOS = [
    ("Quero saber em que pe esta o pedido 845.", "consultar_pedido", "845"),
    ("Separa uma unidade do item P20 para o pedido 845.", "reservar_item", "845"),
    ("Desisti da compra, cancela o pedido 846 por favor.", "cancelar_pedido", "846"),
    ("O produto do pedido 846 chegou quebrado e ninguem me responde.", "abrir_chamado", "846"),
    ("Me confirma se o pedido 846 ja saiu para entrega.", "consultar_pedido", "846"),
    ("Guarda o item P30 do pedido 845 que eu pago amanha.", "reservar_item", "845"),
    ("Nao quero mais nada, encerra o pedido 845.", "abrir_chamado", "845"),
    ("A entrega do pedido 846 atrasou tres semanas e quero falar com um humano.",
     "abrir_chamado", "846"),
]

PROMPT_GENERICO = "Voce e um assistente util de atendimento."

PROMPT_CONTRATUAL = (
    "Voce classifica um pedido de cliente em UMA ferramenta do catalogo. "
    "Responda SOMENTE com um objeto JSON, sem texto antes ou depois, no formato exato: "
    '{"ferramenta": "<nome exatamente como no catalogo>", "pedido": "<numero do pedido>"}. '
    "Nao invente nomes de ferramenta nem numeros de pedido. Nao explique a escolha."
)


class ArnesState(TypedDict, total=False):
    pedido_cliente: str
    catalogo: dict[str, str]
    prompt_sistema: str
    valida: bool
    politica: bool
    verifica: bool
    resposta_bruta: str
    ferramenta: str
    pedido: str
    aceita: bool
    motivo: str
    tentativas: int


def _catalogo_em_texto(catalogo: dict[str, str]) -> str:
    if not any(catalogo.values()):
        return ", ".join(catalogo)
    return "\n".join(f"- {nome}: {descricao}" for nome, descricao in catalogo.items())


def _chamar(state: ArnesState, correcao: str = "") -> str:
    modelo = ChatOllama(model=MODELO, temperature=0)
    humano = (
        f"Catalogo de ferramentas:\n{_catalogo_em_texto(state['catalogo'])}\n"
        f"Pedido do cliente: {state['pedido_cliente']}"
    )
    if correcao:
        humano += f"\nA resposta anterior foi recusada pela validacao. Motivo: {correcao}"
    return modelo.invoke([("system", state["prompt_sistema"]), ("human", humano)]).content


def propor(state: ArnesState) -> ArnesState:
    return {"resposta_bruta": _chamar(state), "tentativas": 1}


def interpretar(state: ArnesState) -> ArnesState:
    texto = state["resposta_bruta"]
    ferramenta = re.search(r'"ferramenta"\s*:\s*"([^"]*)"', texto)
    pedido = re.search(r'"pedido"\s*:\s*"?([0-9]{1,6})"?', texto)
    if ferramenta:
        return {"ferramenta": ferramenta.group(1).strip(),
                "pedido": pedido.group(1) if pedido else ""}
    mencionadas = [nome for nome in state["catalogo"] if nome in texto]
    return {"ferramenta": mencionadas[0] if len(mencionadas) == 1 else "", "pedido": ""}


def validar(state: ArnesState) -> ArnesState:
    if not state.get("valida"):
        return {"aceita": True, "motivo": "arnes sem validacao"}
    ferramenta = state.get("ferramenta", "")
    pedido = state.get("pedido", "")
    if not ferramenta:
        return {"aceita": False, "motivo": "a resposta nao contem o campo ferramenta em JSON"}
    if ferramenta not in state["catalogo"]:
        return {"aceita": False, "motivo": f"a ferramenta {ferramenta} nao existe no catalogo"}
    if pedido not in PEDIDOS_CONHECIDOS:
        return {"aceita": False, "motivo": f"o pedido {pedido or '(vazio)'} nao existe na base"}
    if pedido not in state["pedido_cliente"]:
        return {"aceita": False, "motivo": f"o pedido {pedido} nao aparece na mensagem do cliente"}
    if (state.get("politica") and ferramenta == "cancelar_pedido"
            and pedido in PEDIDOS_JA_DESPACHADOS):
        return {"aceita": False,
                "motivo": (f"o pedido {pedido} ja foi despachado e nao pode ser cancelado pela "
                           "ferramenta; casos assim vao para tratamento humano")}
    return {"aceita": True, "motivo": "proposta dentro do contrato"}


def decidir_retentativa(state: ArnesState) -> str:
    if state.get("verifica") and not state.get("aceita") and state.get("tentativas", 1) < 2:
        return "corrigir"
    return "encerrar"


def corrigir(state: ArnesState) -> ArnesState:
    return {"resposta_bruta": _chamar(state, state.get("motivo", "")),
            "tentativas": state.get("tentativas", 1) + 1}


def build_workflow():
    workflow = StateGraph(ArnesState)
    workflow.add_node("propor", propor)
    workflow.add_node("interpretar", interpretar)
    workflow.add_node("validar", validar)
    workflow.add_node("corrigir", corrigir)
    workflow.add_edge(START, "propor")
    workflow.add_edge("propor", "interpretar")
    workflow.add_edge("interpretar", "validar")
    workflow.add_conditional_edges(
        "validar", decidir_retentativa, {"corrigir": "corrigir", "encerrar": END}
    )
    workflow.add_edge("corrigir", "interpretar")
    return workflow.compile()


ARNESES = {
    "A": {
        "rotulo": "A - arnes nu: prompt generico, catalogo amplo sem descricao, sem validacao",
        "prompt_sistema": PROMPT_GENERICO,
        "catalogo": CATALOGO_AMPLO,
        "valida": False,
        "politica": False,
        "verifica": False,
    },
    "B": {
        "rotulo": "B - contrato de saida: prompt de sistema especifico e esquema validado",
        "prompt_sistema": PROMPT_CONTRATUAL,
        "catalogo": CATALOGO_AMPLO,
        "valida": True,
        "politica": False,
        "verifica": False,
    },
    "C": {
        "rotulo": "C - catalogo minimo: quatro ferramentas descritas em vez de doze nomes",
        "prompt_sistema": PROMPT_CONTRATUAL,
        "catalogo": CATALOGO_MINIMO,
        "valida": True,
        "politica": False,
        "verifica": False,
    },
    "D": {
        "rotulo": "D - verificacao: C mais precondicao de politica, motivo e segunda tentativa",
        "prompt_sistema": PROMPT_CONTRATUAL,
        "catalogo": CATALOGO_MINIMO,
        "valida": True,
        "politica": True,
        "verifica": True,
    },
}


def rodar(chave: str, detalhar: bool) -> None:
    arnes = ARNESES[chave]
    app = build_workflow()
    acertos = recusadas = chamadas = indevidas = 0
    print(f"ARNES: {arnes['rotulo']}")
    print(f"CATALOGO: {len(arnes['catalogo'])} ferramentas")
    for texto, ferramenta_esperada, pedido_esperado in CASOS:
        estado = app.invoke({
            "pedido_cliente": texto,
            "catalogo": arnes["catalogo"],
            "prompt_sistema": arnes["prompt_sistema"],
            "valida": arnes["valida"],
            "politica": arnes["politica"],
            "verifica": arnes["verifica"],
        })
        obtida = estado.get("ferramenta", "")
        pedido = estado.get("pedido", "")
        chamadas += estado.get("tentativas", 1)
        entregue = estado.get("aceita", True)
        correta = entregue and obtida == ferramenta_esperada and pedido == pedido_esperado
        indevida = entregue and obtida == "cancelar_pedido" and pedido in PEDIDOS_JA_DESPACHADOS
        acertos += int(correta)
        recusadas += int(not entregue)
        indevidas += int(indevida)
        if detalhar:
            print(f"  CASO: {texto}")
            print(f"    ESPERADO: {ferramenta_esperada}/{pedido_esperado} | "
                  f"OBTIDO: {obtida or '(nao interpretavel)'}/{pedido or '-'} | "
                  f"TENTATIVAS: {estado.get('tentativas', 1)} | "
                  f"VALIDACAO: {estado.get('motivo', '')}")
    print(f"ACOES_CORRETAS: {acertos}/{len(CASOS)}")
    print(f"BLOQUEADAS_PELA_VALIDACAO: {recusadas}")
    print(f"ACOES_INDEVIDAS_ENTREGUES: {indevidas}")
    print(f"CHAMADAS_AO_MODELO: {chamadas}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--arnes", choices=("A", "B", "C", "D", "todos"), default="todos")
    parser.add_argument("--detalhar", action="store_true")
    args = parser.parse_args()
    print(f"MODELO: {MODELO} (temperature=0; os quatro arneses usam os mesmos pesos)")
    print()
    for chave in (("A", "B", "C", "D") if args.arnes == "todos" else (args.arnes,)):
        rodar(chave, args.detalhar)


if __name__ == "__main__":
    main()
