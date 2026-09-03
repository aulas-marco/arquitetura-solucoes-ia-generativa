# Métricas de avaliação

Esta página explica as métricas usadas nas oficinas dos módulos 3, 4 e 5: o que cada uma mede, o que exige de entrada, como se calcula e o que deixa passar. Os exemplos numéricos vêm da execução real do laboratório do [Módulo 5](../modulo-5-confianca/oficina-de-ferramentas.md), com 45 casos rotulados.

## O que é uma métrica

Uma métrica tem três partes: as **entradas** que consome, a **régua** que aplica e o **limiar** que separa aprovado de reprovado. Sem limiar declarado o número serve apenas para acompanhar: a equipe olha, acha razoável e libera.

Toda métrica também tem um ponto cego, definido por construção. Uma métrica que compara texto por regra não enxerga paráfrase. Uma métrica que usa modelo para julgar traz a variabilidade do modelo para dentro da medição. Escolher métrica é escolher qual erro você prefere não ver.

## Duas camadas

Uma métrica pontua um caso. Uma avaliação descreve um conjunto. As duas camadas respondem a perguntas diferentes, e nenhuma substitui a outra.

| Camada | Unidade | Pergunta | Exemplo |
|---|---|---|---|
| 1 | um caso | esta resposta está adequada? | nota 0,8 na comparação de decisão |
| 2 | o conjunto | este sistema pode ser liberado? | recall de 0,75 na classe de bloqueio |

Uma nota alta em cinco casos não autoriza nada. É a camada 2 que sustenta decisão de liberação, e ela exige rótulos de referência para todos os casos do conjunto.

## Camada 1 — métricas por caso

### Métricas determinísticas

Comparam a resposta com uma referência por regra: igualdade exata, expressão regular, validação de esquema. Custam zero chamadas de modelo, devolvem sempre o mesmo resultado e são auditáveis linha por linha.

`ExactMatchMetric` exige igualdade literal. `PatternMatchMetric` recebe uma expressão regular e devolve 1 quando ela casa. Duas armadilhas de uso aparecem já na primeira execução. A primeira é semântica: a resposta *"Não posso atender a esse pedido"* recusa corretamente, e a métrica reprova porque a palavra `bloquear` não aparece no texto. A segunda é de API: no DeepEval 4.2.0 o padrão é aplicado com `fullmatch`, então o padrão precisa cobrir a resposta inteira. Um padrão como `não posso|não vou` devolve zero em todos os casos, silenciosamente, e a equipe conclui que o sistema falhou em tudo.

O caminho prático é usar um léxico por classe (`(?s).*(não posso|não vou|não forneço).*`) e aceitar que ele erra nos casos em que a recusa foi escrita com outras palavras. No laboratório do Módulo 5 esse léxico classifica corretamente 29 dos 45 casos e deixa 12 como `indefinido`.

### Métricas com juiz

Montam um prompt de avaliação, submetem a um modelo e convertem a saída em nota. Enxergam equivalência semântica, custam pelo menos uma chamada por caso e herdam o comportamento do juiz, inclusive seus vieses.

**`GEval`** compara a decisão observada com a esperada. Aceita duas formas de régua, e a diferença entre elas decide a reprodutibilidade do laboratório:

- com `criteria`, o juiz primeiro **gera os passos de avaliação** a partir do critério em texto livre e só depois aplica esses passos. Duas execuções idênticas podem produzir passos diferentes, e portanto notas diferentes, mesmo com temperatura zero e a mesma resposta de entrada;
- com `evaluation_steps`, os passos são escritos por você. A variação do juiz continua existindo, agora sem a variação adicional da régua.

**`AnswerRelevancyMetric`** mede se a resposta atende à intenção da pergunta. Consome `input` e `actual_output`, sem referência. Serve para separar duas coisas que a nota de decisão funde: uma recusa pode estar correta e ser inútil, porque não diz o próximo passo. Ponto cego: aprova resposta relevante e insegura.

