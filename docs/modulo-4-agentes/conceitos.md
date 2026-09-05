# Conceitos: do diálogo à ação controlada

![Mapa da autonomia controlada: diálogo, fluxo de trabalho, agente e múltiplos agentes formam um continuum; planejamento usa ferramentas tipadas e estado sob políticas, enquanto ações materiais passam por aprovação explícita](../assets/images/m04-mapa-autonomia-controlada.png "Mapa da autonomia controlada")

*Figura — Autonomia não é uma propriedade binária: ela cresce com a capacidade de decidir e agir, e deve encontrar políticas e aprovação antes de cruzar fronteiras materiais.*

## Quatro formas de controle operacional

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

## O arnês: tudo o que cerca o modelo

Catálogo de ferramentas, saída estruturada, estado, memória, contexto e política não são acessórios do modelo. Eles formam o sistema que transforma um modelo em agente. A engenharia deu um nome a esse sistema: *harness*, ou **arnês**, o mesmo termo do equipamento que prende um alpinista à parede e do arreio que atrela um animal ao carro. A formulação canônica aparece em [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness), de Vivek Trivedy: *"if you're not the model, you're the harness"*. Arnês é todo código, configuração e lógica de execução que não é o modelo. A equação que resume o campo é **agente = modelo + arnês**.

O nome importa menos que a consequência de medição. Trivedy relata que a mesma família de modelo sobe de fora das trinta primeiras posições para as cinco primeiras do Terminal Bench 2.0 quando apenas o arnês muda, e que um mesmo modelo pontua de forma diferente dentro e fora do arnês de um produto comercial. Rankings de *benchmark* envelhecem rápido e a posição específica não deve ser decorada; o resultado durável é a direção da relação. Trocar de modelo é uma decisão cara e visível; reconstruir o arnês é uma decisão barata e invisível, e frequentemente produz mais efeito. Addy Osmani sintetiza o mesmo achado em [Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/): um modelo mediano dentro de um bom arnês supera um bom modelo dentro de um arnês ruim.

### Erro composto: a aritmética da trajetória

Um agente é um processo de muitas etapas, e etapas se compõem por multiplicação, não por média. Suponha uma confiabilidade de 99% por etapa, um número que soa excelente:

| Etapas na trajetória | Confiabilidade por etapa | Probabilidade de a trajetória inteira dar certo |
|---:|---:|---:|
| 10 | 99% | 90,4% |
| 20 | 99% | 81,8% |
| 50 | 99% | 60,5% |

A conta é `0,99^n`. Uma taxa de acerto por passo que pareceria ótima num classificador isolado produz uma taxa de fracasso relevante numa trajetória longa. A Anthropic registra o mesmo fenômeno em [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): a autonomia dos agentes traz custo maior e **erros que se compõem**. O modelo não é o lugar onde esse problema se resolve, porque o problema é estrutural do encadeamento. Ele se ataca no arnês, por quatro vias:

- **verificação:** dar ao agente uma forma de conferir o próprio trabalho antes de avançar, o que corta a propagação na origem;
- **pontos de parada:** interromper a trajetória em fronteiras definidas, para que um erro não atravesse dez etapas antes de aparecer;
- **redução do espaço de decisão:** menos ambiguidade por etapa significa menos chance de escolha errada;
- **contexto limpo:** menos ruído na janela significa menos chance de o modelo interpretar mal o estado atual.

