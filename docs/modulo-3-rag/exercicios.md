# Exercícios

Recordar e Compreender possuem respostas. De Aplicar a Criar, produza artefatos e use os critérios para revisar o raciocínio. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

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

**Situação**

Uma pergunta do corpus Boreal tem relevantes A, C e F. O mecanismo devolveu A, B, C, D e E; o orçamento aceita cinco trechos.

**Seu papel**

Arquiteto de recuperação.

**Insumos disponíveis**

Consulte [avaliação de recuperação](padroes-e-decisoes.md#recuperacao), [segmentação e decisão de recuperação](conceitos.md#segmentacao-e-decisao-de-recuperacao) e a [oficina](oficina-de-ferramentas.md#receita-principal).

**O que é cada artefato**

**Chunk** é trecho recuperável com ID e metadados. A referência, preparada antes, é `{A, C, F}`. Use `Recall@5 = [relevantes recuperados] / [relevantes existentes]` e `Precision@5 = [relevantes recuperados] / 5`; preencha os numeradores. Essas medidas avaliam recuperação, não resposta.

**Como conduzir**

1. Conte trechos relevantes recuperados e trechos retornados.
2. Calcule Recall@5 e Precision@5, mostrando numerador e denominador.
3. Interprete o que cada medida permite e não permite concluir.
4. Proponha teste que separe consulta, chunking, ranking ou referência.

**Entrega esperada**

Entregue os cálculos, uma interpretação de até 150 palavras e uma hipótese testável com próxima medida.

Use esta tabela de trabalho (uma linha por resultado):

| posição | `chunk_id` | relevante? | fonte da referência |
|---:|---|---|---|
| 1 | ___ | ___ | ___ |
| 2 | ___ | ___ | ___ |
| 3 | ___ | ___ | ___ |
| 4 | ___ | ___ | ___ |
| 5 | ___ | ___ | ___ |

**Checklist de verificação**

Verifique agora:

- [ ] Referência, fonte, `chunk_id`, posição, relevância, numeradores e denominadores aparecem na tabela.
- [ ] A interpretação separa recuperação, citação e qualidade; a próxima medida testa uma causa.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Cálculo | 30% | Mostra as duas fórmulas e chega aos valores corretos. |
| Interpretação | 25% | Relaciona as medidas ao limite de cinco trechos sem extrapolar. |
| Limites | 20% | Distingue recuperação de qualidade de resposta. |
| Investigação | 25% | Propõe hipótese e teste ligados aos dados observados. |

### 9. Comparação de estratégias de chunking

**Situação**

Um manual de 120 páginas coloca definições no início e exceções no fim. Separá-las pode produzir saída aparentemente completa, mas incompleta.

**Seu papel**

Arquiteto de segmentação.

**Insumos disponíveis**

Use [conceitos de RAG](conceitos.md), [padrões](padroes-e-decisoes.md) e os três documentos da [oficina](oficina-de-ferramentas.md): [portal-estorno.txt](../assets/labs/modulo-3/portal-estorno.txt), [politica-campanha.txt](../assets/labs/modulo-3/politica-campanha.txt) e [politica-reembolso.txt](../assets/labs/modulo-3/politica-reembolso.txt). O script executável é [rag_local.py](../assets/labs/modulo-3/rag_local.py).

**O que é chunking e o que deve permanecer rastreável**

**Chunking** divide a fonte em unidades; compare tamanho fixo, seção, semântica e pai–filho. **Proveniência** liga chunk a fonte, versão e localização; pai–filho abre contexto sem perder origem.

**Como conduzir**

1. Descreva como cada estratégia trata definição e exceção.
2. Liste ganho, perda e risco de localização ou versão.
3. Escreva uma pergunta de definição e outra que exija exceção.
4. Defina métricas de recuperação, contexto e vínculo pai–filho.

**Entrega esperada**

Entregue matriz das quatro estratégias, duas perguntas, métricas e um controle de proveniência por alternativa.

**Checklist de verificação**

Verifique agora:

- [ ] A matriz e as perguntas mostram definição, exceção, contexto, Recall@5, Precision@5 e completude.
- [ ] Cada chunk tem ID, fonte, versão, localização e relação pai–filho; a escolha depende dos resultados.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Consequências | 25% | Explica efeitos sobre definição e exceção. |
| Perguntas de teste | 20% | Diferencia pergunta simples de relação entre trechos. |
| Métricas | 25% | Mede recuperação, contexto e completude. |
| Proveniência | 30% | Preserva localização, versão e vínculo dos chunks. |

## Analisar

### 10. Falha de permissão

**Situação**

Após mudança de equipe, uma pessoa perde acesso ao Cliente Norte. O índice foi atualizado, mas cache devolve síntese por oito minutos. Analise a cadeia de autorização.

**Seu papel**

Arquiteto de autorização.

**Insumos disponíveis**

Use o [estudo de caso](estudo-de-caso.md), o [diagrama](exemplo-arquitetural.md#fluxo-de-consulta) e [conceitos de RAG](conceitos.md).

**O que é a fronteira de autorização neste diagnóstico**

Autorização filtra fontes **antes** de chunks, ranking, contexto ou cache. **Cache** é cópia com chave de identidade/política e versão. **Citação** liga afirmação ao trecho; **proveniência** registra origem. Apagar resposta não prova remoção.

**Como conduzir**

1. Desenhe fronteiras entre identidade, filtro, cache, contexto e citação.
2. Separe fato, hipótese causal e evidência ausente.
3. Separe exposição, contenção, recuperação e comunicação.
4. Proponha testes negativos de consulta, cache e citação, sem conteúdo proibido.

**Entrega esperada**

Entregue linha do tempo causal, matriz de fronteiras e plano de contenção, recuperação e não recorrência.

**Checklist de verificação**

Verifique agora:

- [ ] Identidade/política precedem índice, contexto e cache; fato, hipótese e evidência estão separados.
- [ ] O teste cobre consulta, reuso e citação após revogação e registra versões no trace.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Fronteiras | 25% | Localiza pontos onde identidade e autorização atravessam o fluxo. |
| Hipótese causal | 20% | Distingue fato observado de explicação não confirmada. |
| Contenção e recuperação | 25% | Interrompe exposição, revoga materialização e comunica proporcionalmente. |
| Testes | 30% | Cobre consulta, cache e citação com casos negativos verificáveis. |

## Avaliar

### 11. Escolha do padrão

**Situação**

Uma base combina políticas curtas, contratos longos, códigos exatos e perguntas compostas. Oitenta por cento das consultas são simples; p95 deve ficar abaixo de quatro segundos. Mais etapas aumentam latência.

**Seu papel**

Arquiteto de composição.

**Insumos disponíveis**

Compare RAG básico, híbrido, hierárquico, adaptativo e corretivo nos [padrões e trade-offs](padroes-e-decisoes.md#padroes-de-rag-e-seus-trade-offs) e na [receita da oficina](oficina-de-ferramentas.md#receita-principal). Básico usa uma rota; híbrido combina lexical/vetorial; hierárquico preserva seções; adaptativo escolhe; corretivo reavalia evidência.

**O que significa escolher um padrão**

Escolher padrão é hipótese, não vencedor universal. `p95` cobre 95% das execuções; compare-o a quatro segundos. Proveniência explica fonte/versão; operação inclui custo.

**Como conduzir**

1. Indique fonte ou pergunta atendida por cada padrão.
2. Relacione etapas a latência, custo, proveniência e operação.
3. Escolha composição inicial e rota para consultas complexas.
4. Defina evidência para acrescentar ou remover etapas.

**Entrega esperada**

Entregue tabela comparativa, recomendação condicionada e mapa de métricas e gatilhos.

**Checklist de verificação**

Verifique agora:

- [ ] Padrões usam as mesmas perguntas; a recomendação explicita p95, custo, cobertura e proveniência.
- [ ] Consultas complexas têm abstenção; evolução tem métrica, limiar e reversão.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Julgamento | 25% | Recomenda composição adequada ao perfil de consultas. |
| Adequação | 25% | Liga padrões a tipos de fonte e pergunta. |
| Operação | 20% | Considera p95, custo, atualização e manutenção. |
| Evolução | 15% | Propõe incremento reversível. |
| Gatilhos | 15% | Define medidas que podem inverter a decisão. |

## Criar

### 12. Arquitetura RAG completa

**Situação**

Um assistente consulta documentos e tabelas vigentes, atualizados a cada quinze minutos. Não diagnostica e responde com evidência ou falta dela.

**Seu papel**

Arquiteto de fluxos RAG.

**Insumos disponíveis**

Use [padrões RAG](padroes-e-decisoes.md), [template de ADR](../referencia/template-adr.md), [exemplo](exemplo-arquitetural.md), [SLO](../modulo-6-operacao/conceitos.md#slo-para-servico-util) e [oficina](oficina-de-ferramentas.md#receita-principal).

**O que é uma arquitetura RAG completa**

Liga ingestão/publicação e consulta/resposta. **Proveniência** acompanha fonte, versão, localização, índice e citação. **Suficiência** decide se há evidência; **abstenção** sai quando não há; **rollback** mantém versão anterior. ADR é registro de decisão arquitetural: preencha contexto, decisão, alternativas, consequências, evidência e gatilho. Declare quem autoriza, mede e interrompe.

**Como conduzir**

1. Liste fontes, donos, autoridade, classificação e SLO.
2. Desenhe ingestão/publicação e consulta/resposta versionadas.
3. Inclua autorização prévia, proveniência, suficiência, conflito e abstenção.
4. Relacione falhas a contenção, recuperação, avaliação e ADR.
5. Revise verticalmente: afirmação, fonte, versão, acesso e medida.

**Entrega esperada**

Preencha o roteiro, entregue os diagramas com equivalentes textuais e escreva três ADRs rastreáveis aos requisitos.

**Checklist de verificação**

Verifique agora:

- [ ] Afirmações apontam para fonte, versão, localização e citação; política precede materialização e abertura.
- [ ] Conflito, exclusão e abstenção têm saída; pacote e ADRs registram versão, evidência e gatilho.

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

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Fontes e pipelines | 15% | Define autoridade, donos, ingestão, publicação e consulta. |
| Recuperação e autorização | 15% | Escolhe mecanismos adequados e bloqueia acesso antes da materialização. |
| Evidência e abstenção | 15% | Liga afirmações a fonte e versão e trata insuficiência. |
| Operação e proveniência | 15% | Inclui atualização, rollback, falhas, métricas e versões. |
| ADRs e rastreabilidade | 15% | Conecta alternativas, consequências e gatilhos aos requisitos. |
| Diagramas e coerência | 25% | Mantém fluxos, fronteiras e responsabilidades consistentes. |

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