**`PIILeakageMetric`** procura dado pessoal na resposta. Consome `actual_output`, sem referência. Ponto cego: cobre o texto devolvido ao usuário; o que o sistema gravou em log fica fora do alcance dela.

Uma regra vale para todas: passe apenas os parâmetros que o critério usa. Incluir `input` em uma comparação que só olha decisão observada contra decisão esperada dá ao juiz material para se distrair.

## Camada 2 — métricas clássicas de classificação

O laboratório do Módulo 5 é uma classificação de três classes (`bloquear`, `escalar`, `corrigir`) contra rótulos de referência. Toda métrica desta camada se calcula a partir de três contagens, definidas **por classe**:

| Contagem | Significado na classe `bloquear` |
|---|---|
| VP, verdadeiro positivo | devia bloquear e bloqueou |
| FP, falso positivo | não devia bloquear e bloqueou |
| FN, falso negativo | devia bloquear e não bloqueou |

### Precisão

`precisão = VP / (VP + FP)`

Dos casos em que o sistema acionou a classe, quantos eram mesmo dela. Responde pela confiabilidade do acionamento. Na classe `bloquear` do laboratório: `6 / (6 + 2) = 0,75`. Um quarto das recusas caiu sobre pedido legítimo.

### Recall

`recall = VP / (VP + FN)`

Dos casos que pertenciam à classe, quantos o sistema pegou. Responde pela cobertura. Na mesma classe: `6 / (6 + 2) = 0,75`. Dois pedidos que exigiam recusa foram atendidos.

Precisão e recall respondem a perguntas diferentes e costumam se mover em direções opostas. Aumentar a sensibilidade da recusa eleva o recall e derruba a precisão, porque mais pedidos legítimos passam a ser recusados.

### F1

`F1 = 2 × precisão × recall / (precisão + recall)`

Média harmônica das duas. Ela pune desequilíbrio: precisão 1,00 com recall 0,10 dá F1 de 0,18, enquanto a média simples daria 0,55. Use F1 quando a classe é rara e você precisa de um número único por classe.

### Acurácia e o efeito do desbalanceamento

`acurácia = acertos / total`

No laboratório: `29 / 45 = 0,64`. O número parece informativo até você comparar com uma linha de base trivial. Um classificador que responde `corrigir` para tudo, sem nunca bloquear nada, acerta os 24 casos legítimos e alcança `24 / 45 = 0,53`. A diferença entre 0,53 e 0,64 é o que o sistema realmente agrega, e nenhuma das duas medidas informa que o sistema deixou passar dois pedidos que exigiam recusa.

Quanto mais desbalanceado o conjunto, mais a acurácia mede a classe majoritária. É por isso que ela nunca deve aparecer sozinha.

### Matriz de confusão

Diz **qual** erro acontece, e não apenas quantos. Linha é a decisão esperada, coluna a prevista. Saída real do laboratório:

|  | bloquear | escalar | corrigir | indefinido |
|---|---:|---:|---:|---:|
| **bloquear** | 6 | 0 | 0 | 2 |
| **escalar** | 0 | 9 | 2 | 2 |
| **corrigir** | 2 | 0 | 14 | 8 |

Leia primeiro a diagonal, que são os acertos. Depois procure as células fora dela que têm consequência assimétrica. A célula `corrigir → bloquear` com 2 casos são falsas recusas: usuário legítimo empurrado para fila humana. A célula `bloquear → indefinido` com 2 casos é falha de bloqueio: pedido que devia ser recusado e não foi. As duas contam como erro na acurácia e valem coisas muito diferentes para quem responde pelo sistema.

### Duas taxas que a diretoria entende

- **taxa de falsa recusa** = casos legítimos classificados como bloqueio, sobre o total de casos legítimos. No laboratório: `2 / 37`.
- **falha de bloqueio** = casos que exigiam recusa e não foram recusados, sobre o total desses casos. No laboratório: `2 / 8`.

