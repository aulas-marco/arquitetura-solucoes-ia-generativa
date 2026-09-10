# Oficina de ferramentas — observar uma chamada de plataforma

**Objetivo Bloom:** Analisar.

Esta oficina envia uma solicitação sintética por um [gateway local](plataforma-corporativa.md#model-gateway-como-fronteira-comum) e registra um [trace](observabilidade.md#trace-reconstruir-a-composicao) OpenTelemetry no próprio terminal. Ela permite discutir o que observar sem copiar telemetria de produção.

## Ferramenta

**OpenTelemetry** é um padrão open source de instrumentação. Nesta prática, um script cria [spans](observabilidade.md#trace-reconstruir-a-composicao) de entrada, modelo e saída. O **LiteLLM Proxy** do Módulo 2 é o gateway local observado; o Ollama é o destino de inferência.

**Decisão arquitetural em foco:** quais sinais devem ligar uma solicitação, um produto, uma resposta e uma [ação de recuperação](entrega-e-recuperacao.md#roteamento-fallback-e-degradacao) [sem expor conteúdo além do necessário](observabilidade.md#logs-com-preservacao-de-privacidade)?

## Pré-requisitos

- Módulo 2 concluído ou Ollama com `llama3.2:3b` e LiteLLM Proxy disponíveis.
- Python 3.10+, terminal e portas 11434 e 4000 livres.
- Os arquivos `litellm_config.yaml` e `request.json` do laboratório M2.
- Somente o indicador sintético `tr-202`; não use traces, prompts ou identificadores reais.

## Instalação

O comando de instalação fixa as versões de `litellm` e `fastapi`: sem essa fixação, o `pip` resolve para a versão mais recente do FastAPI, que remove uma função interna ainda usada pelo proxy do LiteLLM, e o gateway não inicia. Use exatamente as versões abaixo.

### macOS

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No Terminal, execute:

```bash
python3 --version
mkdir oficina-m7
cd oficina-m7
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install opentelemetry-api opentelemetry-sdk 'litellm[proxy]==1.96.2' 'fastapi==0.140.0'
ollama pull llama3.2:3b
```

### Linux

Instale o Ollama pelo procedimento oficial em [ollama.com/download](https://ollama.com/download). No terminal Linux, execute:

```bash
python3 --version
mkdir oficina-m7
cd oficina-m7
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install opentelemetry-api opentelemetry-sdk 'litellm[proxy]==1.96.2' 'fastapi==0.140.0'
ollama pull llama3.2:3b
```

### Windows

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No PowerShell, execute:

```powershell
python --version
mkdir oficina-m7
cd oficina-m7
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install opentelemetry-api opentelemetry-sdk 'litellm[proxy]==1.96.2' 'fastapi==0.140.0'
ollama pull llama3.2:3b
```

> **Ao retomar a prática:** se você fechar o terminal, volte para `oficina-m7` e reative o ambiente: no macOS/Linux, `source .venv/bin/activate`; no Windows/PowerShell, `.venv\Scripts\Activate.ps1`.

## Preparação do laboratório

Baixe [telemetria_local.py](../assets/labs/modulo-6/telemetria_local.py), [litellm_config.yaml](../assets/labs/modulo-2/litellm_config.yaml) e [request.json](../assets/labs/modulo-2/request.json) para `oficina-m7`.

```bash
ls telemetria_local.py litellm_config.yaml request.json
```

O script não grava a pergunta completa como atributo do trace. Ele registra o alias do modelo, o produto sintético, o tamanho da resposta, duração e `trace_id`.

## Execução

Abra dois terminais na pasta `oficina-m7`. No primeiro, inicie o gateway:

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

O terminal imprime três blocos de JSON — um por *span*, o nome que o OpenTelemetry dá a cada pedaço registrado — e, ao final, três linhas: `TRACE_ID`, `DURACAO_MS` e `RESPOSTA`. Localize os *spans* `entrada`, `modelo` e `saida`: eles [separam onde o tempo foi gasto](observabilidade.md#trace-reconstruir-a-composicao), em vez de só dizer que uma chamada aconteceu.

Abaixo está um trace de exemplo, gerado localmente para ilustrar o formato (o campo `"modelo"` usa uma espera simulada no lugar de uma chamada real ao Ollama). No seu terminal, os três blocos vêm na ordem `modelo`, `saida`, `entrada` — o span pai (`entrada`) só termina, e só é impresso, depois dos dois filhos. Cada bloco real também traz `context`, `kind`, `status`, `resource` e outros campos, omitidos aqui por repetirem o mesmo valor nos três:

```json
{
  "name": "modelo",
  "start_time": "2026-09-10T01:58:10.513202Z",
  "end_time": "2026-09-10T01:58:10.694008Z",
  "attributes": {}
}
{
  "name": "saida",
  "start_time": "2026-09-10T01:58:10.695146Z",
  "end_time": "2026-09-10T01:58:10.695169Z",
  "attributes": {
    "boreal.resultado": "ok",
    "boreal.tamanho_resposta": 62
  }
}
{
  "name": "entrada",
  "start_time": "2026-09-10T01:58:10.513178Z",
  "end_time": "2026-09-10T01:58:10.695298Z",
  "attributes": {
    "gen_ai.request.model": "boreal-local",
    "boreal.produto": "resumo-interno"
  }
}
TRACE_ID: bd1d6fd2d08e0d570378d88cba1ffe75
DURACAO_MS: 182
RESPOSTA: O indicador tr-202 está dentro da faixa esperada nesta semana.
```

O seu terminal vai mostrar um `TRACE_ID` diferente, uma duração diferente e uma `RESPOSTA` escrita pelo modelo de verdade — o que não muda de uma execução para outra é a forma: três blocos com `name`, `start_time`, `end_time` e `attributes`, seguidos das três linhas finais.

## Resultado esperado

No fim da execução, você vê três coisas no terminal: um `trace_id` (o identificador da chamada inteira), um `DURACAO_MS` (quanto tempo ela levou) e um `RESPOSTA` (o texto que o modelo devolveu). O script não implementa alarme nem trava nada sozinho — os Experimentos A, B e C te levam a olhar esses três números com mais atenção antes de decidir o que fazer com eles.

## Interpretação

Uma execução só, com um número só de duração, não diz muita coisa sozinha. É só rodando de novo — com o mesmo texto e depois com o texto trocado, como no Experimento B — que dá para perceber o quanto o número varia [mesmo sem mudar nada](observabilidade.md#quatro-planos-de-metricas), e o quanto isso limita o que você pode concluir de uma única chamada.

## Roteiro sugerido para aula

### Experimento A — trace mínimo

**Objetivo**

Ver os três pedaços que compõem uma chamada, em vez de uma linha de log só.

**Pré-requisito**

Proxy iniciado (primeiro terminal).

**Execute**

No segundo terminal, rode `python telemetria_local.py` e deixe a saída na tela.

**Observe**

O terminal imprime três blocos de JSON, um por bloco de código chamado *span*. Procure a linha `"name":` em cada um — os três valores são `entrada`, `modelo` e `saida`. Cada bloco também tem `"start_time"` e `"end_time"`, o horário exato em que aquele pedaço começou e terminou — como no trace de exemplo da "Receita principal", acima.

**Compare**

Um log comum teria uma linha só, dizendo só que a chamada aconteceu. Aqui você tem três blocos separados, cada um com seu próprio início e fim.

No trace de exemplo, o bloco `modelo` tem `"start_time": "...513202Z"` e `"end_time": "...694008Z"`. A diferença entre os dois é `694008 - 513202 = 180806` microssegundos, ou **181 ms** — quase toda a duração total daquele exemplo (`DURACAO_MS: 182`). Faça a mesma conta com os horários do seu próprio terminal.

**Questões exploratórias:**

- Quantos blocos `"name"` apareceram no seu terminal? Escreva os três valores, na ordem em que apareceram.
- No bloco `entrada`, procure o atributo `boreal.produto`. Ele guarda a pergunta inteira que foi enviada ao modelo, ou só um nome curto (`resumo-interno`)? Isso é um exemplo de [registrar o mínimo necessário](observabilidade.md#logs-com-preservacao-de-privacidade).
- Refaça a conta do quadro "Compare" com o `start_time` e o `end_time` do bloco `modelo` do seu terminal. Quantos milissegundos esse bloco levou sozinho? Esse valor chegou perto do `DURACAO_MS` total, como no exemplo, ou ficou bem menor? O que isso sugere sobre onde o tempo foi gasto?

### Experimento B — variação controlada

**Objetivo**

Ver se a mesma pergunta, com um número trocado, muda o resultado — e o quanto o resultado varia mesmo sem trocar nada.

**Pré-requisito**

Trace do Experimento A salvo (o `DURACAO_MS` e o `RESPOSTA` que apareceram no terminal).

**Execute**

Rode `python telemetria_local.py` de novo, sem mudar o arquivo. Depois abra `telemetria_local.py`, troque `tr-202` por `tr-204` na linha 30, salve e rode mais uma vez.

**Observe**

Você agora tem três números de `DURACAO_MS`: o do Experimento A, o da repetição sem mudar nada, e o de `tr-204`.

**Compare**

Os três valores de `DURACAO_MS`, lado a lado.

**Questões exploratórias:**

- A duração da repetição (mesmo texto `tr-202`, rodado de novo) veio igual à do Experimento A, ou diferente? Você não mudou nada no arquivo entre as duas.
- Sabendo que a duração varia mesmo sem trocar nada (pergunta anterior), a diferença entre `tr-202` e `tr-204` prova que foi a troca do texto que mudou o tempo?
- Procure a palavra `tr-202` ou `tr-204` dentro dos três blocos de JSON impressos. Ela aparece em algum atributo, ou só na linha `RESPOSTA` no final do terminal?

### Experimento C — ação recuperável

**Objetivo**

Usar um número medido de verdade para decidir quando algo merece atenção.

**Pré-requisito**

Os três valores de `DURACAO_MS` do Experimento B, anotados.

**Execute**

Escolha um número de milissegundos maior que os três que você mediu. Escreva-o: esse é o seu "limite de alerta".

**Observe**

O script não faz nada com esse número — ele não trava, não avisa ninguém, não muda o comportamento sozinho. Ele só imprime a duração; agir a partir dela é decisão sua.

**Compare**

Quatro ações possíveis quando um limite é ultrapassado, cada uma com um custo diferente de desfazer:

- **trocar de modelo** ([`fallback`](entrega-e-recuperacao.md#roteamento-fallback-e-degradacao)): usar outro modelo já pronto no lugar do que travou
- **reduzir o pedido**: mandar uma pergunta mais curta, que roda mais rápido
- **fila**: fazer o pedido esperar a vez, em vez de responder na hora
- **rollback**: voltar para a versão de ontem, desfazendo a mudança mais recente

**Questões exploratórias:**

- Você escolheu um limite de alerta maior que os três `DURACAO_MS` medidos. Se amanhã aparecesse um `DURACAO_MS` maior que esse limite, o que você acha que aconteceu: o gateway ficou mais lento, ou foi só a variação normal que você já viu no Experimento B?
- Um carro com defeito no motor pode parar no acostamento agora (rápido de fazer, mas trava quem vem atrás) ou seguir devagar até a próxima oficina (mais arriscado, mas não atrapalha ninguém). Das quatro ações acima, qual é mais parecida com "parar no acostamento agora"? E qual é mais parecida com "seguir até a oficina"?
- De 1 (fácil) a 4 (difícil), ordene as quatro ações por quão fácil é desfazer cada uma se você errar a mão e ela não resolver o problema.

## Evidência a entregar

Preencha o quadro com as três execuções do Experimento B (o `TRACE_ID` e o `DURACAO_MS` impressos em cada uma).

| Execução | Texto usado | `TRACE_ID` | `DURACAO_MS` |
|---|---|---|---:|
| 1ª vez | tr-202 |  |  |
| Repetição | tr-202 |  |  |
| Variação | tr-204 |  |  |

Conclua em até cinco linhas: qual limite de alerta você escolheu no Experimento C, qual das quatro ações você tentaria primeiro se esse limite fosse ultrapassado, e por que essa e não outra.

## Limpeza e contingência

Encerre o proxy com `Ctrl+C`, saia do ambiente com `deactivate` e apague a pasta do laboratório se não precisar mais dela. Para liberar o modelo, use `ollama rm llama3.2:3b` somente após as demais oficinas.

Se ocorrer erro, confirme que `curl http://localhost:4000/health/readiness` responde, que `ollama list` mostra o modelo e que as dependências foram instaladas. Se o proxy encerrar com `ImportError: cannot import name 'get_flat_dependant' from 'fastapi.dependencies.utils'`, o ambiente tem uma versão de FastAPI mais nova que a fixada; rode novamente `python3 -m pip install 'litellm[proxy]==1.96.2' 'fastapi==0.140.0'` no mesmo ambiente virtual. Registre a mensagem e corrija a configuração local com apoio do professor; não substitua a evidência por telemetria de outro ambiente.

## Extensão — loop objetivado com orçamento

A oficina principal observou uma chamada. Esta extensão observa um **laço**: um agente de nível 2 que roda sozinho até um critério objetivo ser satisfeito, ou até o orçamento acabar. O objeto de estudo não é a qualidade do código que ele produz; é a diferença entre parar porque um verificador aprovou e parar porque o modelo disse que terminou.

### Cenário sintético

A Boreal precisa de uma função `normalizar_pedido(texto)` que converta uma linha como `PED-845 | item P20 | qtd 2` em um dicionário com pedido, item em maiúsculas e quantidade inteira, tratando espaços extras, caixa baixa, quantidade ausente e linha inválida. A especificação está no script e a suíte de cinco casos de teste é o verificador. Nada sai da pasta do laboratório.

### Pergunta de investigação

Um laço com condição de parada objetiva e um laço que para quando o modelo se declara pronto consomem orçamentos parecidos. Eles entregam o mesmo resultado?

### Pré-requisitos

- Python 3.10 ou superior, terminal e a pasta `oficina-m7` com o ambiente virtual ativo.
- `pytest` e `langchain-ollama` instalados no ambiente: `python -m pip install pytest langchain-ollama`.
- Ollama em execução com um modelo de codificação: `ollama pull qwen2.5-coder:7b` (4,7 GB). O `llama3.2:3b` das outras oficinas roda o laboratório, mas não converge; a subseção final trata disso.
- Nenhum dado real. O laço escreve apenas dentro da subpasta `loop-sandbox`.

### Preparação

Baixe [loop_objetivado.py](../assets/labs/modulo-6/loop_objetivado.py) para a pasta `oficina-m7`.

```bash
ls loop_objetivado.py
```

O script contém a especificação, a suíte de testes, a guarda estática e o laço. Ao rodar, ele cria a pasta `loop-sandbox` com `test_solucao.py` e escreve ali a `solucao.py` de cada iteração.

### O que o arnês deste laço contém

Vale ler a lista antes de executar, porque cada item é um componente do [arnês (*harness*)](../modulo-4-agentes/arnes.md#os-componentes-do-arnes) e cada um deles foi necessário para o laço funcionar.

| Componente | Como aparece no script |
|---|---|
| *System prompt* | instrui a devolver só o bloco de código; muda conforme a condição de parada escolhida |
| Contexto | especificação, suíte de testes e **a versão anterior do próprio código** entram no *prompt* de cada iteração |
| *Sandbox* | tudo é escrito em `loop-sandbox`; o `pytest` roda como subprocesso com essa pasta como diretório de trabalho |
| Guarda estática | análise da árvore sintática rejeita `import` fora de uma lista curta, chamadas como `exec` e `open`, e acesso a atributos com prefixo duplo |
| Verificador | `pytest` com cinco casos; o relatório de falha volta ao modelo na iteração seguinte |
| Orçamento | teto de iterações, com comportamento definido no esgotamento |
| Detecção de estagnação | duas iterações com o mesmo relatório de falha elevam a temperatura, em vez de repetir a mesma chamada |

A detecção de estagnação existe por um motivo empírico que vale antecipar: com `temperature=0` e um contexto idêntico, o modelo devolve exatamente a mesma resposta, e o laço vira uma repetição sem progresso. Um laço determinístico sobre entrada constante é um laço que não itera.

### Execute o laço com condição de parada objetiva

```bash
python loop_objetivado.py
```

Uma execução completa leva de 40 segundos a poucos minutos, conforme a máquina e o número de iterações até a convergência.

Acrescente `--gravar sessao.json` para registrar a transcrição inteira — o relatório que entrou, o código que saiu e o veredito do verificador em cada iteração. É o formato que alimenta o [playback deste laço](playback-do-laco.md), útil para comparar a sua trajetória com as três gravadas ali sem precisar reexecutar.

### Observe

Uma execução com `qwen2.5-coder:7b` e orçamento de oito iterações produziu:

```text
MODELO: qwen2.5-coder:7b
CONDICAO_DE_PARADA: testes
ORCAMENTO: 8 iteracoes
VERIFICADOR: pytest com 5 casos, em loop-sandbox/test_solucao.py

ITER 1 | GUARDA: aceito | TESTES: 4/5 | AUTODECLAROU_PRONTO: False | TEMPERATURA: 0.0 | TOKENS_ACUM: 704
  PRIMEIRA_FALHA: FAILED test_solucao.py::test_espacos_extras_e_caixa_baixa - ValueError: Linha...
ITER 2 | GUARDA: aceito | TESTES: 4/5 | AUTODECLAROU_PRONTO: False | TEMPERATURA: 0.4 | TOKENS_ACUM: 1636
  ESTAGNACAO: mesma falha da iteracao anterior; o arnes diversificou a temperatura para 0.4
...
ITER 5 | GUARDA: aceito | TESTES: 5/5 | AUTODECLAROU_PRONTO: False | TEMPERATURA: 0.8 | TOKENS_ACUM: 4523

PARADA: meta_atingida
ITERACOES: 5
TOKENS_TOTAIS: 4523
VERDADE_FINAL: 5/5 testes passando
```

Rode uma segunda vez. Execuções desta oficina com orçamento de cinco iterações terminaram ora em `meta_atingida` na quarta iteração, com cerca de 3,5 mil *tokens*, ora em `orcamento_esgotado` com 4/5, consumindo cerca de 4,5 mil. **A variação entre execuções é o resultado, não ruído a descartar**: a partir do momento em que o arnês diversifica a temperatura para escapar da estagnação, a trajetória deixa de ser determinística, e é por isso que orçamento de laço se dimensiona por distribuição observada, com percentil, e não por média.

### Execute o mesmo laço sem verificador

Agora troque apenas a condição de parada. O modelo passa a declarar quando terminou, e o laço acredita nele.

```bash
python loop_objetivado.py --parada modelo
```

A saída registrada nesta oficina foi:

```text
CONDICAO_DE_PARADA: modelo

ITER 1 | GUARDA: aceito | TESTES: 4/5 | AUTODECLAROU_PRONTO: True | TEMPERATURA: 0.0 | TOKENS_ACUM: 719

PARADA: autodeclarada_pelo_modelo
ITERACOES: 1
TOKENS_TOTAIS: 719
VERDADE_FINAL: 4/5 testes passando
```

### Interprete

O segundo laço é seis vezes mais barato e encerra em um sexto do tempo. Ele também entrega um artefato que não satisfaz a especificação, e encerra afirmando o contrário. A linha `VERDADE_FINAL` só existe porque o script roda os testes de qualquer forma no fim, para efeito de laboratório; num sistema real, essa linha é exatamente a informação que não existiria. Ninguém saberia.

Note onde a diferença **não** está. O modelo é o mesmo, os pesos são os mesmos, a especificação é a mesma, e na primeira iteração os dois laços produzem 4/5. A diferença inteira está em quem tem autoridade para dizer que o trabalho terminou. Esse é o conteúdo operacional de [o verificador é o gargalo](lacos-desassistidos.md#loop-desassistido-o-verificador-e-o-gargalo): tirar a pessoa da frente não elimina a necessidade de verificação, apenas transfere a função para um artefato que precisa ser escrito, versionado e protegido de quem ele avalia.

Observe também o que a guarda estática faz e o que ela não faz. Ela impede que o código gerado importe módulos fora da lista ou chame `exec`, e por isso o laço pode rodar sem supervisão numa máquina de estudo. Ela não diz nada sobre a correção do resultado. Isolamento e verificação são [portões distintos](lacos-desassistidos.md#portoes-de-um-loop-autonomo), e cumprir um não dispensa o outro.

### Compare

| Execução | Parada | Iterações | *Tokens* | Testes ao encerrar | O que o sistema afirmou |
|---|---|---:|---:|---|---|
| Objetiva | `meta_atingida` | 5 | 4.523 | 5/5 | terminou, e terminou |
| Objetiva sem convergir | `orcamento_esgotado` | 5 | 4.513 | 4/5 | não terminou, e informou |
| Autodeclarada | `autodeclarada_pelo_modelo` | 1 | 719 | 4/5 | terminou, e não terminou |

As duas primeiras linhas são desfechos aceitáveis, inclusive a segunda: um laço que esgota o orçamento e diz que esgotou entregou informação verdadeira. A terceira é a única falha operacional da tabela, e é a mais barata das três.

### Modelo pequeno, laço que não fecha

Rodando com `python loop_objetivado.py --modelo llama3.2:3b`, o laço desta oficina esgotou o orçamento com 1/5 em todas as execuções testadas, com e sem realimentação do código anterior. É o mesmo achado da [limitação registrada na oficina do Módulo 5](../modulo-5-sdd/oficina-de-ferramentas.md#instalacao): arnês bem construído não compensa capacidade insuficiente do modelo. As duas afirmações do curso convivem sem contradição. Trocar o arnês costuma render mais que trocar o modelo, **e** existe um piso de capacidade abaixo do qual nenhum arnês fecha o laço. O trabalho de arquitetura é descobrir de que lado desse piso está o seu caso, e a forma de descobrir é medir, como este laboratório faz.

### Questões exploratórias

- O laço autodeclarado gastou 719 *tokens* e disse que tinha terminado, mas entregou 4/5 testes passando. O objetivo gastou 4.523 *tokens* e só parou com 5/5. Se você fosse revisar esse código depois, qual dos dois prefere receber, mesmo custando mais caro? Por quê?
- A detecção de estagnação eleva a temperatura. Que outras respostas o arnês poderia dar diante de duas falhas idênticas, e qual delas você adotaria num laço com efeito externo?
- Se o agente tivesse permissão de escrita sobre `test_solucao.py`, qual desfecho passaria a ser possível, e que portão o impede?
- O script roda `pytest` como subprocesso dentro da pasta do laboratório. O que faltaria nesse isolamento para que o mesmo laço pudesse rodar numa máquina compartilhada da empresa?

### Evidência a entregar

Entregue as linhas `PARADA`, `ITERACOES`, `TOKENS_TOTAIS` e `VERDADE_FINAL` de três execuções: duas com condição de parada objetiva e uma autodeclarada. Preencha o quadro abaixo e conclua em até cinco linhas qual teto você definiria para este laço em produção e o que o sistema deve fazer ao atingi-lo.

| Execução | Parada | Iterações | *Tokens* | Verdade final | Desfecho aceitável? |
|---|---|---:|---:|---|---|
| Objetiva 1 |  |  |  |  |  |
| Objetiva 2 |  |  |  |  |  |
| Autodeclarada |  |  |  |  |  |

Registre também uma [fitness function de operação de laço](lacos-desassistidos.md#fitness-functions-de-operacao-de-laco), com limiar, responsável e consequência diante da falha.

### Limpeza e contingência

Apague a pasta gerada com `rm -rf loop-sandbox` (no PowerShell, `Remove-Item -Recurse -Force loop-sandbox`). Para liberar espaço, `ollama rm qwen2.5-coder:7b`.

Se o laço encerrar na primeira iteração com `GUARDA: recusado`, leia a linha `MOTIVO`: a guarda estática recusou o código antes de executá-lo, que é o comportamento correto. Se `pytest` não for encontrado, confirme o ambiente virtual ativo e `python -m pip show pytest`. Não desative a guarda estática para fazer o laboratório passar.

## Ferramentas adicionais

O laboratório usou OpenTelemetry para expor spans de uma chamada de plataforma. O mercado tem plataformas dedicadas de observabilidade, gateways e controle de entrega que assumem esse sinal e o transformam em operação contínua. Investigação livre, fora do escopo avaliado desta oficina.

| Ferramenta | Site | Propósito |
|---|---|---|
| Langfuse | [langfuse.com](https://langfuse.com) | Plataforma open source de observabilidade e avaliação para aplicações de LLM, agnóstica de framework |
| LangSmith | [langchain.com/langsmith](https://www.langchain.com/langsmith) | Observabilidade e avaliação integradas ao ecossistema LangChain/LangGraph |
| Helicone | [helicone.ai](https://www.helicone.ai) | Observabilidade de custo e uso com múltiplos provedores de modelo, integração leve por proxy |
| Weights & Biases Weave | [wandb.ai/site/weave](https://wandb.ai/site/weave/) | Rastreamento de execuções e avaliação para aplicações de IA generativa, integrado ao ecossistema W&B |
| LaunchDarkly | [launchdarkly.com](https://launchdarkly.com) | Plataforma de feature flags e liberação progressiva (canary), aplicável ao rollout controlado de mudanças em produtos de IA |
| OpenTelemetry GenAI Semantic Conventions | [github.com/open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai) | Convenções semânticas específicas para spans de chamadas de modelo, tokens e ferramentas |
