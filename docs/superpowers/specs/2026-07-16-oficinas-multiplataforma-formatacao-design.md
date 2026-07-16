# Oficinas multiplataforma e legíveis — desenho

**Data:** 2026-07-16  
**Status:** aprovado para especificação; aguardando revisão do documento antes do plano de implementação.

## Objetivo

Corrigir a leitura dos experimentos e tornar a instalação explícita para macOS, Linux e Windows nas seis oficinas locais.

## Padrão visual dos experimentos

Cada experimento terá o título, a classificação e cinco blocos em linhas independentes:

```markdown
**Objetivo**

Texto curto.

**Pré-requisito**

Condição verificável.

**Execute**

Comando ou ação.

**Observe**

Resultado visível.

**Compare**

Variável e critério de comparação.
```

As questões exploratórias permanecem em lista. Não haverá mais a sequência de rótulos em um único parágrafo. O padrão deve funcionar tanto no tema MkDocs quanto na leitura direta no GitHub.

## Instalação multiplataforma

Toda oficina terá a mesma ordem:

1. verificação comum de terminal e Python;
2. subseção **macOS** com instalação oficial do Ollama quando necessário, ativação de ambiente e nota opcional para Homebrew;
3. subseção **Linux** com instalação oficial do Ollama quando necessário, ativação de ambiente e nota opcional para gerenciadores comuns, sem supor distribuição;
4. subseção **Windows** com PowerShell e ativação adequada;
5. verificação de versões e ferramenta específica do laboratório.

Os módulos que não usam Ollama não pedirão a instalação dele. Python será verificado por `python3 --version` em macOS/Linux e `python --version` no Windows. As receitas usarão `python3` em macOS/Linux e explicarão que `python` é o equivalente Windows; a ativação usará `source .venv/bin/activate` ou `.venv\Scripts\Activate.ps1`.

## Abrangência

- M1: Ollama, modelo local, `curl` e três sistemas operacionais.
- M2: Python, Ollama, LiteLLM Proxy e três sistemas operacionais.
- M3: Python, Ollama, LangChain/Chroma e três sistemas operacionais.
- M4: Python e LangGraph; sem requisito de Ollama para a execução do grafo.
- M5: Python, Ollama e DeepEval.
- M6: Python, Ollama, LiteLLM Proxy e OpenTelemetry.

## Critérios de aceitação

- Os 18 experimentos dos módulos 2 a 6 e os quatro do módulo 1 apresentam rótulos em blocos separados.
- Cada oficina possui instruções distinguíveis para macOS, Linux e Windows.
- Os comandos de verificação aparecem antes da instalação específica.
- O texto não exige Homebrew, `apt`, `dnf` ou outra distribuição Linux específica.
- Testes, validação de conteúdo e construção MkDocs estrita continuam passando.
