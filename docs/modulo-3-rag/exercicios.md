# Exercícios

Recordar e Compreender possuem respostas públicas. De Aplicar a Criar, produza artefatos contextualizados e use os critérios de avaliação para revisar seu próprio raciocínio. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

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

Uma pergunta do corpus Boreal tem três trechos relevantes: A, C e F. O mecanismo devolveu A, B, C, D e E, mas o orçamento aceita no máximo cinco trechos antes da geração.

**Seu papel**

Você é o arquiteto responsável por verificar se a recuperação traz evidência suficiente antes de discutir a qualidade da resposta do modelo.

**Insumos disponíveis**

Use as definições de Recall e Precision em [padrões e decisões](padroes-e-decisoes.md), a explicação de recuperação em [conceitos de RAG](conceitos.md) e a saída da [oficina local de RAG](oficina-de-ferramentas.md). A lista de relevantes é o conjunto de referência desta pergunta.

**O que é cada artefato**

Um **chunk** é um trecho recuperável, com identificador e metadados de fonte; não é necessariamente um parágrafo inteiro. O **conjunto de referência** é a lista que um avaliador preparou antes da consulta, neste caso `{A, C, F}`. Ele informa quais trechos contam como relevantes para esta pergunta. `Recall@5` mede quantos relevantes foram recuperados: relevantes recuperados ÷ relevantes existentes, portanto `2 ÷ 3`. `Precision@5` mede quantos dos cinco retornados são relevantes: relevantes recuperados ÷ retornados, portanto `2 ÷ 5`. O `@5` significa que somente a primeira lista de cinco resultados entra na conta. Registre numerador, denominador e a fonte da lista de referência; não trate a média como qualidade da resposta gerada.

**Como conduzir**

1. Conte trechos relevantes recuperados e trechos retornados.
2. Calcule Recall@5 e Precision@5, mostrando numerador e denominador.
3. Explique o que cada medida diz e o que não permite concluir sobre a resposta gerada.
4. Proponha uma investigação para separar consulta, chunking, ranking ou referência incompleta.

**Entrega esperada**

Entregue os cálculos, uma interpretação de até 150 palavras e uma hipótese testável com próxima medida.

**Checklist de verificação**

Antes de entregar, verifique os itens abaixo:

- [ ] O conjunto de referência está identificado e não foi alterado depois de ver os resultados.
- [ ] Recall@5 e Precision@5 mostram numerador, denominador e resultado.
- [ ] A tabela separa `chunk_id`, posição, relevante (sim/não) e fonte da referência.
- [ ] A interpretação não confunde recuperação com fidelidade, citação ou correção da resposta.
- [ ] A próxima medida testa consulta, chunking, ranking ou referência, e não todos ao mesmo tempo.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Cálculo | 30% | Mostra as duas fórmulas e chega aos valores corretos. |
| Interpretação | 25% | Relaciona as medidas ao limite de cinco trechos sem extrapolar. |
| Limites | 20% | Distingue recuperação de qualidade de resposta. |
| Investigação | 25% | Propõe hipótese e teste ligados aos dados observados. |

### 9. Comparação de estratégias de chunking

**Situação**

Um manual de 120 páginas coloca definições no início e exceções no fim das seções. Um chunk que separa essas partes pode produzir uma resposta aparentemente correta, mas incompleta.

**Seu papel**

Você é o arquiteto que compara segmentação antes de escolher um índice.

**Insumos disponíveis**

Use os conceitos de chunking, proveniência e contexto em [conceitos de RAG](conceitos.md), a comparação de padrões em [padrões e decisões](padroes-e-decisoes.md) e os três documentos sintéticos da [oficina de RAG](oficina-de-ferramentas.md). Não precisa implementar os três índices.

**O que é chunking e o que deve permanecer rastreável**

**Chunking** é a decisão de dividir uma fonte em unidades que possam ser encontradas e enviadas ao modelo. Tamanho fixo, seção, semântica e pai–filho são estratégias diferentes; nenhuma é “a correta” sem perguntas de teste. **Proveniência** é o caminho que liga cada chunk à fonte, versão, seção/página e transformação usada. Para esta atividade, o vínculo pai–filho permite recuperar um trecho pequeno e abrir o contexto maior sem perder a localização original.

