# Template de ADR para soluções generativas

Use este modelo para registrar uma decisão arquitetural relevante, suas evidências e as condições que podem torná-la inadequada. Um ADR descreve uma escolha no contexto em que foi tomada; não é documentação promocional de tecnologia.

## Template

```markdown
# ADR-NNN — Título da decisão

## Status
Proposta | Aceita | Substituída | Rejeitada

## Contexto
Problema, stakeholders, limites, restrições, pressupostos e incertezas.

## Direcionadores da decisão
- Objetivos e cenários de atributos de qualidade.
- Riscos, políticas e restrições.
- Evidências já disponíveis.

## Opções
1. Alternativa A — descrição, pontos fortes e limitações.
2. Alternativa B — descrição, pontos fortes e limitações.
3. Alternativa C — descrição, pontos fortes e limitações.

## Decisão
Escolha adotada, escopo e como será implementada.

## Consequências
Benefícios, custos, riscos residuais, compromissos e trabalho futuro.

## Evidências
Experimentos, avaliações, métricas, incidentes ou referências que sustentam a escolha.

## Gatilhos de revisão
Condições mensuráveis que exigem reavaliar a decisão.
```

## Exemplo completo — conhecimento para um assistente de políticas

### Status

Aceita em 14 de julho de 2026.

### Contexto

Um assistente interno responde a perguntas sobre políticas corporativas. Os documentos mudam semanalmente, possuem níveis de acesso distintos e devem ser citados. O modelo, isoladamente, não oferece atualidade, autorização por documento nem proveniência suficiente. O primeiro lançamento atenderá 2.000 pessoas e terá revisão humana para temas sensíveis.

### Direcionadores da decisão

- Respostas fundamentadas e declaração explícita quando não houver evidência.
- Atualização de documentos em até duas horas.
- Respeito à autorização do usuário antes da recuperação.
- p95 de resposta completa inferior a oito segundos.
- Possibilidade de avaliar recuperação separadamente da geração.

### Opções

1. **Conhecimento apenas no modelo:** menor número de componentes, mas sem atualização e controle de acesso compatíveis.
2. **Documento inteiro no contexto:** simples para poucos arquivos, mas custo, latência e seleção pioram com escala.
3. **RAG híbrido com filtros de autorização e reranking:** aumenta complexidade operacional, porém separa conhecimento, recuperação e geração e atende rastreabilidade.
4. **Fine-tuning com o conteúdo:** útil para comportamento, mas inadequado como mecanismo principal de atualização factual e exclusão.

### Decisão

Adotar RAG híbrido. O fluxo offline extrairá, segmentará, classificará e versionará documentos. O fluxo online aplicará identidade e filtros antes da busca lexical e vetorial, fará reranking e entregará ao modelo apenas trechos autorizados com identificadores de fonte. Sem evidência acima do limiar validado, a resposta informará a insuficiência e oferecerá encaminhamento humano.

### Consequências

A solução ganha atualização, proveniência e avaliação por componente. Em contrapartida, exige pipeline de ingestão, índice, sincronização de exclusões, políticas de acesso e observabilidade do caminho de recuperação. O time assume risco residual de conteúdo mal segmentado e de permissão desatualizada.

### Evidências

No conjunto inicial, a busca híbrida com reranking recuperou ao menos um trecho relevante nos cinco primeiros resultados em 94% das perguntas, contra 81% na busca vetorial isolada. O p95 estimado permaneceu em 6,7 s. Cenários sem evidência foram recusados corretamente em 97% dos testes. Esses resultados serão reproduzidos no pipeline antes da liberação.

### Gatilhos de revisão

- Cobertura de recuperação abaixo de 90% por duas versões consecutivas.
- p95 acima de oito segundos durante sete dias.
- Corpus ou custo de indexação crescer mais de três vezes.
- Nova exigência de residência, retenção ou exclusão de dados.
- Contexto longo atingir qualidade equivalente com custo operacional total menor no conjunto aprovado.
