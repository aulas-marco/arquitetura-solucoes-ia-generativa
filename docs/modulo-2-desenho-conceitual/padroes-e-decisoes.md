# Requisitos e padrões de decisão

Requisitos ligam o CONOPS à arquitetura. Em sistemas generativos, essa ligação precisa acomodar comportamento estatístico sem transformar expectativa em promessa vaga. “Responder bem”, “não alucinar” e “ser seguro” não são requisitos verificáveis. Precisamos declarar população, condição, medida, limiar e resposta quando o limiar não for atingido.

## Quatro classes de objetivo

Separar objetivos reduz o risco de usar uma métrica intermediária como prova de sucesso.

### Objetivo de negócio

Expressa resultado organizacional ou social, com baseline, prazo, população e contramétricas. Exemplo: “reduzir em 25% a mediana de preparação em três meses, sem elevar devoluções acima do baseline de 8%”.

### Objetivo de produto

Expressa comportamento útil: apresentar resumo, inspecionar fontes, preservar correções e comunicar insuficiência. Adoção não substitui utilidade.

### Objetivo de dados

Expressa cobertura, qualidade, atualização, autorização e proveniência. Exemplo: “políticas aprovadas ficam consultáveis em duas horas e exclusões propagam-se em quinze minutos”.

### Objetivo de IA

Expressa comportamento probabilístico numa tarefa e população. Exemplo: “em casos elegíveis com evidência, 92% dos resumos recebem nota 4/5 e nenhuma afirmação material contradiz a fonte”. O estudo [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) mostra por que uma pontuação única não representa qualidade universal.

## Do requisito ao requisito arquiteturalmente significativo

Um **requisito arquiteturalmente significativo (RAS)** altera estrutura, interfaces, mecanismos ou decisões difíceis de reverter. Nem todo requisito funcional é um RAS. “Exibir o nome do analista” pode ser local; “nenhum dado pessoal cru pode atravessar a fronteira do serviço de inferência” exige classificação, minimização, mascaramento, contrato de fornecedor, telemetria e testes.

Identifique RAS por quatro sinais:

- afeta vários componentes ou uma fronteira de confiança;
- determina um atributo de qualidade sob condição extrema ou frequente;
- impõe risco alto, obrigação regulatória ou dependência externa;
- restringe opções e torna mudança posterior cara.

Use o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md): **fonte, estímulo, ambiente, artefato, resposta e medida**. Acrescente prioridade, dono, verificação e origem para rastrear qualidade até mecanismos e evidências.

## Restrições não são preferências

Restrição limita o espaço de solução antes da comparação. Exemplos: residência de dados em jurisdição definida; revisão humana obrigatória; integração apenas por interface legada aprovada; orçamento mensal; prazo de retenção; acessibilidade; uso de modelos com termos que proíbam treinamento sobre entradas; implantação em ambiente desconectado.

Registre fonte e força. Lei, política, contrato, limitação técnica e preferência têm pesos diferentes. Tratar “autogerido” como obrigação sem confirmação elimina opções; relativizar revisão humana formal cria risco.

## Critérios probabilísticos de aceitação

Um componente probabilístico não exige critérios frouxos; exige critérios estatisticamente honestos. Um critério completo declara:

1. **população:** quais casos, idiomas, grupos e faixas de risco são cobertos;
2. **amostra:** como o conjunto representa frequência, severidade e bordas;
3. **métrica ou rubrica:** o que será observado e por quem;
4. **limiar:** valor global e, quando necessário, por segmento crítico;
5. **incerteza:** tamanho amostral, intervalo ou regra de repetição;
6. **falha intolerável:** evento que reprova independentemente da média;
7. **ação:** liberar, restringir, voltar versão ou encaminhar.

Exemplo: “em 400 contestações estratificadas por categoria e complexidade, pelo menos 90% dos resumos atingem 4/5 em cobertura, com limite inferior do intervalo acordado acima de 87%; zero caso crítico expõe dado de outro cliente; toda afirmação material possui suporte; abaixo desses limites, a categoria afetada permanece fora do escopo”.

