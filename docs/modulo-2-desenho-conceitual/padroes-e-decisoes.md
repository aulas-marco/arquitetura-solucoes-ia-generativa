# Requisitos e padrões de decisão

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

<a id="uma-sequencia-de-decisao"></a>

## Processo de desenho

Nesta etapa do desenho conceitual, o arquiteto deixa de lado a curiosidade pelo modelo e assume o controle do sistema. O objetivo é converter a oportunidade de negócio em uma **progressão de decisões justificadas**. Para isso, utilizamos padrões de arquitetura de software para "envelopar" o comportamento probabilístico da IA, garantindo que os **atributos de qualidade** (segurança, custo, latência e confiabilidade) sejam atendidos.

### O framework de decisão: perguntas antes de componentes

O desenho conceitual não é um evento único, mas uma sequência de perguntas. Cada resposta deve registrar direcionadores, alternativas, consequência, evidência e gatilho de revisão:

- **É preciso gerar?** Regra, cálculo, busca ou template podem atender melhor uma saída determinística.
- **É preciso conhecimento externo?** Contexto selecionado, consulta estruturada, RAG e fine-tuning respondem a necessidades distintas.
- **É preciso agir?** Uma resposta informativa não autoriza ferramenta com efeito.
- **É preciso autonomia?** Workflow preserva caminhos enumeráveis; agente só se justifica quando a variabilidade do plano cria valor.
- **Onde fica a responsabilidade operacional?** Serviço hospedado e execução autogerida deslocam controle, capacidade, custo e risco de formas diferentes.
- **Como a capacidade será obtida?** Construir, comprar e compor distribuem diferenciação, portabilidade, competência e custo de mudança.

### Padrões de conhecimento: RAG versus fine-tuning

Uma das decisões mais críticas no desenho conceitual é como o modelo terá acesso à verdade. Sob a lente da arquitetura, tratamos isso como um **padrão de integração de dados**.

**Prompt e contexto fornecido** servem quando o material cabe na chamada, muda pouco e já foi selecionado por fonte confiável ou usuário. Ainda exigem controle de tamanho, instruções conflitantes, sensibilidade e versão.

**RAG** é candidato quando conhecimento é amplo, muda de forma independente, exige localização, filtros de autorização e evidência granular. O artigo original de [Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html) combina memória paramétrica e não paramétrica para tarefas intensivas em conhecimento. Em produto corporativo, adotar RAG acrescenta ingestão, segmentação, índice, atualização, recuperação, montagem de contexto, proveniência e avaliação separada.

Pergunta decisiva: **o problema é orientar comportamento ou localizar conhecimento?** Prompt governa a execução atual; RAG seleciona evidências externas. Muitas soluções usam ambos. Não adote RAG quando existe uma pequena ficha estruturada consultável diretamente, nem envie todo o repositório ao prompt só porque cabe na janela.

Em resumo:

A. RAG (Retrieval-Augmented Generation)

- **O Padrão:** Conecta o modelo a uma fonte de dados externa (geralmente um banco de dados vetorial) em tempo real.
- **Racional arquitetural:** escolhido quando a **atualidade dos dados** e a **verificabilidade** (citação de fontes) são requisitos primordiais.
- **Trade-offs:** reduz alucinações e custos de treinamento, mas introduz complexidade na infraestrutura de busca e aumenta a latência da resposta devido à etapa extra de recuperação.

B. Fine-tuning (Ajuste Fino)

- **O Padrão:** Treina o modelo para aprender um vocabulário ou comportamento específico.
- **Racional arquitetural:** escolhido para cenários de alta especialização de domínio ou quando o formato da saída deve ser rigidamente controlado.
- **Trade-offs:** melhora a performance em tarefas específicas, mas o conhecimento torna-se **estático**. Qualquer atualização nos dados exige um novo ciclo de treinamento (custo operacional alto).

### Padrões de ação e autonomia: o arquiteto como orquestrador

Em **workflow com LLM**, a equipe define etapas, transições e pontos de decisão; o modelo interpreta ou gera dentro dessas etapas. É preferível quando o processo é conhecido, efeitos são sensíveis e auditabilidade exige caminhos enumeráveis.