**Como conduzir**

1. Descreva como cada estratégia trata uma definição e sua exceção.
2. Para cada uma, liste ganho, perda e risco de perder localização ou versão.
3. Escreva duas perguntas de teste: uma de definição e outra que exige exceção.
4. Defina métricas de recuperação, completude do contexto e vínculo entre pai e filho.

**Entrega esperada**

Entregue matriz das três estratégias, duas perguntas, métricas e um controle de proveniência por alternativa.

**Checklist de verificação**

Antes de entregar, verifique os itens abaixo:

- [ ] Cada alternativa diz onde ficam definição e exceção e qual contexto é perdido ou preservado.
- [ ] As perguntas de teste estão escritas exatamente como serão executadas na oficina.
- [ ] A matriz informa como medir Recall@5, Precision@5 e completude do contexto.
- [ ] Todo chunk de exemplo possui `chunk_id`, fonte, versão, localização e relação pai–filho.
- [ ] A escolha final é condicionada aos resultados; não é justificada apenas por tamanho em tokens.

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

Após uma mudança de equipe, uma pessoa perde acesso ao Cliente Norte. O índice foi atualizado, mas um cache continua devolvendo síntese de contrato por oito minutos. A questão é analisar a cadeia de autorização, não apenas apagar a resposta exibida.

**Seu papel**

Você é o arquiteto que conduz o diagnóstico e precisa dizer onde a política deveria ter sido aplicada e que evidência comprova a contenção.

**Insumos disponíveis**

