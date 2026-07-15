# Plano de Disciplina — Arquitetura de Soluções com IA Generativa

## 1. Identificação

| Item | Definição |
|---|---|
| Disciplina | Arquitetura de Soluções com IA Generativa |
| Carga horária | 24 horas |
| Organização | 6 encontros de 4 horas |
| Nível | Pós-graduação — formação de especialistas |
| Modalidade didática | Aulas conceituais, análise de arquiteturas, estudos de caso e protótipos orientados |
| Pré-requisitos | Fundamentos de arquitetura de software, sistemas distribuídos, APIs, dados e computação em nuvem |

## 2. Ementa

Fundamentos de sistemas com inteligência artificial generativa. Modelos fundacionais e propriedades arquiteturalmente significativas dos grandes modelos de linguagem. Anatomia e ciclo de vida de soluções generativas. Desenho conceitual, requisitos e atributos de qualidade. Seleção entre prompting, RAG, uso de ferramentas, agentes e fine-tuning. Arquiteturas de recuperação de conhecimento. Agentes e integração com sistemas corporativos. Segurança, privacidade, guardrails e governança. Avaliação, observabilidade e LLMOps. Plataformas corporativas de IA generativa. Análise de trade-offs e comunicação de decisões arquiteturais.

## 3. Contexto e posicionamento

A disciplina parte do pressuposto de que os alunos já conhecem os fundamentos de arquitetura de software. O objetivo não é reapresentar estilos arquiteturais tradicionais, mas analisar como as propriedades probabilísticas, orientadas por dados e dependentes de modelos modificam o trabalho do arquiteto.

A primeira aula realiza um nivelamento específico em IA generativa para criar um vocabulário comum entre alunos com diferentes experiências no tema. Nas aulas seguintes, os conceitos são aprofundados antes da apresentação dos respectivos estudos de caso.

O livro *Architecting AI Software Systems* fornece a base conceitual. Sua sequência não será reproduzida literalmente: os capítulos serão reorganizados em torno das decisões que um arquiteto de soluções com IA generativa precisa tomar.

## 4. Objetivo geral

Capacitar os alunos a projetar, avaliar e defender arquiteturas de soluções com IA generativa, considerando valor de negócio, dados, conhecimento, modelos, integração, atributos de qualidade, riscos, governança e operação em produção.

## 5. Resultados de aprendizagem

Ao final da disciplina, o aluno deverá ser capaz de:

1. Explicar as propriedades dos modelos generativos que afetam o desenho de sistemas.
2. Distinguir modelo, componente inteligente, aplicação de IA e sistema sociotécnico completo.
3. Identificar casos nos quais IA generativa é adequada ou inadequada.
4. Selecionar, combinar e justificar prompting, RAG, ferramentas, agentes e fine-tuning.
5. Transformar objetivos de negócio em requisitos e atributos de qualidade verificáveis.
6. Decompor soluções generativas em componentes, responsabilidades e interfaces.
7. Projetar pipelines de ingestão, recuperação e geração fundamentada em conhecimento.
8. Definir limites de autonomia e mecanismos de controle para agentes.
9. Incorporar segurança, privacidade, guardrails, auditoria e governança desde o desenho.
10. Definir estratégias de avaliação, observabilidade e operação contínua.
11. Analisar trade-offs entre qualidade, latência, custo, controle e dependência de fornecedores.
12. Comunicar e defender decisões por meio de diagramas, cenários e registros arquiteturais.

## 6. Princípios didáticos

### 6.1 Conceitos antes dos casos

Cada encontro segue a sequência:

> conceituar → exemplificar → comparar padrões → aplicar no caso → refletir

O estudo de caso é utilizado para consolidar e avaliar a compreensão dos conceitos, e não para introduzi-los sem preparação.

### 6.2 Arquitetura aplicada

Os protótipos são pequenos experimentos destinados a validar hipóteses arquiteturais. A disciplina não pretende ensinar um framework específico nem se transformar em um curso intensivo de programação.

### 6.3 Estudos de caso independentes

Cada encontro utiliza um domínio diferente. Assim, o aluno entra em contato com múltiplos contextos, restrições e atributos de qualidade. Os casos são independentes, mas a complexidade das decisões aumenta progressivamente.

### 6.4 Independência de fornecedor

Produtos e plataformas podem aparecer como exemplos, mas os conceitos, padrões e critérios de decisão devem ser ensinados de forma independente de fornecedor.

