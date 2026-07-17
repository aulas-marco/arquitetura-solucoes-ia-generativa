# Exercícios: construir evidência de confiança

Use o assistente de RH quando não houver outro contexto. Nos níveis iniciais, consulte a resposta após tentar. Nos superiores, entregue os artefatos e revise-os pelos critérios de avaliação.

## Recordar

### 1. O que distingue confiança sistêmica de confiança no modelo?

<details>
<summary>Resposta comentada</summary>

Confiança sistêmica é uma expectativa justificada sobre a solução no contexto de uso. Inclui modelo, dados, recuperação, ferramentas, identidade, políticas, pessoas, fornecedores e operação. Avaliar apenas o modelo ignora falhas de composição, como acesso indevido, fonte contaminada ou aprovação humana sem informação.

</details>

### 2. Defina risco inerente e risco residual.

<details>
<summary>Resposta comentada</summary>

Risco inerente é avaliado antes de considerar controles. Risco residual é o que permanece após controles e condições operacionais. Controle pode reduzir probabilidade, impacto, tempo de detecção ou recuperação, mas não transforma automaticamente risco em zero. A aceitação do residual cabe a um proprietário com autoridade.

</details>

### 3. Quais são as seis camadas de guardrails usadas neste módulo?

<details>
<summary>Resposta comentada</summary>

Entrada, contexto, recuperação, ferramenta, saída e aprovação humana. Elas cobrem modos de falha diferentes. A ordem não implica que a última camada seja infalível: aprovação pode falhar por fadiga, viés ou contexto enganoso.

</details>

### 4. Quais dimensões compõem o prisma de avaliação?

<details>
<summary>Resposta comentada</summary>

Factualidade, relevância, fundamentação, segurança, utilidade, latência e custo. Dimensões críticas podem ser portões; dimensões negociáveis podem ter metas. Uma média única não deve compensar um evento intolerável.

</details>

## Compreender

### 5. Por que separar instrução e conteúdo recuperado ajuda, mas não elimina injeção indireta?

<details>
<summary>Resposta comentada</summary>

Marcação de fronteiras, contexto mínimo e tratamento da fonte como dado tornam a intenção arquitetural mais clara e reduzem algumas confusões. Porém o modelo continua processando linguagem de instrução e conteúdo com o mesmo mecanismo, e ataques novos podem atravessar a separação. Por isso autorização e execução de ferramentas permanecem fora do modelo, com catálogo mínimo, política, validação e aprovação por risco.

</details>

### 6. Por que rastreabilidade e minimização não são objetivos opostos?

<details>
<summary>Resposta comentada</summary>

Rastreabilidade requer reconstruir versões, fontes, decisões, aprovações e resultados relevantes; não exige guardar todo conteúdo indefinidamente. Identificadores, hashes, categorias, métricas e amostras controladas podem fornecer evidência com menos exposição. Quando o texto completo for necessário, acesso, finalidade e prazo devem ser explícitos.

</details>

### 7. Compare verificações determinísticas, critérios humanos e avaliação assistida por modelo.

<details>
<summary>Resposta comentada</summary>

Verificações determinísticas são reproduzíveis para propriedades codificáveis, mas não capturam toda nuance. Critérios humanos trazem contexto, mas têm custo, fadiga e divergência. Avaliação assistida por modelo amplia escala, porém introduz variância, viés e correlação. A combinação calibrada produz evidência mais diversa; nenhuma é padrão-ouro universal.

</details>

## Aplicar

### 8. Identificação de ameaças em uma nova integração

**Situação**

O assistente de RH passará a ler anexos enviados por empregados e a criar um rascunho de chamado. O anexo pode ser autorizado para aquele usuário sem ser confiável como instrução. Há risco de injeção indireta, vazamento e consumo econômico.

**Seu papel**

Você é o arquiteto responsável por construir um primeiro modelo de ameaças ligado ao fluxo real, e não apenas copiar nomes de um catálogo.

**Insumos disponíveis**

Use as seis camadas de guardrails do módulo, o diagrama do exemplo arquitetural e os casos sintéticos da oficina de confiança.

**Como conduzir**

1. Desenhe o fluxo anexo → contexto → modelo → rascunho de chamado.
2. Para cinco ameaças, registre ativo, ator, precondição, percurso, impacto e sinal observável.
3. Separe autorização de acesso e integridade do conteúdo.
4. Marque uma hipótese que precisa de teste negativo antes de qualquer piloto.

**Entrega esperada**

Entregue uma tabela com cinco ameaças e um parágrafo explicando a diferença entre anexo autorizado e instrução confiável.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Ativos e atores | 20% | Nomeia o que pode ser afetado e quem participa do percurso. |
| Percursos | 20% | Descreve precondições e caminhos plausíveis até o impacto. |
| Impacto | 20% | Relaciona ameaça a pessoas, organização e efeito operacional. |
| Sinais | 20% | Define evidência que permitiria detectar ou investigar. |
| Autorização e integridade | 20% | Não confunde acesso permitido com conteúdo confiável. |

