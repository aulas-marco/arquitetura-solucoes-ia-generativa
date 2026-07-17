# Exercícios: construir evidência de confiança

Use o [assistente de RH do caso](estudo-de-caso.md#a-proposta). Nos níveis superiores, entregue artefatos e revise-os pelos critérios.

## Recordar

### 1. O que distingue confiança sistêmica de confiança no modelo?

<details>
<summary>Resposta comentada</summary>

Confiança sistêmica é expectativa justificada sobre a solução em uso, considerando modelo, dados, recuperação, ferramentas, identidade, políticas, pessoas, fornecedores e operação. Avaliar só o modelo ignora falhas de composição.

</details>

### 2. Defina risco inerente e risco residual.

<details>
<summary>Resposta comentada</summary>

Risco inerente é avaliado antes dos controles; residual permanece depois deles. Controles reduzem probabilidade, impacto, detecção ou recuperação, mas não tornam risco zero. A aceitação cabe a proprietário com autoridade.

</details>

### 3. Quais são as seis camadas de guardrails usadas neste módulo?

<details>
<summary>Resposta comentada</summary>

Entrada, contexto, recuperação, ferramenta, saída e aprovação humana. Cada camada cobre falhas diferentes; aprovação também pode falhar por fadiga, viés ou contexto enganoso.

</details>

### 4. Quais dimensões compõem o prisma de avaliação?

<details>
<summary>Resposta comentada</summary>

Factualidade, relevância, fundamentação, segurança, utilidade, latência e custo. Dimensões críticas podem ser portões; média não compensa evento intolerável.

</details>

## Compreender

### 5. Por que separar instrução e conteúdo recuperado ajuda, mas não elimina injeção indireta?

<details>
<summary>Resposta comentada</summary>

Fronteiras e contexto mínimo reduzem confusão, mas o modelo processa instruções e conteúdo juntos. Autorização e execução devem ficar fora dele, com catálogo, política, validação e aprovação por risco.

</details>

### 6. Por que rastreabilidade e minimização não são objetivos opostos?

<details>
<summary>Resposta comentada</summary>

Rastreabilidade reconstrói versões, fontes, decisões, aprovações e resultados; não exige guardar tudo. Identificadores, hashes, categorias, métricas e amostras controladas reduzem exposição; texto completo exige acesso, finalidade e prazo.

</details>

### 7. Compare verificações determinísticas, critérios humanos e avaliação assistida por modelo.

<details>
<summary>Resposta comentada</summary>

Verificações determinísticas são reproduzíveis, mas limitadas; critérios humanos trazem contexto com custo e divergência; avaliador-modelo escala com variância e viés. Combine-os com calibração.

</details>

## Aplicar

### 8. Identificação de ameaças em uma nova integração

**Ativo** é o que precisa ser preservado; **ameaça**, a causa potencial de incidente (**o que é** cada um?). Consulte a [definição de ativo e ameaça](conceitos.md#do-perigo-ao-risco-residual) e a [oficina](oficina-de-ferramentas.md).

**Situação**

O assistente de RH passará a ler anexos enviados por empregados e a criar um rascunho de chamado. O anexo pode ser autorizado para aquele usuário sem ser confiável como instrução. Há risco de injeção indireta, vazamento e consumo econômico.

**Seu papel**

Você é o arquiteto que modela ameaças no fluxo real.

**Insumos disponíveis**

Consulte [exemplo](exemplo-arquitetural.md) e [oficina](oficina-de-ferramentas.md).

**Como conduzir**

1. Desenhe o fluxo anexo → contexto → modelo → rascunho de chamado.
2. Para cinco ameaças, registre ativo, ator, precondição, percurso, impacto e sinal observável.
3. Separe autorização de acesso e integridade do conteúdo.
4. Marque uma hipótese que precisa de teste negativo antes de qualquer piloto.

**Entrega esperada**

Entregue uma tabela com cinco ameaças e um parágrafo explicando a diferença entre anexo autorizado e instrução confiável.

**Como verificar**

Confira ativo, ameaça, impacto e sinal nos anexos benigno e malicioso.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Ativos e atores | 20% | Nomeia o que pode ser afetado e quem participa do percurso. |
| Percursos | 20% | Descreve precondições e caminhos plausíveis até o impacto. |
| Impacto | 20% | Relaciona ameaça a pessoas, organização e efeito operacional. |
| Sinais | 20% | Define evidência que permitiria detectar ou investigar. |
| Autorização e integridade | 20% | Não confunde acesso permitido com conteúdo confiável. |

### 9. Mapeamento de controles por camada

**Controle em profundidade** é uma barreira numa camada; seu limite diz o que ainda pode ocorrer (**o que é** controle?). Leia [responsabilidade](conceitos.md#responsabilidade-compartilhada-papeis-identificaveis).

**Situação**

Escolha três ameaças da tabela anterior. O objetivo não é preencher seis caixas com palavras genéricas, mas mostrar qual controle reduz qual percurso e o que permanece possível quando o controle falha.

**Seu papel**

Você é o arquiteto que transforma ameaças em controles testáveis.

**Insumos disponíveis**

Consulte as camadas no [padrão](padroes-e-decisoes.md) e o relatório da [oficina](oficina-de-ferramentas.md).

**Como conduzir**

1. Para cada ameaça, escolha controles em camadas diferentes.
2. Declare redução esperada, limite, proprietário e modo de falha.
3. Inclua evidência de teste, especialmente um teste negativo de autorização.
4. Descreva uma degradação segura se um guardrail estiver indisponível.

**Entrega esperada**

Entregue uma matriz ameaça → camadas → controle → limite → teste → proprietário.

**Como verificar**

Confira percurso, controle, modo de falha e testes negativos.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Cobertura de camadas | 20% | Usa as seis camadas sem presumir que uma delas resolve tudo. |
| Relação causal | 25% | Liga ameaça, controle e redução esperada. |
| Limites e propriedade | 20% | Nomeia o que o controle não garante e quem responde por ele. |
| Testes | 20% | Define evidência reproduzível, incluindo negação. |
| Degradação | 15% | Mantém caminho seguro quando o guardrail falha. |

## Analisar

### 10. Diagnóstico de uma regressão composta

**Fatia** é subconjunto que pode revelar diferença; **portão**, condição que bloqueia promoção (**o que é** cada um?). Consulte [qualidade](conceitos.md#qualidade-tem-varias-dimensoes).

**Situação**

Após trocar modelo e reindexar políticas, a factualidade média sobe de 3,2 para 3,5 em 4, mas recuperação de documentos vigentes cai de 96% para 91%; gestores melhoram, terceirizados pioram; dois de 80 casos obrigatórios deixam de escalar; latência p95 aumenta 40%; e o avaliador quase nunca discorda.

**Seu papel**

Você decide se o rollout avança, separando recuperação, geração, avaliador e composição.

**Insumos disponíveis**

Consulte o [pipeline](estudo-de-caso.md) e os casos da [oficina](oficina-de-ferramentas.md); média global não libera.

**Como conduzir**

1. Liste sinais por dimensão: factualidade, recuperação, escalonamento, latência e comportamento do avaliador.
2. Formule uma hipótese causal para cada dimensão e diga que evidência a sustentaria.
3. Separe casos de gestores e terceirizados e casos obrigatórios dos demais.
4. Defina experimentos refutáveis e portões que pausam ou bloqueiam o rollout.

**Entrega esperada**

Entregue uma tabela causa → evidência → teste → decisão e um parecer de liberação de até 400 palavras.

**Como verificar**

Confira métricas por fatia, portão e evidência refutadora.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Decomposição causal | 25% | Não trata a variação média como causa única. |
| Fatias e severidade | 20% | Considera população, casos obrigatórios e afetados. |
| Avaliador | 15% | Questiona concordância automática e possíveis vieses. |
| Experimentos | 20% | Define testes que podem refutar hipóteses. |
| Decisão de rollout | 20% | Liga evidência a portão, ação e comunicação. |

## Avaliar

### 11. Julgamento de risco residual

**Risco residual** permanece após controles; **critério de avaliação** é regra observável (**o que é** cada um?). Consulte [risco](conceitos.md#do-perigo-ao-risco-residual).

**Situação**

Um piloto encontrou zero vazamentos em 2 mil casos, 99% de escalonamento obrigatório, custo dentro do orçamento e 8% de falsas recusas. Vazamento teria alto impacto; falsa recusa leva ao canal humano em um dia. Segurança quer ampliar; RH quer corrigir primeiro 1% de falhas de escalonamento.

**Seu papel**

Você recomenda tratamento do risco residual, com autoridade e revisão.

**Insumos disponíveis**

Consulte [risco residual](conceitos.md#do-perigo-ao-risco-residual) e [qualidade](conceitos.md#qualidade-tem-varias-dimensoes).

**Como conduzir**

1. Separe ausência observada de risco zero e descreva a incerteza da amostra.
2. Compare severidade, pessoas afetadas, falsa recusa e falha de escalonamento.
3. Escolha aceitar, reduzir, transferir, suspender ou combinar tratamentos.
4. Defina autoridade, prazo, controle compensatório e gatilho de revisão.

**Entrega esperada**

Entregue parecer de uma página com recomendação, riscos residuais, responsáveis, prazo e gatilhos.

**Como verificar**

Confira amostra, autoridade, expiração e gatilho; não confunda “não observado” com “impossível”.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Incerteza | 15% | Não transforma zero casos observados em risco zero. |
| Severidade e afetados | 20% | Diferencia impacto de vazamento, recusa e falha de escalonamento. |
| Tratamento | 20% | Recomenda controles proporcionais ao risco residual. |
| Autoridade e prazo | 20% | Nomeia quem aceita, trata ou suspende e em quanto tempo. |
| Gatilhos e coerência | 25% | Liga decisão, evidência e revisão futura. |

## Criar

### 12. Arquitetura de confiança e critérios de avaliação

**Situação**

Você recebeu um assistente de RH que atende empregados e gestores, consulta políticas públicas e restritas e pode encaminhar casos sensíveis. A arquitetura precisa explicar onde cada controle atua e o que acontece quando ele falha.

**O que é** confiança verificável? Controle, evidência e decisão com limite explícito.

**Seu papel**

Você é o arquiteto responsável por transformar ameaças em controles verificáveis, critérios de avaliação e decisão de risco residual para uma primeira liberação.

**Insumos disponíveis**

Use o [exemplo arquitetural](exemplo-arquitetural.md), o [caso de governança](estudo-de-caso.md#decisoes-de-risco-e-governanca), os [padrões](padroes-e-decisoes.md), a [oficina](oficina-de-ferramentas.md) e o [catálogo](../referencia/atributos-de-qualidade.md).

**Como conduzir**

Fases, checkpoints e modelos:

1. **Fase 1 — Contexto:** preencha `atores | ativos | dados | fronteiras`. **Checkpoint:** usos permitidos e proibidos.
2. **Fase 2 — Ameaças:** preencha `ameaça | percurso | impacto | sinal`. **Checkpoint:** cinco cenários, incluindo fornecedor e memória.
3. **Fase 3 — Controles:** preencha `camada | controle | limite | teste | proprietário`. **Checkpoint:** teste negativo e falha segura.
4. **Fase 4 — Avaliação:** preencha `fatia | critério | evidência | portão`. **Checkpoint:** casos comuns, raros, adversariais e recusa.
5. **Fase 5 — Liberação:** preencha `canary | rollback | residual | autoridade | gatilho`. **Checkpoint:** decisão reversível.

Preencha os oito artefatos:

1. diagrama com atores, ativos, fronteiras, identidade, recuperação, modelo, ferramenta de leitura, validação, aprovação e telemetria;
2. cinco cenários de ameaça, incluindo cadeia de fornecedores e manipulação de memória;
3. controles em profundidade com limitações e modo seguro de falha;
4. governança de minimização, retenção, segregação, catálogo, versões, auditoria e política de uso;
5. critérios de avaliação em quatro níveis para factualidade, fundamentação, segurança e utilidade;
6. conjunto de referência com fatias comuns, raras, adversariais e de recusa;
7. pipeline de avaliação por componente e ponta a ponta, com verificações determinísticas, avaliador assistido por modelo e amostra humana;
8. portões de liberação, canary, rollback e regra de aceitação do risco residual.

**Entrega esperada**

Entregue pacote versionado com os oito artefatos.

Inclua equivalente textual do diagrama e justifique decisões por cenário. Controles devem declarar atuação, falha reduzida e limite.

**Como verificar**

- Siga um caso permitido e um caso adversarial do usuário até recuperação, modelo, ferramenta, aprovação e telemetria.
- Confirme que cada controle tem proprietário, teste, limite e ação de contenção.
- Verifique se critérios, portões, canary, rollback e risco residual aparecem tanto no diagrama quanto no texto.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Ameaças e fronteiras | 15% | Liga ativos, identidade, percursos e efeitos a controles. |
| Identidade e segregação | 15% | Restringe acesso por perfil e impede confiança implícita. |
| Defesas e limites | 15% | Usa camadas independentes e declara falhas residuais. |
| Privacidade | 10% | Define minimização, retenção e acesso no ciclo de vida. |
| Governança | 10% | Nomeia proprietários, responsabilidades e autoridade. |
| Avaliação | 15% | Define critérios multidimensionais, casos e calibração humana. |
| Portões e recuperação | 10% | Inclui canary, rollback e escalonamento obrigatório. |
| Rastreabilidade | 10% | Mantém diagrama, texto, evidências e decisões coerentes. |

## Orientação para revisão entre pares

Ao revisar, procure “impede”, “garante” e “100% seguro”. Peça evidência, universo e modo de falha; verifique responsáveis e autoridade para desligar.

Feche o módulo com a [Síntese e referências](sintese-e-referencias.md).
