# Exercícios

Responda antes de abrir os blocos de feedback. Recordar e Compreender possuem respostas públicas; Aplicar, Analisar, Avaliar e Criar dependem de contexto e apresentam critérios de avaliação. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

## Recordar

### 1. Elementos do CONOPS

Liste seis elementos que um conceito de operações deve explicitar.

<details>
<summary>Ver resposta</summary>

Uma resposta possível: atores e responsabilidades; informação e autoridade; atividades humanas; modos operacionais; efeitos permitidos e proibidos; degradação e recuperação. Evidências e condições de contestação também são elementos válidos.
</details>

### 2. Classes de objetivo

Nomeie as quatro classes de objetivo usadas para evitar confundir resultado final e métrica intermediária.

<details>
<summary>Ver resposta</summary>

Objetivo de negócio, objetivo de produto, objetivo de dados e objetivo de IA.
</details>

### 3. Requisito significativo

Defina requisito arquiteturalmente significativo e cite dois sinais usados para identificá-lo.

<details>
<summary>Ver resposta</summary>

É um requisito cuja satisfação influencia de modo relevante estrutura, interfaces ou mecanismos. Sinais incluem atravessar componentes ou fronteiras, determinar atributo de qualidade, responder a risco ou obrigação alta e restringir opções de difícil reversão.
</details>

### 4. Partes do critério probabilístico

Liste cinco partes que tornam um critério probabilístico de aceitação verificável.

<details>
<summary>Ver resposta</summary>

Entre as partes estão população, amostra, métrica ou critério qualitativo, limiar, tratamento de incerteza, falha intolerável e ação resultante. Cinco delas atendem ao pedido, desde que definidas para o caso.
</details>

## Compreender

### 5. Valor versus capacidade

Explique por que demonstrar que um modelo resume bem documentos não confirma que um copiloto reduzirá o tempo de um processo.

<details>
<summary>Ver resposta</summary>

O resumo demonstra uma hipótese de capacidade sob entradas selecionadas. O valor depende também de coleta e autorização de dados, integração ao trabalho, cobertura de casos, revisão, confiança calibrada e contramétricas. O processo pode continuar lento antes ou depois da geração.
</details>

### 6. Revisão humana efetiva

Explique por que exigir um clique de aprovação não é, por si só, controle humano.

<details>
<summary>Ver resposta</summary>

O revisor precisa de competência, tempo, autoridade, evidências e interface para discordar. Sem essas condições, a aprovação pode virar ritual e aumentar dependência da recomendação. Responsabilidades, exceções e registro de correções devem estar no desenho.
</details>

### 7. Restrição versus preferência

Distinga restrição de preferência e explique o efeito de classificá-las incorretamente.

<details>
<summary>Ver resposta</summary>

Restrição limita o espaço de solução por obrigação confirmada; preferência favorece uma opção, mas pode ser negociada. Tratar preferência como restrição elimina alternativas prematuramente; tratar obrigação como preferência admite soluções inviáveis ou não conformes.
</details>

## Aplicar

### 8. Ficha de oportunidade para triagem jurídica

**O que é:** ficha de oportunidade descreve problema observável, impacto e teste; não é lista de ferramentas.