### 9. Mapeamento de controles por camada

**Situação**

Escolha três ameaças da tabela anterior. O objetivo não é preencher seis caixas com palavras genéricas, mas mostrar qual controle reduz qual percurso e o que permanece possível quando o controle falha.

**Seu papel**

Você é o arquiteto que transforma ameaças em defesa em profundidade, com proprietário e teste.

**Insumos disponíveis**

Use as camadas de entrada, contexto, recuperação, ferramenta, saída e aprovação humana e o relatório da oficina local.

**Como conduzir**

1. Para cada ameaça, escolha controles em camadas diferentes.
2. Declare redução esperada, limite, proprietário e modo de falha.
3. Inclua evidência de teste, especialmente um teste negativo de autorização.
4. Descreva uma degradação segura se um guardrail estiver indisponível.

**Entrega esperada**

Entregue uma matriz ameaça → camadas → controle → limite → teste → proprietário.

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

**Situação**

Após trocar modelo e reindexar políticas, a factualidade média sobe de 3,2 para 3,5 em 4, mas recuperação de documentos vigentes cai de 96% para 91%; gestores melhoram, terceirizados pioram; dois de 80 casos obrigatórios deixam de escalar; latência p95 aumenta 40%; e o avaliador quase nunca discorda.

**Seu papel**

Você é o arquiteto que decide se o rollout pode avançar, separando regressão de recuperação, geração, avaliador e composição.

**Insumos disponíveis**

Use o pipeline de avaliação, as métricas por fatia e os cinco casos sintéticos da oficina. A média global não é suficiente para liberar.

**Como conduzir**

1. Liste sinais por dimensão: factualidade, recuperação, escalonamento, latência e comportamento do avaliador.
2. Formule uma hipótese causal para cada dimensão e diga que evidência a sustentaria.
3. Separe casos de gestores e terceirizados e casos obrigatórios dos demais.
4. Defina experimentos refutáveis e portões que pausam ou bloqueiam o rollout.

**Entrega esperada**

Entregue uma tabela causa → evidência → teste → decisão e um parecer de liberação de até 400 palavras.

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

**Situação**

Um piloto encontrou zero vazamentos em 2 mil casos, 99% de escalonamento obrigatório, custo dentro do orçamento e 8% de falsas recusas. Vazamento teria alto impacto; falsa recusa leva ao canal humano em um dia. Segurança quer ampliar; RH quer corrigir primeiro 1% de falhas de escalonamento.

**Seu papel**

Você é o arquiteto que recomenda tratamento de risco residual, deixando claro quem tem autoridade para aceitar e quando a decisão será revista.

**Insumos disponíveis**

Use as definições de risco inerente e residual, o prisma de avaliação, as métricas do piloto e os critérios do caso.

**Como conduzir**

1. Separe ausência observada de risco zero e descreva a incerteza da amostra.
2. Compare severidade, pessoas afetadas, falsa recusa e falha de escalonamento.
3. Escolha aceitar, reduzir, transferir, suspender ou combinar tratamentos.
4. Defina autoridade, prazo, controle compensatório e gatilho de revisão.

**Entrega esperada**

Entregue parecer de uma página com recomendação, riscos residuais, responsáveis, prazo e gatilhos.

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

Crie uma arquitetura de confiança para um assistente que atende empregados e gestores, usa políticas públicas e restritas, consulta dados pessoais e encaminha casos sensíveis. Entregue:

1. diagrama com atores, ativos, fronteiras, identidade, recuperação, modelo, ferramenta de leitura, validação, aprovação e telemetria;
2. cinco cenários de ameaça, incluindo cadeia de fornecedores e manipulação de memória;
3. controles em profundidade com limitações e modo seguro de falha;
4. governança de minimização, retenção, segregação, catálogo, versões, auditoria e política de uso;
5. critérios de avaliação em quatro níveis para factualidade, fundamentação, segurança e utilidade;
6. conjunto de referência com fatias comuns, raras, adversariais e de recusa;
7. pipeline de avaliação por componente e ponta a ponta, com verificações determinísticas, avaliador assistido por modelo e amostra humana;
8. portões de liberação, canary, rollback e regra de aceitação do risco residual.

Inclua um equivalente textual do diagrama. Justifique cada decisão por cenário e atributo de qualidade. Não use “criptografia”, “filtro” ou “humano no loop” como garantia genérica: diga onde atua, qual falha reduz e qual permanece.

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

Ao revisar, procure “impede”, “garante” e “100% seguro”. Peça evidência, universo testado e modo de falha. Verifique ainda quem mantém, responde ao alerta, aceita o risco e pode desligar. A revisão revela premissas ocultas pelo diagrama.

Feche o módulo com a [Síntese e referências](sintese-e-referencias.md).
