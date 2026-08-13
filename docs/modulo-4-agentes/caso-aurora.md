# Caso contínuo: Cooperativa Aurora — autonomia

**Caso contínuo — Cooperativa Aurora.** [← Módulo 3: RAG](../modulo-3-rag/caso-aurora.md) · [Módulo 5: Confiança e avaliação →](../modulo-5-confianca/caso-aurora.md)

O [Módulo 2](../modulo-2-desenho-conceitual/caso-aurora.md) decidiu manter a Cooperativa Aurora sem agente. O [Módulo 3](../modulo-3-rag/caso-aurora.md) deu a ela seu próprio caminho de conhecimento (RAG híbrido em lote com adaptador de leitura). Este módulo reavalia autonomia com a evidência acumulada até aqui — e a Aurora **não** chega à mesma conclusão do [Banco Lume](caso-lume.md), tratado em sua própria página.

## Os dois gatilhos do ADR-Aurora-001 se cumprem

No Módulo 3, a Aurora ganhou um adaptador de leitura quase em tempo real sobre contrato e pagamento dos sistemas legados (só leitura, sem idempotência de gravação) para sustentar a atualização do índice de RAG. Essa mesma capacidade de leitura, somada à evidência de que a ordem de consulta entre contrato, pagamento e política varia por campanha de forma não enumerável, cumpre os dois gatilhos de reavaliação registrados no ADR-Aurora-001 do Módulo 2.

### Contratos de ferramenta (somente leitura)

| Ferramenta | Efeito | Autorização | Idempotência |
|---|---|---|---|
| `consultar_contrato` | leitura | identidade do especialista + finalidade renegociação | não aplicável (sem efeito) |
| `consultar_pagamento` | leitura | idem | não aplicável |
| `consultar_politica_campanha` | leitura | idem + vigência da campanha | não aplicável |

Nenhuma ferramenta grava, altera contrato, limite, taxa ou status, nem envia comunicação — restrições confirmadas desde o Módulo 2. O agente **propõe** um dossiê de renegociação; não existe ferramenta de efeito neste incremento.

### Autonomia orçada

