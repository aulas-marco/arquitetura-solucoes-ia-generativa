# Exercícios

Recordar e Compreender possuem respostas públicas. De Aplicar a Criar, produza artefatos contextualizados e use as rubricas. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

## Recordar

### 1. Dois fluxos

Nomeie os dois fluxos de RAG e indique o resultado de cada um.

<details>
<summary>Ver resposta</summary>

O fluxo offline de ingestão produz conhecimento pesquisável, versionado e governado. O fluxo online de consulta produz resposta apoiada, esclarecimento, resultado parcial ou abstenção a partir de evidências autorizadas.
</details>

### 2. Estratégias de busca

Defina busca lexical, busca vetorial e recuperação híbrida.

<details>
<summary>Ver resposta</summary>

Lexical usa termos e é forte em códigos e expressões exatas. Vetorial compara embeddings e alcança paráfrases. Híbrida reúne sinais das duas estratégias e combina seus rankings.
</details>

### 3. Proveniência

Liste quatro elementos mínimos da proveniência de um chunk.

<details>
<summary>Ver resposta</summary>

Fonte, versão, localização e transformação são exemplos. Também são válidos aquisição, extrator, estratégia de segmentação, modelo de embedding, versão do índice e identificador estável.
</details>

### 4. Suficiência

Cite quatro condições que podem exigir abstenção.

<details>
<summary>Ver resposta</summary>

Fonte obrigatória ausente, baixa cobertura, resultados fracos, conflito não resolvido, conteúdo expirado, pergunta fora do escopo ou falta de autorização.
</details>

## Compreender

### 5. Banco vetorial

Explique por que um banco vetorial não constitui, sozinho, uma arquitetura RAG.

<details>
<summary>Ver resposta</summary>

Ele pode armazenar e buscar embeddings, mas não governa necessariamente aquisição, extração, autorização, busca lexical, atualização, proveniência, contexto, citação, abstenção, geração e avaliação ponta a ponta.
</details>

### 6. Autorização antecipada

Por que recuperar conteúdo e ocultá-lo depois é insuficiente?

<details>
<summary>Ver resposta</summary>

O conteúdo já pode ter alcançado ranking, cache, log ou modelo. A política deve restringir o universo antes da materialização e continuar válida ao abrir citações e reutilizar caches.
</details>

### 7. Citação versus suporte

Por que uma resposta com links ainda pode não estar fundamentada?

<details>
<summary>Ver resposta</summary>

Um link pode tratar do tema sem implicar a afirmação. Fundamentação exige correção e completude por afirmação, fonte vigente e acesso verificável ao trecho correspondente.
</details>

## Aplicar

### 8. Cálculo de métricas de recuperação

Para uma pergunta, o gabarito possui três chunks relevantes: A, C e F. O ranking top-5 retornou A, B, C, D e E. Calcule Recall@k para k = 5 e Precision@5. Explique o que cada resultado sugere para uma aplicação cujo orçamento aceita somente cinco chunks e proponha uma investigação.

**Rubrica (0–4 pontos):** 1 ponto por Recall@5 = 2/3; 1 por Precision@5 = 2/5; 1 por interpretar perda de F e desperdício de três posições; 1 por investigação coerente sobre consulta, chunking, recuperação ou ranking.

### 9. Comparação de estratégias de chunking

Um manual de 120 páginas contém definições no início de cada seção e exceções no fim. Compare três estratégias de chunking: tamanho fixo com sobreposição, por seção e pai–filho. Defina um pequeno experimento, métricas e um risco de proveniência para cada alternativa.

**Rubrica (0–4 pontos):** 1 ponto por consequências específicas das três estratégias; 1 por perguntas que exijam definição e exceção; 1 por métricas de recuperação e contexto; 1 por preservar localização, versão e vínculo entre chunks.

## Analisar

### 10. Falha de permissão

Após uma mudança de equipe, um colaborador perde acesso ao Cliente Norte. O índice foi atualizado, mas um cache de respostas continua devolvendo síntese de contrato por oito minutos. Faça a análise da falha de permissão: reconstrua fronteiras, causa provável, ativos expostos, contenção, recuperação, evidências e testes de não recorrência. Diferencie revogação no índice, decisão de política, chave de cache e autorização ao abrir citação.

**Rubrica (0–5 pontos):** 1 ponto por localizar mais de uma fronteira; 1 por hipótese causal verificável; 1 por contenção imediata e revogação; 1 por recuperação e comunicação proporcionais; 1 por testes adversariais que cobrem consulta, cache e citação sem revelar conteúdo proibido.

## Avaliar

### 11. Escolha do padrão

Uma base combina 20 mil políticas curtas, contratos longos, códigos exatos e perguntas compostas; 80% das consultas são simples e o p95 deve ficar abaixo de quatro segundos. Avalie RAG básico, híbrido, hierárquico, adaptativo e corretivo. Recomende uma composição inicial e declare evidência que justificaria acrescentar ou remover cada etapa.

**Rubrica (0–5 pontos):** 1 ponto por julgamento explícito; 1 por ligar padrões aos tipos de fonte e pergunta; 1 por considerar latência e operação; 1 por evolução incremental; 1 por métricas e gatilhos capazes de inverter a decisão.

## Criar

### 12. Arquitetura RAG completa

Projete uma arquitetura RAG completa para um assistente de procedimentos hospitalares administrativos. Há documentos, tabelas vigentes, grupos por unidade, atualização em quinze minutos e proibição de diagnóstico. Inclua:

```text
Fontes, donos, autoridade, classificação e SLO:
Pipeline offline completo e publicação/rollback:
Chunking, metadados, embeddings e índices:
Pipeline online completo e contratos:
Transformação, busca lexical/vetorial/estruturada e reranking:
Fronteira de autorização, caches e citações:
Montagem de contexto e isolamento de instruções:
Critério de suficiência, conflito e abstenção:
Proveniência e pacote de versões:
Falhas, contenção, recuperação e modo degradado:
Conjunto de avaliação e métricas por camada:
Três ADRs com alternativas e gatilhos de revisão:
Diagramas de ingestão, consulta e sequência com equivalentes textuais:
```

**Rubrica (0–7 pontos):** 1 ponto por governança das fontes; 1 pelos dois pipelines completos; 1 por recuperação adequada a documentos e tabelas; 1 por autorização antes da materialização; 1 por evidência, citações e abstenção; 1 por operação, proveniência e avaliação; 1 por diagramas e ADRs rastreáveis aos requisitos.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