A matemática também impõe um limite honesto. Reduzir o número de etapas é frequentemente mais eficaz que aumentar a confiabilidade de cada uma: um fluxo de dez passos com 99% é mais confiável que um de cinquenta passos com 99,5%. Essa é a versão quantitativa do [critério de entrada](#o-criterio-de-entrada) discutido adiante.

### Os componentes do arnês

A lista abaixo reúne os componentes que aparecem de forma recorrente nos ensaios de Trivedy e Osmani e na documentação da Anthropic. A coluna da direita mostra que o curso já ensina cada um deles, disperso entre módulos; o vocabulário de arnês é o que permite tratá-los como um sistema único e projetá-los juntos.

| Componente | Pergunta que ele responde | Onde este curso já trata |
|---|---|---|
| *System prompt* | Que caráter, limites e convenções governam toda tarefa? | [Prompt como contrato](../modulo-1-fundamentos/conceitos.md) e [saída estruturada](#uso-de-ferramentas-e-saidas-estruturadas) |
| Ferramentas | O que o agente pode fazer, e com que contrato? | [Contrato de ferramenta](padroes-e-decisoes.md#comece-pelo-contrato-de-ferramenta) |
| Gestão de contexto | O que entra na janela agora, e o que é descartado? | [Estado, memória e contexto](#estado-memoria-e-contexto) |
| Verificação | Como o agente confere o que fez antes de avançar? | [Fitness functions para autonomia](padroes-e-decisoes.md#fitness-functions-para-autonomia) e Módulo 5 |
| Memória | O que persiste entre execuções, com que autorização? | [Memória persistente](#estado-memoria-e-contexto) |
| *Sandbox* | Onde o código roda sem alcançar produção nem dado real? | Oficinas locais e [ambientes](../modulo-6-operacao/conceitos.md#ambientes-e-promocao) |
| *Hooks* | Em que ponto do ciclo um controle determinístico intervém? | [Políticas como fronteira executável](#politicas-como-fronteira-executavel) |

Os dois primeiros itens costumam receber toda a atenção, e são os de menor retorno isolado. O quarto é o de maior retorno comprovado, tema da subseção seguinte.

Vale registrar de onde o vocabulário vem, para não importá-lo sem crítica. Ele nasceu na comunidade de agentes de codificação, onde o arnês é um produto de linha de comando e os componentes têm nomes de arquivo concretos. A Anthropic documenta essa camada de forma explícita em [Steering Claude Code](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more), que separa mecanismos que **guiam** o modelo, como arquivos de contexto e *skills*, de mecanismos que **impõem** comportamento, como *hooks* e permissões, com uma frase que este curso já defende desde o Módulo 1: uma proteção real precisa ser determinística. A generalização para sistemas corporativos é legítima, mas a tradução não é automática: num agente de atendimento, o *sandbox* não é um contêiner de código, é a fronteira entre ferramenta de leitura e ferramenta de escrita.

### Diagnosticar pelo tipo de falha

A utilidade prática de decompor o arnês em componentes é transformar "o agente errou" em uma hipótese endereçável. Cada tipo de falha aponta para um componente diferente, e tratar o tipo errado consome orçamento sem mover o resultado.

| Sintoma observado | Componente provável | Primeira intervenção |
|---|---|---|
| O agente entendeu mal o que era para fazer, ou violou uma convenção nunca escrita | *system prompt* | tornar explícitos limites, convenções e o que nunca fazer |
| O agente escolheu a ferramenta errada entre opções parecidas | ferramentas | consolidar o catálogo e descrever fronteiras |
| O agente falhou ao executar, ou produziu efeito onde não devia | ferramentas e *sandbox* | contrato validável e isolamento do ambiente de execução |
| O agente se contradiz entre execuções, ou repete trabalho já feito | memória | definir o que persiste, com finalidade e prazo |
| O agente perdeu o fio numa trajetória longa | gestão de contexto | recortar o contexto por etapa e resumir o estado |
| O erro atravessou várias etapas antes de aparecer | verificação | conferência por etapa, com o motivo devolvido |
| O agente decidiu sozinho quando escalar | *hooks* | ponto de intervenção definido pelo projeto, não pelo modelo |

Quatro perguntas organizam o trabalho de melhoria, e valem tanto para um agente de codificação quanto para um agente de atendimento. Onde este agente falha mais, e a que componente esse tipo de falha corresponde? Ele tem alguma forma de verificar o próprio trabalho, e se não tem, qual seria a mais barata? Que contexto ele não recebe hoje e deveria receber, que hoje existe apenas na cabeça de alguém? E qual das tarefas que ele executa tem critério de sucesso inteiramente objetivo, porque essa é a candidata a subir de nível na escada da próxima seção.

A ordem entre as quatro importa. Trocar de modelo é a última pergunta, não a primeira.

### Mais ferramentas não significa menos erro

A intuição diante de um agente que erra é ampliar sua capacidade. A evidência aponta para o contrário. A Vercel [removeu 80% das ferramentas](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools) de um agente de texto para SQL, trocando dezesseis ferramentas especializadas por acesso a um sistema de arquivos com execução de comandos, e relatou taxa de sucesso subindo de 80% para 100%, com 40% menos *tokens*, 40% menos passos e tempo médio de resposta caindo de 274 para 77 segundos.

A explicação é a mesma do erro composto. Cada ferramenta adicional amplia o espaço de decisão de cada etapa, e ferramentas com fronteiras parecidas criam pontos de decisão ambíguos. A orientação da Anthropic em [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) formula o critério de forma verificável: se uma pessoa da engenharia não consegue dizer com segurança qual ferramenta usar numa situação, não se pode esperar que o modelo decida melhor. O corolário arquitetural é consolidar ferramentas por fluxo de trabalho em vez de espelhar cada endpoint da API, e nomeá-las com prefixos que revelem a fronteira.

Existe um custo simétrico que a lição não deve esconder. Descrições de ferramenta ocupam contexto antes de qualquer requisição: a Anthropic relata, em [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp), um caso em que carregar definições sob demanda em vez de todas de uma vez reduziu o consumo de 150 mil para 2 mil *tokens*. Catálogo mínimo é, ao mesmo tempo, decisão de qualidade e decisão de custo.

Arnês, portanto, não é maximizar capacidade. É otimizar o caminho até o resultado certo, e a operação que mais frequentemente melhora esse caminho é uma remoção.

### O arnês é onde mora a autoridade

Há uma leitura arquitetural que o vocabulário de arnês torna nítida e que fecha esta seção. Tudo o que decide **se** uma ação acontece vive no arnês, não no modelo. O catálogo apresentado ao modelo é interface de descoberta; a política é avaliada no executor; a aprovação vincula pessoa, objeto e prazo; o *hook* interrompe num ponto definido pelo projeto. Quando alguém diz que "o agente decidiu escalar", ou o arnês define esse ponto explicitamente, ou não existe ponto de escalonamento e sim uma coincidência.

Isso também delimita o que um bom arnês não faz. Ele reduz a probabilidade de erro e limita o raio de impacto; não torna segura uma ação irreversível, não substitui aceitação de risco residual com dono nomeado e não produz autorização. As [fronteiras de componente](#responsabilidades-e-fronteiras-de-componente) da próxima seção são a forma concreta de manter essa separação quando o arnês cresce.

## Responsabilidades e fronteiras de componente

O **planejador** propõe próximo passo; o **executor** valida e realiza a chamada; o **motor de políticas** decide permissão; o **estado** preserva a trajetória autorizada; a **aprovação** vincula pessoa, objeto imutável e prazo; o **catálogo** expõe somente ferramentas permitidas; e a **telemetria** registra evidências minimizadas. O planejador não recebe credenciais, o executor não redefine política, a aprovação não altera parâmetros e a telemetria não vira memória de trabalho. Essas fronteiras reduzem acoplamento e permitem trocar modelo ou orquestrador sem alterar autoridade ou efeito.

Separar componentes também acrescenta chamadas, latência e operação. A fronteira se justifica quando responsabilidade, risco, ciclo de mudança ou atributo de qualidade exigem independência.

## Agente único e múltiplos agentes

No **agente único**, um planejador recebe objetivo e catálogo limitado. Há menos mensagens, estados e pontos de coordenação. É a opção inicial quando uma trajetória cabe num contexto controlável e uma equipe pode manter os contratos.

Em **múltiplos agentes**, papéis especializados — atendimento, política, pedido — trocam mensagens ou são coordenados por um supervisor. A divisão pode reduzir contexto por papel e permitir políticas distintas, mas não cria conhecimento nem confiabilidade automaticamente. Multiplica prompts, modelos possíveis, handoffs, latência, custo, estados, permissões e falhas de consenso. “Debate” entre modelos não é aprovação independente se todos compartilham a mesma evidência defeituosa.

Use múltiplos agentes quando houver fronteiras reais: domínios mantidos por equipes diferentes, contextos incompatíveis, competências ou credenciais separadas, ou paralelismo medido. Defina protocolo, proprietário do estado, limite de delegação, formato de entrega e regra de encerramento. Se a motivação for apenas organizar um prompt grande, módulos determinísticos ou ferramentas especializadas costumam ser mais simples.

**n8n** automatiza workflows; **LangGraph** e **AutoGen** organizam estados ou agentes. Nenhum delega autoridade: política e aprovação permanecem externas.

## O critério de entrada

Um agente é candidato quando: a sequência útil varia de modo difícil de enumerar; ferramentas devolvem feedback verificável; erros podem ser contidos; a tarefa tem conclusão observável; e orçamento/autoridade podem ser delimitados. Rejeite ou limite autonomia quando o caminho é estável, o efeito é irreversível, a autorização é ambígua, o feedback chega tarde ou não existe recuperação proporcional.

## Características e tensões da autonomia

| Característica | Prioridade | Tensão aceita | Medida e responsável |
|---|---|---|---|
| Segurança e autorização | Não negociável | validação adicional aumenta latência | ação material sem política válida: zero; Segurança |
| Confiabilidade | Alta | idempotência e compensação aumentam estado | efeitos duplicados e compensações pendentes; Operações |
| Auditabilidade | Alta | trace retém metadados técnicos | execução reconstruível por versão; Auditoria |
| Latência e custo | Importante | orçamento pode limitar autonomia | p95, chamadas e custo por execução; Produto e plataforma |
| Modificabilidade | Importante | adaptadores e contratos acrescentam componentes | troca localizada e teste de contrato; Arquitetura |

Autonomia adequada é a que atende essas prioridades no cenário, não a que maximiza o número de ferramentas ou etapas escolhidas pelo modelo.

## Quatro níveis de loop

O arnês responde à pergunta "o que cerca o modelo". Falta a pergunta seguinte: **quem aciona o arnês, e quantas vezes**. É o que a engenharia de loop trata.

O ciclo básico já está descrito nas seções anteriores, e a Anthropic o formula em quatro tempos em [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk): **reunir contexto, agir, verificar o trabalho, repetir**. Cada rodada de uma conversa com um agente já é uma execução desse ciclo. A pergunta de engenharia é quanto dele fica com a pessoa e quanto passa para o sistema.

A Anthropic organiza a resposta em [Getting started with loops](https://claude.com/blog/getting-started-with-loops) como uma escada de quatro degraus. A escada se lê assim: **a cada degrau você entrega uma coisa a mais para a máquina**, e o que você entrega é exatamente o que precisa ter tornado verificável antes de subir.

| Nível | O que dispara | O que você entrega | Como o loop para | Exemplo |
|---|---|---|---|---|
| 1 — por rodada | seu *prompt* | a verificação | o agente julga que terminou ou precisa de contexto | pedir uma alteração, o agente edita, testa e responde |
| 2 — por objetivo | seu *prompt*, uma vez | a condição de parada | o objetivo é atingido ou o teto de rodadas é alcançado | "rode até a suíte de testes passar" |
| 3 — por tempo | um intervalo ou agendamento | o gatilho | você cancela ou o trabalho termina | a cada cinco minutos, verificar a fila e tratar o que chegou |
| 4 — proativo | um evento, sem pessoa presente | o próprio *prompt* | cada tarefa encerra ao atingir seu objetivo; a rotina roda até ser desligada | triagem contínua de erros reportados |

A diferença entre o nível 1 e o nível 2 é a mais importante e a menos percebida. No nível 1, o agente para quando **acha** que terminou. No nível 2, ele para quando um critério objetivo é satisfeito. Trocar julgamento por critério é o que permite tirar a pessoa da frente sem trocar supervisão por esperança.

### De uma piada a uma disciplina

A técnica que popularizou o nível 2 é deliberadamente simples. Em [Ralph Wiggum as a "software engineer"](https://ghuntley.com/ralph/), de 14 de julho de 2025, Geoffrey Huntley publicou um laço de uma linha:

```bash
while :; do cat PROMPT.md | claude-code ; done
```

O nome homenageia o personagem menos brilhante dos Simpsons, e a descrição do autor é honesta: a técnica é "deterministicamente ruim num mundo indeterminado". Ela funciona porque o estado não vive na conversa, vive nos arquivos e no histórico do repositório: cada iteração começa com contexto limpo e enxerga o que a anterior deixou no disco. Huntley é explícito sobre a condição que sustenta o laço, e que ele chama de contrapressão obrigatória: testes, análise estática e portões de validação que rejeitam código ruim. Sem isso, o laço apenas repete.

Um ano depois, a mesma ideia aparece como mecanismo de produto. A Anthropic distribui um [plugin oficial Ralph Wiggum](https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md) que implementa o laço dentro da própria sessão: um *hook* de encerramento bloqueia a saída e reinjeta o mesmo *prompt*. A documentação do plugin traz dois avisos que valem como princípio de projeto, muito além da ferramenta. O primeiro: a frase de conclusão é comparada por igualdade exata de texto, portanto não distingue "terminei com sucesso" de "terminei bloqueado", e o **limite de iterações é o mecanismo de segurança primário**, não a promessa de conclusão. O segundo é a lista de casos em que não se deve usar laço: tarefas que exigem julgamento humano, operações de uma vez só, tarefas sem critério de sucesso claro e depuração em produção.

O que esse par ensina é direto. O nível 2 não é uma técnica de produtividade pessoal; é uma decisão de projeto sobre autoridade e orçamento, com as mesmas perguntas de qualquer sistema agêntico: qual é a condição de parada, quem responde por ela, qual é o teto de consumo e o que acontece quando o teto é atingido sem sucesso.

### O gargalo é o verificador

O componente com maior retorno documentado é a verificação. Boris Cherny, criador do Claude Code, afirma que [dar ao modelo uma forma de verificar o próprio trabalho](https://x.com/bcherny/status/2007179861115511237) multiplica por dois ou três a qualidade do resultado final, e que essa é provavelmente a coisa mais importante a fazer. O que conta como verificação muda com o domínio: rodar um comando, executar uma suíte de testes, abrir a interface e conferir o resultado. A Anthropic descreve três famílias no Agent SDK: realimentação por regras, que é a mais forte porque diz qual regra falhou e por quê; realimentação visual; e um segundo modelo como avaliador, útil para critérios difusos e sujeito às limitações que o Módulo 5 detalha.

Daí sai o critério para subir a escada, e ele é restritivo de propósito. **Só é candidata ao nível 2 uma tarefa cujo critério de sucesso seja inteiramente objetivo**: testes que passam, compilação que conclui, análise estática que zera, indicador que atinge um limiar. Sem esse critério, um laço desassistido não é automação, é consumo de orçamento sem condição de término, e o pior desfecho não é o gasto, é o falso positivo: o sistema declara conclusão e ninguém confere.

Existe uma consequência prática agradável para quem já pratica desenvolvimento guiado por testes. Testes escritos antes da implementação não são só verificação: são a condição de parada de um laço de nível 2. Quem já os escreve primeiro tem o pré-requisito pronto. A mesma observação vale para o fluxo guiado por especificação da segunda metade deste módulo, e é por isso que ele aparece aqui: um processo com constitution, spec, plano, tarefas e portões é, em vocabulário de arnês, o arnês de um agente que escreve software. A operação desses laços fora da sessão de trabalho, com orçamento, isolamento, interrupção e trilha, é assunto do [Módulo 6](../sobre/plano-da-disciplina.md#modulo-6).

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
