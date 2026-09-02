# Exercícios: construir evidência de confiança

Todos os exercícios usam o [assistente de RH do caso](estudo-de-caso.md#a-proposta) como cenário. Recordar e Compreender possuem respostas públicas. De Aplicar a Criar, produza artefatos contextualizados e revise-os pelos critérios de avaliação. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

## Recordar

### 1. Confiança sistêmica e confiança no modelo

Um fornecedor apresenta a ficha do modelo com resultados de referência e conclui que a solução é confiável. O assistente de RH usa esse modelo, mas também recuperação, ferramenta de leitura, identidade, políticas e uma fila humana de escalonamento.

Explique em uma frase o que distingue confiança sistêmica de confiança no modelo, e diga o que a ficha do fornecedor deixa de cobrir.

<details>
<summary>Ver resposta</summary>

Confiança sistêmica é expectativa justificada sobre a solução em uso, considerando modelo, dados, recuperação, ferramentas, identidade, políticas, pessoas, fornecedores e operação. Avaliar só o modelo ignora falhas de composição: o índice pode estar desatualizado, a identidade pode resolver o perfil errado, a fila de escalonamento pode não existir na prática. A ficha do fornecedor descreve o componente, não o sistema.

</details>

### 2. Risco inerente e risco residual

Depois de instalar validação de entrada e aprovação humana para casos sensíveis, a equipe do assistente de RH quer registrar no relatório de governança "risco eliminado".

Defina risco inerente e risco residual, e diga por que esse registro está errado.

<details>
<summary>Ver resposta</summary>

Risco inerente é avaliado antes dos controles; residual permanece depois deles. Controles reduzem probabilidade, limitam impacto, aumentam detecção ou facilitam recuperação, mas não tornam risco zero — a aprovação humana, por exemplo, falha por fadiga e por contexto enganoso. "Risco eliminado" não é uma classificação disponível: o que existe é risco residual aceito, com prazo e proprietário nomeado.

</details>

### 3. As seis camadas de guardrails

Uma equipe propõe concentrar toda a proteção na validação de saída, com o argumento de que ali se vê o texto final antes de entregar.

Nomeie as seis camadas de guardrail usadas neste módulo e diga o que a proposta perde.

<details>
<summary>Ver resposta</summary>

Entrada, contexto, recuperação, ferramenta, saída e aprovação humana. Cada camada cobre falhas diferentes, e a validação de saída chega tarde para o que já aconteceu: o documento envenenado já entrou no contexto, a ferramenta já foi chamada, o dado de outro usuário já foi recuperado. Vale ainda a ressalva sobre a última camada — aprovação humana também falha, por fadiga, viés ou contexto enganoso.

</details>

### 4. As dimensões do prisma de avaliação

O relatório de um piloto traz uma única nota agregada: 4,1 de 5. A pessoa responsável pela liberação pergunta se isso basta.

Liste as dimensões que compõem o prisma de avaliação e explique por que a média não responde à pergunta.

<details>
<summary>Ver resposta</summary>

Factualidade, relevância, fundamentação, segurança, utilidade, latência e custo. Dimensões críticas funcionam como portão, não como parcela de uma média: uma nota alta em utilidade e latência pode encobrir uma falha de segurança, e média não compensa evento intolerável. A pergunta certa é qual dimensão está abaixo do limite e para qual fatia de usuários.

</details>

## Compreender

### 5. O limite da separação entre instrução e conteúdo

O assistente de RH marca todo documento recuperado como dado, nunca como instrução, e delimita o bloco com marcadores explícitos. Ainda assim, o time de segurança recusa a afirmação "estamos protegidos contra injeção indireta".

Explique por que a separação ajuda mas não elimina o risco, e diga onde a proteção precisa estar.

<details>
<summary>Ver resposta</summary>

Fronteiras e contexto mínimo reduzem a confusão, mas o modelo processa instrução e conteúdo pelo mesmo mecanismo — não existe canal com garantia de que um trecho seja lido apenas como dado. A consequência arquitetural é que autorização e execução ficam fora do modelo: catálogo de ferramentas, política que decide, validação de saída e aprovação proporcional ao risco. O guardrail de entrada reduz probabilidade; o controle de ferramenta limita impacto.

</details>

### 6. Rastreabilidade e minimização

A área de privacidade quer reter o mínimo possível. A área de auditoria quer reconstruir qualquer atendimento questionado. As duas tratam a discussão como disputa de soma zero.

Explique por que rastreabilidade e minimização não são objetivos opostos, e dê dois exemplos do que gravar no lugar do conteúdo integral.

<details>
<summary>Ver resposta</summary>

Rastreabilidade exige reconstruir versões, fontes, decisões, aprovações e resultados — não exige guardar tudo. Identificadores de documento, *hashes* do prompt, versão do índice, categorias de decisão, métricas e amostras controladas sustentam a auditoria com exposição bem menor que o texto completo. Quando o conteúdo integral for mesmo necessário, ele passa a exigir acesso restrito, finalidade declarada e prazo de expiração — vira exceção governada, não o padrão de coleta.

</details>

### 7. Três formas de verificar

Para liberar uma mudança no assistente, a equipe tem três instrumentos disponíveis: um conjunto de testes automáticos com resposta esperada fixa, uma revisão feita por duas pessoas de RH, e o avaliador `GEval` do laboratório com juiz local.

Compare os três quanto a reprodutibilidade, custo e viés, e proponha como combiná-los.

<details>
<summary>Ver resposta</summary>

Verificações determinísticas são reproduzíveis e baratas, mas só cobrem o que foi antecipado em regra. Critérios humanos trazem contexto e julgamento sobre casos novos, com custo alto e divergência entre revisores. O avaliador assistido por modelo escala para muitos casos, com variância entre execuções e viés — agravado quando o mesmo modelo responde e julga, como no laboratório. A combinação usual: determinístico como portão do que é objetivo, avaliador-modelo para varredura ampla, e amostra humana periódica para calibrar o avaliador e arbitrar divergência.

</details>

## Aplicar

### 8. Identificação de ameaças em uma nova integração

**O que é:** **ativo** é o que precisa ser preservado; **ameaça** é a causa potencial de incidente. Consulte a [definição de ativo e ameaça](conceitos.md#do-perigo-ao-risco-residual) e a [oficina](oficina-de-ferramentas.md).

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

**O que é:** **controle em profundidade** é uma barreira numa camada; seu limite diz o que ainda pode ocorrer. Leia [responsabilidade](conceitos.md#responsabilidade-compartilhada-papeis-identificaveis).

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

**O que é:** **fatia** é subconjunto que pode revelar diferença; **portão** é condição que bloqueia promoção. Consulte [qualidade](conceitos.md#qualidade-tem-varias-dimensoes).

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

### 11. Comparação de decisões seguras entre Lume e Aurora

**O que é:** um **avaliador assistido por modelo** (`GEval` com juiz `OllamaModel`) pontua se uma resposta corresponde a um critério declarado; a nota é evidência, não veredito de segurança. Consulte [Guardrails em profundidade](padroes-e-decisoes.md#guardrails-em-profundidade) e os registros de risco do [Lume](caso-lume.md#registro-de-risco) e da [Aurora](caso-aurora.md#registro-de-risco).

**Situação**

Você rodou `avaliar_confianca_lume_aurora.py` duas vezes — `--caso lume` e `--caso aurora` — e tem os dois relatórios (`relatorio-confianca-lume.json`, `relatorio-confianca-aurora.json`) com nota e justificativa por caso sintético. A Aurora tem três casos que só existem por causa da camada de ferramenta (`A-01`, `A-02`, `A-05`); os outros dois pares (`L-02`/`A-03`, `L-04`/`A-04`) têm estrutura equivalente entre os dois casos.

**Seu papel**

Você é o arquiteto que decide se a diferença de nota entre Lume e Aurora reflete diferença real de risco ou apenas variação do juiz.

**Insumos disponíveis**

Os dois relatórios JSON gerados pelo laboratório, o [registro de risco do Lume](caso-lume.md#registro-de-risco), o [registro de risco da Aurora](caso-aurora.md#registro-de-risco) e o [padrão de guardrails em profundidade](padroes-e-decisoes.md#guardrails-em-profundidade).

**Como conduzir**

1. Separe os cinco casos da Aurora em dois grupos: exclusivos da camada de ferramenta (`A-01`, `A-02`, `A-05`) e estruturalmente equivalentes ao Lume (`A-03` com `L-02`; `A-04` com `L-04`).
2. Para os três casos exclusivos, verifique se a nota alta (quando houver) decorre de o Ollama ter respondido com segurança por conta própria, ou de um controle de camada de ferramenta que o script não simula — ele só chama o modelo, sem executar catálogo, contrato por ferramenta ou orçamento de passos reais.
3. Para os pares equivalentes, compare nota e justificativa entre Lume e Aurora; considere como hipóteses variação do juiz, ambiguidade do texto de entrada e diferença real de contexto.
4. Decida se a nota isolada do relatório basta para liberar promoção, ou que evidência complementar (teste negativo de catálogo, orçamento de passos observado, revisão humana) seria exigida antes de uma liberação real.

**Entrega esperada**

Entregue uma tabela caso → grupo (exclusivo de ferramenta ou equivalente) → nota → justificativa observada → evidência complementar necessária, e um parágrafo de até 200 palavras concluindo se a Aurora é ou não mais arriscada do que o relatório automatizado sozinho sugere.

**Como verificar**

Confira se a tabela nomeia os cinco casos da Aurora, separa os grupos corretamente e se o parágrafo não trata a nota do `GEval` como prova de controle real de ferramenta.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Separação por grupo | 20% | Distingue casos exclusivos de ferramenta dos equivalentes ao Lume. |
| Leitura crítica do juiz | 25% | Não confunde nota alta do `GEval` com controle de ferramenta real. |
| Comparação Lume × Aurora | 20% | Usa os pares equivalentes para isolar variação do juiz de diferença real. |
| Evidência complementar | 20% | Nomeia teste ou controle que o script não cobre. |
| Conclusão fundamentada | 15% | O parágrafo final liga evidência a uma posição sobre risco relativo. |

## Avaliar

### 12. Julgamento de risco residual

**O que é:** **risco residual** permanece após controles; **critério de avaliação** é regra observável. Consulte [risco](conceitos.md#do-perigo-ao-risco-residual).

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
4. Defina autoridade, prazo, controle compensatório, fitness function e gatilho de revisão.

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
| Gatilhos, fitness functions e coerência | 25% | Liga decisão, evidência verificável e revisão futura. |

## Criar

### 13. Arquitetura de confiança e critérios de avaliação

**Situação**

Você recebeu um assistente de RH que atende empregados e gestores, consulta políticas públicas e restritas e pode encaminhar casos sensíveis. A arquitetura precisa explicar onde cada controle atua e o que acontece quando ele falha.

**O que é** confiança verificável? Controle, evidência e decisão com limite.

**Seu papel**

Você é o arquiteto responsável por transformar ameaças em controles verificáveis, critérios de avaliação e decisão de risco residual para uma liberação.

**Insumos disponíveis**

Use o [exemplo arquitetural](exemplo-arquitetural.md), o [caso de governança](estudo-de-caso.md#decisoes-de-risco-e-governanca), os [padrões](padroes-e-decisoes.md), a [oficina](oficina-de-ferramentas.md) e o [catálogo](../referencia/atributos-de-qualidade.md).

**Como conduzir**

**Campos:** ator/ativo = sujeito/alvo; percurso = caminho; limite = condição aceitável; portão = bloqueio; residual = risco restante.

Fases, checkpoints e modelos:

1. **Fase 1 — Contexto:** preencha `atores | ativos | dados | fronteiras`. **Checkpoint:** usos permitidos e proibidos.
2. **Fase 2 — Ameaças:** preencha `ameaça | percurso | impacto | sinal`. **Checkpoint:** cinco cenários, incluindo fornecedor e memória.
3. **Fase 3 — Controles:** preencha `camada | controle | limite | teste | proprietário`. Declare que recuperação, guardrail, política, avaliação, aprovação e observabilidade não decidem no lugar um do outro. **Checkpoint:** teste negativo e falha segura.
4. **Fase 4 — Avaliação:** preencha `fatia | critério | evidência | portão`. Declare prioridade e tensão entre segurança, privacidade, auditabilidade, confiabilidade, utilidade, latência, custo e modificabilidade. **Checkpoint:** casos comuns, raros, adversariais e recusa.
5. **Fase 5 — Liberação:** preencha `canary | rollback | residual | autoridade | fitness function | gatilho`. **Checkpoint:** decisão reversível.

Preencha os oito artefatos:

1. diagrama com atores, ativos, fronteiras, identidade, recuperação, modelo, ferramenta de leitura, validação, aprovação e telemetria;
2. cinco cenários de ameaça, incluindo cadeia de fornecedores e manipulação de memória;
3. controles em profundidade com limitações e modo seguro de falha;
4. governança de minimização, retenção, segregação, catálogo, versões, auditoria e política de uso;
5. critérios de avaliação em quatro níveis para factualidade, fundamentação, segurança e utilidade;
6. conjunto de referência com fatias comuns, raras, adversariais e de recusa;
7. pipeline de avaliação por componente e ponta a ponta, com verificações determinísticas, avaliador assistido por modelo e amostra humana;
8. portões de liberação, canary, rollback e regra de aceitação do risco residual.
9. fitness functions para autorização, regressão, escalonamento, trace e mudança de dependência, com responsável e reação à falha.

**Entrega esperada**

Entregue pacote versionado com os oito artefatos.

Inclua equivalente textual; declare atuação, falha e limite.

**Como verificar**

- Siga um caso permitido e um caso adversarial do usuário até recuperação, modelo, ferramenta, aprovação e telemetria.
- Confirme que cada controle tem proprietário, teste, limite e ação de contenção.
- Verifique se cada fitness function tem limiar, responsável e reação quando a condição falhar.
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
| Portões, fitness functions e recuperação | 10% | Inclui canary, rollback, escalonamento e reação à falha. |
| Rastreabilidade | 10% | Mantém diagrama, texto, evidências e decisões coerentes. |

## Orientação para revisão entre pares

Ao revisar, procure “impede”, “garante” e “100% seguro”. Peça evidência, universo e modo de falha; verifique responsáveis e autoridade para desligar.

Feche o módulo com a [Síntese e referências](sintese-e-referencias.md).