### 6.5 Evidências em lugar de preferências

Toda decisão arquitetural deve ser relacionada a objetivos, cenários, atributos de qualidade, riscos ou evidências produzidas por experimentos.

## 7. Organização-padrão de cada encontro

| Etapa | Duração | Finalidade |
|---|---:|---|
| Apresentação dos conceitos | 70 min | Construção do vocabulário e dos modelos mentais |
| Padrões e exemplos arquiteturais | 40 min | Materialização dos conceitos |
| Intervalo | 15 min | Pausa |
| Análise comparativa | 35 min | Discussão de alternativas e trade-offs |
| Estudo de caso | 55 min | Aplicação orientada |
| Experimento ou protótipo | 35 min | Validação de uma hipótese arquitetural |
| Síntese e avaliação | 30 min | Consolidação, defesa e feedback |
| **Total** | **240 min** | **4 horas** |

Os tempos podem ser ajustados de acordo com a complexidade da oficina, preservando-se a ordem didática.

---

# 8. Programação aula a aula

<a id="modulo-1"></a>

## Encontro 1 — Fundamentos de sistemas com IA generativa

### Propósito

Criar uma base comum para alunos com diferentes níveis de familiaridade com IA generativa e prepará-los para interpretar arquiteturas mais complexas nos encontros seguintes.

### Resultados específicos

Ao final do encontro, o aluno deverá conseguir:

- explicar a diferença entre modelo generativo, aplicação de IA e sistema de IA;
- identificar componentes determinísticos e probabilísticos;
- reconhecer as principais camadas de uma solução generativa;
- descrever, em nível introdutório, prompting, RAG, ferramentas, agentes e fine-tuning;
- identificar atributos de qualidade e riscos iniciais.

### Conceitos

#### 1. De software convencional a sistemas com IA

- Componentes determinísticos e probabilísticos.
- Não determinismo e comportamento emergente.
- Dados e contexto como parte do comportamento do sistema.
- Diferença entre testar código e avaliar comportamento.
- Modelo, componente inteligente, aplicação e sistema sociotécnico.
- Ampliação das responsabilidades do arquiteto.

#### 2. Fundamentos de IA generativa

- Modelos fundacionais e grandes modelos de linguagem.
- Treinamento, inferência e geração.
- Tokens, contexto e janela de contexto.
- Prompts, mensagens e parâmetros de geração.
- Embeddings e representação semântica.
- Conhecimento paramétrico e suas limitações.
- Alucinação, variabilidade e desatualização.
- Modelos proprietários, abertos, hospedados e autogerenciados.
- Introdução à multimodalidade.

Não é objetivo da aula estudar em profundidade a matemática dos modelos. O foco está nas propriedades que afetam decisões de arquitetura.

#### 3. Anatomia de uma solução generativa

Arquitetura de referência inicial organizada em camadas:

1. Canais e experiência do usuário.
2. Aplicação, serviços e APIs.
3. Orquestração e gerenciamento de contexto.
4. Modelos e serviços de inferência.
5. Conhecimento, dados e memória.
6. Ferramentas e sistemas corporativos.
7. Infraestrutura e operação.
8. Segurança, governança, avaliação e observabilidade como capacidades transversais.

#### 4. Mapa inicial das abordagens

- Prompting e geração direta.
- Geração com contexto fornecido.
- Retrieval-Augmented Generation — RAG.
- Uso de ferramentas.
- Workflows com LLM.
- Agentes.
- Fine-tuning.
- Combinação de abordagens.

#### 5. Atributos de qualidade

- Qualidade e fundamentação das respostas.
- Latência percebida.
- Custo por interação.
- Privacidade e segurança.
- Disponibilidade e resiliência.
- Observabilidade.
- Explicabilidade e rastreabilidade.
- Manutenibilidade diante da evolução dos modelos.
- Controle da autonomia.

### Estudo de caso

**Assistente de consulta a documentos internos.**

Os alunos recebem três propostas: conexão direta com um modelo, envio integral de documentos ao contexto e arquitetura inicial com recuperação de conhecimento. A atividade consiste em identificar componentes, riscos, pressupostos e perguntas não respondidas. Não se espera o desenho completo de um RAG.

### Experimento orientado

Comparar respostas geradas:

1. Sem contexto adicional.
2. Com um documento completo no prompt.
3. Com trechos relevantes previamente selecionados.

