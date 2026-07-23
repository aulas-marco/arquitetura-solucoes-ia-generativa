# Conceitos: do diálogo à ação controlada

![Mapa da autonomia controlada: diálogo, fluxo de trabalho, agente e múltiplos agentes formam um continuum; planejamento usa ferramentas tipadas e estado sob políticas, enquanto ações materiais passam por aprovação explícita](../assets/images/m04-mapa-autonomia-controlada.png "Mapa da autonomia controlada")

*Figura — Autonomia não é uma propriedade binária: ela cresce com a capacidade de decidir e agir, e deve encontrar políticas e aprovação antes de cruzar fronteiras materiais.*

## Quatro formas que não devem ser confundidas

Um **chatbot** oferece interação conversacional. Pode responder por conhecimento paramétrico, contexto fornecido ou RAG. Conversar em várias rodadas não implica escolher ferramentas nem produzir efeitos externos. A conversa é uma forma de interface.

Um **copiloto** apoia uma pessoa em uma tarefa: resume, sugere, preenche rascunhos ou propõe uma ação. A pessoa mantém o controle decisório e normalmente aciona o efeito em uma interface convencional. Um botão “aplicar sugestão” pode executar código determinístico; isso não transforma automaticamente o copiloto em agente.

Um **workflow determinístico** tem etapas, transições, condições e tratamento de erros definidos pela aplicação. Uma etapa pode usar um modelo para classificar texto ou gerar conteúdo, mas o modelo não decide livremente a próxima etapa. “Consultar pedido → validar regra → pedir aprovação → atualizar CRM” continua sendo workflow mesmo quando duas etapas são generativas.

