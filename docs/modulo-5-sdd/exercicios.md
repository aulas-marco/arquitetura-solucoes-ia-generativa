# Exercícios

Recordar e Compreender possuem respostas públicas. De Aplicar a Criar, produza artefatos contextualizados e use os critérios de avaliação para revisar a decisão. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

## Recordar

### 1. Artefatos do SDD

O fluxo `constitution → specify → clarify → plan → tasks → analyze → implement → verify` tem oito etapas, cada uma respondendo a uma pergunta diferente.

Associe constitution, spec, plan, tasks, implement e verify à pergunta principal que cada artefato responde.

<details>
<summary>Ver resposta</summary>

Constitution responde quais princípios governam o projeto; spec define o que e por que construir; plan registra como a arquitetura realiza a intenção; tasks decompõe em fatias e dependências; implement executa cada fatia com testes; verify demonstra aderência à spec e qualidade técnica.
</details>

## Compreender

### 2. Spec viva não é documentação extensa

Uma spec longa não é, por isso, uma spec viva.

Explique por que o tamanho de uma spec não demonstra que ela é viva ou executável.

<details>
<summary>Ver resposta</summary>

Uma spec é viva quando mudanças de intenção, regra, risco e evidência atualizam o contrato versionado. É executável quando critérios e interfaces conseguem derivar ou verificar planos, tarefas e testes. Um documento longo pode continuar vago, divergente do código e incapaz de decidir aceite.
</details>

## Aplicar

### 3. Clarificação e critérios de aceite

**Situação**

Uma área solicita “permita reabrir uma avaliação encerrada”, sem informar autoridade, prazo, efeito sobre notas publicadas, auditoria ou reversão.

**Seu papel**

Você responde pelo portão (*gate*) 1 e deve tornar a intenção implementável sem escolher tecnologia.

**Insumos disponíveis**