Avaliação por outro modelo pode ampliar escala, mas não é verdade de referência. O trabalho primário [G-Eval](https://aclanthology.org/2023.emnlp-main.153/) demonstra uma técnica de avaliação de geração com modelos e alinhamento humano; arquiteturalmente, isso cria nova dependência que deve ser calibrada com especialistas, versionada e auditada. Combine regras, julgamentos humanos, métricas de tarefa e avaliações automatizadas conforme o risco.

## Uma sequência de decisão

Antes das comparações específicas, aplique quatro filtros:

1. **é preciso gerar?** Se regra, consulta ou template resolve, escolha o mecanismo convencional;
2. **é preciso conhecimento externo?** Se a tarefa depende apenas da entrada atual, não introduza recuperação;
3. **é preciso agir?** Se a saída é informativa, não conceda ferramentas de efeito;
4. **é preciso autonomia?** Se etapas e exceções são conhecidas, um workflow preserva previsibilidade.

As decisões não são universais; cada uma responde a direcionadores diferentes.

## Prompt versus RAG

**Prompt e contexto fornecido** servem quando o material cabe na chamada, muda pouco e já foi selecionado por fonte confiável ou usuário. Ainda exigem controle de tamanho, instruções conflitantes, sensibilidade e versão.

**RAG** é candidato quando conhecimento é amplo, muda de forma independente, exige localização, filtros de autorização e evidência granular. O artigo original de [Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html) combina memória paramétrica e não paramétrica para tarefas intensivas em conhecimento. Em produto corporativo, adotar RAG acrescenta ingestão, segmentação, índice, atualização, recuperação, montagem de contexto, proveniência e avaliação separada.

Pergunta decisiva: **o problema é orientar comportamento ou localizar conhecimento?** Prompt governa a execução atual; RAG seleciona evidências externas. Muitas soluções usam ambos. Não adote RAG quando existe uma pequena ficha estruturada consultável diretamente, nem envie todo o repositório ao prompt só porque cabe na janela.

## RAG versus fine-tuning

RAG muda o **contexto disponível em inferência**. Fine-tuning muda **parâmetros e tendências de comportamento** por treinamento adicional. Para conteúdo factual que muda, precisa ser excluído ou citado, RAG geralmente oferece melhor separação entre conhecimento e comportamento. Para formato, estilo, vocabulário, classificação ou padrão de resposta repetitivo, fine-tuning pode ser candidato após prompts e exemplos demonstrarem o comportamento desejado.

Fine-tuning introduz curadoria de dataset, execução de treinamento, avaliação por versão, governança de pesos, rollback e risco de regressão. Não é banco de dados. RAG introduz dependência de recuperação e risco de evidência omitida ou irrelevante. Uma composição pode recuperar fatos e usar modelo adaptado para a tarefa, mas só se o ganho justificar dois ciclos operacionais.

## Workflow versus agente

Em **workflow com LLM**, a equipe define etapas, transições e pontos de decisão; o modelo interpreta ou gera dentro dessas etapas. É preferível quando o processo é conhecido, efeitos são sensíveis e auditabilidade exige caminhos enumeráveis.

Em **agente**, o modelo escolhe próximos passos e ferramentas dentro de limites. É candidato quando a sequência não pode ser enumerada economicamente, o ambiente fornece feedback confiável e o objetivo admite diferentes estratégias. Acrescenta autonomia, estado, orçamento de passos, contratos de ferramenta, autorização por ação, prevenção de loops e avaliação de trajetórias.

Pergunta decisiva: **a variabilidade do plano cria valor suficiente para justificar o novo espaço de falhas?** Se o Banco Lume sempre consulta três fontes, resume, solicita revisão e registra, um workflow é mais claro. Chamar esse fluxo de agente não o torna mais inteligente; apenas obscurece quem controla a transição.

## Modelo único versus múltiplos modelos

Um **modelo único** simplifica integração, avaliação e operação. Pode custar demais em tarefas simples e concentra dependência.

**Múltiplos modelos** permitem roteamento por tarefa, risco, custo ou disponibilidade, mas multiplicam contratos, versões e avaliações. O roteador precisa de critério explícito e evidência de que o fallback é seguro para a mesma categoria.

Comece com a menor diversidade suficiente. Redundância requer compatibilidade, capacidade, teste periódico e degradação.

## Hospedado versus autogerido

No **serviço hospedado**, outra organização opera a inferência. Há velocidade e elasticidade, mas surge fronteira de fornecedor para dados, disponibilidade, versões e portabilidade. Avalie região, retenção, uso de entradas, suporte, observabilidade e saída.

No **modelo autogerido**, a organização controla infraestrutura e assume capacidade, atualização, otimização, segurança, escala e plantão. “Dados ficam dentro” não encerra pesos, dependências e cadeia de suprimentos. O [perfil SSDF para IA generativa do NIST](https://doi.org/10.6028/NIST.SP.800-218A) cobre práticas seguras nesse ciclo.

Compare custo total e risco residual no volume e nível de serviço esperados. Uma prova em notebook não estima operação autogerida; um preço por token não estima todo o custo hospedado.

## Construir, comprar ou compor

- **Construir** controla capacidade diferenciadora, assumindo evolução e operação.
- **Comprar** acelera capacidade padronizada, exigindo diligência e portabilidade.
- **Compor** combina serviços, dados e componentes próprios.

Decida por capacidade: o Banco Lume pode comprar inferência, reutilizar identidade e construir regras. Avalie diferenciação, sensibilidade, maturidade, reversibilidade, competências e custo de mudança.

Evite construir infraestrutura genérica por sensação de controle ou comprar decisão crítica sem evidência exportável. Preserve identidade, dados, métricas, histórico e substituição proporcional ao risco.

## Da comparação à ADR

Uma matriz ajuda a tornar consequências visíveis, mas não decide sozinha. Registre a escolha no [Template de ADR](../referencia/template-adr.md) com contexto, direcionadores, opções, decisão, consequências, evidências e gatilhos de revisão. Diferencie fato medido, restrição confirmada e pressuposto. Quando a evidência é insuficiente, a decisão adequada pode ser “experimento limitado”, com critério explícito de promoção ou abandono.

A página seguinte mostra o encadeamento completo: objetivo, contexto, cenários, vistas, falhas e duas ADRs para o copiloto financeiro.

**Próxima página:** [Exemplo arquitetural — Banco Lume](exemplo-arquitetural.md).