Em **agente**, o modelo escolhe próximos passos e ferramentas dentro de limites. É candidato quando a sequência não pode ser enumerada economicamente, o ambiente fornece feedback confiável e o objetivo admite diferentes estratégias. Acrescenta autonomia, estado, orçamento de passos, contratos de ferramenta, autorização por ação, prevenção de loops e avaliação de trajetórias.

Ao avançar para a decisão de "Agir", o arquiteto deve decidir como a IA interagirá com o ecossistema de APIs da organização.

- **Padrão Mediator para Agentes:** Em vez de permitir que o modelo chame APIs diretamente, utilizamos um mediador. A IA decide *o que* fazer, mas o código determinístico do sistema executa a ação, aplica logs e valida a segurança. Isso garante que a autonomia seja **controlada e observável**.
- **Encadeamento de Tarefas (Chains):** Para fluxos complexos, aplicamos o estilo de **Pipes and Filters**. O resultado de uma chamada de IA passa por um "filtro" de validação antes de seguir para o próximo componente, garantindo que erros probabilísticos não se propaguem em cascata pelo sistema distribuído.

### Integração e infraestrutura: o uso de gateways e chassi

Para que a solução seja **operável**, o desenho conceitual deve prever padrões de governança transversais.

- **AI Gateway (Gateway de API Mínimo):** Assim como em microsserviços tradicionais, utilizamos gateways para gerenciar o tráfego. No contexto de IA, o gateway é responsável por:

  - **Throttling e Quotas:** Controlar o consumo de tokens para evitar custos explosivos.
  - **Segurança (Redactions):** Filtrar dados sensíveis (PII) antes que eles saiam para provedores de nuvem externos.
  - **Fallback:** Alternar entre modelos (ex: de um GPT-4 para um modelo local menor) caso o provedor principal falhe ou a latência aumente.
  - **Chassi Arquitetural para IA:** Um conjunto de bibliotecas e padrões que todas as soluções de IA da empresa devem seguir, padronizando a **observabilidade** (rastreamento de prompts) e a injeção de configurações.
- **Escolha do modelo:** considere capacidades, forças e limitações do catálogo de modelos disponível; o nome do fornecedor não substitui avaliação para a tarefa e o risco definidos.
- **Modelo único ou vários modelos:**
  - Um **modelo único** simplifica integração, avaliação e operação. Pode custar demais em tarefas mais específicas e concentrar a dependência.
  - **Múltiplos modelos** permitem roteamento por tarefa, risco, custo ou disponibilidade, mas multiplicam contratos, versões e avaliações. O roteador precisa de critério explícito e evidência para usar o modelo mais apropriado ao contexto.
  - Dica - Comece com a menor diversidade suficiente. Redundância requer compatibilidade, capacidade, teste periódico e degradação.

Um gateway ou chassi não é obrigatório. Ele reduz duplicação de controles e aumenta consistência de telemetria, mas pode centralizar dependências, criar fila de evolução, aumentar latência e virar ponto de falha. Adote-o quando os controles e contratos são realmente compartilhados; mantenha no produto a política de finalidade, autorização e decisão que depende do domínio.

### Hospedado, autogerido e obtenção de capacidade

No **serviço hospedado**, outra organização opera a inferência: há velocidade e elasticidade, mas surgem fronteiras de fornecedor para dados, disponibilidade, versões e portabilidade. No **modelo autogerido**, a organização controla infraestrutura e assume capacidade, atualização, otimização, segurança, escala e plantão. Compare custo total e risco residual no volume e nível de serviço esperados; uma prova em notebook não estima operação autogerida, e preço por token não estima todo o custo hospedado.

**Construir** controla capacidade diferenciadora, assumindo evolução e operação. **Comprar** acelera uma capacidade padronizada, exigindo diligência e saída proporcional ao risco. **Compor** combina serviços, dados e componentes próprios. Decida por capacidade: uma solução pode comprar inferência, reutilizar identidade e construir regras. Preserve dados, métricas, histórico e substituição para evitar dependência sem evidência exportável.