Use a [spec como artefato vivo](modos-de-trabalho.md#a-spec-como-artefato-central-e-vivo), a etapa de [clarificação](fluxo.md#3-clarify-que-ambiguidades-mudariam-a-solucao) e a [Decisão 3](decisoes.md#decisao-3-formular-criterios-antes-de-tarefas). Trate a área solicitante e a plataforma como fictícias.

**Como conduzir**

1. Construa um **registro epistemológico** — em inglês *ledger* —, que é uma tabela de quatro colunas separando o que é fato confirmado, o que é hipótese, o que permanece desconhecido e o que está fora de escopo.
2. Formule oito perguntas de clarificação ordenadas pelo impacto.
3. Escolha respostas fictícias e declare-as decisões do exercício.
4. Escreva cinco requisitos EARS e três cenários BDD: sucesso, negação e conflito.
5. Defina dois atributos de qualidade mensuráveis e quatro itens fora de escopo.
6. Antes de entregar, confira se cada requisito EARS tem condição e resposta observáveis por alguém que não participou da conversa.

**Entrega esperada**

Mini-spec de duas a quatro páginas que outra pessoa revise sem a conversa original.

**Critérios de avaliação**

| Critério | Peso | Evidência |
|---|---:|---|
| Incerteza explícita | 20% | Não transforma hipótese em fato. |
| Perguntas | 20% | Cobrem autoridade, estado, consequência e reversibilidade. |
| Requisitos | 25% | Condição e resposta são observáveis. |
| Aceite e qualidade | 25% | Cenários e medidas permitem decidir. |
| Escopo | 10% | Evita implementação especulativa. |

## Analisar

### 4. Consistência entre spec, plano, tarefas e testes

**Situação**

A spec exige autorização por unidade, expiração em 24 horas e auditoria sem conteúdo. O plano descreve link público por sete dias. As tarefas incluem envio por e-mail, embora esteja fora de escopo. Os testes validam apenas geração do arquivo.

**Seu papel**

Você conduz a análise de consistência antes do Gate 2 e responde por bloquear ou liberar a execução.

**Insumos disponíveis**

Use a etapa de [análise de consistência](fluxo.md#6-analyze-os-artefatos-contam-a-mesma-historia), os [oito artefatos](fluxo.md#oito-artefatos-de-uma-demanda-governada) e a [Decisão 8](decisoes.md#decisao-8-manter-os-artefatos-coerentes). Os artefatos citados são fictícios.

**Como conduzir**

1. Construa a matriz `requisito → plano → tarefa → teste`.
2. Classifique achados como lacuna, contradição, ambiguidade ou **expansão de escopo** (*scope creep*), que significa trabalho previsto em um artefato sem origem em nenhum requisito aprovado.
3. Indique o artefato que deve mudar e a autoridade que aprova.
4. Separe bloqueios de riscos residuais.
5. Proponha tarefas como fatias verticais com bloqueadores.
6. Antes de fechar o relatório, confira se todo achado aponta artefato a mudar, autoridade que aprova e consequência de não mudar.

**Entrega esperada**

Relatório de consistência com severidade, evidência, correção e decisão de gate.

**Critérios de avaliação**

| Critério | Peso | Evidência |
|---|---:|---|
| Cobertura | 25% | Mapeia requisitos e fora de escopo. |
| Classificação | 20% | Distingue tipos de inconsistência. |
| Autoridade | 15% | Agente não redefine produto ou risco. |
| Fatias | 25% | Cada tarefa entrega comportamento. |
| Gate | 15% | Bloqueios são proporcionais. |

## Avaliar

### 5. Comparação de fluxos SDD

**Situação**

O fluxo A usa um agente para especificar, implementar e revisar. O fluxo B usa Spec Kit, revisões separadas de Spec e Standards e três portões (*gates*). B dobra a preparação, mas reduz retrabalho; A produz protótipos mais cedo.

**Seu papel**

Você assessora a liderança de engenharia na escolha de profundidade por classe de mudança.

**Insumos disponíveis**

Use a [comparação das abordagens](sintese-e-referencias.md#comparacao-das-abordagens), a [Decisão 1](decisoes.md#decisao-1-escolher-a-profundidade-proporcional) e os [limites honestos](sintese-e-referencias.md#limites-honestos). Os dois fluxos são hipotéticos.

**Como conduzir**

1. Defina critérios de risco, reversibilidade, coordenação, rastreabilidade, *lead time* e retrabalho. *Lead time* aqui significa o intervalo entre a chegada da demanda e a entrega em produção, não o tempo de codificação.
2. Pondere-os para protótipo descartável e autorização financeira.
3. Avalie independência das revisões e risco de aprovação automática.
4. Considere uma opção híbrida.
5. Declare evidências de 60 dias que poderiam inverter a escolha.
6. Verifique se a recomendação continuaria válida caso o custo de retrabalho dobrasse; se não continuar, o critério ainda depende de uma estimativa frágil.

**Entrega esperada**

Matriz, recomendação por classe, riscos residuais e experimento de adoção.

**Critérios de avaliação**

| Critério | Peso | Evidência |
|---|---:|---|
| Contexto | 25% | Pesos mudam por classe. |
| Trade-offs | 25% | Considera preparação e retrabalho. |
| Governança | 20% | Avalia autoridade e independência. |
| Recomendação | 15% | Decorre da matriz. |
| Experimento | 15% | Métricas podem inverter a decisão. |

## Criar

### 6. Iniciativa completa com SDD

**Situação**

Escolha uma feature do projeto final que atravesse interface, regra, dados, integração e operação, com ao menos um risco de segurança e um atributo de qualidade. A demanda chega como uma frase de negócio, sem decisões técnicas tomadas.

**Seu papel**

Você conduz a iniciativa inteira como arquiteto responsável: define a profundidade, escreve os artefatos, posiciona os gates e responde pelo que for aprovado.

**Insumos disponíveis**

Use o [fluxo completo](fluxo.md#da-intencao-a-implementacao-o-fluxo-completo), os [três gates](fluxo.md#tres-gates-dois-papeis-humanos), o [exemplo arquitetural](exemplo-arquitetural.md) e o [template de ADR](../referencia/template-adr.md). Nenhum dado real deve ser usado.

**Como conduzir**

1. Escreva a constitution com cinco princípios verificáveis. Princípio verificável significa aquele que rejeita alguma coisa: se nenhuma mudança plausível o violaria, ele é decoração.
2. Produza spec com histórias, EARS, BDD, RNFs, segurança e fora de escopo.
3. Compare duas arquiteturas e registre um ADR.
4. Identifique seams e estratégia de testes.
5. Fatia o plano e desenhe dependências.
6. Defina papéis humanos, agentes e três gates.
7. Crie matriz `requisito → decisão → tarefa → teste → evidência`.
8. Defina métricas e feedback de produção para a spec.
9. Verifique a coerência entre os artefatos antes de entregar: cada requisito precisa aparecer no plano, numa tarefa e num teste.

**Entrega esperada**

Pacote versionável que outra equipe consiga implementar sem decisões ocultas em conversa.

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