A turma analisa o efeito sobre qualidade, custo, latência, rastreabilidade e arquitetura.

### Entregável avaliativo

Leitura arquitetural comentada contendo:

- componentes identificados;
- cinco riscos ou incertezas;
- atributos de qualidade prioritários;
- recomendação preliminar de abordagem.

### Leitura-base

- *Fundamentals of AI System Architecture*.
- *The Case for Architecture*.
- eBook *Fundamentos da Arquitetura de Sistemas de Inteligência Artificial*.

---

<a id="modulo-2"></a>

## Encontro 2 — Desenho conceitual e decisões arquiteturais

### Propósito

Ensinar a transformar uma oportunidade de IA generativa em uma concepção de sistema justificável antes da escolha de tecnologias ou do início da implementação.

### Resultados específicos

Ao final do encontro, o aluno deverá conseguir:

- avaliar se IA generativa é apropriada para um problema;
- alinhar objetivos de negócio, experiência, IA e operação;
- elaborar cenários, casos de uso e modos operacionais;
- especificar requisitos verificáveis para comportamento probabilístico;
- comparar prompting, RAG, ferramentas, agentes e fine-tuning;
- registrar decisões e alternativas descartadas.

### Conceitos

#### 1. Da oportunidade ao Concept of Operations

- Problema, oportunidade e hipótese de valor.
- Stakeholders, usuários afetados e operadores.
- Limites do sistema e dependências externas.
- Cenários de uso normal, exceção, manutenção e recuperação.
- Interação humano–IA e distribuição de responsabilidades.
- Critérios para não utilizar IA generativa.

#### 2. Objetivos e requisitos

- Objetivos de negócio, produto, dados e IA.
- Requisitos funcionais e não funcionais.
- Requisitos para respostas probabilísticas.
- Critérios de aceitação baseados em distribuições e limiares.
- Restrições legais, organizacionais, financeiras e operacionais.
- Priorização de atributos de qualidade.

#### 3. Estratégias de solução

- Prompting versus busca de conhecimento.
- RAG versus fine-tuning.
- Workflow determinístico versus agente.
- Modelo único versus estratégia multimodelo.
- Serviço gerenciado versus modelo autogerenciado.
- Buy, build e composição de capacidades.

#### 4. Comunicação das decisões

- Diagrama de contexto.
- Diagrama de contêineres ou blocos funcionais.
- Cenários de atributos de qualidade.
- Registros de decisão arquitetural.
- Riscos, hipóteses e experimentos necessários.

### Estudo de caso

**Copiloto para atendimento em uma empresa de serviços financeiros.**

A organização quer reduzir o tempo médio de atendimento, mas possui dados sensíveis, sistemas legados e exigência de revisão humana. Os grupos devem comparar uma automação convencional, um copiloto baseado em contexto, um RAG e um agente com ferramentas.

### Experimento orientado

Testar a mesma tarefa com três configurações de contexto e observar variação, aderência às instruções e capacidade de justificar a resposta.

### Entregável avaliativo

- Diagrama de contexto.
- Cenário de uso principal e cenário de falha.
- Cinco requisitos arquiteturalmente significativos.
- Dois registros de decisão com alternativas e consequências.

### Leitura-base

- *The Case for Architecture*.
- *Software Engineering and Architecture*.
- *Conceptual Design for AI Systems*.

---

<a id="modulo-3"></a>

## Encontro 3 — Arquitetura de RAG e sistemas de conhecimento

### Propósito

Projetar soluções capazes de produzir respostas fundamentadas, rastreáveis e atualizáveis a partir de fontes de conhecimento controladas.

### Resultados específicos

Ao final do encontro, o aluno deverá conseguir:

- explicar o pipeline completo de uma arquitetura RAG;
- projetar ingestão, preparação, indexação e recuperação;
- selecionar estratégias de segmentação, metadados e busca;
- incorporar controle de acesso e proveniência;
- definir métricas para recuperação e resposta;
- analisar trade-offs entre RAG, contexto longo e fine-tuning.

### Conceitos

#### 1. Fundamentos de recuperação aumentada

- Limitações do conhecimento paramétrico.
- Separação entre conhecimento, recuperação e geração.
- Fluxos offline e online.
- Fontes estruturadas, semiestruturadas e não estruturadas.
- Relação entre recuperação, contexto e resposta.

