# Exercícios

Recordar e Compreender possuem respostas públicas. De Aplicar a Criar, produza artefatos contextualizados e use os critérios de avaliação para revisar a decisão. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

## Recordar

### 1. Quatro formas de controle

Defina chatbot, copiloto, workflow determinístico e agente em uma frase cada.

<details>
<summary>Ver resposta</summary>

Chatbot é interface conversacional. Copiloto apoia uma pessoa, que preserva a decisão/execução. Workflow determinístico tem etapas e transições definidas pela aplicação, ainda que use geração. Agente delega ao modelo a escolha de próximos passos ou ferramentas dentro de limites.
</details>

### 2. Estado e memórias

Nomeie estado da execução, memória de trabalho, memória persistente e contexto.

<details>
<summary>Ver resposta</summary>

Estado é o registro autoritativo da trajetória e dos efeitos. Memória de trabalho é temporária e específica da execução. Memória persistente atravessa execuções sob finalidade e governança. Contexto é a visão limitada enviada ao modelo em uma chamada.
</details>

### 3. Contrato de ferramenta

Liste seis campos de um contrato de ferramenta além de nome e descrição.

<details>
<summary>Ver resposta</summary>

Esquemas de entrada/saída, classe de efeito, erros tipados, identidade/autorização, idempotência, concorrência, timeout, retry, auditoria, dados sensíveis, versão e compensação são respostas válidas.
</details>

### 4. Resiliência

Defina idempotência, timeout, retry, circuit breaker e compensação.

<details>
<summary>Ver resposta</summary>

Idempotência evita efeitos lógicos duplicados; timeout limita espera sem provar ausência de efeito; retry repete falha transitória de modo limitado e seguro; circuit breaker interrompe pressão sobre dependência degradada; compensação desfaz ou neutraliza um efeito confirmado quando rollback global não existe.
</details>

## Compreender

### 5. Saída estruturada não é autorização

Explique por que um objeto JSON válido ainda pode produzir ação indevida.

<details>
<summary>Ver resposta</summary>

O esquema garante forma, não intenção, regra de negócio, propriedade do recurso ou limite de risco. Política determinística deve avaliar identidade, ferramenta, parâmetros, estado e delegação imediatamente antes da execução.
</details>

### 6. Aprovar antes e revisar depois

Diferencie aprovação humana antes da ação de revisão humana depois da ação.

<details>
<summary>Ver resposta</summary>

A aprovação prévia bloqueia o efeito até uma pessoa aceitar objeto imutável, evidência e consequência. A revisão posterior detecta e corrige desvios já ocorridos; só é adequada a efeitos aceitáveis, reversíveis ou baixos e não autoriza dano retroativamente.
</details>

### 7. Agente único versus múltiplos agentes

Por que especializar papéis não prova que múltiplos agentes serão melhores?

<details>
<summary>Ver resposta</summary>

Especialização pode isolar contexto ou autoridade, mas multiplica handoffs, estados, custos, latência, permissões e falhas de coordenação. O benefício precisa ser comparado ao agente único e a ferramentas/módulos determinísticos por métricas de tarefa e operação.
</details>

## Aplicar

### 8. Seleção de ferramentas

**Situação**

Um cliente pede “cancele meu pedido e devolva via Pix”. O catálogo contém ferramentas de leitura, regra, proposta, escrita financeira e registro idempotente. O pedido pode já ter sido despachado e o sistema financeiro pode estar indisponível.

**Seu papel**

Você é o arquiteto que decide quais capacidades o modelo pode solicitar e quais efeitos permanecem atrás de regras e aprovação.

**Insumos disponíveis**

Use o catálogo de ferramentas, o contrato de saída estruturada e o [workflow da oficina local](oficina-de-ferramentas.md). Nenhuma ferramenta real será chamada.

**Como conduzir**

1. Ordene consulta, elegibilidade, proposta e efeito.
2. Marque cada ferramenta como exposta ao modelo, chamada por regra ou proibida naquele estado.
3. Especifique identidade, parâmetros, versão, idempotência e aprovação.
4. Escreva condições de interrupção para pedido despachado, pagamento indisponível e estado desconhecido.

**Entrega esperada**

