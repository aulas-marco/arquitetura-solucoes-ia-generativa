# Guia de ferramentas e plataformas

## Como usar este guia

Ferramenta não é decisão arquitetural. Escolha-a para tornar uma hipótese observável: contrato, fronteira de dados, evidência recuperada, estado de um workflow, resultado de avaliação ou trace. Um framework organiza componentes; ele não substitui os critérios da decisão. Nas oficinas, o ponto de partida é sempre local, open source e baseado em dados sintéticos.

Antes de instalar algo, registre: qual decisão quer observar, qual entrada sintética será usada, que resultado espera ver, que arquivo será produzido e como limpar o ambiente.

## Mapa das ferramentas da disciplina

| Módulo | Ferramenta local open source | O que o aluno executa | Evidência arquitetural |
|---|---|---|---|
| Fundamentos | Ollama | modelo e temperatura pela API local | contexto, fonte e variação |
| Desenho conceitual | LiteLLM Proxy + Ollama | gateway e manifesto de modelo | contrato estável e troca de destino |
| RAG | LangChain + Chroma + Ollama | ingestão e recuperação de corpus | ID, versão, trecho e citação |
| Agentes | LangGraph | workflow com aprovação simulada | estado, idempotência e parada |
| Confiança | DeepEval + Ollama | casos e relatório de avaliação | regra, falha e justificativa |
| Operação | OpenTelemetry + LiteLLM Proxy | trace de chamada sintética | atributo, duração e recuperação |

## Critérios de seleção

| Pergunta de decisão | Evidência mínima no laboratório | Risco a controlar |
|---|---|---|
| O dado pode deixar o dispositivo? | descrição da entrada, saída e fronteira local | exposição indevida |
| O contrato do modelo é portátil? | manifesto, alias e requisição imutável | acoplamento do produto ao modelo |
| O contexto é rastreável? | corpus, IDs, versões e trechos recuperados | resposta sem fonte autorizada |
| Um agente pode agir? | estado, aprovação e chave de idempotência | efeito não autorizado ou duplicado |
| A resposta está pronta para uso? | caso, critério e relatório | julgamento sem evidência |
| A plataforma é operável? | trace, limiar, dono e ação | alerta sem recuperação |

## Instalação local por papel arquitetural

### Executor de modelos — Ollama

Ollama executa modelos localmente e é o componente comum às oficinas 1, 2, 3, 5 e 6. Instale-o em [ollama.com/download](https://ollama.com/download) e confirme:

```bash
ollama --version
ollama pull llama3.2:3b
```

Para o laboratório RAG, baixe também o modelo de embeddings:

```bash
ollama pull nomic-embed-text
```

### Gateway — LiteLLM Proxy

LiteLLM Proxy faz a aplicação consumir um alias em vez de chamar o modelo diretamente. Ele é usado nos módulos 2 e 6:

```bash
python -m pip install 'litellm[proxy]'
litellm --config litellm_config.yaml --port 4000
```

### Recuperação — LangChain e Chroma

LangChain organiza os componentes; Chroma preserva o índice local. Eles são usados no módulo 3:

```bash
python -m pip install langchain langchain-chroma chromadb langchain-ollama
```

### Orquestração — LangGraph

LangGraph representa estados e transições explícitas no módulo 4:

```bash
python -m pip install langgraph langchain-ollama
```

### Avaliação — DeepEval

DeepEval transforma casos e critérios em resultados comparáveis. No módulo 5, o juiz é o Ollama local:

```bash
python -m pip install deepeval
```

### Observação — OpenTelemetry

OpenTelemetry descreve spans e atributos sem prender a arquitetura a um único backend. O módulo 6 usa o exportador de console:

```bash
python -m pip install opentelemetry-api opentelemetry-sdk
```

## Limites que permanecem mesmo em ambiente local

Ambiente local não elimina custo de CPU, memória, disco, energia ou tempo de instalação. Também não transforma um corpus sintético em fonte autorizada de produção. Use os laboratórios para observar decisões, declarar pressupostos e formular testes; não para validar um sistema real com dados reais.

## Checklist de encerramento

- [ ] Dados, prompts, respostas e capturas são sintéticos.
- [ ] A ferramenta, versão e modelo usados foram registrados na evidência.
- [ ] Arquivos temporários, índices e relatórios foram removidos ou guardados conscientemente.
- [ ] A conclusão diferencia o que foi observado do que ainda precisa de avaliação.
- [ ] A próxima ação tem responsável, limiar ou gatilho de revisão.