### Formalização da arquitetura: ADRs e evidências

O resultado final deste módulo não é apenas um diagrama, mas um conjunto de **decisões justificáveis**.

- **ADRs (Architecture Decision Records):** cada escolha deve registrar contexto, decisão e consequências técnicas.
- **Evidências sintéticas:** o arquiteto deve definir como provará que a solução funciona, inclusive sob estresse ou diante de entradas maliciosas.

> **Decisão arquitetural:** Uma matriz ajuda a tornar consequências visíveis, mas não decide sozinha. Registre a escolha no [Template de ADR](../referencia/template-adr.md) com contexto, direcionadores, opções, decisão, consequências, evidências e gatilhos de revisão. Diferencie fato medido, restrição confirmada e pressuposto. Quando a evidência é insuficiente, a decisão adequada pode ser “experimento limitado”, com critério explícito de promoção ou abandono.

Ao expandir o desenho conceitual com esses padrões, o arquiteto garante que a IA Generativa não seja um "puxadinho" tecnológico, mas uma **extensão robusta da plataforma de APIs e dados da organização**. O foco sai da "mágica" do prompt e entra no **racional arquitetural**, onde cada componente tem uma função clara, um custo previsto e um risco mitigado.

Requisitos ligam o CONOPS à arquitetura. Em sistemas generativos, essa ligação precisa acomodar comportamento estatístico sem transformar expectativa em promessa vaga. “Responder bem”, “não alucinar” e “ser seguro” não são requisitos verificáveis. Precisamos declarar população, condição, medida, limiar e resposta quando o limiar não for atingido.

## Priorizar características e tensões

| Característica | Prioridade no caso | Tensão aceita | Medida e dono |
|---|---|---|---|
| Privacidade e segurança | Não negociável | minimização pode reduzir detalhe disponível | exposição cruzada zero; Segurança e Privacidade |
| Proveniência | Alta | seleção e registro adicionam latência e armazenamento técnico | afirmações materiais com fonte, versão e finalidade; dono da política |
| Confiabilidade | Alta | fallback pode reduzir capacidade ou cobertura | modo degradado e recuperação testados; Operações |
| Latência e custo | Importante | limites podem restringir modelos ou contexto | p95 e custo por caso; produto e plataforma |
| Modificabilidade | Importante | adaptadores e interfaces aumentam componentes | troca localizada e teste de contrato; arquitetura |

Prioridade é contextual: uma decisão pode sacrificar latência para preservar proveniência em um caso regulado, mas não deve esconder esse custo.

## Como medir a aderência - critérios probabilísticos de aceitação

Um componente probabilístico não exige critérios frouxos; exige critérios estatisticamente honestos. Um critério completo declara:

1. **população:** quais casos, idiomas, grupos e faixas de risco são cobertos;
2. **amostra:** como o conjunto representa frequência, severidade e bordas;
3. **métrica ou critério qualitativo:** o que será observado e por quem;
4. **limiar:** valor global e, quando necessário, por segmento crítico;
5. **incerteza:** tamanho amostral, intervalo ou regra de repetição;
6. **falha intolerável:** evento que reprova independentemente da média;
7. **ação:** liberar, restringir, voltar versão ou encaminhar.

Exemplo: “em 400 contestações estratificadas por categoria e complexidade, pelo menos 90% dos resumos atingem 4/5 em cobertura, com limite inferior do intervalo acordado acima de 87%; zero caso crítico expõe dado de outro cliente; toda afirmação material possui suporte; abaixo desses limites, a categoria afetada permanece fora do escopo”.

Avaliação por outro modelo pode ampliar escala, mas não é verdade de referência. O trabalho primário [G-Eval](https://aclanthology.org/2023.emnlp-main.153/) demonstra uma técnica de avaliação de geração com modelos e alinhamento humano; arquiteturalmente, isso cria nova dependência que deve ser calibrada com especialistas, versionada e auditada. Combine regras, julgamentos humanos, métricas de tarefa e avaliações automatizadas conforme o risco.

**Próxima página:** [Exemplo arquitetural — Banco Lume](exemplo-arquitetural.md).