#### 2. Pipeline de conhecimento

- Aquisição, extração, limpeza e normalização.
- Segmentação de conteúdo.
- Enriquecimento e metadados.
- Embeddings e indexação vetorial.
- Atualização, versionamento e remoção.
- Proveniência e linhagem do conteúdo.

#### 3. Pipeline de consulta

- Transformação e expansão da consulta.
- Busca vetorial, lexical e híbrida.
- Filtros por metadados e autorização.
- Reranking.
- Montagem e compressão de contexto.
- Geração de respostas com evidências e citações.
- Tratamento da ausência de evidência.

#### 4. Padrões e variações

- RAG simples.
- RAG híbrido.
- RAG hierárquico.
- RAG adaptativo.
- Recuperação corretiva.
- Recuperação em múltiplas fontes.
- RAG para dados estruturados.

#### 5. Avaliação e atributos de qualidade

- Precisão e cobertura da recuperação.
- Relevância do contexto.
- Fundamentação e fidelidade da resposta.
- Atualidade e proveniência.
- Latência e custo.
- Segurança e isolamento do conhecimento.

### Estudo de caso

**Assistente corporativo para políticas, contratos e documentos internos.**

O sistema deve respeitar permissões individuais, citar fontes, refletir atualizações rapidamente e informar quando não possui evidência suficiente.

### Experimento orientado

Comparar duas estratégias de segmentação e recuperação em um pequeno conjunto documental. Identificar como as escolhas alteram precisão, contexto, custo e resposta.

### Entregável avaliativo

- Diagrama dos fluxos offline e online.
- Responsabilidades dos principais componentes.
- Estratégia de autorização e proveniência.
- Três decisões arquiteturais justificadas.
- Plano mínimo de avaliação.

### Leitura-base

- *Requirements and Architecture for AI Pipelines*.
- *Design, Integration, and Testing*.
- *Architecting a Generative AI System – A Case Study*.

---

<a id="modulo-4"></a>

## Encontro 4 — Agentes e integração com sistemas corporativos

### Propósito

Projetar soluções que utilizam modelos para selecionar ferramentas, coordenar etapas e executar ações, mantendo limites claros de autonomia e controle.

### Resultados específicos

Ao final do encontro, o aluno deverá conseguir:

- diferenciar chatbot, copiloto, workflow e agente;
- decidir quando a autonomia é justificável;
- projetar ferramentas e contratos de integração seguros;
- modelar estado, memória e fluxo de execução;
- incorporar aprovação humana e contenção de falhas;
- analisar arquiteturas de agente único e múltiplos agentes.

### Conceitos

#### 1. Do modelo que responde ao sistema que age

- Geração, decisão e ação.
- Uso de ferramentas e saídas estruturadas.
- Planejamento e decomposição de tarefas.
- Workflows determinísticos com etapas generativas.
- Autonomia progressiva.

#### 2. Arquitetura de agentes

- Orquestrador.
- Catálogo e contratos de ferramentas.
- Estado da execução.
- Memória de trabalho e memória persistente.
- Contexto e políticas.
- Agente único e especialização por agentes.
- Supervisão e coordenação.

#### 3. Integração corporativa

- APIs, mensageria e eventos.
- Sistemas legados e adaptadores.
- Identidade do usuário e delegação de autorização.
- Idempotência, timeout, retry e circuit breaker.
- Transações, compensações e consistência.
- Auditoria das ações.

#### 4. Limites e controles

- Matriz de autonomia.
- Aprovação humana antes e depois da ação.
- Políticas sobre ferramentas e parâmetros.
- Orçamento de etapas, tempo e custo.
- Fallback para workflow determinístico.
- Interrupção e recuperação.

#### 5. Trade-offs

- Flexibilidade versus previsibilidade.
- Autonomia versus controle.
- Agente único versus múltiplos agentes.
- Memória versus privacidade.
- Acoplamento com ferramentas e fornecedores.

### Estudo de caso

**Agente de resolução de solicitações de clientes.**

O agente consulta CRM, estoque, pedidos e políticas comerciais. Algumas ações exigem confirmação do cliente; outras dependem de aprovação de um supervisor.

### Experimento orientado

Executar um protótipo com duas ferramentas simuladas. Observar seleção incorreta, parâmetros inválidos, repetição de ações e falhas de integração. Em seguida, adicionar restrições e comparar o comportamento.

### Entregável avaliativo

