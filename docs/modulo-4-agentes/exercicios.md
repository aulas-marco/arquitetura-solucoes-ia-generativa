# Exercícios

Recordar e Compreender possuem respostas públicas. De Aplicar a Criar, produza artefatos contextualizados e use as rubricas. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

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

Um cliente pede “cancele meu pedido e devolva via Pix”. O catálogo contém `consultar_pedido` (leitura), `calcular_elegibilidade` (regra), `propor_cancelamento` (sem efeito), `cancelar_pedido` (escrita), `emitir_reembolso` (financeiro) e `registrar_interacao` (escrita idempotente). Faça a **seleção de ferramentas** para um fluxo controlado: ordem, ferramenta exposta ou não ao modelo, contrato essencial, aprovações e critério de interrupção. Considere pedido já despachado e sistema financeiro indisponível.

**Rubrica (0–5 pontos):** 1 ponto por sequência que separa consulta, regra, proposta e efeito; 1 por catálogo mínimo e justificativa; 1 por identidade, parâmetros, versão e idempotência; 1 por aprovação proporcional antes de cancelamento/reembolso; 1 por falhas, estado parcial e fallback sem prometer conclusão.

### 9. Classificação de autonomia

Faça a **classificação de autonomia** A0–A5 para: responder horário, consultar pedido próprio, sugerir substituto, reservar item, cancelar pedido de R$ 80, cancelar pedido de R$ 8 mil e conceder desconto excepcional. Preencha uma matriz com risco, reversibilidade, identidade, aprovação antes, revisão depois, orçamento e condição que mudaria o nível.

**Rubrica (0–5 pontos):** 1 ponto por classificar por ação e não por produto; 1 por ligar nível a efeito/reversibilidade; 1 por aprovação e revisão coerentes; 1 por limites mensuráveis; 1 por gatilhos de promoção/redução sustentados por evidência.

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

**Rubrica (0–6 pontos):** 1 ponto pela reconstrução causal sustentada pelo trace; 1 pela análise explícita das incertezas; 1 pela identificação de violações de contrato e estado; 1 pela contenção e recuperação proporcionais; 1 pela coerência das correções propostas; 1 por testes de não recorrência que discriminem as hipóteses.

## Avaliar

### 11. Crítica arquitetural

Faça uma **crítica arquitetural** da proposta: “quatro agentes — CRM, estoque, pedidos e supervisor — compartilham o histórico completo e uma conta administrativa; decidem por maioria; qualquer agente pode delegar; retries são ilimitados; logs guardam prompts; revisão humana semanal corrige erros”. Defenda rejeitar, limitar a experimento ou redesenhar. Compare agente único, múltiplos agentes e workflow; avalie identidade, privacidade, autoridade, consenso, orçamento, idempotência, aprovação e observabilidade. Declare evidência que poderia inverter sua recomendação.

**Rubrica (0–6 pontos):** 1 ponto por julgamento explícito; 1 por localizar falhas causais, não só rótulos; 1 por alternativa mínima; 1 por agente único versus multiagente com métricas; 1 por controles de identidade, efeito e dados; 1 por experimento/gatilho de revisão verificável.

## Criar

### 12. Arquitetura de agente controlado

Crie uma **arquitetura de agente controlado** para resolver solicitações de uma operadora de saúde: consultar cadastro e rede, sugerir prestadores, solicitar pré-autorização e cancelar solicitação ainda não analisada. Decisão clínica, alteração cadastral e aprovação de procedimento ficam fora do agente. Entregue:

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

**Rubrica (0–8 pontos):** 1 ponto por escopo e decisão conceitual; 1 por ferramentas/contratos; 1 por identidade e políticas; 1 por estado/memória/contexto; 1 por autonomia e humanos; 1 por resiliência/compensação; 1 por orçamento, fallback e observabilidade; 1 por diagramas, testes e ADRs coerentes.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