Nível [A2 — recomendar](padroes-e-decisoes.md#matriz-de-autonomia): o agente escolhe quais ferramentas de leitura consultar e em que ordem; a pessoa especialista revisa e recomenda; o aprovador distinto aprova ou devolve, como já valia no Módulo 2. Orçamento de passos: no máximo 6 chamadas de ferramenta por solicitação; ao aproximar do teto, o agente conclui com o que tem e sinaliza lacuna, em vez de repetir chamadas.

```mermaid
flowchart LR
    E[Especialista] --> AG[Agente]
    AG -->|consultar_contrato| L1[Sistemas legados: contrato]
    AG -->|consultar_pagamento| L2[Sistemas legados: pagamento]
    AG -->|consultar_politica_campanha| P[Política de campanha]
    AG --> D[Dossiê proposto]
    D --> ESP[Especialista revisa]
    ESP --> AP[Aprovador]
```

**Equivalente textual.** O agente decide a ordem das três consultas de leitura conforme o caso, mas nunca grava nem comunica. O dossiê proposto sempre passa por revisão do especialista e aprovação de pessoa distinta antes de qualquer oferta.

### ADR-Aurora-003 — Agente com ferramentas somente leitura, orçamento de passos

**Status.** Proposta.

**Contexto.** Os dois gatilhos do ADR-Aurora-001 (Módulo 2) se cumpriram: leitura quase em tempo real sobre legados (Módulo 3) e sequência de consulta não enumerável por campanha. Revisão humana obrigatória e segregação entre proponente e aprovador continuam restrições confirmadas.

**Direcionadores da decisão.** Reduzir o tempo de consolidação de contrato, pagamento e política sem ampliar autoridade além de leitura; manter aprovação humana antes de qualquer oferta; tornar o caminho de decisão do agente reconstruível — ver atributos [Autonomia](../referencia/atributos-de-qualidade.md#autonomia) e [Observabilidade](../referencia/atributos-de-qualidade.md#observabilidade).

**Opções.**

1. **Manter copiloto com contexto fixo (status quo do Módulo 2/3):** simples e previsível, mas não se adapta quando a ordem de consulta varia por campanha, deixando lacunas manuais.
2. **Agente com ferramentas somente leitura e orçamento de passos:** adapta a sequência a cada caso, mantendo aprovação humana e nenhuma ferramenta de efeito.
3. **Agente com ferramentas de leitura e escrita:** resolveria também a criação da oferta, mas contraria a restrição confirmada de revisão humana obrigatória e ausência de gravação por modelo.

**Decisão.** Adotar a opção 2, usando os padrões [Uso controlado de ferramentas](../referencia/catalogo-de-padroes.md#uso-controlado-de-ferramentas), [Agente com orçamento limitado](../referencia/catalogo-de-padroes.md#agente-com-orcamento-limitado) e [Aprovação humana por risco](../referencia/catalogo-de-padroes.md#aprovacao-humana-por-risco).

**Consequências.** Ganha-se adaptação à variação real de campanhas sem ampliar autoridade de efeito. Em troca, o time assume contratos de ferramenta, autorização por chamada, orçamento de passos e avaliação de trajetória como responsabilidades novas e permanentes.

**Evidências.** Nos casos do Módulo 3, a ordem de consulta variou em mais de um terço das campanhas testadas, sem padrão fixo previsível por regra simples — o que justifica autonomia de leitura em vez de sequência fixa.

**Gatilhos de revisão.** Reavaliar se alguma trajetória ultrapassar o orçamento de passos com frequência relevante, se o agente repetir a mesma ferramenta com argumentos canônicos sem nova informação, ou se surgir demanda para qualquer ferramenta de efeito.

## Execução local

**Objetivo.** Observar em código a autonomia orçada do ADR-Aurora-003: ferramentas somente leitura, sem efeito, e parada por orçamento de passos — ver [matriz de autonomia](padroes-e-decisoes.md#matriz-de-autonomia) e [Orçamentos, interrupção e fallback](padroes-e-decisoes.md#orcamentos-interrupcao-e-fallback).

**Pré-requisitos.** Python 3.11+, o mesmo padrão de venv das oficinas anteriores.

**Instalação.**

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install langgraph
```

**Execução.**

```bash
python docs/assets/labs/modulo-4/agente_lume_aurora.py --caso aurora
```

Aceita também `--orcamento N` para variar o teto de chamadas (padrão: 6).

**Resultado esperado.** O script imprime a trajetória entre as três ferramentas de leitura, o número de chamadas usado e o dossiê proposto para revisão. Nesta implementação de referência, a prioridade de consulta é fixa (`contrato` → `pagamento` → `política`) e não muda entre execuções; o que varia é **quantas** chamadas completam antes de o orçamento (`--orcamento`) se esgotar — com `--orcamento 1` o dossiê contém apenas contrato, com `--orcamento 2` contrato e pagamento, e a partir de 3 o dossiê fica completo. É o orçamento de passos do ADR-Aurora-003 em ação, não uma escolha dinâmica de ordem; contrasta com a sequência fixa e sem orçamento do [caso Lume](caso-lume.md).

**Perguntas exploratórias.**

1. Rode o script com `--orcamento 1`, `--orcamento 2` e `--orcamento 6` (repita cada valor duas vezes). O que muda entre as execuções: a ordem das ferramentas ou o número de chamadas completadas?
2. Se o dossiê ficar incompleto (por exemplo, com `--orcamento 1`), quem deveria decidir se o especialista recebe um dossiê parcial ou se a execução é interrompida antes da revisão?
3. O ADR-Aurora-003 descreve um cenário de produção em que "a ordem de consulta variou em mais de um terço das campanhas". O que precisaria mudar neste script para que a ordem de fato dependesse do caso, em vez de seguir sempre a mesma prioridade?

**Entrega de evidência.** Para cada valor de `--orcamento` testado, registre o número de chamadas, o conteúdo do dossiê e a sequência do trace — essa evidência alimenta o exercício [Autonomia orçada em execução real](exercicios.md#13-autonomia-orcada-em-execucao-real).

**Limpeza.** `deactivate` e remover o diretório `.venv`. Nenhum dado real deve substituir os identificadores sintéticos do script.

## Continuidade

O Módulo 5 avalia confiança e risco dos dois casos — a superfície da Aurora é maior por ser agêntica, o que dá contraste direto com o [Lume](../modulo-5-confianca/caso-lume.md).

---

**Continua:** [Módulo 5 — confiança e avaliação](../modulo-5-confianca/caso-aurora.md)