Entregue uma sequência ou diagrama, catálogo mínimo de contratos e matriz de aprovação e parada.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Sequência de controle | 20% | Separa consulta, regra, proposta e efeito. |
| Catálogo e contratos | 20% | Expõe somente capacidades necessárias e define entradas e saídas. |
| Identidade e idempotência | 25% | Propaga identidade, versão, chave e repetição segura. |
| Aprovação e parada | 20% | Exige aprovação proporcional e interrompe estados não confirmados. |
| Falhas e comunicação | 15% | Degrada sem prometer conclusão e informa próximo passo. |

### 9. Classificação de autonomia

**Situação**

As ações variam de responder horário a cancelar pedidos e conceder desconto. O nível de autonomia deve acompanhar efeito, reversibilidade e autoridade, não o nome do produto.

**Seu papel**

Você é o arquiteto que define limites de autonomia e explica como eles podem mudar com evidência.

**Insumos disponíveis**

Use a escala A0–A5, o padrão de aprovação e os exemplos de estado e memória do módulo. Trate todos os pedidos como fictícios.

**Como conduzir**

1. Classifique cada ação por efeito, reversibilidade e risco.
2. Para cada nível, registre identidade, aprovação antes, revisão depois e orçamento.
3. Escreva condição concreta que aumentaria ou reduziria o nível.
4. Verifique se o mesmo produto pode ter níveis diferentes por ação.

**Entrega esperada**

Entregue uma matriz A0–A5 e explique dois casos em que a mesma interface precisa de controles diferentes.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Classificação por ação | 25% | Não atribui autonomia apenas pelo produto ou canal. |
| Efeito e reversibilidade | 25% | Liga nível ao dano possível e à capacidade de desfazer. |
| Aprovação e revisão | 20% | Define controles antes e depois do efeito. |
| Limites | 15% | Usa orçamento, identidade e parâmetros observáveis. |
| Gatilhos | 15% | Define evidência para promover ou reduzir autonomia. |

 

## Analisar

### 10. Diagnóstico de trace

Faça o **diagnóstico de trace** abaixo. O cliente recebeu duas reservas e nenhum cancelamento:

```text
10:00:00 execution E7 budget.steps=6
10:00:01 model -> reservar_item(order=42, sku=B, qty=1)
10:00:01 policy allow v9
10:00:01 call key=E7-step2-attempt1 -> timeout
10:00:03 model -> reservar_item(order=42, sku=B, qty=1)
10:00:03 policy allow v9
10:00:03 call key=E7-step3-attempt1 -> reservation R2
10:00:04 order update -> conflict expected=v4 actual=v5
10:00:04 execution completed
```

Reconstrua causas e violações. Indique evidências ausentes, contenção, reconciliação, compensação, correções de idempotência/estado e testes de não recorrência. Discuta os significados possíveis do timeout e avalie se o estado `completed` é sustentado pelas evidências.

**Situação**

O trace mostra duas tentativas de reservar o mesmo item, um timeout, uma chave diferente e um conflito de versão, mas termina como `completed`. Ele não prova sozinho se a primeira tentativa teve efeito.

**Seu papel**

Você é o arquiteto de confiabilidade que separa fato, hipótese e estado autoritativo antes de corrigir o workflow.

**Insumos disponíveis**

Use o trace acima, os conceitos de timeout, idempotência e estado desconhecido e o script da oficina de agentes.

**Como conduzir**

1. Reescreva a sequência em linha do tempo com chamada, política, chave e resultado.
2. Marque o que o trace prova e formule hipóteses para timeout e reserva duplicada.
3. Defina contenção, reconciliação e eventual compensação antes de nova tentativa.
4. Proponha correções e testes que discriminem as hipóteses.

**Entrega esperada**

Entregue linha do tempo anotada, decisão sobre `completed` e plano de recuperação e não recorrência.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Causalidade | 20% | Reconstrói o que ocorreu sem inventar o resultado do timeout. |
| Incertezas | 20% | Identifica evidências ausentes e hipóteses alternativas. |
| Contratos e estado | 20% | Localiza violações de idempotência, versão e estado autoritativo. |
| Recuperação | 20% | Propõe contenção, reconciliação e compensação proporcionais. |
| Testes | 20% | Define casos que diferenciam hipóteses. |

## Avaliar

### 11. Crítica arquitetural

**Situação**