Use o [estudo de caso de RAG](estudo-de-caso.md), o [diagrama de consulta](exemplo-arquitetural.md#fluxo-de-consulta) e os conceitos de autorização antecipada, cache, citação e proveniência em [conceitos de RAG](conceitos.md).

**O que é a fronteira de autorização neste diagnóstico**

Autorização antecipada significa filtrar o universo de fontes **antes** de materializar chunks, ranking, contexto ou cache. **Cache** é uma cópia reutilizável de decisão, resultado ou contexto; sua chave precisa incluir identidade/política e versão quando esses dados mudam. **Citação** é o vínculo verificável entre uma afirmação e o trecho autorizado que a sustenta. **Proveniência** registra de onde veio esse trecho. Use esses quatro significados para localizar a falha; “apagar a resposta” não prova que o material proibido deixou de estar no índice ou no cache.

**Como conduzir**

1. Desenhe as fronteiras entre identidade, filtro, cache, contexto e citação.
2. Formule causa provável e separe fatos de explicações ainda não confirmadas.
3. Separe ativos expostos, contenção imediata, recuperação e comunicação.
4. Proponha testes negativos para consulta, cache e citação, sem reproduzir conteúdo proibido.

**Entrega esperada**

Entregue linha do tempo causal, matriz de fronteiras e plano de contenção, recuperação e não recorrência.

**Checklist de verificação**

Antes de entregar, verifique os itens abaixo:

- [ ] A identidade e a decisão de política aparecem antes de índice, reranking, contexto e cache.
- [ ] O diagnóstico distingue fato observado, hipótese causal e evidência ainda ausente.
- [ ] A contenção invalida cache e bloqueia nova materialização sem copiar o contrato exposto.
- [ ] O teste negativo cobre consulta, reuso de cache e abertura de citação após revogação.
- [ ] O plano registra versão da política, corpus, cache e trace para permitir reconstrução.

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

Uma base combina 20 mil políticas curtas, contratos longos, códigos exatos e perguntas compostas. Oitenta por cento das consultas são simples e o p95 deve ficar abaixo de quatro segundos. Mais etapas podem melhorar cobertura, mas aumentam latência e operação.

**Seu papel**

Você é o arquiteto que recomenda uma composição inicial e diz sob quais sinais ela deve evoluir.

**Insumos disponíveis**

Compare RAG básico, híbrido, hierárquico, adaptativo e corretivo usando os [padrões do módulo](padroes-e-decisoes.md) e as métricas da [oficina local](oficina-de-ferramentas.md). RAG básico recupera e gera em uma rota simples; híbrido combina busca lexical e vetorial; hierárquico preserva relações de seção; adaptativo escolhe rota conforme a pergunta; corretivo reavalia ou busca novamente quando a evidência é insuficiente.

**O que significa escolher um padrão**

Escolher um padrão é propor uma hipótese de arquitetura para um perfil de fontes e consultas, não declarar que um rótulo vence sempre. `p95` é o tempo abaixo do qual ficam 95% das execuções; compare-o com o limite de quatro segundos. Proveniência é a capacidade de explicar fonte, versão e transformação; operação inclui custo, atualização, fallback e manutenção.

**Como conduzir**

1. Indique o tipo de fonte ou pergunta atendido por cada padrão.
2. Relacione cada etapa a latência, custo, proveniência e operação.
3. Escolha composição inicial e trate separadamente consultas complexas.
4. Defina evidência que justificaria acrescentar ou remover cada etapa.

**Entrega esperada**

Entregue tabela comparativa, recomendação condicionada e mapa de métricas e gatilhos.

**Checklist de verificação**

Antes de entregar, verifique os itens abaixo:

- [ ] A tabela usa os mesmos tipos de pergunta e conjunto de teste para todos os padrões.
- [ ] A recomendação explicita p95, custo, cobertura, autorização e proveniência.
- [ ] Consultas complexas têm rota ou critério de abstenção próprios.
- [ ] Cada evolução tem métrica, limiar e plano de reversão.
- [ ] O gatilho de mudança é observável e não depende de “pareceu melhor”.

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

Um assistente de procedimentos hospitalares administrativos consulta documentos e tabelas vigentes por unidade, atualizados a cada quinze minutos. Ele não pode diagnosticar e deve responder com evidência ou declarar insuficiência.

**Seu papel**

Você é o arquiteto que compõe fluxos offline e online e torna explícitos autoridade, rollback, abstenção e avaliação.

**Insumos disponíveis**

Use os [padrões RAG](padroes-e-decisoes.md), o [template de ADR](../referencia/template-adr.md), o [exemplo arquitetural](exemplo-arquitetural.md) e os arquivos sintéticos da [oficina](oficina-de-ferramentas.md). O hospital é fictício.

**O que é uma arquitetura RAG completa**

Uma arquitetura RAG completa liga dois fluxos: ingestão/publicação da fonte e consulta/resposta. **Proveniência** deve acompanhar fonte, versão, localização, transformação, índice, contexto e citação. **Suficiência** é a regra que decide se há evidência aplicável e completa; **abstenção** é a saída explícita quando essa regra falha. **Rollback** mantém a versão anterior ativa quando a candidata não passa nos testes. Desenhe cada fronteira e escreva quem autoriza, quem transforma, quem mede e quem pode interromper.

**Como conduzir**

1. Comece por fontes, donos, autoridade, classificação e SLO.
2. Desenhe ingestão/publicação e consulta/resposta como dois fluxos versionados.
3. Inclua autorização antes da materialização, proveniência, suficiência, conflito e abstenção.
4. Relacione cada falha a contenção, recuperação, avaliação e ADR.
5. Faça uma revisão vertical: afirmação, fonte, versão, acesso e medida.

**Entrega esperada**

Preencha o roteiro, entregue os diagramas com equivalentes textuais e escreva três ADRs rastreáveis aos requisitos.

**Checklist de verificação**

Antes de entregar, verifique os itens abaixo:

- [ ] Cada afirmação de exemplo aponta para fonte, versão, localização e citação autorizada.
- [ ] A política é aplicada antes da materialização e novamente ao abrir uma citação.
- [ ] O fluxo trata conflito, fonte desatualizada, exclusão, rollback e abstenção.
- [ ] O pacote de versões permite reproduzir uma resposta sem armazenar conteúdo sensível desnecessário.
- [ ] Os ADRs registram alternativa rejeitada, consequência, evidência e gatilho de revisão.

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
