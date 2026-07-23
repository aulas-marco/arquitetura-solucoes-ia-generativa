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

### 5. Artefatos do SDD

Associe constitution, spec, plan, tasks, implement e verify à pergunta principal que cada artefato responde.

<details>
<summary>Ver resposta</summary>

Constitution responde quais princípios governam o projeto; spec define o que e por que construir; plan registra como a arquitetura realiza a intenção; tasks decompõe em fatias e dependências; implement executa cada fatia com testes; verify demonstra aderência à spec e qualidade técnica.
</details>

## Compreender

### 6. Saída estruturada não é autorização

Explique por que um objeto JSON válido ainda pode produzir ação indevida.

<details>
<summary>Ver resposta</summary>

O esquema garante forma, não intenção, regra de negócio, propriedade do recurso ou limite de risco. Política determinística deve avaliar identidade, ferramenta, parâmetros, estado e delegação imediatamente antes da execução.
</details>

### 7. Aprovar antes e revisar depois

Diferencie aprovação humana antes da ação de revisão humana depois da ação.

<details>
<summary>Ver resposta</summary>

A aprovação prévia bloqueia o efeito até uma pessoa aceitar objeto imutável, evidência e consequência. A revisão posterior detecta e corrige desvios já ocorridos; só é adequada a efeitos aceitáveis, reversíveis ou baixos e não autoriza dano retroativamente.
</details>

### 8. Agente único, múltiplos agentes e fluxo spec-driven

Por que especializar papéis não prova que múltiplos agentes serão melhores, e como uma spec e critérios de aceite limitam essa decisão?

<details>
<summary>Ver resposta</summary>

Especialização pode isolar contexto ou autoridade, mas multiplica handoffs, estados, custos, latência, permissões e falhas de coordenação. Uma spec e critérios de aceite tornam o objetivo e a evidência explícitos; o benefício ainda precisa ser comparado ao agente único e a ferramentas/módulos determinísticos por métricas de tarefa e operação.
</details>

### 9. Spec viva não é documentação extensa

Explique por que o tamanho de uma spec não demonstra que ela é viva ou executável.

<details>
<summary>Ver resposta</summary>

Uma spec é viva quando mudanças de intenção, regra, risco e evidência atualizam o contrato versionado. É executável quando critérios e interfaces conseguem derivar ou verificar planos, tarefas e testes. Um documento longo pode continuar vago, divergente do código e incapaz de decidir aceite.
</details>

## Aplicar

### 10. Seleção de ferramentas

**Situação**

Um cliente pede “cancele meu pedido e devolva via Pix”. O catálogo contém ferramentas de leitura, regra, proposta, escrita financeira e registro idempotente. O pedido pode já ter sido despachado e o sistema financeiro pode estar indisponível.

**Seu papel**

Você é o arquiteto que decide quais capacidades o modelo pode solicitar e quais efeitos permanecem atrás de regras e aprovação.

**Insumos disponíveis**

