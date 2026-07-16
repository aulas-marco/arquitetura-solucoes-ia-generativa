# Oficina de ferramentas — observar uma chamada de plataforma

**Objetivo Bloom:** Analisar.

Esta oficina envia uma solicitação sintética por um gateway local e registra um trace OpenTelemetry no próprio terminal. Ela permite discutir o que observar sem copiar telemetria de produção.

## Ferramenta

**OpenTelemetry** é um padrão open source de instrumentação. Nesta prática, um script cria spans de entrada, modelo e saída. O **LiteLLM Proxy** do Módulo 2 é o gateway local observado; o Ollama é o destino de inferência.

**Decisão arquitetural em foco:** quais sinais devem ligar uma solicitação, um produto, uma resposta e uma ação de recuperação sem expor conteúdo além do necessário?

## Pré-requisitos

- Módulo 2 concluído ou Ollama com `llama3.2:3b` e LiteLLM Proxy disponíveis.
- Python 3.10+, terminal e portas 11434 e 4000 livres.
- Os arquivos `litellm_config.yaml` e `request.json` do laboratório M2.
- Somente o indicador sintético `tr-202`; não use traces, prompts ou identificadores reais.

## Instalação

### macOS

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No Terminal, execute:

```bash
python3 --version
mkdir oficina-m6
cd oficina-m6
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install opentelemetry-api opentelemetry-sdk 'litellm[proxy]'
ollama pull llama3.2:3b
```

### Linux

Instale o Ollama pelo procedimento oficial em [ollama.com/download](https://ollama.com/download). No terminal Linux, execute:

```bash
python3 --version
mkdir oficina-m6
cd oficina-m6
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install opentelemetry-api opentelemetry-sdk 'litellm[proxy]'
ollama pull llama3.2:3b
```

### Windows

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No PowerShell, execute:

```powershell
python --version
mkdir oficina-m6
cd oficina-m6
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install opentelemetry-api opentelemetry-sdk 'litellm[proxy]'
ollama pull llama3.2:3b
```

> **Ao retomar a prática:** se você fechar o terminal, volte para `oficina-m6` e reative o ambiente: no macOS/Linux, `source .venv/bin/activate`; no Windows/PowerShell, `.venv\Scripts\Activate.ps1`.

## Preparação do laboratório

Baixe [telemetria_local.py](../assets/labs/modulo-6/telemetria_local.py), [litellm_config.yaml](../assets/labs/modulo-2/litellm_config.yaml) e [request.json](../assets/labs/modulo-2/request.json) para `oficina-m6`.

```bash
ls telemetria_local.py litellm_config.yaml request.json
```

O script não grava a pergunta completa como atributo do trace. Ele registra o alias do modelo, o produto sintético, o tamanho da resposta, duração e `trace_id`.

## Execução

Abra dois terminais na pasta `oficina-m6`. No primeiro, inicie o gateway:

```bash
# macOS/Linux
source .venv/bin/activate
litellm --config litellm_config.yaml --port 4000
```

No Windows/PowerShell, use:

```powershell
.venv\Scripts\Activate.ps1
litellm --config litellm_config.yaml --port 4000
```

No segundo, execute a chamada instrumentada:

```bash
# macOS/Linux
source .venv/bin/activate
python telemetria_local.py
```

No Windows/PowerShell, use:

```powershell
.venv\Scripts\Activate.ps1
python telemetria_local.py
```

## Receita principal

O terminal imprime três spans em JSON e, ao final, `TRACE_ID`, `DURACAO_MS` e `RESPOSTA`. Localize os spans `entrada`, `modelo` e `saida`. Eles mostram que observabilidade precisa relacionar fases do fluxo, e não apenas contar chamadas.

## Resultado esperado

Você deve obter um único `trace_id`, duração em milissegundos, resposta sintética e atributos minimizados. A execução não implementa quotas, SLOs ou alertas de produção; ela torna palpável que esses controles dependem de sinais com dono, limiar e ação de recuperação.

## Interpretação

No script, altere somente o texto sintético `tr-202` por `tr-204` e execute novamente. Compare duração, erro caso ocorra, tamanho da resposta e os atributos emitidos. A diferença de duas execuções não prova causalidade: ela sugere uma hipótese que exigiria amostra, limiar e contexto operacional antes de mudar uma plataforma.

## Roteiro sugerido para aula

### Experimento A — trace mínimo (Essencial em aula)

**Objetivo**

Reconhecer os sinais de uma chamada.

**Pré-requisito**

Proxy iniciado.

**Execute**

Rode o script.

**Observe**

`trace_id`, spans e duração.

**Compare**

Log isolado e trace com etapas relacionadas.

**Questões exploratórias:**

- Qual atributo identifica o produto sem registrar o conteúdo inteiro?
- Que sinal permitiria separar falha do modelo e falha do gateway?
- Quem deve ser dono do limiar de duração observado?

### Experimento B — variação controlada (Exploração em dupla)

**Objetivo**

Tratar medição como hipótese.

**Pré-requisito**

Primeiro trace salvo.

**Execute**

Altere apenas `tr-202` para `tr-204`.

**Observe**

Duração, tamanho e erro.

**Compare**

Dois traces locais.

**Questões exploratórias:**

- Por que duas amostras não demonstram causa raiz?
- Que metadado de modelo e manifesto ajuda a reproduzir um desvio?
- Que dado deve ficar fora do trace para preservar privacidade?

### Experimento C — ação recuperável (Extensão)

**Objetivo**

Transformar sinal em decisão operacional.

**Pré-requisito**

Comparativo de traces.

**Execute**

Escolha um limiar e uma ação.

**Observe**

Evidência necessária antes de alterar o gateway.

**Compare**

Fallback, redução de contexto, fila e rollback.

**Questões exploratórias:**

- Que produto deve ter prioridade quando a capacidade é limitada?
- Quando uma parada segura vira incidente?
- Qual ação deve ser reversível primeiro?

## Evidência a entregar

Entregue as linhas `TRACE_ID` e `DURACAO_MS` de duas execuções e o quadro abaixo.

| Execução | Produto/indicador | Duração | Atributos minimizados | Hipótese | Próxima ação |
|---|---|---:|---|---|---|
| Inicial | tr-202 |  |  |  |  |
| Variação | tr-204 |  |  |  |  |

Conclua em até cinco linhas que sinal exigiria uma parada segura, que sinal exigiria investigação e qual informação adicional você coletaria antes de mudar o gateway.

## Limpeza e contingência

Encerre o proxy com `Ctrl+C`, saia do ambiente com `deactivate` e apague a pasta do laboratório se não precisar mais dela. Para liberar o modelo, use `ollama rm llama3.2:3b` somente após as demais oficinas.

Se ocorrer erro, confirme que `curl http://localhost:4000/health/readiness` responde, que `ollama list` mostra o modelo e que as dependências foram instaladas. Registre a mensagem e corrija a configuração local com apoio do professor; não substitua a evidência por telemetria de outro ambiente.
