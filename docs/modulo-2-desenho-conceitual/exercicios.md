# Exercícios

Responda antes de abrir os blocos de feedback. Recordar e Compreender possuem respostas públicas; Aplicar, Analisar, Avaliar e Criar dependem de contexto e apresentam rubricas. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

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

Entre as partes estão população, amostra, métrica ou rubrica, limiar, tratamento de incerteza, falha intolerável e ação resultante. Cinco delas atendem ao pedido, desde que definidas para o caso.
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

Um departamento quer “usar IA para revisar contratos” porque analistas relatam excesso de trabalho. Produza uma ficha com problema observável, stakeholder, baseline que falta, resultado desejado, contramétrica, hipótese de valor e experimento de descoberta. Inclua um critério que poderia levar à rejeição de GenAI.

**Rubrica (0–4 pontos):** 1 ponto por reformular a intenção sem pressupor solução; 1 por baseline, resultado e contramétrica mensuráveis; 1 por separar hipótese de valor e capacidade; 1 por experimento refutável e critério de rejeição coerente.

### 9. Aceitação de extração e síntese

Para um sistema que extrai obrigações de licenças ambientais e produz um resumo revisado por especialista, escreva dois critérios: um determinístico para campos estruturados e um probabilístico para a síntese. Declare população, amostra, limiar, falha intolerável e ação quando o critério falhar.

**Rubrica (0–4 pontos):** 1 ponto por separar contratos determinísticos e avaliação comportamental; 1 por população e amostra representativas; 1 por limiar e falha intolerável sem esconder segmentos críticos na média; 1 por ação operacional clara de bloqueio, restrição ou revisão.

## Analisar

### 10. Paisagem de decisões para suporte técnico

Uma empresa possui 600 manuais atualizados semanalmente, três sistemas somente de leitura e um processo de diagnóstico com dez sequências conhecidas. Compare: prompt com documentos selecionados versus RAG; workflow versus agente; modelo único versus múltiplos; hospedado versus autogerido; construir, comprar ou compor. Relacione cada eixo a requisitos, novas responsabilidades e evidência necessária. Proponha uma arquitetura incremental e uma incógnita capaz de inverter duas escolhas.

**Rubrica (0–5 pontos):** 1 ponto por tratar os cinco eixos sem acoplá-los indevidamente; 1 por consequências causais específicas; 1 por distinguir requisito, restrição e hipótese; 1 por incremento que adia complexidade sem fechar evolução; 1 por incógnita testável capaz de mudar a decisão.

## Avaliar

### 11. Contestação do “agente por estratégia”

O patrocinador de um sistema de compras exige um agente com ferramentas porque “os melhores produtos já são agênticos”. O processo real tem cinco etapas estáveis, aprovação humana acima de R$ 5 mil e APIs de escrita não idempotentes. Defenda aceitar, limitar a experimento ou rejeitar a proposta. Compare-a com workflow e automação convencional, estabeleça condições de revisão e escreva o núcleo de uma ADR.

**Rubrica (0–5 pontos):** 1 ponto por julgamento explícito; 1 por usar estabilidade, aprovação e idempotência como direcionadores; 1 por comparar alternativas sem apelo a tendência; 1 por separar evidência presente de hipótese; 1 por limites e gatilhos mensuráveis que permitam rever o julgamento.

## Criar

### 12. Dossiê conceitual de um assistente clínico administrativo

Projete o desenho conceitual de um sistema que ajuda equipes a preparar documentação administrativa para autorização de procedimentos. Ele pode resumir registros autorizados e políticas, mas não diagnostica, prescreve nem envia solicitação sem revisão. Há dados sensíveis, fontes conflitantes e uma dependência indisponível durante manutenção semanal. Produza um dossiê independente de fornecedor.

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

**Rubrica (0–7 pontos):** 1 ponto por oportunidade e escopo sem solução prematura; 1 por CONOPS, stakeholders e responsabilidade humana; 1 por objetivos e requisitos rastreáveis; 1 por critérios mensuráveis e falhas intoleráveis; 1 por alternativas e ADR com trade-offs; 1 por diagrama, fronteiras e modos de falha coerentes; 1 por experimento econômico capaz de refutar a hipótese principal.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
