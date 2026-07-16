# Oficina de ferramentas — workflow, aprovação e efeito simulado

**Objetivo Bloom:** Aplicar e Analisar.

Esta oficina executa um workflow local que separa intenção, aprovação e efeito. Nenhuma chamada alcança CRM, estoque, pedidos ou qualquer sistema externo.

## Ferramenta

**LangGraph** é uma biblioteca open source para definir grafos de estado. O grafo Boreal desta prática tem três resultados explícitos: `aguardando_aprovacao`, `reservado` e `outcome_unknown`.

**Decisão arquitetural em foco:** em que fronteira uma intenção deixa de ser texto proposto e passa a produzir um efeito que exige autorização?

## Pré-requisitos

- Python 3.10 ou superior e terminal.
- Uma pasta descartável e somente os dados sintéticos do laboratório.
- O arquivo `troca_boreal.py` baixado na etapa seguinte.

## Instalação

```bash
mkdir oficina-m4
cd oficina-m4
python -m venv .venv
source .venv/bin/activate
python -m pip install langgraph langchain-ollama
```

No Windows PowerShell, use `.venv\Scripts\Activate.ps1`.

## Preparação do laboratório

Baixe [troca_boreal.py](../assets/labs/modulo-4/troca_boreal.py) para a pasta `oficina-m4`. O arquivo contém um pedido fictício `PED-104`, uma chave de idempotência `TROCA-PED-104-1` e uma reserva simulada `RES-501`.

```bash
ls troca_boreal.py
```

O script é o workflow inteiro: cada nó devolve um estado tipado e o grafo escolhe entre aguardar aprovação ou reservar. Não há ferramenta externa escondida.

## Execução

Primeiro execute sem aprovação:

```bash
python troca_boreal.py --aprovado false
```

Depois execute com aprovação e, por fim, repita a mesma intenção:

```bash
python troca_boreal.py --aprovado true
python troca_boreal.py --aprovado true --repetir
```

## Receita principal

O script percorre o grafo completo e imprime o estado após o nó de aprovação. O resultado `RES-501` é uma confirmação simulada e tipada; ele não é uma frase produzida pelo modelo.

Leia as linhas `ESTADO`, `CHAVE`, `RESULTADO` e `TRACE` de cada execução. Sem aprovação, o estado esperado é `aguardando_aprovacao` e o resultado é “nenhum efeito”. Com aprovação, o estado é `reservado` e o resultado é `RES-501`. Na repetição, o trace declara que não foi criada uma segunda reserva.

## Resultado esperado

Você terá três traces comparáveis: parada segura, efeito simulado aprovado e repetição idempotente. A prática mostra o fluxo de controle, não prova que a autorização de uma organização real está correta.

## Interpretação

Altere apenas o argumento `--aprovado` ou `--repetir`; não modifique a chave de idempotência. Compare o ponto em que o workflow para, o resultado autoritativo e a evidência de repetição. Se uma confirmação tivesse sido interrompida após a intenção, o estado correto seria `outcome_unknown`: a arquitetura deveria consultar o registro pela chave antes de tentar novamente.

## Roteiro sugerido para aula

### Experimento A — intenção sem efeito (Essencial em aula)

**Objetivo:** distinguir proposta e autorização. **Pré-requisito:** script instalado. **Execute:** `--aprovado false`. **Observe:** parada em `aguardando_aprovacao`. **Compare:** pedido em linguagem natural e decisão de escrita.

**Questões exploratórias:**

- Que dado do estado mostra que nenhuma reserva ocorreu?
- Por que um modelo não deve decidir a aprovação por conta própria?
- Onde a identidade e a política entrariam em um sistema real?

### Experimento B — aprovação e idempotência (Exploração em dupla)

**Objetivo:** observar uma escrita simulada e sua repetição. **Pré-requisito:** Experimento A. **Execute:** `--aprovado true` e depois `--repetir`. **Observe:** `RES-501` e trace de repetição. **Compare:** primeira execução e segunda execução.

**Questões exploratórias:**

- Quem deve criar e guardar a chave de idempotência?
- Que falha uma chave duplicada evita?
- Por que a resposta do modelo não substitui o resultado autoritativo?

### Experimento C — resultado desconhecido (Extensão)

**Objetivo:** planejar recuperação após confirmação ausente. **Pré-requisito:** traces anteriores. **Execute:** descreva a interrupção entre intenção e confirmação. **Observe:** o limite entre repetir e reconciliar. **Compare:** retry cego, consulta por chave e escalonamento.

**Questões exploratórias:**

- Que componente deve persistir `outcome_unknown`?
- Qual dado é necessário para reconciliação?
- Quando a revisão humana é um controle obrigatório?

## Evidência a entregar

Entregue as três saídas ou uma tabela equivalente e uma conclusão de até cinco linhas.

| Execução | Estado | Chave | Resultado | O que a arquitetura comprovou? |
|---|---|---|---|---|
| Sem aprovação |  |  |  |  |
| Com aprovação |  |  |  |  |
| Repetição |  |  |  |  |

Explique qual condição impede a reserva, como a repetição é contida e como você trataria `outcome_unknown`.

## Limpeza e contingência

Saia do ambiente com `deactivate` e apague a pasta `oficina-m4` quando terminar. Se houver erro, confira `python --version`, a ativação do ambiente e `python -m pip show langgraph`. Registre a mensagem e corrija a instalação local antes de continuar; não conecte o exercício a sistemas reais.
