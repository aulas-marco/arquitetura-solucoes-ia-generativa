# Decisões e limites do SDD

As oito decisões que calibram profundidade, fatiamento, costuras e revisão, os dois ADRs que registram a escolha, e os casos em que o método vira cerimônia.

As decisões abaixo pressupõem o [fluxo de oito etapas](fluxo.md) e o [vocabulário mínimo](index.md#vocabulario-minimo). Cada uma é apresentada como decisão de arquitetura, com o que se ganha, o que se paga e o sinal que indicaria ter escolhido errado.

## Padrão — Desenvolvimento guiado por especificação

**Contexto.** Um agente de codificação pode alterar múltiplos artefatos e executar ferramentas rapidamente.

**Problema.** Pedidos vagos transformam implementação em interpretação silenciosa; testes podem passar sem atender à necessidade original.

**Solução.** Manter constitution, spec, plan e tasks como contratos explícitos. Implementar em fatias verificáveis, testar nas interfaces acordadas e revisar separadamente padrões do repositório e aderência à spec.

**Consequências.** Há mais preparação e portões (*gates*), mas decisões, critérios de aceite e riscos permanecem auditáveis. O modelo ganha autonomia limitada para implementar; não ganha autoridade para redefinir o objetivo.

> **Decisão arquitetural:** posicione gates humanos após a specification, após verify e antes da liberação. Um gate deve receber artefatos imutáveis, evidência de testes e o diff correspondente.

## Decisão 1 — escolher a profundidade proporcional

O método deve acompanhar risco e incerteza. Aplicar o mesmo pacote documental a toda alteração transforma SDD em fila de aprovação; aplicar somente a mudanças grandes permite que riscos pequenos e frequentes se acumulem.

Use três classes:

| Classe | Situação | Contrato mínimo |
|---|---|---|
| S — localizada | comportamento conhecido, baixo blast radius, reversível | problema, teste de regressão, diff e revisão |
| M — feature | novo comportamento, mais de um componente ou decisão | spec, critérios, plano, fatias, testes e gates 1/3 |
| L — iniciativa | múltiplos domínios, migração, risco material ou vários times | constitution aplicável, spec, arquitetura, ADRs, plano, grafo de tarefas e três gates |

Classifique pelo maior risco, não pelo número de linhas. Três demandas da mesma semana, classificadas:

- corrigir o texto “Aguardando pagto.” para “Aguardando pagamento” em três telas → **S**, porque não há regra associada e o retorno é trivial;
- permitir que o cliente cancele o pedido até a separação começar → **L**, mesmo sendo poucas linhas, porque a regra de cancelamento hoje só existe no código e ninguém sabe recitá-la;
- migrar duzentos arquivos para um novo formato de importação → **M**, apesar do tamanho, porque a transformação é mecânica e reversível arquivo a arquivo.

A segunda é a que costuma ser subestimada: o critério é o risco, e uma linha que muda autorização carrega mais risco que duzentos arquivos que mudam formato. Uma mudança curta em autorização pode ser classe L; uma migração mecânica extensa pode ser classe M com estratégia *expand–contract*. Registre o motivo da classificação para que a simplificação seja uma decisão, não omissão.

> **Decisão arquitetural:** adote classe M como padrão para comportamento novo. Reduza para S ou eleve para L por critérios explícitos de risco, reversibilidade, coordenação e evidência.

## Decisão 2 — separar “o quê” de “como”

Misturar tecnologia na spec torna a intenção instável. “Usuário baixa CSV” pode ser requisito; “endpoint FastAPI usa Celery e S3” pertence ao plano. A separação permite:

- comparar arquiteturas sem reescrever o problema;
- mudar tecnologia preservando critérios;
- revisar produto e arquitetura por autoridades diferentes;
- gerar mais de um plano a partir da mesma intenção;
- localizar onde ocorreu uma decisão incorreta.

Há exceções: uma restrição tecnológica pode ser requisito quando vem do ambiente — “deve operar desconectado”, “deve usar a identidade corporativa”, “não pode transferir dados para fora do país”. Nesse caso, registre a restrição e sua fonte na spec; o plano decide como atendê-la.

Use este teste: se a tecnologia fosse substituída por outra equivalente, a necessidade do usuário continuaria a mesma? Se sim, mantenha-a fora da especificação funcional.

## Decisão 3 — formular critérios antes de tarefas

Tarefas derivadas de requisitos sem critérios de aceite viram atividades, não compromissos de comportamento. Antes de fatiar, escreva exemplos observáveis:

```gherkin
Cenário: exportação expira
  Dado que uma exportação foi criada há mais de 24 horas
  Quando o solicitante usa o link original
  Então o sistema nega o download
  E permite solicitar uma nova exportação
  E registra o motivo sem persistir o conteúdo exportado
```

Esse cenário cria trabalho em autorização, UX, expiração, auditoria e teste. Sem ele, “implementar expiração” pode significar apagar um arquivo, esconder um botão ou invalidar um token, cada opção com consequências diferentes.

Critérios não devem prescrever asserts internos. Devem descrever comportamento e propriedades relevantes. Para atributos de qualidade, use cenários:

```text
Fonte: gestor autenticado
Estímulo: solicita 50 mil registros autorizados
Ambiente: horário de pico
Resposta: sistema aceita, processa e disponibiliza arquivo
Medida: 95% concluídos em até 30 s; nenhuma linha fora do escopo
```

> **Decisão arquitetural:** nenhuma tarefa de implementação é considerada pronta sem critério observável e método de verificação associado.

## Decisão 4 — fatiar verticalmente

Uma fatia vertical entrega uma trajetória estreita de ponta a ponta. Para exportação:

1. solicitar exportação vazia e observar estado pendente;
2. gerar arquivo com um tipo de registro autorizado;
3. adicionar processamento assíncrono e consulta de estado;
4. adicionar expiração e nova solicitação;
5. ampliar volume e medir SLO.

Cada fatia possui comportamento demonstrável e mantém a suíte verde. Uma decomposição horizontal — tabela, repositório, serviço, API, interface — só demonstra valor depois de integrar tudo. Para a mesma exportação, a versão horizontal seria: criar a tabela de exportações; criar o repositório; criar o serviço; criar o endpoint; criar a tela. Depois de quatro dessas cinco tarefas, ninguém consegue exportar nada, e o primeiro erro de contrato só aparece na quinta. Também aumenta a probabilidade de agentes implementarem suposições incompatíveis em paralelo.

Tarefas paralelas devem ter:

- arquivos ou componentes com baixa sobreposição;
- contratos já aprovados;
- resultados integráveis independentemente;
- bloqueadores explícitos;
- responsável pelo fechamento da integração.

Quando uma alteração ampla não pode ser fatiada sem quebrar consumidores, use **expand–contract**:

1. **expandir:** adicionar nova interface ao lado da antiga;
2. **migrar:** mover consumidores em lotes verificáveis;
3. **contrair:** remover a forma antiga quando não houver uso.

Esse padrão preserva integração contínua e reduz branches longas.

## Decisão 5 — escolher seams duráveis

Antes de gerar testes, identifique as interfaces pelas quais consumidores observam comportamento. Prefira poucas seams de alta alavancagem.

| Seam | Boa para | Evite |
|---|---|---|
| comando CLI | transformação ou operação reproduzível | testar cada função privada chamada |
| endpoint/contrato HTTP | autorização, validação e resposta | acoplar teste ao framework sem necessidade |
| evento publicado | integração assíncrona e esquema | afirmar ordem interna de métodos |
| função pública de domínio | regra determinística | simular o próprio comportamento testado |
| adaptador | tradução de dependência externa | chamar serviço real em toda suíte |

Uma seam profunda permite trocar implementação mantendo contrato. Uma seam rasa expõe muitos detalhes e multiplica testes frágeis. Concretamente, no caso da exportação: o teste que entra por `POST /exportacoes` com o token de uma coordenadora da unidade Sul e confere que o arquivo traz só a unidade Sul continua valendo depois de trocar o banco, a fila ou a biblioteca de CSV. O teste que chama `montarConsultaSql()` e compara a string gerada quebra na primeira refatoração que não muda comportamento nenhum — e pior, ensina o agente a preservar a string por ela mesma. O plano deve registrar assinatura, invariantes, tipos de erro e dados sensíveis de cada interface.

> **Decisão arquitetural:** teste comportamento na seam mais alta que permaneça rápida, determinística e diagnóstica; use testes internos apenas para propriedades que não podem ser observadas adequadamente por ela.

## Decisão 6 — usar revisão em dois eixos

Revisão de **Spec** pergunta:

- todas as histórias prioritárias foram atendidas?
- critérios possuem evidência?
- regras e fora de escopo foram respeitados?
- alguma decisão de produto foi inventada durante implementação?
- riscos e desconhecidos foram resolvidos ou continuam visíveis?

Revisão de **Standards** pergunta:

- a implementação segue convenções e arquitetura do repositório?
- interfaces e nomes expressam o domínio?
- há duplicação, acoplamento ou dependência injustificada?
- testes observam comportamento e sobrevivem a refatoração?
- segurança, privacidade e operação estão adequadas?

Os relatórios permanecem separados. Um “passa” em Standards não compensa requisito ausente; um “passa” em Spec não compensa vulnerabilidade crítica. Quando possível, use contextos de revisão independentes para reduzir ancoragem na solução do implementador.

Achados devem citar evidência: requisito, princípio, trecho de diff ou padrão do repositório. “Não gostei” não é finding; “o requisito FR-07 exige autorização por unidade, mas o endpoint filtra apenas por usuário” é.

## Decisão 7 — tratar segurança como parte da transformação

Segurança não é revisão posterior. A spec identifica ativos, atores, dados e usos proibidos; o plano define trust boundaries, identidade, autorização, proteção e observabilidade; tarefas carregam testes negativos; verificação compara o diff às ameaças.

Checklist mínimo:

- autenticação e autorização no servidor;
- princípio de menor privilégio;
- validação e normalização de entrada;
- dados pessoais minimizados em armazenamento e logs;
- segredos fora de prompts e repositório;
- dependências e imagens examinadas;
- ações materiais auditadas;
- falha segura e recuperação;
- abuso, automação e limites de taxa considerados;
- risco residual com dono e prazo.

Um agente de segurança pode aumentar cobertura, mas não aceita risco. O efeito de antecipar aparece assim: na exportação de avaliações, a pergunta “quem pode exportar dados de qual unidade” entrou na especificação e virou um teste negativo — coordenadora da unidade Sul pedindo dados da Norte recebe 403. Se a mesma pergunta só aparecesse na revisão final, o resultado provável seria um filtro aplicado na tela, com o endpoint continuando a devolver tudo para quem soubesse chamá-lo direto. Achado crítico bloqueia o portão (*gate*) até correção ou aceitação formal por autoridade competente.

## Decisão 8 — manter os artefatos coerentes

Artefatos vivos exigem regras de mudança:

| Mudança descoberta | Atualizar |
|---|---|
| necessidade ou regra | spec e critérios |
| restrição organizacional | constitution ou spec, conforme alcance |
| escolha técnica relevante | plano e ADR |
| nova dependência entre trabalhos | tasks |
| bug de comportamento | critério e teste de regressão |
| incidente ou métrica de produção | requisito de qualidade, risco e experimento |

Antes do merge, execute uma análise de cobertura:

```text
requisito → cenário → decisão/plano → tarefa → teste → evidência
```

Relações não precisam estar num sistema sofisticado. Identificadores estáveis e links bastam para começar. O importante é conseguir navegar em ambas as direções: “que código implementa FR-07?” e “por que esta validação existe?”.

Evite atualizar specs por regeneração cega. A alteração deve aparecer como diff revisável. Texto aprovado por pessoa não pode ser sobrescrito porque um novo template produziu formulação diferente.

## ADR — onde colocar os gates do fluxo SDD

**Contexto.** Gates demais criam espera; gates tardios deixam decisões caras chegarem ao final.

**Opções consideradas.**

1. **Somente revisão final:** menor interrupção, mas requisitos e arquitetura incorretos são descobertos depois do código.
2. **Gate em toda etapa:** alta supervisão, mas filas e aprovações mecânicas reduzem fluxo.
3. **Três gates por mudança material:** intenção, arquitetura e entrega; etapas internas continuam dentro da autonomia aprovada.

**Decisão.** Usar três gates para classe L; gate de intenção e entrega para classe M; revisão final para classe S. Um gate é pulado apenas com motivo registrado.

**Consequências.** Decisões de maior custo são validadas antes; o time precisa manter critérios de entrada/saída claros e tempo de resposta dos responsáveis.

**Gatilho de revisão.** Se tempo em fila superar tempo de trabalho ou se defeitos escaparem apesar dos gates, revisar granularidade, autoridade e qualidade dos artefatos.

## ADR — Spec Kit como fio operacional, não como metodologia exclusiva

**Contexto.** A disciplina precisa de um fluxo reproduzível, mas ferramentas e integrações mudam.

**Opções consideradas.**

1. Ensinar princípios sem ferramenta: durável, porém abstrato para a oficina.
2. Tratar Spec Kit como padrão universal: concreto, porém cria acoplamento e confunde ferramenta com método.
3. Usar Spec Kit como implementação de referência e comparar variações.

**Decisão.** Adotar a terceira opção. Constitution, spec, plan, tasks e implement fornecem uma trajetória observável. As [quatro abordagens comparadas](fluxo.md#quatro-abordagens-para-o-mesmo-padrao) mostram que o mesmo padrão admite mecanismos distintos: OpenSpec organiza por mudança, SPDD comprime tudo num Painel REASONS e Superpowers disciplina a execução sem manter spec principal. Matt Pocock aprofunda *vertical slices*, deep modules, TDD e revisão em dois eixos, enquanto Kiro, BMAD e Tessl mostram outras escolhas de ambiente e artefatos.

**Consequências.** O aluno pratica comandos concretos e consegue transferir princípios. Materiais devem fixar versões e distinguir recurso atual de conceito durável.

**Gatilho de revisão.** Mudança incompatível nos comandos, templates ou licença; surgimento de alternativa que ofereça melhor acesso e evidência para a turma.

## As abordagens não cobram o mesmo tipo de rigor

As [quatro abordagens](fluxo.md#quatro-abordagens-para-o-mesmo-padrao) apresentadas na página anterior podem ser comparadas sob dez critérios. A tabela serve para escolher, não para classificar.

| Critério | OpenSpec | GitHub Spec Kit | SPDD / OpenSPDD | Superpowers |
|---|---|---|---|---|
| Natureza | ferramenta e fluxo de mudança orientado por especificação | toolkit extensível para fluxos orientados por intenção | método e implementação de referência centrados no prompt estruturado | framework de habilidades e metodologia de execução |
| Unidade principal | mudança | funcionalidade sob princípios de projeto | incremento descrito por um Painel REASONS | tarefa ou plano de implementação |
| Artefato central | especificação atual e delta da mudança | constitution, especificação, plano e tarefas | prompt ou Painel versionado | design, plano, código e testes |
| Relação com SDD | predominantemente *spec-anchored* | pode operar de *spec-first* a *spec-anchored* | *spec-anchored* com sincronização bidirecional proposta | adjacente, disciplina a execução de uma spec ou design |
| Governança transversal | não é o padrão, mas pode ser customizada | constitution e checagens explícitas | normas e salvaguardas no Painel, ativos reutilizáveis | habilidades e regras do fluxo, sem constitution de domínio |
| Manutenção da intenção | deltas sincronizados e arquivados na spec principal | depende do uso contínuo dos artefatos e da convergência | atualização requisito → prompt → código e sincronização código → prompt | documentos por mudança, testes e código sustentam o comportamento |
| Estratégia de verificação | validação de artefatos e verificação opcional da implementação | checklist, análise cruzada e convergência | revisões do Painel, API, código e sincronização, parte do ferramental é opcional | TDD, revisão em duas etapas e verificação antes de concluir |
| Tipo de custo dominante | manter deltas e specs consolidadas coerentes | produzir e governar uma cadeia maior de artefatos | modelagem detalhada e expertise sênior antecipada | disciplina operacional, testabilidade e planos granulares |
| Melhor encaixe | produto longevo com mudanças incrementais | múltiplos times e políticas compartilhadas | lógica complexa, repetição e restrições fortes | execução confiável em bases testáveis |
| Falha típica se mal aplicado | arquivar sem sincronizar ou manter uma spec decorativa | constitution genérica e aprovações mecânicas | Painel detalhado baseado em premissa errada ou desatualizado | testes confirmarem uma interpretação incompleta do problema |

Há duas conclusões menos óbvias nessa tabela.

A primeira é que **documentação e rigor operacional são eixos diferentes**. Spec Kit pode ser documentalmente pesado, enquanto Superpowers pode ser operacionalmente exigente. Dizer apenas que uma abordagem é “leve” ou “pesada” esconde onde o custo realmente aparece.

A segunda é que as abordagens podem ser complementares. Uma organização pode usar a constitution do Spec Kit para princípios transversais, deltas do OpenSpec para manter comportamento de domínio e práticas de TDD e verificação inspiradas em Superpowers para executar. Isso não significa instalar tudo. Significa reconhecer camadas distintas e evitar que dois artefatos concorram como fonte da mesma decisão.

## Como escolher sem transformar o processo em religião

Uma heurística prática é escolher primeiro o artefato que precisa sobreviver:

- Se nada precisa sobreviver porque o resultado é descartável, use vibe coding conscientemente.
- Se apenas a tarefa e sua evidência precisam sobreviver, assistência de codificação ou um fluxo como Superpowers pode bastar.
- Se o comportamento atual do domínio precisa permanecer legível após muitas mudanças, OpenSpec é um encaixe natural.
- Se princípios organizacionais precisam governar várias funcionalidades e times, Spec Kit oferece uma camada explícita para isso.
- Se a organização precisa revisar e reutilizar não apenas requisitos, mas também a estratégia de implementação, normas e salvaguardas em incrementos de lógica, SPDD oferece o artefato mais detalhado.

Depois, calibre o fluxo pelo risco, usando as mesmas classes da Decisão 1:

| Situação | Ponto de partida provável |
|---|---|
| protótipo descartável, sem dados reais | vibe coding com limite explícito de vida e descarte |
| correção pequena em código conhecido | assistência com testes, revisão e registro no ticket |
| funcionalidade incremental em produto longevo | OpenSpec, acrescentando disciplina de teste conforme o risco |
| mudança crítica que atravessa vários times | Spec Kit ou fluxo equivalente de governança e rastreabilidade |
| família de APIs ou regras semelhantes sob forte conformidade | SPDD, desde que haja expertise para revisar o Painel |
| base testável que sofre com agentes precipitados ou conclusões sem evidência | Superpowers, isoladamente ou executando uma especificação externa |
| incidente ativo de produção | restaurar o serviço primeiro, fechando depois a dívida de intenção com teste, post-mortem e atualização dos artefatos |

Nenhuma matriz elimina julgamento. Uma mudança de três linhas pode alterar autorização. Uma funcionalidade de centenas de linhas pode ser um experimento reversível. Tamanho do diff é um indicador fraco de risco, como já argumentou a [Decisão 1](#decisao-1-escolher-a-profundidade-proporcional).

## Quando SDD falha

SDD não corrige automaticamente entendimento ruim. Ele pode produzir **documentação em escala** sem produzir conhecimento. Os principais antipadrões são:

- **spec teatral:** documento extenso que não contém decisões nem critérios testáveis;
- **falsa precisão:** números e regras inventados pelo modelo para preencher lacunas;
- **waterfall regenerado:** tentar completar tudo antes de qualquer experimento;
- **artefatos divergentes:** spec, plano, tarefas e código evoluem separadamente;
- **aprovação automática:** o mesmo agente produz e “aprova” todos os artefatos;
- **task slicing horizontal:** tarefas por camada sem resultado demonstrável;
- **testes espelho:** testes copiam a implementação e não expressam intenção;
- **constitution ornamental:** princípios sem consequência sobre o plano;
- **regeneração destrutiva:** atualizar artefatos sobrescreve decisões humanas sem diff revisável;
- **contexto excessivo:** despejar todo o repositório no agente em vez de oferecer interfaces e fontes relevantes.

Também há tarefas em que o custo não compensa: correção óbvia e localizada com teste de regressão; atualização mecânica de dependência; protótipo descartável; exploração cuja finalidade é descobrir se uma abordagem é possível. Nesses casos, use um contrato menor: problema, limite, teste e evidência.

## Como medir adoção sem medir burocracia

Contar specs criadas incentiva produção de arquivos. Métricas melhores observam efeito:

| Pergunta | Indicador possível |
|---|---|
| intenção ficou clara antes do código? | percentual de implementações iniciadas após aceite versionado |
| tarefas carregavam trajetórias completas? | percentual de fatias demonstráveis sem esperar outras camadas |
| testes nasceram dos critérios? | cobertura de critérios por cenários, não apenas linhas |
| implementação respeitou a spec? | desvios encontrados na revisão de aderência |
| segurança entrou cedo? | riscos críticos descobertos antes e depois da implementação |
| artefatos permaneceram vivos? | mudanças de comportamento acompanhadas por atualização de spec/teste |
| o método melhorou fluxo? | tempo de clarificação, retrabalho, lead time e defeitos escapados |

Velocidade de geração isolada é uma métrica perigosa. Um caso concreto: uma equipe passou de quatro para onze *pull requests* por semana depois de adotar o agente, e no mesmo trimestre o retrabalho por defeito escapado subiu de 8% para 21% das horas. O primeiro número sozinho recomendaria ampliar o uso; os dois juntos recomendam olhar onde a intenção está se perdendo. Se o agente produz mais código e aumenta retrabalho, o sistema local ficou rápido e o fluxo global piorou.

### O que medir num piloto

A tabela acima mede uma prática já instalada. Antes disso vem outra pergunta: vale instalar? Adotar SDD em toda a organização antes de aprender com mudanças reais repete o mesmo erro que o processo tenta evitar, que é comprometer-se cedo demais com uma solução. Um piloto deve comparar classes semelhantes de tarefa e observar o sistema de entrega inteiro, não apenas o tempo até a primeira geração.

Alguns indicadores úteis são:

- tempo da solicitação até a aceitação em produção.
- número de ciclos de retrabalho após a primeira implementação.
- tempo e tamanho da fila de revisão.
- defeitos encontrados antes e depois da implantação.
- requisitos ou decisões sem teste ou evidência correspondente.
- divergências entre especificação, plano, código e comportamento observado.
- esforço gasto para atualizar os artefatos depois de uma mudança.
- tempo necessário para uma pessoa nova compreender e alterar a funcionalidade.
- frequência com que portões encontram um problema relevante, e com que frequência viram aprovação automática.

O objetivo não é provar que “a IA ficou mais produtiva”. É descobrir se o fluxo reduz retrabalho e risco sem transferir um custo desproporcional para especificação e revisão.

Um bom piloto começa com poucas mudanças representativas, define quais etapas são obrigatórias e registra exceções. Ao final, o time deve ser capaz de responder: qual artefato realmente foi consultado, qual portão mudou uma decisão, qual etapa não agregou valor e quem manterá o processo quando a ferramenta evoluir.

## O que permanece humano

SDD desloca trabalho, não elimina responsabilidade. Pessoas continuam responsáveis por:

- escolher problemas que merecem investimento;
- ouvir usuários e reconhecer conflito de interesses;
- aceitar risco e consequências;
- decidir trade-offs arquiteturais;
- identificar quando a linguagem não representa o domínio;
- julgar suficiência de evidência;
- responder por efeitos em produção.

Agentes ampliam pesquisa, comparação, consistência, geração e revisão. Eles são particularmente úteis para manter relações entre muitos artefatos. Mas não possuem mandato organizacional. A spec não é central porque foi escrita em linguagem natural; é central porque pessoas autorizadas a adotaram como contrato e mantêm mecanismos para testá-la.

O salto além do vibe coding, portanto, não acontece quando o time instala mais comandos. Acontece quando a intenção deixa de depender da memória de quem conversou com o agente e passa a ser verificável por outras pessoas. Cada uma das quatro abordagens preserva uma coisa diferente, e cada uma pode falhar de um jeito diferente. A especificação pode estar errada. A constitution pode virar burocracia. O Painel pode envelhecer. Os testes podem provar apenas a premissa que o agente inventou. O elemento comum continua sendo julgamento humano: confirmar que o problema foi compreendido, que o risco foi coberto e que a evidência apresentada é suficiente.

A pergunta madura não é “qual ferramenta gera mais código?”, mas “qual combinação de intenção, governança e evidência torna esta mudança segura o bastante para sobreviver a quem a criou?”.