Uma proposta usa quatro agentes com histórico completo, conta administrativa, decisão por maioria, delegação livre, retries ilimitados e revisão humana semanal. Ela mistura autonomia, acesso e efeito sem indicar autoridade final.

**Seu papel**

Você é o arquiteto que critica a composição e propõe o menor redesenho capaz de reduzir os riscos mais graves.

**Insumos disponíveis**

Use o modelo de interação e controle, o catálogo de ferramentas e os padrões de agente único, multiagente e workflow.

**Como conduzir**

1. Escolha rejeitar, limitar a experimento ou redesenhar e escreva o motivo principal.
2. Localize falhas causais em identidade, dados, consenso, retries, efeito e observabilidade.
3. Compare agente único, múltiplos agentes e workflow com métricas adequadas.
4. Defina alternativa mínima, experimento e evidência que poderiam inverter a recomendação.

**Entrega esperada**

Entregue parecer de até 500 palavras, matriz de riscos e experimento de revisão.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Julgamento | 20% | Assume posição clara sobre a proposta. |
| Causas e efeitos | 20% | Liga cada risco a mecanismo, efeito e evidência. |
| Alternativa mínima | 20% | Reduz complexidade sem esconder responsabilidades. |
| Comparação | 20% | Compara arquiteturas com métricas e condições. |
| Revisão | 20% | Define teste e gatilho capazes de alterar o julgamento. |

## Criar

### 12. Arquitetura de agente controlado

**Situação**

Uma operadora de saúde quer consultar cadastro e rede, sugerir prestadores, solicitar pré-autorização e cancelar uma solicitação ainda não analisada. Decisão clínica, alteração cadastral e aprovação ficam fora do agente.

**Seu papel**

Você é o arquiteto que desenha um agente controlado, deixando visíveis intenção, estado, autorização, efeito e recuperação.

**Insumos disponíveis**

Use os conceitos de workflow, ferramentas, estado, memória e autonomia, o diagrama de exemplo e o [template de ADR](../referencia/template-adr.md). O caso é sintético.

**Como conduzir**

1. Declare objetivo, atores, restrições e falhas intoleráveis antes de listar componentes.
2. Compare chatbot, copiloto, workflow e agente e escolha evolução incremental.
3. Defina contratos de duas ferramentas, identidade delegada, estado, memória e autonomia.
4. Desenhe aprovação, idempotência, timeout, compensação, fallback e retomada.
5. Feche com trace minimizado, testes, ADRs e condição de evolução.

**Entrega esperada**

Entregue o roteiro preenchido, diagramas com equivalentes textuais, três ADRs e quatro testes de comportamento.

```text
Objetivo, atores, restrições e falhas intoleráveis:
Comparação chatbot/copiloto/workflow/agente e decisão incremental:
Catálogo mínimo e contratos completos de duas ferramentas:
Identidade, autorização delegada, segredos e políticas:
Estado, memória de trabalho, memória persistente e contexto:
Matriz de autonomia por ação e justificativas:
Aprovação antes, revisão depois e experiência de contestação:
APIs, mensagens/eventos, adaptadores e consistência:
Idempotência, timeout, retry, circuit breaker e concorrência:
Saga, compensações e efeitos residuais:
Orçamentos de etapas, tempo, custo, tokens e ações:
Fallback determinístico, interrupção e retomada:
Agente único versus múltiplos agentes e critério de evolução:
Trace/auditoria com minimização e retenção:
Diagrama de componentes e sequência com equivalentes textuais:
Teste do caminho feliz, negação, repetição e compensação:
Três ADRs com alternativas, consequências e gatilhos:
```

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Escopo e decisão | 10% | Delimita o que o agente pode e não pode fazer. |
| Ferramentas e contratos | 15% | Define catálogo, parâmetros, autoridade e resultados. |
| Identidade, estado e autonomia | 15% | Propaga identidade e controla memória, contexto e efeitos. |
| Aprovação e resiliência | 15% | Inclui aprovação, timeout, idempotência, compensação e retomada. |
| Operação e observabilidade | 10% | Define orçamento, fallback, trace e retenção proporcional. |
| Diagramas, testes e ADRs | 20% | Mantém artefatos coerentes e verificáveis. |
| Clareza da composição | 15% | Permite revisar o fluxo sem inferir responsabilidades ocultas. |

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
