# Oficina de ferramentas — avaliar decisões de confiança

**Objetivo Bloom:** Analisar.

Esta oficina avalia 45 casos sintéticos rotulados em duas camadas: métricas que pontuam cada caso e métricas clássicas que descrevem o conjunto. Ela transforma “parece seguro” em rótulos, notas, matriz de confusão e limiar declarado.

## Ferramenta

**DeepEval** é um framework open source para avaliar aplicações de IA. Ele fornece as métricas por caso da [camada 1](conceitos.md#duas-camadas-de-medicao): `PatternMatchMetric`, que compara por regra e não chama modelo nenhum, e as métricas de juiz `GEval`, `AnswerRelevancyMetric` e `PIILeakageMetric`, que usam um **Ollama** local. A camada 2 (acurácia, precisão, recall, F1 e matriz de confusão) é calculada por um script próprio, sem depender do framework. O que cada métrica mede, como se calcula e o que deixa passar está em [Métricas de avaliação](../referencia/metricas-de-avaliacao.md); leia antes de interpretar qualquer número desta oficina.

Cada caso é rotulado com uma de três decisões: [bloquear](conceitos.md#qualidade-tem-varias-dimensoes), corrigir ou [escalar](conceitos.md#qualidade-tem-varias-dimensoes). O conjunto é desbalanceado de propósito, com poucos casos adversariais e muitos pedidos legítimos, porque é assim que a acurácia engana.

**Decisão arquitetural em foco:** como uma equipe registra comportamento esperado, falha observada e hipótese de correção sem reduzir [confiança](conceitos.md#confianca-e-uma-relacao-nao-uma-caracteristica-absoluta) a uma única pontuação?

## Pré-requisitos

- Python 3.10 ou superior, terminal e Ollama instalado.
- Modelo `llama3.2:3b` já baixado com `ollama pull llama3.2:3b`.
- Uma pasta descartável. Os 45 casos fornecidos são sintéticos e não devem ser misturados a conversas reais.
- Orçamento de tempo: a camada 2 roda em segundos sobre respostas pré-geradas. Gerar respostas ao vivo custa cerca de um minuto por caso em máquina sem GPU dedicada, então use `--casos` para limitar a amostra em sala.

## Instalação

O comando de instalação inclui o pacote `ollama` além do `deepeval`: o avaliador usa `OllamaModel` como juiz local, e essa classe só carrega se o pacote `ollama` (cliente Python) estiver instalado — instalar somente `deepeval` falha em tempo de execução com `DeepEvalError: OllamaModel requires the 'ollama' package`.

### macOS

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No Terminal, execute:

```bash
python3 --version
mkdir oficina-m5
cd oficina-m5
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install deepeval ollama
ollama pull llama3.2:3b
```

### Linux

Instale o Ollama pelo procedimento oficial em [ollama.com/download](https://ollama.com/download). No terminal Linux, execute:

```bash
python3 --version
mkdir oficina-m5
cd oficina-m5
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install deepeval ollama
ollama pull llama3.2:3b
```

### Windows

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No PowerShell, execute:

```powershell
python --version
mkdir oficina-m5
cd oficina-m5
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install deepeval ollama
ollama pull llama3.2:3b
```

> **Ao retomar a prática:** se você fechar o terminal, volte para `oficina-m5` e reative o ambiente: no macOS/Linux, `source .venv/bin/activate`; no Windows/PowerShell, `.venv\Scripts\Activate.ps1`. Com o ambiente ativo, `python` funciona nos três sistemas.

## Preparação do laboratório

Baixe os quatro arquivos para a pasta `oficina-m5`:

- [casos_confianca.json](../assets/labs/modulo-5/casos_confianca.json): 45 entradas sintéticas com a decisão esperada de cada uma.
- [respostas_pregeradas.json](../assets/labs/modulo-5/respostas_pregeradas.json): respostas de referência escritas à mão para o laboratório, com erros deliberados, para que a camada 2 rode sem esperar o modelo.
- [avaliar_confianca.py](../assets/labs/modulo-5/avaliar_confianca.py): camada 1, pontua caso a caso e grava o relatório.
- [agregar_confianca.py](../assets/labs/modulo-5/agregar_confianca.py): camada 2, lê o relatório e calcula as métricas de conjunto.

Confira os nomes antes de executar:

```bash
ls casos_confianca.json respostas_pregeradas.json avaliar_confianca.py agregar_confianca.py
```

A decisão esperada é a referência de avaliação; ela não é enviada como instrução ao usuário final.

## Execução

Comece pelas respostas pré-geradas, sem Ollama. As duas camadas rodam em sequência:

```bash
python avaliar_confianca.py
python agregar_confianca.py
```

Depois, com o Ollama em execução, gere respostas ao vivo para uma amostra pequena e acrescente as métricas de juiz:

```bash
python avaliar_confianca.py --fonte ao-vivo --casos 5 --metricas todas --saida relatorio-ao-vivo.json
python agregar_confianca.py --relatorio relatorio-ao-vivo.json
```

## Receita principal

`avaliar_confianca.py` percorre os casos, obtém a resposta (do arquivo ou do modelo), classifica a decisão observada por regra e aplica as métricas escolhidas. Grava `relatorio-confianca.json` com decisão esperada, decisão prevista, resposta, notas e tempo por caso. `agregar_confianca.py` lê esse relatório e imprime acurácia, matriz de confusão, precisão, recall e F1 por classe, taxa de falsa recusa e falha de bloqueio.

```bash
python -m json.tool relatorio-confianca.json | head -40
```

## Resultado esperado

Com as respostas pré-geradas, a acurácia fica em torno de 0,64, com 6 dos 8 casos adversariais recusados e 2 recusas indevidas sobre pedidos legítimos. Parte dos casos aparece como `indefinido`: a regra determinística não encontra nenhum termo do léxico e se recusa a chutar. A varredura de limiar só aparece quando o relatório tem nota de juiz.

## Interpretação

Leia a matriz de confusão antes da acurácia. Uma acurácia de 0,64 sobre um conjunto com 24 pedidos legítimos e 8 adversariais esconde qual erro está acontecendo, e os dois erros têm consequências opostas: falha de bloqueio expõe dado de terceiro, falsa recusa manda usuário legítimo para fila humana. A classe `bloquear` tem 8 casos, então cada erro move o recall em 0,125, o que também mostra por que conjuntos pequenos não sustentam conclusão.

Repare que o mesmo modelo responde e julga quando você usa `--metricas todas`. É a configuração menos confiável possível para um portão de qualidade, e o laboratório a usa de propósito, para que o efeito apareça na varredura de limiar.

## Roteiro sugerido para aula

### Experimento A — os dois erros não são iguais

**Objetivo**

Ler a matriz de confusão e decidir qual erro a arquitetura tolera.

**Pré-requisito**

Camadas 1 e 2 executadas sobre as respostas pré-geradas.

**Execute**

Localize no relatório os casos em que a decisão esperada era `bloquear` e a prevista não foi, e os casos legítimos recusados.

**Observe**

O que cada um desses erros produz para a pessoa do outro lado.

**Compare**

Recall da classe `bloquear` contra taxa de falsa recusa.

**Questões exploratórias:**

- Qual dos dois erros deve [bloquear uma entrega](padroes-e-decisoes.md#fitness-functions-de-confianca), e quem assina essa decisão?
- Que [controle](padroes-e-decisoes.md#guardrails-em-profundidade) reduziria a falha de bloqueio sem aumentar a falsa recusa?
- Como uma recusa preserva a dignidade da pessoa usuária?

### Experimento B — quem escreve a régua

**Objetivo**

Medir a variação que vem do avaliador, e não do sistema avaliado.

**Pré-requisito**

Ollama em execução.

**Execute**

Rode três vezes com a régua gerada pelo próprio juiz e três vezes com os passos fixos, sempre sobre os mesmos casos:

```bash
python avaliar_confianca.py --fonte pregerada --metricas todas --regua gerada --casos 5 --saida gerada.json
python avaliar_confianca.py --fonte pregerada --metricas todas --regua fixa --casos 5 --saida fixa.json
```

**Observe**

A amplitude das notas entre execuções em cada modo. As respostas são idênticas nas seis execuções, porque vêm do arquivo.

**Compare**

Dispersão com régua gerada e com régua fixa.

**Questões exploratórias:**

- Por que `criteria` produz notas diferentes com a mesma entrada, se a temperatura é zero?
- Quem aprova a régua antes de ela virar [portão de qualidade](padroes-e-decisoes.md#fitness-functions-de-confianca)?
- Que [amostra humana](padroes-e-decisoes.md#privacidade-por-ciclo-de-vida) calibraria a régua?

### Experimento C — o limiar é uma decisão de arquitetura

**Objetivo**

Escolher um limiar e assumir o que ele custa.

**Pré-requisito**

Relatório com nota de juiz.

**Execute**

Leia a varredura de limiar impressa pela camada 2.

**Observe**

Como precisão e recall se movem em direções opostas conforme o limiar sobe.

**Compare**

Um limiar permissivo e um restritivo, em número de casos aprovados.

**Questões exploratórias:**

- Que limiar você levaria para a esteira de CI, e qual erro ele deixa passar?
- Que evidência adicional evitaria falso bloqueio?
- Como [versionar](padroes-e-decisoes.md#governanca-que-acompanha-mudancas) régua, limiar e conjunto de casos juntos?

## Evidência a entregar

Entregue a saída da camada 2 e uma leitura de até dez linhas com quatro elementos: a matriz de confusão comentada, o limiar escolhido com a justificativa, o erro que você decidiu tolerar e o responsável por essa decisão. Registre também uma fitness function, seu responsável e a ação automática ou humana quando ela falhar.

| Item | Valor obtido | Consequência declarada |
|---|---|---|
| acurácia |  |  |
| recall de `bloquear` |  |  |
| taxa de falsa recusa |  |  |
| limiar do juiz |  |  |

## Limpeza e contingência

Saia do ambiente com `deactivate`. Apague `relatorio-confianca.json` e os relatórios auxiliares se não quiser preservar a evidência local. Se o script falhar, confira `ollama list`, `python -m pip show deepeval ollama` e a existência dos dois arquivos. Se o erro for `DeepEvalError: OllamaModel requires the 'ollama' package`, rode `python -m pip install ollama` no mesmo ambiente virtual. Registre o erro e corrija o ambiente local com apoio do professor antes de prosseguir.

## Ferramentas adicionais

O laboratório usou DeepEval com um juiz local para transformar "parece seguro" em casos, critério e relatório. O mercado tem ferramentas de avaliação, guardrails e red teaming com o mesmo objetivo em escopos distintos. Investigação livre, fora do escopo avaliado desta oficina.

| Ferramenta | Site | Propósito |
|---|---|---|
| Promptfoo | [promptfoo.dev](https://www.promptfoo.dev) | Framework open source de teste e red teaming de prompts, com dezenas de tipos de vulnerabilidade e integração a esteiras de CI |
| Garak | [github.com/NVIDIA/garak](https://github.com/NVIDIA/garak) | Scanner de vulnerabilidades para LLMs mantido pela NVIDIA, com dezenas de sondas (probes) automatizadas |
| PyRIT | [github.com/Azure/PyRIT](https://github.com/Azure/PyRIT) | Framework de red teaming da Microsoft para ataques de múltiplos turnos e múltiplas modalidades |
| Giskard | [giskard.ai](https://www.giskard.ai) | Plataforma de testes de qualidade e segurança para modelos de aprendizado de máquina e LLM |
| NeMo Guardrails | [github.com/NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Biblioteca da NVIDIA para adicionar trilhos de segurança programáveis a assistentes conversacionais |
| Arize Phoenix | [phoenix.arize.com](https://phoenix.arize.com) | Plataforma open source de avaliação e observabilidade para aplicações de RAG e agentes |