Um **agente** é um sistema em que o modelo escolhe pelo menos parte do próximo passo — ferramenta, ordem, decomposição ou interrupção — para perseguir um objetivo, dentro de limites. O artigo [ReAct](https://openreview.net/forum?id=WE_vluYUL-X) investiga a combinação de raciocínio e ações intercaladas; arquiteturalmente, o valor está no ciclo observar–escolher–agir, não em expor raciocínio interno como prova. O trace deve registrar decisões observáveis e resultados, não alegar acesso fiel ao processo mental do modelo.

As categorias descrevem **controle**, não qualidade ou maturidade. Um workflow pode ser superior a um agente; um agente pode conversar; um copiloto pode chamar ferramentas somente de leitura para preparar uma sugestão. Pergunte sempre: quem escolhe a transição, quem executa o efeito e quem responde por ele?

## Geração, decisão e ação

Separe três atos numa trajetória:

- **geração:** produzir texto ou dados candidatos;
- **decisão:** selecionar uma opção segundo objetivo, evidência e política;
- **ação:** causar efeito observável fora da geração, como consultar, reservar, cancelar ou enviar.

O modelo pode participar dos três, mas controles determinísticos devem envolver decisões e ações. Uma proposta de reembolso é geração; verificar limite é regra; registrar reembolso é ação. Misturar os atos em “o agente resolveu” oculta fronteiras de autorização, teste e auditoria.

## Uso de ferramentas e saídas estruturadas

Uma **ferramenta** é uma capacidade exposta ao modelo por uma interface controlada. Pode consultar CRM, calcular frete ou solicitar alteração de pedido. O modelo não deveria montar SQL livre, escolher credenciais nem chamar diretamente qualquer endpoint. Ele produz uma **solicitação de ferramenta**; o orquestrador valida esquema, política, identidade, orçamento e estado antes de executar.

Uma **saída estruturada** restringe a forma, por exemplo a um objeto com `tool_name`, `arguments` e `justification_code`. Esquema válido reduz ambiguidade sintática, mas não garante semântica, autorização ou segurança. `quantidade: 1000` pode ser inteiro válido e ainda violar política. O estudo [Toolformer](https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html) é uma fonte primária sobre modelos aprendendo a usar ferramentas; em produção corporativa, capacidade de seleção precisa ser cercada por contratos e execução mediada.

## Planejamento e decomposição

**Planejamento** transforma objetivo em passos. Ele pode ser:

- pré-definido pelo workflow;
- proposto de uma vez pelo modelo e validado antes da execução;
- incremental, escolhendo o próximo passo após cada observação;
- híbrido, com macroetapas determinísticas e autonomia local.

Planos não são compromissos confiáveis por si. O ambiente muda: estoque pode acabar entre consulta e reserva; uma aprovação pode expirar. Por isso cada passo revalida precondições e autorização. O agente deve reconhecer conclusão, falta de progresso, limite alcançado e necessidade de escalonamento. Uma regra de “não repetir a mesma ferramenta com os mesmos argumentos e a mesma versão de estado” ajuda a impedir loops, mas não substitui orçamento total.

## Estado, memória e contexto

**Estado da execução** é o registro autoritativo da trajetória: identificador, objetivo, etapa, versão, ações propostas, aprovações, chamadas concluídas, chaves de idempotência, resultados, orçamento consumido e status de compensação. Deve ser durável quando há efeitos, concorrência ou retomada. Atualizações usam controle de versão para impedir duas continuações sobre o mesmo estado.

**Memória de trabalho** é temporária e específica da execução: fatos normalizados, resultados recentes, plano corrente e resumo para caber no contexto. Pode ser reconstruída do estado e expira ao concluir. Não deve virar depósito silencioso de dados pessoais.

**Memória persistente** atravessa execuções: preferências consentidas, fatos duráveis ou lições operacionais aprovadas. Exige finalidade, origem, autorização, prazo, correção e exclusão. A frase do usuário “sempre aprove trocas” não pode se tornar política; conteúdo conversacional não altera autorização.

**Contexto** é a visão enviada ao modelo numa chamada: instruções, objetivo, ferramentas permitidas, recorte do estado, memória autorizada e observações. É transitório e limitado. Estado não cabe inteiro no prompt; memória não é sinônimo de histórico; contexto não é fonte de verdade.

## Políticas como fronteira executável

Políticas determinam quais ferramentas e parâmetros estão disponíveis para aquela identidade, ação, recurso, risco e estado. Devem operar fora do modelo. A descrição “use apenas quando permitido” orienta, mas a autorização real ocorre no executor. O catálogo apresentado ao modelo já deve ser mínimo, e a política é repetida imediatamente antes da ação para lidar com revogação e mudanças.

Uma decisão de política pode retornar `allow`, `deny` ou `require_approval`, acompanhada de versão, motivo e obrigações: mascarar campo, limitar valor, exigir confirmação do cliente ou escolher aprovador. Negação vira resultado explícito; o agente não deve contorná-la por outra ferramenta equivalente.

## Agente único e múltiplos agentes

No **agente único**, um planejador recebe objetivo e catálogo limitado. Há menos mensagens, estados e pontos de coordenação. É a opção inicial quando uma trajetória cabe num contexto controlável e uma equipe pode manter os contratos.

Em **múltiplos agentes**, papéis especializados — atendimento, política, pedido — trocam mensagens ou são coordenados por um supervisor. A divisão pode reduzir contexto por papel e permitir políticas distintas, mas não cria conhecimento nem confiabilidade automaticamente. Multiplica prompts, modelos possíveis, handoffs, latência, custo, estados, permissões e falhas de consenso. “Debate” entre modelos não é aprovação independente se todos compartilham a mesma evidência defeituosa.

Use múltiplos agentes quando houver fronteiras reais: domínios mantidos por equipes diferentes, contextos incompatíveis, competências ou credenciais separadas, ou paralelismo medido. Defina protocolo, proprietário do estado, limite de delegação, formato de entrega e regra de encerramento. Se a motivação for apenas organizar um prompt grande, módulos determinísticos ou ferramentas especializadas costumam ser mais simples.

**n8n** automatiza workflows; **LangGraph** e **AutoGen** organizam estados ou agentes. Nenhum delega autoridade: política e aprovação permanecem externas.

## O critério de entrada

Um agente é candidato quando: a sequência útil varia de modo difícil de enumerar; ferramentas devolvem feedback verificável; erros podem ser contidos; a tarefa tem conclusão observável; e orçamento/autoridade podem ser delimitados. Rejeite ou limite autonomia quando o caminho é estável, o efeito é irreversível, a autorização é ambígua, o feedback chega tarde ou não existe recuperação proporcional.

## Ferramentas no mercado

Compare contratos no [Guia de ferramentas](../referencia/guia-de-ferramentas.md).

| Ferramenta | Quando ajuda | Pré-requisito | Limite arquitetural |
|---|---|---|---|
| n8n | Desenhar workflow. | Ambiente, credenciais e dados sintéticos. | Não autoriza ações ou garante idempotência. |
| LangGraph | Modelar estado e retomada. | Schema, limites e ferramentas. | Não substitui política externa. |
| AutoGen | Testar papéis de agentes. | Protocolo, orçamento e catálogo mínimo. | Mais agentes não são aprovação. |

Com essa base, passamos de “o que é um agente” para “como integrá-lo sem entregar o controle”: [Padrões e decisões](padroes-e-decisoes.md).

## Do agente que age ao agente que constrói software

O agente que constrói software é um caso especialmente instrutivo de autonomia. Suas ferramentas — ler arquivos, editar código, executar comandos, criar branches e propor commits — produzem efeitos duráveis. Uma alteração pode compilar e ainda violar uma regra de negócio, enfraquecer segurança, introduzir acoplamento ou resolver um problema diferente daquele que motivou o trabalho. Portanto, a pergunta arquitetural permanece a mesma: **qual liberdade o modelo recebe, qual contrato orienta suas escolhas e que evidência autoriza o próximo passo?**

O uso de IA no desenvolvimento não começa com geração de código. Começa com a transformação de uma intenção incompleta em um conjunto de decisões verificáveis. É nesse ponto que o **desenvolvimento guiado por especificação**, ou SDD (*Specification-Driven Development*), se conecta ao tema do módulo: a especificação funciona como estado autoritativo do objetivo, enquanto agentes especializados ajudam a descobrir, formalizar, planejar, implementar e revisar.

## Vibe coding, assistência e SDD

Três modos de trabalho costumam ser confundidos:

| Modo | Artefato que governa | Como a qualidade é julgada | Risco dominante |
|---|---|---|---|
| *Vibe coding* | conversa corrente e resultado aparente | “parece funcionar” | intenção implícita, regressão e dívida invisível |
| assistência de codificação | ticket, código existente e revisão do desenvolvedor | testes e revisão após gerar | contexto fragmentado e decisões não registradas |
| SDD | constitution, spec, plano, tarefas, testes e gates versionados | rastreabilidade entre intenção, implementação e evidência | custo de especificar sem aprender ou manter artefatos vivos |

*Vibe coding* é útil para exploração descartável: provar uma interação, experimentar uma API ou descobrir uma pergunta de design. Ele se torna perigoso quando o protótipo atravessa silenciosamente a fronteira para produto. A conversa contém decisões que não aparecem no repositório; o código incorpora suposições que ninguém aprovou; o teste confirma apenas o que foi implementado; e uma nova sessão não possui o contexto que orientou a anterior.

Assistência de codificação é mais disciplinada. A pessoa mantém o desenho e usa o modelo para completar funções, explicar código, gerar testes ou revisar um diff. Isso pode produzir excelente engenharia, mas não constitui SDD por si: a especificação ainda pode ser um ticket curto e descartável, sem critérios suficientes para orientar mais de um agente ou reconstruir por que o sistema ficou daquela forma.

SDD muda a relação entre os artefatos. Em vez de tratar a especificação como andaime abandonado quando o código começa, trata-a como expressão versionada da intenção. O código é uma implementação possível daquela intenção, condicionada por arquitetura, plataforma e momento. Essa inversão não significa que prosa esteja sempre certa ou que código possa ser regenerado sem custo. Significa que uma mudança relevante deve começar por tornar explícito **o que mudou na intenção**, e que plano, testes e implementação precisam mostrar sua relação com essa mudança.

> **Decisão arquitetural:** use SDD quando a tarefa contém decisões, riscos ou coordenação suficientes para justificar um contrato durável. Para um experimento descartável, registre a pergunta e o resultado; não simule uma burocracia completa.

## A spec como artefato central e vivo

Uma boa spec não é uma descrição longa. É uma fronteira de decisão. Ela deve permitir que pessoas diferentes respondam, sem ler a mente do autor:

- qual problema vale resolver e para quem;
- qual comportamento observável caracteriza sucesso;
- o que está explicitamente fora do escopo;
- quais termos têm significado específico no domínio;
- quais regras não podem ser violadas;
- quais atributos de qualidade alteram a solução;
- quais incertezas permanecem abertas;
- qual evidência permitirá aceitar ou rejeitar a entrega.

“Adicionar exportação” não é uma spec. Ainda faltam ator, finalidade, formato, volume, autorização, tratamento de dados sensíveis, tempo aceitável, falhas e resultado observável. “Construir exportação CSV para gestores baixarem até 50 mil registros autorizados em menos de 30 segundos, sem expor colunas restritas” começa a formar uma especificação porque restringe interpretações e permite derivar decisões e testes.

A spec é **viva** quando uma descoberta altera o artefato apropriado. Se o domínio revela que relatórios fechados não podem ser regenerados, a regra entra na spec. Se o banco escolhido não sustenta o volume, a decisão e suas consequências entram no plano ou ADR; isso não deve ser escondido como detalhe do código. Se um incidente mostra que o controle de autorização falhou, a correção não termina no patch: requisito, cenário adversarial e teste de regressão passam a governar trabalhos futuros.

Ela é **executável em sentido amplo** quando consegue produzir ou verificar outros artefatos: cenários tornam-se testes; entidades orientam modelo de dados; contratos orientam APIs; atributos de qualidade geram experimentos; regras de segurança produzem casos negativos; tarefas carregam critérios de conclusão. Executável não quer dizer que toda prosa se transforme mecanicamente em código nem que o modelo seja um compilador infalível. A transformação continua sujeita a interpretação, ferramentas e revisão.

## Constitution: princípios antes da feature

O [Spec Kit](https://github.com/github/spec-kit) começa pela **constitution**, um conjunto versionado de princípios que todas as features devem respeitar. Ela reduz a necessidade de repetir decisões organizacionais em cada prompt e impede que o agente trate convenções fundamentais como preferências locais.

Uma constitution útil contém regras capazes de bloquear ou redirecionar um plano:

- interfaces públicas exigem compatibilidade ou estratégia de migração;
- toda escrita material precisa de autorização no servidor;
- comportamento novo começa por um teste que falha pelo motivo esperado;
- dependências adicionais exigem justificativa;
- dados pessoais não entram em logs;
- módulos expõem interfaces pequenas e testáveis;
- documentação e ADRs mudam junto com o contrato que descrevem;
- a esteira deve permanecer verde a cada fatia integrável.

Princípios vagos — “escreva código limpo”, “priorize segurança”, “use boas práticas” — não governam. Eles não definem o que o agente deve fazer diante de um trade-off. Uma constitution precisa declarar consequências: se um requisito viola um princípio, o plano registra a exceção e pede decisão humana; não prossegue silenciosamente.

A constitution também não deve congelar o projeto. Mudá-la é possível, mas exige uma decisão de alcance maior que uma feature. A alteração pode tornar specs e implementações anteriores não conformes; por isso tem versão, justificativa, impacto e plano de adoção. Em termos arquiteturais, ela opera como política do sistema de desenvolvimento.

## Da intenção à implementação: o fluxo completo

O fluxo didático deste módulo usa:

`constitution → specify → clarify → plan → tasks → analyze → implement → verify`

Cada etapa reduz um tipo de incerteza e entrega um artefato diferente.

### 1. Constitution — quais regras governam todas as mudanças?

Antes de discutir a feature, o time estabelece princípios de qualidade, arquitetura, testes, segurança e experiência. O comando `/speckit.constitution` ajuda a estruturar o documento, mas a autoridade é humana. Uma regra constitucional não deve nascer apenas porque o modelo a sugeriu.

### 2. Specify — o que e por que construir?

`/speckit.specify` transforma uma intenção em spec orientada a usuários e resultados. O foco permanece em **o quê** e **por quê**, evitando escolher prematuramente framework, banco ou forma interna. Histórias e cenários devem ser priorizados e testáveis de maneira independente.

Uma especificação madura inclui:

1. contexto e problema;
2. atores, objetivos e linguagem do domínio;
3. jornadas ou histórias priorizadas;
4. requisitos funcionais;
5. requisitos não funcionais mensuráveis;
6. regras de negócio e invariantes;
7. segurança, privacidade e conformidade;
8. critérios de aceite;
9. casos extremos e falhas;
10. fora de escopo;
11. premissas, dúvidas e evidências pendentes.

O agente pode redigir, organizar e detectar lacunas. Ele não decide sozinho o que a organização quer, qual risco aceita ou que público pode ser prejudicado.

### 3. Clarify — que ambiguidades mudariam a solução?

`/speckit.clarify` existe porque prosa plausível pode esconder escolhas incompatíveis. “Usuários podem excluir relatórios” deixa perguntas: exclusão física ou lógica? quem pode excluir? há retenção legal? links compartilhados deixam de funcionar? a ação é reversível? Cada resposta pode alterar dados, autorização, UX e operação.

A clarificação deve priorizar perguntas de alto impacto e fazê-las uma por vez quando a resposta muda o próximo ramo. Um **ledger epistemológico** ajuda:

| Estado | Significado | Tratamento |
|---|---|---|
| fato | confirmado por fonte ou decisão autorizada | pode governar requisito |
| hipótese | explicação ou escolha ainda não confirmada | exige experimento ou decisão |
| desconhecido | informação ausente que muda solução | pergunta ou bloqueio |
| fora de escopo | deliberadamente não resolvido nesta entrega | registrar consequência |

Marcar incerteza é superior a preencher lacunas com a opção mais provável. Modelos são bons em produzir continuidade textual; exatamente por isso precisam de mecanismos que tornem o desconhecido visível.

### 4. Plan — como a arquitetura realizará a intenção?

`/speckit.plan` traduz a spec em decisões técnicas: componentes, dados, contratos, integrações, migração, segurança, observabilidade e estratégia de teste. Essa é a etapa em que tecnologia entra explicitamente.

O plano não repete requisitos em linguagem técnica. Ele mostra como cada decisão atende requisitos e atributos de qualidade, quais alternativas foram descartadas e onde há risco. Quando uma escolha merece existência independente, vira ADR. Quando falta evidência, vira experimento com hipótese, método e critério de parada.

Em brownfield, planejar começa por ler o sistema existente. O agente deve identificar interfaces estáveis, convenções, testes, dependências e blast radius. Um plano que ignora padrões do repositório cria uma segunda arquitetura imaginária.

### 5. Tasks — quais fatias entregam evidência independente?

`/speckit.tasks` decompõe o plano em unidades executáveis. Uma boa tarefa informa arquivo ou área, comportamento, teste, dependência, resultado esperado e definição de pronto. “Implementar backend” não é tarefa; “aceitar solicitação de exportação autorizada e persistir estado pendente, com teste de contrato” é.

As melhores unidades são **fatias verticais**: atravessam o mínimo necessário de interface, regra, persistência e teste para demonstrar comportamento. Fatias horizontais — “criar todas as tabelas”, depois “todas as APIs”, depois “todas as telas” — acumulam trabalho sem uma trajetória verificável e dificultam perceber cedo que o desenho não fecha.

Dependências formam um grafo. Tarefas sem bloqueadores entram na fronteira de execução e podem ser atribuídas a agentes diferentes; tarefas que compartilham arquivos, contratos ou decisões permanecem ordenadas. Paralelismo não é “usar o máximo de agentes”, mas explorar independência real sem aumentar conflitos e reintegração.

### 6. Analyze — os artefatos contam a mesma história?

Antes de implementar, `/speckit.analyze` procura contradições, lacunas e cobertura insuficiente entre constitution, spec, plano e tarefas. Exemplos:

- requisito de auditoria sem componente ou tarefa correspondente;
- tarefa que introduz dependência proibida pela constitution;
- plano com migração irreversível sem rollback;
- critério de aceite sem teste;
- requisito de desempenho sem volume ou ambiente;
- tarefa que implementa função fora do escopo.

Essa revisão não prova correção. Ela reduz erros de transformação antes que virem código.

### 7. Implement — executar decisões, não reinventá-las

`/speckit.implement` percorre tarefas e produz código e testes. O agente implementador deve ter autonomia estreita: pode escolher detalhes locais dentro das decisões aprovadas, mas pausa quando encontra ambiguidade que altera contrato, arquitetura ou risco.

O ciclo mínimo é:

1. selecionar uma fatia desbloqueada;
2. escrever um teste que expresse o comportamento;
3. executar e observar a falha correta;
4. escrever o mínimo para passar;
5. refatorar mantendo o teste verde;
6. executar verificações locais e regressão relevante;
7. comparar o diff à tarefa, ao plano e à spec;
8. registrar evidência e concluir a tarefa.

Gerar teste e código na mesma resposta sem observar a falha perde uma evidência importante: o teste pode estar confirmando comportamento já existente, não alcançar a implementação ou reproduzir exatamente o mesmo erro conceitual do código.

### 8. Verify — o que demonstra que a entrega corresponde à intenção?

Verificação possui ao menos dois eixos independentes:

- **aderência à spec:** requisitos, critérios, fora de escopo e riscos foram respeitados?
- **qualidade da implementação:** código segue padrões, arquitetura, segurança, testes e operabilidade do repositório?

As [skills de engenharia de Matt Pocock](https://github.com/mattpocock/skills/tree/main/docs/engineering) tornam essa separação explícita em revisão. Uma implementação pode ser tecnicamente elegante e resolver a necessidade errada; pode atender ao comportamento e introduzir uma estrutura insustentável. Misturar os eixos num único “aprovado” permite que força em um esconda fraqueza no outro.

## Requisitos que orientam agentes

Uma spec para agentes precisa ser precisa sem prescrever cada linha. A formulação EARS ajuda a escrever requisitos observáveis:

| Forma | Estrutura | Exemplo |
|---|---|---|
| ubíqua | o sistema deve… | O sistema deve registrar o autor de cada exportação. |
| orientada a evento | quando…, o sistema deve… | Quando a exportação terminar, o sistema deve disponibilizar o arquivo ao solicitante. |
| orientada a estado | enquanto…, o sistema deve… | Enquanto o relatório estiver fechado, o sistema deve impedir regeneração. |
| comportamento indesejado | se…, então o sistema deve… | Se a autorização expirar, o sistema deve negar o download e solicitar nova autenticação. |
| opcional | onde…, o sistema deve… | Onde retenção regulatória se aplicar, o sistema deve preservar o registro pelo prazo configurado. |

EARS não substitui linguagem do domínio ou cenários. Serve para retirar ambiguidade de condições e respostas. Critérios BDD complementam:

```gherkin
Cenário: gestor exporta somente registros autorizados
  Dado que Ana gerencia a unidade Sul
  E existem registros das unidades Sul e Norte
  Quando Ana solicita uma exportação mensal
  Então o arquivo contém somente registros da unidade Sul
  E o evento registra solicitante, filtro e versão da política
```

O cenário descreve uma seam pública. Ele não exige que o teste conheça classes privadas ou consultas internas. Isso permite refatorar a implementação sem reescrever o contrato.

## Deep modules e testes pelas seams

Um **deep module** oferece muito comportamento atrás de uma interface pequena. Para agentes, isso reduz contexto: o implementador precisa compreender contrato, invariantes e exemplos, não todos os detalhes internos do sistema. Interfaces grandes e vazamentos de abstração multiplicam arquivos que precisam ser lidos e decisões que podem divergir.

A **seam** é o ponto estável por onde o comportamento é observado ou substituído: endpoint, função pública, comando, evento ou adaptador. Testar pela mesma seam usada pelo consumidor aumenta a durabilidade do teste. Testes acoplados a métodos privados, ordem de chamadas internas ou estrutura exata de objetos quebram em refatorações que não mudam comportamento e induzem agentes a preservar acidentes históricos.

Isso não elimina testes unitários. Significa escolher o nível mais alto que continue rápido, determinístico e diagnóstico. Um contrato de autorização pode ser testado na função pública de política; uma trajetória de exportação pode exigir integração entre endpoint, fila e armazenamento; um detalhe de formatação pode permanecer unitário.

## Três gates, dois papéis humanos

No modelo de squad híbrida adotado como referência didática, dois papéis humanos mantêm autoridade:

- **Product Owner:** responde pelo problema, prioridade, regras e critérios de aceite;
- **Arquiteto ou dev sênior:** responde por decisões técnicas, atributos de qualidade, ADRs, riscos e revisão final.

Agentes especializados produzem rascunhos e evidências: entrevistador, especificador, arquiteto/planejador, implementador, engenheiro de testes e segurança. O número exato não é princípio; fronteiras claras são. Um único agente pode assumir vários papéis em tarefas pequenas. Separar contextos ajuda quando revisão precisa ser independente ou quando especializações usam fontes diferentes.

Os três gates impedem avanço sem decisão humana proporcional:

1. **Gate de intenção:** PO aprova spec, critérios, fora de escopo e riscos conhecidos.
2. **Gate de arquitetura:** arquiteto aprova plano, ADRs, seams, migração e estratégia de teste.
3. **Gate de entrega:** evidências de spec, qualidade, segurança e operação são revisadas antes do merge ou da liberação.

O gate não é uma reunião obrigatória. Pode ser uma aprovação versionada no pull request. Seu valor está em vincular pessoa, artefato, versão, evidência e consequência. “Pode seguir” numa conversa sem identificar a versão aprovada é frágil.

## Oito artefatos de uma demanda governada

Uma aplicação organizacional pode exigir oito conjuntos:

1. processo de negócio afetado;
2. spec de requisitos e regras;
3. arquitetura de referência;
4. ADRs;
5. casos de teste;
6. automação de testes;
7. esteira de CI/CD;
8. análise de segurança.

Nem toda alteração precisa de oito documentos separados. O princípio é cobertura, não quantidade de arquivos. Uma mudança pequena pode reunir processo, requisitos e aceite no mesmo `spec.md`; ADR só nasce quando há decisão significativa; segurança pode ser checklist vinculada à spec. O erro oposto é usar YAGNI para omitir risco real.

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

Velocidade de geração isolada é uma métrica perigosa. Se o agente produz mais código e aumenta retrabalho, o sistema local ficou rápido e o fluxo global piorou.

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