- Diagrama de sequência do caminho principal.
- Fluxos de exceção e compensação.
- Matriz de autonomia.
- Contrato conceitual de duas ferramentas.
- Estratégia de tratamento de falhas.

### Leitura-base

- *Software Engineering and Architecture*.
- *Conceptual Design for AI Systems*.
- *Design, Integration, and Testing*.
- *Architecting a Generative AI System – A Case Study*.

---

<a id="modulo-5"></a>

## Encontro 5 — Confiança, segurança, avaliação e governança

### Propósito

Projetar sistemas generativos cujo comportamento possa ser limitado, avaliado e auditado de forma compatível com seu contexto de risco.

### Resultados específicos

Ao final do encontro, o aluno deverá conseguir:

- modelar ameaças específicas de aplicações com LLMs;
- definir guardrails em diferentes pontos da arquitetura;
- projetar controles de privacidade, isolamento e auditoria;
- decompor qualidade em dimensões verificáveis;
- elaborar uma estratégia de avaliação proporcional ao risco;
- definir responsabilidades e artefatos de governança.

### Conceitos

#### 1. Confiança como propriedade sistêmica

- Limites do modelo e limites do sistema.
- Risco técnico, operacional, jurídico e reputacional.
- Rastreabilidade e prestação de contas.
- Distribuição de responsabilidades entre pessoas, equipes e fornecedores.

#### 2. Segurança de aplicações generativas

- Prompt injection direta e indireta.
- Vazamento de contexto, dados e segredos.
- Uso indevido de ferramentas.
- Conteúdo não confiável recuperado de fontes externas.
- Manipulação de memória e estado.
- Ataques de negação de serviço econômico.
- Dependência da cadeia de fornecedores.

#### 3. Guardrails por camada

- Validação de entrada.
- Isolamento e filtragem do contexto.
- Políticas de recuperação.
- Restrição de ferramentas e parâmetros.
- Validação de saídas.
- Regras determinísticas e classificadores.
- Aprovação humana.
- Recusa, fallback e degradação segura.

#### 4. Privacidade e governança

- Minimização e finalidade dos dados.
- Retenção, exclusão e mascaramento.
- Segregação entre usuários e organizações.
- Catálogo de modelos, prompts, fontes e ferramentas.
- Versionamento e aprovação de mudanças.
- Evidências, logs e trilhas de auditoria.
- Políticas de uso e responsabilidade humana.

#### 5. Avaliação de sistemas generativos

- Qualidade como conceito multidimensional.
- Avaliação de factualidade, relevância, fundamentação e segurança.
- Critérios determinísticos, rubricas humanas e avaliação apoiada por modelos.
- Conjuntos de referência e cenários adversariais.
- Testes de regressão.
- Avaliação de componentes e de ponta a ponta.
- Limitações e vieses do avaliador automatizado.

### Estudo de caso

**Assistente de recursos humanos.**

O sistema processa documentos internos e responde sobre políticas, benefícios e situações funcionais. Ele deve proteger dados pessoais, separar conteúdos públicos e restritos e encaminhar situações sensíveis para especialistas humanos.

### Experimento orientado

Executar cenários normais e adversariais contra um protótipo. Aplicar controles em diferentes camadas e comparar taxa de bloqueio, falsos positivos, utilidade e capacidade de auditoria.

### Entregável avaliativo

- Threat model.
- Mapa de guardrails por camada.
- Matriz de riscos e controles.
- Conjunto mínimo de cenários de avaliação.
- Papéis e decisões de governança.

### Leitura-base

- *The Case for Architecture* — governança, conformidade e explicabilidade.
- *Conceptual Design for AI Systems* — mitigação de riscos.
- *Design, Integration, and Testing* — requisitos e tipos de teste.

---

<a id="modulo-6"></a>

## Encontro 6 — Operação, LLMOps e plataformas corporativas

### Propósito

Integrar as decisões dos encontros anteriores em uma arquitetura operável, evolutiva e reutilizável em escala organizacional.

### Resultados específicos

Ao final do encontro, o aluno deverá conseguir:

- projetar observabilidade para componentes generativos;
- definir versionamento e entrega controlada;
- relacionar avaliações offline e monitoramento online;
- desenhar mecanismos de fallback, canary e rollback;
- identificar serviços compartilháveis em uma plataforma corporativa;
- analisar trade-offs entre padronização, autonomia e dependência de fornecedor.