**Onde encontrar:** use [CONOPS](conceitos.md#conops-o-sistema-em-operacao), objetivos e o [template de ADR](../referencia/template-adr.md).

**Situação**

Um departamento quer “usar IA para revisar contratos” porque analistas relatam excesso de trabalho. Ainda não sabemos em qual etapa o tempo é gasto, quais contratos variam mais nem qual erro seria inaceitável.

**Seu papel**

Você é o arquiteto que conduz uma triagem inicial. Antes de escolher modelo ou fornecedor, precisa descobrir se existe uma oportunidade verificável.

**Insumos disponíveis**

Use a seção de objetivos e requisitos deste módulo, a ficha CONOPS e o [template de ADR](../referencia/template-adr.md). Trabalhe com contratos fictícios e não suponha acesso a dados jurídicos reais.

**Como conduzir**

1. Reformule a intenção como problema observável para um stakeholder específico.
2. Liste o baseline que falta e uma forma simples de medi-lo.
3. Separe hipótese de valor (melhorar o trabalho) de hipótese de capacidade (o sistema consegue executar a tarefa).
4. Proponha um experimento pequeno e um critério que faria a equipe rejeitar GenAI ou limitar seu uso.

**Entrega esperada**

Entregue uma ficha de uma página com problema, stakeholder, baseline, resultado, contramétrica, hipóteses, experimento e decisão de rejeição.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Problema e escopo | 25% | Reformula a intenção sem escolher solução prematuramente. |
| Medição de valor | 30% | Define baseline, resultado e contramétrica observáveis. |
| Hipóteses | 20% | Distingue valor do processo e capacidade da solução. |
| Experimento e rejeição | 25% | Propõe teste refutável e limite que pode interromper a adoção. |

**Como verificar antes de entregar:** confira problema, baseline, contramétrica, hipóteses separadas e limite de rejeição.

### 9. Aceitação de extração e síntese

**O que é:** critério de aceitação define população, amostra, medida, limiar e ação para uma saída.

**Onde encontrar:** consulte [critérios probabilísticos](padroes-e-decisoes.md#criterios-probabilisticos-de-aceitacao) e o [catálogo de atributos](../referencia/atributos-de-qualidade.md).

**Situação**

Um sistema extrai obrigações de licenças ambientais e prepara um resumo que será revisado por especialista. Campos como data e identificador precisam obedecer ao formato; já a síntese pode variar na redação, mas não pode omitir obrigação crítica.

**Seu papel**

Você é o arquiteto responsável por transformar a diferença entre contrato determinístico e comportamento probabilístico em critérios de aceitação operáveis.

**Insumos disponíveis**

Consulte o capítulo sobre critérios probabilísticos e o catálogo de atributos. Use uma coleção fictícia de licenças com tipos de documento e exceções diferentes.

**Como conduzir**

1. Escreva um critério determinístico para os campos estruturados, incluindo formato e ação diante de erro.
2. Escreva um critério probabilístico para a síntese, informando população, amostra e modo de revisão.
3. Defina limiar, falha intolerável e tratamento; não esconda segmentos críticos em uma média.
4. Diga que evidência permite liberar, bloquear, restringir ou encaminhar para revisão.

**Entrega esperada**

Entregue dois critérios em tabela, uma nota sobre a amostra e uma regra operacional para cada falha.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Contratos distintos | 25% | Separa validação de campo e julgamento de síntese. |
| População e amostra | 25% | Inclui tipos de licença, exceções e casos críticos. |
| Limite e falha | 25% | Define limiar e resultado intolerável sem mascarar fatias. |
| Ação operacional | 25% | Explica quando bloquear, restringir ou exigir revisão. |

**Como verificar antes de entregar:** confira formato, amostra, segmentos críticos e ação para cada falha.

## Analisar

### 10. Paisagem de decisões para suporte técnico

**O que é:** paisagem de decisões separa escolhas com responsáveis e consequências diferentes.

**Onde encontrar:** use [padrões de desenho conceitual](padroes-e-decisoes.md) e a [oficina local](oficina-de-ferramentas.md).

**Situação**

Uma empresa possui 600 manuais atualizados semanalmente, três sistemas somente de leitura e um diagnóstico com dez sequências conhecidas. A equipe pede “uma solução de IA”, mas cada eixo da decisão muda responsabilidades diferentes.

**Seu papel**

Você é o arquiteto que organiza uma paisagem de escolhas antes de desenhar a arquitetura-alvo.

**Insumos disponíveis**

Use os padrões de desenho conceitual, os conceitos de workflow, agente, RAG, hospedagem e AI Gateway e a oficina de contrato local do módulo.

**Como conduzir**

1. Crie uma tabela com os cinco eixos: contexto, controle, composição de modelos, hospedagem e construir/comprar/compor.
2. Em cada eixo, escreva requisito, responsabilidade nova, risco e evidência que falta.
3. Separe restrições confirmadas de preferências e hipóteses.
4. Proponha um primeiro incremento que adie complexidade sem fechar evolução.
5. Escolha uma incógnita capaz de inverter duas decisões e descreva como medi-la.

**Entrega esperada**

Entregue uma matriz de cinco eixos, uma arquitetura incremental em até três passos e uma hipótese de reversão.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Cobertura dos eixos | 20% | Trata cada eixo sem misturar decisões que têm responsáveis distintos. |
| Consequências causais | 25% | Relaciona escolha a dados, operação, risco e evidência necessária. |
| Requisitos e hipóteses | 20% | Distingue obrigação, preferência e informação ainda não medida. |
| Incremento | 20% | Propõe evolução reversível sem criar dependência prematura. |
| Incógnita testável | 15% | Define medida capaz de alterar a decisão. |

**Como verificar antes de entregar:** confira cinco eixos, responsáveis, riscos, evidências e reversibilidade.

## Avaliar

### 11. Contestação do “agente por estratégia”

**O que é:** contestação arquitetural testa necessidade comparando alternativas, condições e evidências.

**Onde encontrar:** consulte [workflow e agente](conceitos.md), o [exemplo arquitetural](exemplo-arquitetural.md) e o [template de ADR](../referencia/template-adr.md).

**Situação**

O patrocinador de compras exige um agente porque “os melhores produtos já são agênticos”. O processo real tem cinco etapas estáveis, aprovação humana acima de R$ 5 mil e APIs de escrita não idempotentes.

**Seu papel**

Você é o arquiteto que precisa contestar uma solução orientada por tendência sem desqualificar a necessidade do patrocinador.

**Insumos disponíveis**

Use os conceitos de workflow, agente, idempotência e aprovação, o exemplo arquitetural e o template de ADR.

**Como conduzir**

1. Declare se aceita, limita a experimento ou rejeita o agente como primeira opção.
2. Compare agente, workflow e automação convencional usando estabilidade, aprovação e idempotência.
3. Separe evidência presente da hipótese de que autonomia trará valor.
4. Escreva condições, métricas e gatilhos que permitiriam ampliar, reduzir ou reverter a decisão.

**Entrega esperada**

Entregue um parecer de uma página e o núcleo de uma ADR com decisão, alternativas, consequências e revisão.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Julgamento | 25% | Assume uma posição explícita e proporcional ao contexto. |
| Direcionadores | 25% | Usa estabilidade, aprovação e idempotência como razões arquiteturais. |
| Alternativas | 25% | Compara opções sem apelar a tendência ou marca. |
| Revisão | 25% | Define limites, métricas e gatilhos que podem reverter a decisão. |

**Como verificar antes de entregar:** confira posição, comparação, hipótese separada, métricas e gatilhos de reversão.

## Criar

### 12. Dossiê conceitual de um assistente clínico administrativo

**O que é:** dossiê conceitual reúne oportunidade, operação, arquitetura, riscos e evidências para revisão independente.

**Onde encontrar:** consulte [conceitos e padrões](conceitos.md), [template de ADR](../referencia/template-adr.md) e [oficina local](oficina-de-ferramentas.md).

**Situação**

Um sistema ajuda equipes a preparar documentação administrativa para autorização de procedimentos. Pode resumir registros autorizados e políticas, mas não diagnostica, prescreve nem envia solicitação sem revisão. Há dados sensíveis, fontes conflitantes e uma dependência indisponível durante manutenção semanal.

**Seu papel**

Você é o arquiteto que compõe um dossiê independente de fornecedor para uma decisão que ainda precisa ser discutida com domínio, segurança, privacidade e operação.

**Insumos disponíveis**

Use todos os conceitos e padrões do módulo, o [template de ADR](../referencia/template-adr.md), o exemplo arquitetural e a oficina de gateway local. O caso é fictício; não use prontuários ou documentos reais.

**Como conduzir**

1. Comece por oportunidade, baseline, stakeholders, fora de escopo e responsabilidade humana.
2. Modele os modos normal, degradado e bloqueado antes de escolher componentes.
3. Rastreie objetivos até requisitos, mecanismos e evidências.
4. Compare alternativas, explicite conflitos e registre decisões reversíveis e irreversíveis.
5. Feche com falhas, critérios de aceitação, experimento refutável e gatilhos de revisão.

**Entrega esperada**

Entregue o dossiê preenchido, um diagrama com equivalente textual e pelo menos uma ADR. O texto deve permitir revisão por alguém que não acompanhou sua elaboração.

**Template do entregável**

```text
Oportunidade, baseline e hipótese de valor:
Critérios de adequação e rejeição de GenAI:
Stakeholders, preocupações e fora de escopo:
CONOPS — modo normal, degradado e bloqueado:
Matriz de responsabilidade humano–IA:
Objetivos de negócio, produto, dados e IA:
Três cenários de atributo de qualidade com seis partes:
Critérios probabilísticos e falhas intoleráveis:
Comparação de ao menos três alternativas:
Diagrama de contexto e equivalente textual:
Componentes e fronteiras de confiança:
Falhas — detecção — contenção — recuperação:
ADR com evidências e gatilhos de revisão:
Experimento que pode refutar a hipótese:
Mapa objetivo → requisito → mecanismo → evidência:
```

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Oportunidade e escopo | 15% | Delimita valor, stakeholders e usos proibidos sem escolher solução cedo demais. |
| CONOPS e responsabilidade | 20% | Explica modos de operação, revisão humana e autoridade. |
| Rastreabilidade | 15% | Liga objetivos, requisitos, mecanismos, evidências e falhas. |
| Alternativas e ADR | 15% | Expõe trade-offs, consequências e condições de revisão. |
| Diagrama e modos de falha | 15% | Mantém fronteiras, fluxos e contenções coerentes. |
| Experimento | 20% | Define teste econômico que pode refutar a hipótese principal. |

**Como verificar antes de entregar:** confira modos, rastreabilidade, fronteiras, detecção, recuperação e gatilhos na ADR.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