A escolha entre reduzir uma ou outra não é técnica. Ela declara qual dano a organização prefere absorver, e precisa de responsável com nome.

### Macro e micro

**Macro** tira a média simples da métrica entre as classes, dando o mesmo peso a cada uma. No laboratório, macro-F1 = `(0,75 + 0,82 + 0,70) / 3 = 0,76`. **Micro** agrega as contagens de todas as classes antes de dividir; em classificação de rótulo único, coincide com a acurácia. Use macro quando a classe rara importa tanto quanto a comum, que é o caso quando a classe rara é a de segurança.

### Suporte e tamanho de amostra

Suporte é o número de casos rotulados de cada classe. A classe `bloquear` tem 8 casos, então cada caso vale 0,125 de recall: um único erro a mais move a métrica de 0,75 para 0,625. Com cinco casos, como no laboratório original, recall só pode assumir os valores 0, 0,2, 0,4, 0,6, 0,8 e 1. Ler variação de ruído como sinal é o erro mais comum de quem monta o primeiro conjunto.

Métrica agregada precisa de suporte por classe antes de sustentar decisão. Se a classe crítica tem menos de algumas dezenas de casos, o número serve para orientar investigação; liberar versão exige mais suporte.

### Limiar e a troca precisão-recall

Métricas de juiz devolvem valor contínuo, e o limiar transforma esse valor em aprovado ou reprovado. Varrer o limiar de 0,1 a 0,9 e registrar precisão e recall em cada ponto mostra a troca em números concretos. Limiar baixo aprova quase tudo e a precisão do portão cai; limiar alto reprova casos bons e o portão passa a gerar retrabalho.

O limiar é decisão de arquitetura, com responsável e revisão, do mesmo tipo que uma [fitness function](../modulo-5-confianca/padroes-e-decisoes.md#fitness-functions-de-confianca). Copiar o valor padrão do exemplo é a forma mais rápida de ter um portão que não protege nada.

### Fatias

Média esconde grupo frágil. Recalcule as métricas por público, idioma, tipo de pergunta, nível de acesso e rota de fallback. Um recall global de 0,90 pode conviver com 0,40 na fatia de casos adversariais, que é exatamente a fatia que motivou a avaliação.

## O que pertence a outros módulos

| Métrica | Módulo | Por que não serve aqui |
|---|---|---|
| `Recall@k`, MRR, nDCG | [Módulo 3](../modulo-3-rag/index.md) | medem ordenação de recuperação e exigem contexto recuperado |
| `FaithfulnessMetric`, `ContextualPrecisionMetric`, `ContextualRecallMetric` | [Módulo 3](../modulo-3-rag/index.md) | exigem `retrieval_context` e avaliam a fundamentação da resposta |
| `ToolCorrectnessMetric`, `ToolPermissionMetric` | [Módulo 4](../modulo-4-agentes/index.md) | exigem trace de chamadas de ferramenta |

## Resumo

| Métrica | Camada | Entradas | Custo por caso | Ponto cego |
|---|---|---|---|---|
| `PatternMatchMetric` | 1 | resposta + regex | zero chamadas | paráfrase; `fullmatch` |
| `GEval` | 1 | resposta + esperada | 1 chamada, mais a geração da régua se usar `criteria` | viés do juiz |
| `AnswerRelevancyMetric` | 1 | pergunta + resposta | 1 ou mais chamadas | resposta relevante e insegura |
| `PIILeakageMetric` | 1 | resposta | 1 ou mais chamadas | dado gravado em log |
| Precisão, recall, F1 | 2 | rótulos + previsões | zero chamadas | suporte pequeno |
| Matriz de confusão | 2 | rótulos + previsões | zero chamadas | não pondera custo do erro |
| Acurácia | 2 | rótulos + previsões | zero chamadas | desbalanceamento |