### Conceitos

#### 1. O ciclo operacional

- Da experimentação à produção.
- Ambientes, configurações e segregação.
- Versionamento de modelos, prompts, dados, índices, ferramentas e políticas.
- Reprodutibilidade de execuções.
- Entrega contínua com avaliação contínua.

#### 2. Observabilidade

- Tracing de prompts, contexto, recuperação, ferramentas e respostas.
- Métricas de produto, modelo, operação e negócio.
- Latência, tokens, erros, custo e consumo por usuário.
- Indicadores de qualidade e segurança.
- Logs com privacidade e retenção adequada.
- SLOs para sistemas generativos.

#### 3. Mudança e recuperação

- Testes de regressão antes da liberação.
- Canary e experimentação controlada.
- Roteamento e fallback entre modelos.
- Rollback de prompts, modelos e conhecimento.
- Detecção e tratamento de degradação.
- Resposta a incidentes generativos.

#### 4. Plataforma corporativa de IA generativa

- Gateway e roteamento de modelos.
- Serviços compartilhados de prompts, RAG, ferramentas e guardrails.
- Catálogo de modelos e capacidades.
- Identidade, segregação e tenancy.
- Políticas e governança como código.
- Portabilidade e estratégia multimodelo.
- Reutilização versus acoplamento.
- Times de plataforma e times de produto.
- Custos, cotas, showback e chargeback.

#### 5. Trade-offs de escala

- Plataforma central versus autonomia das equipes.
- Padronização versus experimentação.
- Serviço gerenciado versus operação própria.
- Modelo único versus portfólio de modelos.
- Otimização de custo versus qualidade e resiliência.

### Estudo de caso final

**Plataforma corporativa para múltiplas soluções generativas.**

Uma organização possui protótipos independentes de copiloto, RAG e agentes. Há duplicação de componentes, contratos diferentes com fornecedores, pouca rastreabilidade e custos crescentes. Cada grupo recebe uma combinação distinta de domínio, restrições e atributos de qualidade.

### Oficina e banca

Os grupos elaboram e defendem uma proposta arquitetural. A banca questiona pressupostos, alternativas, riscos, operação e evidências.

### Entregável final

- Visão de contexto e stakeholders.
- Requisitos e atributos de qualidade prioritários.
- Diagrama de componentes e responsabilidades.
- Fluxos críticos de dados, conhecimento e ações.
- Principais decisões e alternativas descartadas.
- Estratégia de segurança, guardrails e governança.
- Estratégia de avaliação, observabilidade e evolução.
- Riscos residuais e experimentos recomendados.

### Leitura-base

- *Requirements and Architecture for AI Pipelines*.
- *Design, Integration, and Testing*.
- *Architecting a Generative AI System – A Case Study*.

---

# 9. Progressão da disciplina

A progressão dos seis encontros pode ser resumida da seguinte forma:

1. **Compreender** — reconhecer a anatomia e as propriedades dos sistemas generativos.
2. **Decidir** — converter oportunidades em requisitos e escolhas justificadas.
3. **Fundamentar** — conectar modelos a conhecimento verificável.
4. **Agir** — integrar ferramentas e controlar a autonomia.
5. **Proteger e avaliar** — limitar riscos e produzir evidências de qualidade.
6. **Operar e escalar** — sustentar múltiplas soluções em produção.

# 10. Avaliação da aprendizagem

## 10.1 Composição sugerida

| Componente | Peso | Descrição |
|---|---:|---|
| Desafios arquiteturais dos encontros 1 a 5 | 40% | Cinco entregas curtas; pode-se considerar as quatro melhores notas |
| Estudo de caso final | 50% | Proposta arquitetural e defesa em banca no encontro 6 |
| Participação em críticas arquiteturais | 10% | Qualidade das perguntas, feedback aos pares e uso de evidências |

## 10.2 Critérios gerais

| Critério | O que será observado |
|---|---|
| Compreensão do problema | Clareza sobre objetivos, stakeholders, limites e restrições |
| Qualidade das decisões | Relação entre escolhas, requisitos, evidências e trade-offs |
| Coerência arquitetural | Compatibilidade entre componentes, interfaces e fluxos |
| Atributos de qualidade | Tratamento explícito de qualidade, latência, custo, segurança e operação |
| Riscos e governança | Identificação de falhas, controles e responsabilidades |
| Avaliabilidade | Definição de métricas, cenários, experimentos e critérios de aceitação |
| Comunicação | Diagramas legíveis, argumentação objetiva e reconhecimento de incertezas |

