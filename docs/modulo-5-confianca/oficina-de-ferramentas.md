# Oficina de ferramentas — avaliar decisões de confiança

**Objetivo Bloom:** Analisar.

Esta oficina executa uma avaliação local de cinco casos sintéticos. Ela transforma “parece seguro” em casos, respostas, critério e relatório inspecionável.

## Ferramenta

**DeepEval** é um framework open source para avaliar aplicações de IA. Nesta prática ele usa um juiz **Ollama** local para avaliar se a resposta observada se aproxima da decisão esperada: [bloquear](conceitos.md#qualidade-tem-varias-dimensoes), corrigir ou [escalar](conceitos.md#qualidade-tem-varias-dimensoes).

**Decisão arquitetural em foco:** como uma equipe registra comportamento esperado, falha observada e hipótese de correção sem reduzir [confiança](conceitos.md#confianca-e-uma-relacao-nao-uma-caracteristica-absoluta) a uma única pontuação?

## Pré-requisitos

- Python 3.10 ou superior, terminal e Ollama instalado.
- Modelo `llama3.2:3b` já baixado com `ollama pull llama3.2:3b`.
- Uma pasta descartável. Os cinco casos fornecidos são sintéticos e não devem ser misturados a conversas reais.

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

Baixe os dois arquivos para a pasta `oficina-m5`:

- [casos_confianca.json](../assets/labs/modulo-5/casos_confianca.json) — entradas e decisões esperadas.
- [avaliar_confianca.py](../assets/labs/modulo-5/avaliar_confianca.py) — gera respostas locais, aplica a métrica e grava o relatório.

Confira os nomes antes de executar:

```bash
ls casos_confianca.json avaliar_confianca.py
```

Cada caso possui um identificador, uma entrada sintética e uma decisão esperada. A decisão esperada é a referência de avaliação; ela não é enviada como instrução ao usuário final.

## Execução

Rode o script **uma única vez** agora. Ele gera o relatório que os três experimentos vão inspecionar; nenhum deles pede nova execução antes de você alterar alguma coisa no conjunto de casos.

Com o Ollama em execução:

```bash
python avaliar_confianca.py
```

## Receita principal

O script pede ao modelo local uma resposta para cada entrada, submete a resposta ao juiz e grava `relatorio-confianca.json`, imprimindo uma linha por caso. Cada item contém caso, decisão esperada, resposta observada, pontuação e justificativa do avaliador. Abra o relatório:

```bash
python -m json.tool relatorio-confianca.json
```

## Resultado esperado

Você deve encontrar cinco resultados (`C-01` a `C-05`). Casos de [injeção](padroes-e-decisoes.md#instrucoes-adversariais) e tentativa de burlar identidade devem tender a bloqueio; pedido ambíguo deve pedir contexto; contestação deve escalar para um caminho humano.

## Interpretação

Leia a resposta e a justificativa antes de olhar a pontuação — é por isso que o relatório grava as três coisas. Uma nota alta pode vir de o modelo ter respondido com segurança por conta própria, e não de um controle da solução; uma nota baixa pode vir de ambiguidade no texto de entrada. Note também que o mesmo modelo responde e julga, o que é a configuração menos confiável possível para um portão de qualidade.

Com esse relatório em mãos, siga o roteiro abaixo. O Experimento B é onde você altera a regra esperada e roda de novo.

## Roteiro sugerido para aula

### Experimento A — caso adversarial

**Objetivo**

Verificar uma decisão de bloqueio.

**Pré-requisito**

Relatório gerado.

**Execute**

Leia `C-01` e `C-03`.

**Observe**

Resposta, pontuação e justificativa.

**Compare**

Bloquear com explicação e bloquear sem próximo passo.

**Questões exploratórias:**

- Que trecho da resposta configuraria [vazamento de contexto ou de segredo](padroes-e-decisoes.md#exposicao-e-efeitos-indevidos), e não apenas "informação sensível" em termos genéricos?
- Qual [controle](padroes-e-decisoes.md#guardrails-em-profundidade) deve existir antes da geração?
- Como uma recusa preserva a dignidade da pessoa usuária?

### Experimento B — regra e avaliador

**Objetivo**

Distinguir comportamento observado de referência.

**Pré-requisito**

Caso alterado.

**Execute**

Escolha um único caso em `casos_confianca.json` e altere somente `decisao_esperada` — por exemplo, `C-05` de `escalar` para `bloquear`. Salve e rode `python avaliar_confianca.py` de novo. Guarde os dois relatórios antes de sobrescrever.

**Observe**

Diferença entre os dois relatórios. A variável controlada é a regra esperada; a resposta do modelo pode variar mesmo com temperatura zero, então parte da diferença não vem da sua mudança.

**Compare**

Regra original e regra alterada.

**Questões exploratórias:**

- Quem aprova uma regra esperada antes de ela virar [portão de qualidade](padroes-e-decisoes.md#fitness-functions-de-confianca)?
- Que [viés](padroes-e-decisoes.md#guardrails-em-profundidade) pode surgir se o mesmo modelo responde e julga?
- Que [amostra humana](padroes-e-decisoes.md#privacidade-por-ciclo-de-vida) ajudaria a calibrar a métrica?

### Experimento C — priorização de correção

**Objetivo**

Escolher uma hipótese de melhoria.

**Pré-requisito**

Dois relatórios.

**Execute**

Selecione uma falha.

**Observe**

Decisão, justificativa e impacto.

**Compare**

Corrigir prompt, contexto, [guardrail](padroes-e-decisoes.md#guardrails-em-profundidade) ou UX.

**Questões exploratórias:**

- Qual falha deve [bloquear uma entrega](padroes-e-decisoes.md#fitness-functions-de-confianca)?
- Que evidência adicional evitaria falso bloqueio?
- Como [versionar](padroes-e-decisoes.md#governanca-que-acompanha-mudancas) a regra e o conjunto de casos?

## Evidência a entregar

Entregue `relatorio-confianca.json` ou a tabela preenchida e uma conclusão de até cinco linhas.

| Caso | Decisão esperada | Resultado observado | Justificativa | Hipótese de correção |
|---|---|---|---|---|
| C-01 |  |  |  |  |
| C-02 |  |  |  |  |
| C-03 |  |  |  |  |
| C-04 |  |  |  |  |
| C-05 |  |  |  |  |

Indique uma falha que exigiria bloqueio, uma que exigiria melhoria de experiência e uma que precisaria de revisão humana. Registre também uma fitness function, seu responsável e a ação automática ou humana quando ela falhar.

## Limpeza e contingência

Saia do ambiente com `deactivate`. Apague `relatorio-confianca.json` se não quiser preservar a evidência local. Se o script falhar, confira `ollama list`, `python -m pip show deepeval ollama` e a existência dos dois arquivos. Se o erro for `DeepEvalError: OllamaModel requires the 'ollama' package`, rode `python -m pip install ollama` no mesmo ambiente virtual. Registre o erro e corrija o ambiente local com apoio do professor antes de prosseguir.

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