Use o [catálogo de ferramentas](padroes-e-decisoes.md#comece-pelo-contrato-de-ferramenta), o [contrato de saída estruturada](conceitos.md#uso-de-ferramentas-e-saidas-estruturadas) e o [workflow da oficina local](oficina-de-ferramentas.md). Nenhuma ferramenta real será chamada.

**O que é o artefato que você vai produzir**

Um **contrato de ferramenta** é a interface estreita que declara entrada, saída, efeito, identidade, versão, erros e limites; não é um prompt dizendo “cancele o pedido”. **Idempotência** é a propriedade de repetir a mesma intenção sem criar um segundo efeito lógico: registre uma chave estável e o resultado autoritativo. A sequência deve separar consulta (sem efeito), regra de elegibilidade, proposta (ainda sem efeito) e escrita financeira (efeito material). O modelo pode propor, mas a política e o executor decidem se uma chamada é permitida.

**Como conduzir**

1. Ordene consulta, elegibilidade, proposta e efeito.
2. Marque cada ferramenta como exposta ao modelo, chamada por regra ou proibida naquele estado.
3. Especifique identidade, parâmetros, versão, idempotência e aprovação.
4. Escreva condições de interrupção para pedido despachado, pagamento indisponível e estado desconhecido.

**Entrega esperada**

Entregue uma sequência ou diagrama, catálogo mínimo de contratos e matriz de aprovação e parada.

**Checklist de verificação**

Antes de entregar, verifique os itens abaixo:

- [ ] Cada ferramenta tem entrada, saída, efeito, identidade, versão, erro e chave de idempotência explícitos.
- [ ] O diagrama mostra consulta e regra antes da proposta e da escrita financeira.
- [ ] Pedido despachado, pagamento indisponível e estado desconhecido levam a parada ou encaminhamento, não a retry cego.
- [ ] A aprovação contém objeto imutável, consequência, identidade do aprovador e expiração.
- [ ] Nenhuma chamada real ou credencial é necessária para avaliar o desenho.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Sequência de controle | 20% | Separa consulta, regra, proposta e efeito. |
| Catálogo e contratos | 20% | Expõe somente capacidades necessárias e define entradas e saídas. |
| Identidade e idempotência | 25% | Propaga identidade, versão, chave e repetição segura. |
| Aprovação e parada | 20% | Exige aprovação proporcional e interrompe estados não confirmados. |
| Falhas e comunicação | 15% | Degrada sem prometer conclusão e informa próximo passo. |

### 11. Classificação de autonomia

**Situação**

As ações variam de responder horário a cancelar pedidos e conceder desconto. O nível de autonomia deve acompanhar efeito, reversibilidade e autoridade, não o nome do produto.

**Seu papel**

Você é o arquiteto que define limites de autonomia e explica como eles podem mudar com evidência.

**Insumos disponíveis**

Use a [matriz de autonomia](padroes-e-decisoes.md#matriz-de-autonomia), [estado, memória e contexto](conceitos.md#estado-memoria-e-contexto) e o trace da [oficina local](oficina-de-ferramentas.md#receita-principal). Trate todos os pedidos como fictícios.

**O que significa A0–A5**

A0–A5 é uma escala por ação. Siga a matriz: **A0** não usa escolha do modelo; **A1** informa sem ferramenta de efeito; **A2** recomenda e a pessoa executa; **A3** age de modo reversível e limitado; **A4** aguarda aprovação antes de efeito material; **A5** escolhe sequência dentro de classes aprovadas e limites estreitos. Para cada nível, registre escolha, efeito, identidade, aprovação/revisão e orçamento; o nível depende do cenário, não do produto.

**Como conduzir**

1. Classifique cada ação por efeito, reversibilidade e risco.
2. Para cada nível, registre identidade, aprovação antes, revisão depois e orçamento.
3. Escreva condição concreta que aumentaria ou reduziria o nível.
4. Verifique se o mesmo produto pode ter níveis diferentes por ação.

**Entrega esperada**

Entregue uma matriz A0–A5 e explique dois casos em que a mesma interface precisa de controles diferentes.

**Checklist de verificação**

Antes de entregar, verifique os itens abaixo:

- [ ] Cada ação tem nível, efeito, reversibilidade, identidade e orçamento próprios.
- [ ] A matriz distingue aprovação antes da ação de revisão depois da ação.
- [ ] O mesmo canal pode receber níveis diferentes sem esconder a fronteira no prompt.
- [ ] Há evidência observável para promover ou reduzir autonomia.
- [ ] Nenhuma promoção de nível depende apenas de uma resposta “parecer boa”.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Classificação por ação | 25% | Não atribui autonomia apenas pelo produto ou canal. |
| Efeito e reversibilidade | 25% | Liga nível ao dano possível e à capacidade de desfazer. |
| Aprovação e revisão | 20% | Define controles antes e depois do efeito. |
| Limites | 15% | Usa orçamento, identidade e parâmetros observáveis. |
| Gatilhos | 15% | Define evidência para promover ou reduzir autonomia. |

 

### 12. Clarificação e critérios de aceite

**Situação:** uma área solicita “permita reabrir uma avaliação encerrada”, sem informar autoridade, prazo, efeito sobre notas publicadas, auditoria ou reversão.

**Seu papel:** você responde pelo Gate 1 e deve tornar a intenção implementável sem escolher tecnologia.

**Como conduzir**

1. Construa um ledger com fatos, hipóteses, desconhecidos e fora de escopo.
2. Formule oito perguntas de clarificação ordenadas pelo impacto.
3. Escolha respostas fictícias e declare-as decisões do exercício.
4. Escreva cinco requisitos EARS e três cenários BDD: sucesso, negação e conflito.
5. Defina dois atributos de qualidade mensuráveis e quatro itens fora de escopo.

**Entrega esperada:** mini-spec de duas a quatro páginas que outra pessoa revise sem a conversa original.

**Critérios de avaliação**

| Critério | Peso | Evidência |
|---|---:|---|
| Incerteza explícita | 20% | Não transforma hipótese em fato. |
| Perguntas | 20% | Cobrem autoridade, estado, consequência e reversibilidade. |
| Requisitos | 25% | Condição e resposta são observáveis. |
| Aceite e qualidade | 25% | Cenários e medidas permitem decidir. |
| Escopo | 10% | Evita implementação especulativa. |

## Analisar

### 13. Diagnóstico de trace

**Situação**

O cliente recebeu duas reservas e nenhum cancelamento:

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

Há uma observação externa de duas reservas e nenhum cancelamento. O trace prova duas propostas, duas chaves, um timeout, uma reserva `R2`, um conflito e o estado `completed`; não prova se a chamada que expirou teve efeito. Separe essa observação externa do que o trace demonstra.

**Seu papel**

Você é o arquiteto de confiabilidade que separa fato, hipótese e estado autoritativo antes de corrigir o workflow.

**Insumos disponíveis**

Use o trace acima, os conceitos de timeout, idempotência e estado desconhecido em [conceitos de agentes](conceitos.md), as regras de [padrões e decisões](padroes-e-decisoes.md) e o script da [oficina de agentes](oficina-de-ferramentas.md).

**O que é trace, timeout e estado desconhecido**

Um [**trace**](padroes-e-decisoes.md#auditoria-e-observabilidade) é a sequência correlacionada de propostas, políticas, chamadas, tentativas, versões e resultados de uma execução. **Timeout** encerra a espera local; não prova que o destino não executou. Por isso uma escrita que excede o prazo entra em **estado desconhecido** (`outcome_unknown`) até reconciliação no sistema de destino pela mesma chave. Fato observado, hipótese (“a primeira reserva foi criada”), contenção e reconciliação devem aparecer em colunas separadas.

**Como conduzir**

Faça o **diagnóstico de trace** usando a sequência acima.

1. Reescreva a sequência em linha do tempo com chamada, política, chave e resultado.
2. Marque o que o trace prova e formule hipóteses para timeout e reserva duplicada.
3. Defina contenção, reconciliação e eventual compensação antes de nova tentativa.
4. Proponha correções e testes que discriminem as hipóteses.

**Entrega esperada**

Entregue linha do tempo anotada, decisão sobre `completed` e plano de recuperação e não recorrência.

**Checklist de verificação**

Antes de entregar, verifique os itens abaixo:

- [ ] A linha do tempo preserva `execution_id`, chave de cada tentativa, política, versão e resultado.
- [ ] O timeout é tratado como estado desconhecido até consulta autoritativa no destino.
- [ ] A decisão sobre `completed` cita evidência; não usa apenas a última linha do trace.
- [ ] A contenção impede nova escrita antes da reconciliação e prevê compensação se houver efeito.
- [ ] Os testes cobrem repetição, conflito de versão, timeout com efeito e timeout sem efeito.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Causalidade | 20% | Reconstrói o que ocorreu sem inventar o resultado do timeout. |
| Incertezas | 20% | Identifica evidências ausentes e hipóteses alternativas. |
| Contratos e estado | 20% | Localiza violações de idempotência, versão e estado autoritativo. |
| Recuperação | 20% | Propõe contenção, reconciliação e compensação proporcionais. |
| Testes | 20% | Define casos que diferenciam hipóteses. |

### 14. Consistência entre spec, plano, tarefas e testes

**Situação:** a spec exige autorização por unidade, expiração em 24 horas e auditoria sem conteúdo. O plano descreve link público por sete dias. As tarefas incluem envio por e-mail, embora esteja fora de escopo. Os testes validam apenas geração do arquivo.

**Como conduzir**

1. Construa a matriz `requisito → plano → tarefa → teste`.
2. Classifique achados como lacuna, contradição, ambiguidade ou *scope creep*.
3. Indique o artefato que deve mudar e a autoridade que aprova.
4. Separe bloqueios de riscos residuais.
5. Proponha tarefas como fatias verticais com bloqueadores.

**Entrega esperada:** relatório de consistência com severidade, evidência, correção e decisão de gate.

**Critérios de avaliação**

| Critério | Peso | Evidência |
|---|---:|---|
| Cobertura | 25% | Mapeia requisitos e fora de escopo. |
| Classificação | 20% | Distingue tipos de inconsistência. |
| Autoridade | 15% | Agente não redefine produto ou risco. |
| Fatias | 25% | Cada tarefa entrega comportamento. |
| Gate | 15% | Bloqueios são proporcionais. |

## Avaliar

### 15. Crítica arquitetural

**Situação**

Uma proposta usa quatro agentes com histórico completo, conta administrativa, decisão por maioria, delegação livre, retries ilimitados e revisão humana semanal. Ela mistura autonomia, acesso e efeito sem indicar autoridade final.

**Seu papel**

Você é o arquiteto que critica a composição e propõe o menor redesenho capaz de reduzir os riscos mais graves.

**Insumos disponíveis**

Use o [modelo de interação e controle](conceitos.md), o [catálogo de ferramentas](padroes-e-decisoes.md#comece-pelo-contrato-de-ferramenta) e os padrões de agente único, multiagente e workflow descritos em [padrões e decisões](padroes-e-decisoes.md).

**O que significa comparar essas composições**

Compare três composições concretas: um agente único, vários agentes com handoffs e um workflow determinístico com módulos de geração. Para cada uma, indique onde ficam identidade, decisão, autorização, efeito, trace e revisão. Use métricas de tarefa (conclusão, negação correta, duplicação) e de operação (latência, custo, incidentes); “mais agentes” não é por si só uma melhoria.

**Como conduzir**

1. Escolha rejeitar, limitar a experimento ou redesenhar e escreva o motivo principal.
2. Localize falhas causais em identidade, dados, consenso, retries, efeito e observabilidade.
3. Compare agente único, múltiplos agentes e workflow com métricas adequadas.
4. Defina alternativa mínima, experimento e evidência que poderiam inverter a recomendação.

**Entrega esperada**

Entregue parecer de até 500 palavras, matriz de riscos e experimento de revisão.

**Checklist de verificação**

Antes de entregar, verifique os itens abaixo:

- [ ] Cada risco aponta para uma causa, um efeito e uma evidência que pode ser observada.
- [ ] A proposta não usa conta administrativa ou histórico completo sem finalidade e controle.
- [ ] Retries têm limite, condição e idempotência; revisão semanal não substitui bloqueio prévio.
- [ ] A alternativa mínima preserva autoridade final e permite rollback.
- [ ] O experimento define grupo de comparação, métrica, duração e gatilho de decisão.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Julgamento | 20% | Assume posição clara sobre a proposta. |
| Causas e efeitos | 20% | Liga cada risco a mecanismo, efeito e evidência. |
| Alternativa mínima | 20% | Reduz complexidade sem esconder responsabilidades. |
| Comparação | 20% | Compara arquiteturas com métricas e condições. |
| Revisão | 20% | Define teste e gatilho capazes de alterar o julgamento. |

### 16. Comparação de fluxos SDD

**Situação:** o fluxo A usa um agente para especificar, implementar e revisar. O fluxo B usa Spec Kit, revisões separadas de Spec e Standards e três gates. B dobra a preparação, mas reduz retrabalho; A produz protótipos mais cedo.

**Como conduzir**

1. Defina critérios de risco, reversibilidade, coordenação, rastreabilidade, lead time e retrabalho.
2. Pondere-os para protótipo descartável e autorização financeira.
3. Avalie independência das revisões e risco de aprovação automática.
4. Considere uma opção híbrida.
5. Declare evidências de 60 dias que poderiam inverter a escolha.

**Entrega esperada:** matriz, recomendação por classe, riscos residuais e experimento de adoção.

**Critérios de avaliação**

| Critério | Peso | Evidência |
|---|---:|---|
| Contexto | 25% | Pesos mudam por classe. |
| Trade-offs | 25% | Considera preparação e retrabalho. |
| Governança | 20% | Avalia autoridade e independência. |
| Recomendação | 15% | Decorre da matriz. |
| Experimento | 15% | Métricas podem inverter a decisão. |

## Criar

### 17. Arquitetura de agente controlado

**Situação**

Uma operadora de saúde quer consultar cadastro e rede, sugerir prestadores, solicitar pré-autorização e cancelar uma solicitação ainda não analisada. Decisão clínica, alteração cadastral e aprovação ficam fora do agente.

**Seu papel**

Você é o arquiteto que desenha um agente controlado, deixando visíveis intenção, estado, autorização, efeito e recuperação.

**Insumos disponíveis**

Use os conceitos de workflow, ferramentas, estado, memória e autonomia em [conceitos de agentes](conceitos.md), o [diagrama de exemplo](exemplo-arquitetural.md) e o [template de ADR](../referencia/template-adr.md). O caso é sintético.

**O que é um agente controlado neste exercício**

É um componente que escolhe o próximo passo, mas executa ferramentas com contrato, identidade delegada e política verificável. **Estado** é o registro autoritativo; **memória** é informação reutilizável sob finalidade; **trace** é evidência minimizada de decisões e efeitos. ADR significa registro de decisão arquitetural: preencha contexto, decisão, alternativas, consequências, evidência e gatilho. A matriz A0–A5 aparece por ação; consulta, proposta e efeito têm fronteiras diferentes.

**Como conduzir**

1. Declare objetivo, atores, restrições e falhas intoleráveis antes de listar componentes.
2. Compare chatbot, copiloto, workflow e agente e escolha evolução incremental.
3. Defina contratos de duas ferramentas, identidade delegada, estado, memória e autonomia.
4. Desenhe aprovação, idempotência, timeout, compensação, fallback e retomada.
5. Feche com trace minimizado, testes, ADRs e condição de evolução.

**Entrega esperada**

Entregue o roteiro preenchido, diagramas com equivalentes textuais, três ADRs e quatro testes de comportamento.

**Checklist de verificação**

Antes de entregar, verifique os itens abaixo:

- [ ] O objetivo e as falhas intoleráveis definem o limite do agente antes dos componentes.
- [ ] Cada contrato declara parâmetros, identidade, aprovação, idempotência, timeout e resultado tipado.
- [ ] Estado, memória, contexto e trace têm finalidade, retenção e controle de acesso definidos.
- [ ] O caminho de efeito passa por política antes e depois de esperas, conflitos ou retomadas.
- [ ] Os quatro testes cobrem caminho feliz, negação, repetição e compensação sem usar dados reais.

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

### 18. Iniciativa completa com SDD

Escolha uma feature do projeto final que atravesse interface, regra, dados, integração e operação, com ao menos um risco de segurança e um atributo de qualidade.

**Como conduzir**

1. Escreva constitution com cinco princípios acionáveis.
2. Produza spec com histórias, EARS, BDD, RNFs, segurança e fora de escopo.
3. Compare duas arquiteturas e registre um ADR.
4. Identifique seams e estratégia de testes.
5. Fatia o plano e desenhe dependências.
6. Defina papéis humanos, agentes e três gates.
7. Crie matriz `requisito → decisão → tarefa → teste → evidência`.
8. Defina métricas e feedback de produção para a spec.

**Entrega esperada:** pacote versionável que outra equipe consiga implementar sem decisões ocultas em conversa.

**Critérios de avaliação**

| Critério | Peso | Evidência |
|---|---:|---|
| Intenção e domínio | 15% | Problema e escopo explícitos. |
| Arquitetura e ADR | 15% | Alternativas ligadas a requisitos. |
| Fatias e seams | 20% | Trabalho integrável e testável. |
| Segurança e qualidade | 15% | Riscos entram antes do código. |
| Governança | 15% | Autoridade, agentes e gates claros. |
| Rastreabilidade | 10% | Matriz navegável nos dois sentidos. |
| Evolução | 10% | Produção retroalimenta a spec. |

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