## 10.3 Rubrica do estudo de caso final

| Dimensão | Peso |
|---|---:|
| Contexto, requisitos e atributos de qualidade | 15% |
| Decomposição e coerência da arquitetura | 20% |
| Decisões, alternativas e trade-offs | 20% |
| Segurança, guardrails e governança | 15% |
| Avaliação, observabilidade e operação | 15% |
| Riscos, hipóteses e plano de validação | 10% |
| Clareza da defesa | 5% |

# 11. Estratégias de ensino

- Exposição dialogada com modelos visuais de arquitetura.
- Comparação de alternativas e análise de consequências.
- Leitura e crítica de diagramas incompletos ou problemáticos.
- Estudos de caso em pequenos grupos.
- Protótipos mínimos para testar hipóteses.
- Bancas rápidas de arquitetura.
- Revisão por pares orientada por rubricas.
- Registros de decisão arquitetural.
- Discussão de incidentes e modos de falha.

# 12. Recursos necessários

- Ambiente de acesso a pelo menos um modelo generativo.
- Pequeno corpus documental para os experimentos de RAG.
- Ferramenta de desenho colaborativo de arquitetura.
- Repositório ou ambiente virtual da disciplina.
- Exemplos preparados de prompts, respostas, traces e avaliações.
- APIs ou ferramentas simuladas para o encontro de agentes.
- Planilhas ou painéis simples para comparar qualidade, latência e custo.

Os experimentos devem possuir alternativa demonstrativa para que indisponibilidade de serviços externos não impeça a aula.

# 13. Bibliografia-base por capítulo

## Livro principal

*Architecting AI Software Systems*.

Capítulos e materiais utilizados:

1. *Fundamentals of AI System Architecture*.
2. *The Case for Architecture*.
3. *Software Engineering and Architecture*.
4. *Conceptual Design for AI Systems*.
5. *Requirements and Architecture for AI Pipelines*.
6. *Design, Integration, and Testing*.
7. *Architecting a Generative AI System – A Case Study*.

## Material de nivelamento

*Fundamentos da Arquitetura de Sistemas de Inteligência Artificial*.

# 14. Matriz de alinhamento

| Encontro | Decisão arquitetural dominante | Artefato principal | Capítulos-base |
|---|---|---|---|
| 1. Fundamentos | Como ler e decompor uma solução generativa | Leitura arquitetural comentada | 1 e 2 + eBook |
| 2. Desenho conceitual | Quando e como utilizar IA generativa | Contexto, cenários, requisitos e decisões | 2, 3 e 4 |
| 3. RAG | Como conectar modelos a conhecimento controlado | Arquitetura dos fluxos offline e online | 5, 6 e 7 |
| 4. Agentes | Como permitir ações mantendo controle | Sequência, ferramentas e matriz de autonomia | 3, 4, 6 e 7 |
| 5. Confiança | Como limitar riscos e demonstrar qualidade | Threat model, guardrails e plano de avaliação | 2, 4 e 6 |
| 6. Operação e escala | Como operar e reutilizar capacidades | Arquitetura integrada e plano operacional | 5, 6 e 7 |

# 15. Orientações para preparação das aulas

Para cada encontro, o professor deverá preparar:

1. Objetivos observáveis da aula.
2. Leitura prévia curta e perguntas orientadoras.
3. Arquitetura de referência com revelação progressiva.
4. Pelo menos duas alternativas para comparação.
5. Estudo de caso com contexto, restrições e dados suficientes.
6. Protótipo ou evidência previamente testada.
7. Template do entregável.
8. Rubrica curta para feedback.
9. Síntese com padrões, anti-padrões e perguntas em aberto.

# 16. Limites de escopo

A disciplina não tem como objetivos principais:

- ensinar programação em Python;
- aprofundar a matemática de treinamento de modelos;
- certificar o aluno em uma plataforma de nuvem;
- ensinar detalhadamente um framework de agentes;
- cobrir todo o campo de machine learning tradicional;
- produzir um sistema completo pronto para produção durante as aulas.

Esses limites preservam o foco na formação do arquiteto especialista: compreender o problema, tomar decisões justificadas, orientar a implementação e avaliar as consequências do sistema como um todo.

