# O fluxo SDD

Oito etapas, três portões humanos e oito artefatos que precisam contar a mesma história sobre a mesma mudança.

O fluxo descrito aqui é o do [Spec Kit](https://github.com/github/spec-kit), que nomeia cada etapa por um comando: `constitution`, `specify`, `clarify`, `plan`, `tasks`, `analyze`, `implement` e `verify`. Os nomes ficam em inglês porque é assim que você vai digitá-los; o que cada um significa está no [vocabulário mínimo](index.md#vocabulario-minimo) do módulo. Nenhuma etapa depende de ferramenta: o que importa é qual incerteza cada uma remove.

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

A clarificação deve priorizar perguntas de alto impacto e fazê-las uma por vez quando a resposta muda o próximo ramo. Um **registro epistemológico (*ledger*) epistemológico** ajuda:

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

## Quatro abordagens para o mesmo padrão

Os oito comandos acima são a implementação do Spec Kit, não o único jeito de fazer SDD. Quatro abordagens resolvem o mesmo problema, transformar intenção em evidência, com formas bem diferentes de organizar o trabalho. Conhecê-las evita confundir o comando `/speckit.plan` com o princípio que ele serve.

OpenSpec, Spec Kit e SPDD colocam artefatos de intenção antes da implementação e tentam mantê-los úteis ao longo da mudança. Superpowers, embora não seja uma ferramenta de SDD no mesmo sentido, serve como contraponto relevante. Sua ênfase está menos em uma especificação principal do sistema e mais na disciplina de execução: design aprovado, plano detalhado, isolamento, desenvolvimento dirigido por testes, revisão e verificação.

> **Nota de escopo.** Ferramentas para desenvolvimento agêntico mudam rapidamente. Comandos e recursos descritos aqui refletem a documentação pública consultada em 12 de setembro de 2026. A comparação privilegia o modelo de trabalho de cada abordagem, não uma fotografia exaustiva de todas as integrações disponíveis.

### Um caso comum para comparar

Para tornar a comparação concreta, as quatro abordagens serão aplicadas à mesma tarefa hipotética: adicionar limitação de tentativas de login à API de um banco digital consumida por vários canais. O caso é diferente da exportação de avaliações usada no restante desta página de propósito, porque comparar quatro abordagens exige um problema pequeno o suficiente para caber quatro vezes seguidas.

O pedido inicial, “bloquear a conta depois de cinco tentativas”, parece pequeno, mas esconde perguntas que a etapa de [clarificação](#3-clarify-que-ambiguidades-mudariam-a-solucao) precisa fazer:

- A contagem é por conta, dispositivo, endereço IP ou uma combinação desses identificadores?
- A janela é fixa ou deslizante? Quando o contador expira?
- Uma tentativa bem-sucedida zera o contador?
- O bloqueio impede apenas o login ou também a recuperação de senha?
- Como evitar que um atacante bloqueie deliberadamente contas conhecidas?
- O sistema tem várias instâncias? O contador precisa de consistência atômica?
- Qual resposta HTTP deve ser devolvida sem revelar se a conta existe?
- Quais métricas e alertas permitem detectar abuso e falso positivo?
- Há exigência de trilha de auditoria? Por quanto tempo os dados podem ser retidos?
- Como a mudança será desativada ou revertida se bloquear usuários legítimos?

Cada pergunta sem resposta é um item que o agente preencheria sozinho com a opção mais provável. Para comparar os fluxos em igualdade de condições, suponha que o time tenha definido o seguinte comportamento:

- cinco falhas por conta numa janela deslizante de quinze minutos
- bloqueio de novas autenticações por quinze minutos
- sucesso zera o contador
- recuperação de senha permanece disponível
- a resposta externa não revela se a conta existe
- atualização do contador é atômica num armazenamento compartilhado
- eventos de bloqueio geram métrica sem registrar credenciais nem dados sensíveis
- uma configuração permite desativar a regra sem nova implantação

O ponto do exemplo não é afirmar que essas são as melhores decisões para todo banco. É mostrar como cada abordagem transforma as mesmas decisões em artefatos, tarefas e verificações.

### OpenSpec: a mudança como unidade de governança

**Como funciona.** O [OpenSpec](https://github.com/Fission-AI/OpenSpec) se apresenta como uma camada leve de acordo entre a pessoa e o agente. Há dois espaços principais no repositório: `openspec/specs/`, que descreve o comportamento atual do sistema, e `openspec/changes/`, que contém uma pasta por mudança proposta. A mudança padrão reúne quatro tipos de artefato: proposta, especificações-delta, design e tarefas. Quando o trabalho termina, os deltas são incorporados às especificações principais e a pasta da mudança é arquivada, preservando seu histórico (Fission-AI, 2026a).

No perfil básico atual, o caminho típico é explorar opcionalmente, propor, aplicar, sincronizar e arquivar. O perfil expandido separa a criação progressiva dos artefatos e acrescenta uma verificação explícita da implementação contra a proposta, o design, as tarefas e os requisitos. Os artefatos não formam uma cascata imutável: a documentação orienta que sejam corrigidos quando a implementação revelar algo novo (Fission-AI, 2026b). Isso aproxima o OpenSpec de *spec-anchored*, na taxonomia vista na [página anterior](modos-de-trabalho.md#o-que-sdd-pode-significar).

**Exemplo aplicado.** Na limitação de login, a exploração faria o agente localizar o fluxo de autenticação, o armazenamento compartilhado, os padrões de resposta e os mecanismos existentes de configuração e observabilidade. A proposta registraria o problema, o escopo e o impacto esperado. A especificação-delta acrescentaria cenários como:

- depois da quinta falha dentro da janela, novas autenticações são rejeitadas durante quinze minutos.
- a resposta externa permanece indistinguível para conta existente e inexistente.
- uma autenticação bem-sucedida antes do limite zera o contador.
- o fluxo de recuperação de senha continua acessível.
- atualizações concorrentes não permitem ultrapassar o limite por condição de corrida.

O design explicaria a escolha do armazenamento, a chave usada no contador, a operação atômica, a expiração, a configuração de emergência e a instrumentação. A lista de tarefas decomporia implementação, testes, telemetria e documentação. Antes do arquivamento, a verificação compararia o código com esses artefatos. A sincronização incorporaria o delta ao domínio de autenticação.

**O que faz bem.** O maior ganho é separar o estado do sistema da história das mudanças. Um mantenedor consegue ler a especificação consolidada para saber como o login funciona hoje e consultar a pasta arquivada quando precisa entender por que a regra foi introduzida. Deltas reduzem a tentação de reescrever documentos inteiros e tornam revisável a diferença de comportamento proposta. O OpenSpec também permite calibrar a cerimônia: uma mudança clara pode gerar os artefatos de uma vez, e uma mudança ambígua pode passar por exploração e construção progressiva. Schemas personalizáveis permitem adaptar os tipos de artefato e suas dependências.

**Onde exige cuidado.** A ferramenta oferece estrutura, mas não prova que a especificação está correta. A verificação de alinhamento continua dependendo da capacidade do agente e da revisão humana. Além disso, o fluxo só permanece *spec-anchored* se sincronização e arquivamento forem hábitos reais. A documentação atual informa que o arquivamento alerta sobre tarefas incompletas, mas pode prosseguir. Por isso, políticas de CI ou revisão podem ser necessárias quando a organização precisa de um bloqueio efetivo. O OpenSpec também não impõe, por padrão, uma constitution acima de todas as mudanças. Isso reduz peso, mas exige outro mecanismo para princípios transversais, como segurança, privacidade, compatibilidade e observabilidade.

**Melhor encaixe:** produtos de longa duração que evoluem por mudanças incrementais e precisam de uma especificação atual do comportamento, sem adotar de saída uma camada extensa de governança organizacional.

### GitHub Spec Kit: intenção sob uma constitution de projeto

**Como funciona.** É o fio operacional percorrido nas oito etapas acima. Na documentação atual, o fluxo agêntico inclui nove comandos: constitution, especificação, esclarecimento, plano, checklist, tarefas, análise, implementação e convergência. Esclarecimento, checklist e análise funcionam como portões de qualidade acionados conforme a ambiguidade e o risco. A convergência procura requisitos ou decisões ainda não atendidos e acrescenta trabalho rastreável à lista de tarefas. A ferramenta também passou a oferecer extensões, presets e workflows para adaptar ou automatizar o processo (GitHub, 2026a, 2026b).

**Exemplo aplicado.** No banco digital, a constitution poderia determinar que alterações em autenticação:

- não revelem a existência de contas por mensagens ou tempo de resposta.
- preservem o fluxo de recuperação e um mecanismo operacional de contingência.
- produzam métricas sem incluir identificadores sensíveis.
- tenham cenários automatizados para concorrência, expiração e compatibilidade.
- registrem justificativa para novos componentes de infraestrutura.

A especificação descreveria atores, cenários, critérios de aceitação e resultados observáveis sem decidir prematuramente a tecnologia. O esclarecimento identificaria lacunas como janela deslizante, redefinição do contador e comportamento em múltiplos dispositivos. O plano escolheria o armazenamento e a operação atômica. A checagem constitucional impediria que o plano usasse uma resposta que expõe a existência da conta. O checklist avaliaria a qualidade dos requisitos. A análise procuraria inconsistências entre constitution, especificação, plano e tarefas. E a convergência verificaria, após a implementação, o que ainda falta.

**O que faz bem.** Oferece vocabulário e pontos de controle para organizações que precisam demonstrar não apenas o que foi implementado, mas também como a mudança respeitou princípios compartilhados. A separação entre especificação funcional e plano técnico, que é a [Decisão 2](decisoes.md#decisao-2-separar-o-que-de-como), evita que uma escolha prematura de tecnologia seja confundida com necessidade de negócio. Os portões intermediários distribuem a carga de revisão: primeiro a ambiguidade, depois a arquitetura, depois a cobertura e a consistência. A diversidade de integrações reduz dependência de um único agente.

**Onde exige cuidado.** Constituições ruins viram coleções de slogans genéricos ou regras demais. No primeiro caso, não alteram decisão alguma. No segundo, bloqueiam mudanças legítimas e incentivam aprovações automáticas. A constitution também pode duplicar instruções já presentes em arquivos do repositório, políticas de segurança e pipelines, criando fontes concorrentes. O número de artefatos aumenta a superfície de inconsistência, e o time precisa de critérios claros para abreviar o fluxo, sob pena de cada pessoa improvisar um SDD diferente. Por fim, a constitution governa o processo apenas se violações tiverem consequência. Um agente declarar conformidade não substitui revisão especializada, testes independentes nem controles automatizados.

**Melhor encaixe:** programas com múltiplos times, princípios arquiteturais compartilhados, exigência de auditoria ou necessidade de padronizar como intenção, plano e execução se conectam.

### SPDD: o prompt estruturado como contrato de implementação

**Como funciona.** O [Structured Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/), publicado pela Thoughtworks, trata o prompt como artefato de entrega versionado, revisável, reutilizável e mantido junto do código. Seu núcleo é o Painel REASONS, que organiza a especificação em sete dimensões (Zhang & Xia, 2026):

- **Requirements:** problema, escopo e definição de pronto.
- **Entities:** conceitos do domínio e seus relacionamentos.
- **Approach:** estratégia escolhida e trade-offs.
- **Structure:** componentes, dependências e encaixe no sistema.
- **Operations:** passos de implementação concretos e verificáveis.
- **Norms:** convenções transversais de engenharia.
- **Safeguards:** limites e invariantes que não podem ser violados.

O Painel comprime, num artefato só, o que o Spec Kit distribui entre constitution (Norms e Safeguards), especificação (Requirements e Entities) e plano (Approach, Structure e Operations). O OpenSPDD materializa o fluxo em comandos para analisar requisitos e código existente, produzir o Painel, gerar a implementação, atualizar o prompt quando o requisito muda e sincronizar de volta alterações feitas no código (Zhang & Xia, 2026, e Zhang, 2026).

**Exemplo aplicado.** Para a limitação de login, o Painel poderia registrar:

- em **Requirements**, os cenários de bloqueio, expiração, recuperação e resposta indistinguível.
- em **Entities**, conta, tentativa, janela, bloqueio e evento de segurança, com suas relações.
- em **Approach**, contador distribuído com expiração e atualização atômica, além da mitigação contra bloqueio malicioso.
- em **Structure**, os pontos exatos do serviço de autenticação, do adaptador de armazenamento, da configuração e da telemetria.
- em **Operations**, a ordem das alterações, assinaturas relevantes, testes e critérios de conclusão.
- em **Norms**, os padrões existentes para erros, logs, métricas, injeção de dependência e nomenclatura.
- em **Safeguards**, a proibição de registrar credenciais, de revelar existência da conta, de alterar a recuperação de senha e de introduzir estado apenas em memória local.

Se a revisão descobrir que o bloqueio por conta cria um vetor de negação de serviço, a correção deve primeiro alterar o contrato de intenção e só depois ajustar o código. Se uma refatoração legítima mudar a estrutura sem alterar comportamento, o fluxo inverso atualiza o Painel para evitar que ele se torne documentação enganosa. É a [Decisão 8](decisoes.md#decisao-8-manter-os-artefatos-coerentes) aplicada a um artefato único em vez de uma cadeia.

**O que faz bem.** O REASONS torna explícitos três níveis que prompts livres costumam misturar: intenção, design e governança. Isso oferece ao revisor um objeto consistente para examinar antes de receber um diff grande. Normas e salvaguardas reduzem a tendência de o agente extrapolar escopo, enquanto Operações diminuem decisões locais deixadas para o momento da geração. O método também reconhece que sincronização não é aprendizagem autônoma: o modelo não “absorve” silenciosamente as correções do time, e o fluxo humano precisa atualizar o ativo versionado.

**Onde exige cuidado.** O SPDD desloca parte importante do trabalho para antes da geração, o que exige profissionais capazes de modelar o domínio, avaliar abstrações e escrever limites verificáveis. O próprio artigo reconhece custo alto de mudança de mentalidade, dependência de experiência sênior e necessidade de automação para evitar um teto de produtividade. Estrutura também não elimina variação: dois profissionais podem produzir Painéis diferentes a partir do mesmo requisito, e um Painel formalmente completo ainda pode estar semanticamente errado.

A sequência de testes merece decisão consciente. O fluxo de referência valida a API antes da revisão detalhada do código e gera testes unitários depois que a implementação se estabiliza. Isso prioriza comportamento externo antes do investimento de revisão, mas diverge do TDD praticado na [etapa 7](#7-implement-executar-decisoes-nao-reinventa-las) e pode conflitar com políticas que exigem testes guiando o design desde o início. O método tem retorno menor em protótipos descartáveis, scripts únicos, hotfixes durante um incidente e trabalho predominantemente estético. Em “buracos negros de contexto”, nos quais nem o negócio consegue definir regras e fronteiras, um Painel detalhado pode apenas conferir aparência de precisão a premissas frágeis.

**Melhor encaixe:** domínios ricos em lógica, mudanças repetíveis, restrições rígidas e necessidade de manter intenção de design próxima da implementação.

### Superpowers: disciplina de engenharia ao redor do agente

**Como funciona.** O [Superpowers](https://github.com/obra/superpowers) é um conjunto de habilidades combináveis para agentes e uma metodologia de desenvolvimento. Seu fluxo básico começa com levantamento de ideias e aprovação do design, cria uma cópia isolada do repositório, produz um plano de tarefas pequenas e então executa esse plano. Durante a implementação, exige o ciclo vermelho-verde-refatorar do TDD, revisão em duas etapas (conformidade com o plano e qualidade do código) e verificação antes de qualquer declaração de conclusão. Ao final, apresenta opções para integrar, manter ou descartar o trabalho (Vincent & Prime Radiant, 2026).

É importante classificá-lo corretamente. Superpowers registra design e plano, portanto não se resume a “código e conversa”. Mas não estabelece, por padrão, uma especificação consolidada do comportamento do sistema que recebe deltas ao longo de várias mudanças. Ele é melhor entendido como um harness de execução disciplinada, adjacente ao SDD, que pode consumir uma especificação produzida por outro processo.

**Exemplo aplicado.** Para a limitação de login, o levantamento inicial faria perguntas sobre janela, escopo do bloqueio, concorrência, recuperação, privacidade e contingência. O agente apresentaria o design em partes para aprovação e produziria um plano com arquivos, passos e verificações específicas. A implementação ocorreria em uma árvore de trabalho isolada e começaria por um teste que falha. Casos como quinta falha, sexta tentativa, expiração, sucesso que zera contador, concorrência entre instâncias e resposta sem enumeração de contas guiariam o código mínimo. Depois da refatoração, uma revisão verificaria primeiro se a mudança cumpre o design aprovado e depois se a qualidade interna é aceitável.

**O que faz bem.** Combate duas falhas comuns de agentes: começar a codificar antes de compreender a tarefa e declarar conclusão com base em impressão. O isolamento protege o estado principal enquanto o agente experimenta. O TDD cria ciclos curtos de evidência. A revisão separada de conformidade e qualidade é a mesma [revisão em dois eixos](decisoes.md#decisao-6-usar-revisao-em-dois-eixos) da Decisão 6, chegando por outro caminho. Por ser modular, o conjunto cobre também depuração sistemática, execução por lotes e coordenação de tarefas, e pode complementar uma abordagem de especificação: OpenSpec ou Spec Kit fornecem a intenção e os artefatos, Superpowers disciplina a execução e a verificação.

**Onde exige cuidado.** A ausência de uma especificação cumulativa significa que decisões de domínio podem ficar distribuídas em documentos de design por mudança. Testes preservam comportamento executável, mas não substituem a justificativa, os limites e os trade-offs que futuros times precisam entender. Também é enganoso chamá-lo simplesmente de “leve”: a governança documental é menor do que a do Spec Kit, mas a disciplina operacional é alta, e em bases sem testes rápidos ou difíceis de isolar a adoção exige investimento de engenharia. Como em qualquer fluxo guiado pelo mesmo agente, existe risco de autocorrelação, com o agente escrevendo plano, código e revisão sob a mesma interpretação equivocada.

**Melhor encaixe:** times que querem elevar a disciplina de execução agêntica, especialmente em bases com boa testabilidade, sem necessariamente instituir uma especificação de domínio como artefato central.

### O que muda e o que não muda

As quatro implementações concordam no princípio e discordam no mecanismo. Todas separam intenção de execução. Todas preservam alguma forma de evidência antes de considerar o trabalho concluído. Todas dão à pessoa humana autoridade sobre decisões que o agente não deveria tomar sozinho. O que muda é onde o contrato mora, quantos portões existem e se o comando é digitado ou disparado automaticamente. A comparação sistemática das quatro, com dez critérios e um guia de escolha por situação, está em [Decisões e limites do SDD](decisoes.md#as-abordagens-nao-cobram-o-mesmo-tipo-de-rigor).

## Requisitos que orientam agentes

Uma especificação para agentes precisa ser precisa sem prescrever cada linha. A formulação **EARS** ajuda — a sigla é *Easy Approach to Requirements Syntax*, um conjunto de cinco moldes de frase criado na Rolls-Royce para eliminar ambiguidade de requisito sem recorrer a notação formal. Cada molde fixa a condição e a resposta esperada:

| Forma | Estrutura | Exemplo |
|---|---|---|
| ubíqua | o sistema deve… | O sistema deve registrar o autor de cada exportação. |
| orientada a evento | quando…, o sistema deve… | Quando a exportação terminar, o sistema deve disponibilizar o arquivo ao solicitante. |
| orientada a estado | enquanto…, o sistema deve… | Enquanto o relatório estiver fechado, o sistema deve impedir regeneração. |
| comportamento indesejado | se…, então o sistema deve… | Se a autorização expirar, o sistema deve negar o download e solicitar nova autenticação. |
| opcional | onde…, o sistema deve… | Onde retenção regulatória se aplicar, o sistema deve preservar o registro pelo prazo configurado. |

EARS não substitui linguagem do domínio nem dispensa cenários. Ele serve para retirar ambiguidade de condição e resposta: “o sistema deve ser seguro” não cabe em nenhum dos cinco moldes, e essa recusa é o próprio diagnóstico.

Os cenários completam o quadro no formato **BDD** — *Behaviour-Driven Development*, em que cada caso é escrito como dado (a situação inicial), quando (a ação) e então (o resultado observável). O formato abaixo se chama Gherkin e é lido tanto por pessoas quanto por ferramentas de teste:

```gherkin
Cenário: gestor exporta somente registros autorizados
  Dado que Ana gerencia a unidade Sul
  E existem registros das unidades Sul e Norte
  Quando Ana solicita uma exportação mensal
  Então o arquivo contém somente registros da unidade Sul
  E o evento registra solicitante, filtro e versão da política
```

O cenário descreve uma seam pública. Ele não exige que o teste conheça classes privadas ou consultas internas. Isso permite refatorar a implementação sem reescrever o contrato.

<a id="deep-modules-e-testes-pelas-seams"></a>

## Módulos profundos (*deep modules*) e costuras (*seams*)

Dois termos entram aqui, os dois vindos da literatura de projeto de software em inglês.

Um **módulo profundo** — *deep module*, termo de John Ousterhout — oferece muito comportamento atrás de uma interface pequena. O contrário é o módulo raso: interface grande, comportamento pouco. Um exemplo do próprio curso: a função `autorizar(usuario, recurso, acao)` devolve `permitir`, `negar` ou `exigir_aprovacao` e esconde atrás disso a tabela de políticas, a hierarquia de unidades e a expiração de credencial. Quem chama precisa entender três argumentos e três respostas. A versão rasa exporia `carregarPoliticas()`, `resolverHierarquia()`, `checarExpiracao()` e deixaria a composição por conta de quem chama — que passa a poder compor errado.

Para um agente, a diferença é de contexto: com módulo profundo, ele precisa compreender contrato, invariantes e exemplos; com módulo raso, precisa ler todos os arquivos internos e ainda pode divergir da composição correta.

Uma **costura** — *seam*, termo de Michael Feathers — é o ponto estável por onde o comportamento pode ser observado ou substituído sem alterar o código em volta. Costuras típicas: um endpoint HTTP, uma função pública, um comando de linha, um evento publicado, um adaptador de banco. No exemplo da exportação de avaliações, a costura é o endpoint `POST /exportacoes`: é por ele que o consumidor entra, e é por ele que o teste deve entrar também.

Testar pela mesma costura que o consumidor usa aumenta a durabilidade do teste. Já os testes acoplados a métodos privados, ordem de chamadas internas ou estrutura exata de objetos quebram em refatorações que não mudam comportamento e induzem agentes a preservar acidentes históricos.

Isso não elimina testes unitários. Significa escolher o nível mais alto que continue rápido, determinístico e diagnóstico. Um contrato de autorização pode ser testado na função pública de política; uma trajetória de exportação pode exigir integração entre endpoint, fila e armazenamento; um detalhe de formatação pode permanecer unitário.

## Três gates, dois papéis humanos

No modelo de squad híbrida adotado como referência didática, dois papéis humanos mantêm autoridade:

- **Product Owner:** responde pelo problema, prioridade, regras e critérios de aceite;
- **Arquiteto ou dev sênior:** responde por decisões técnicas, atributos de qualidade, ADRs, riscos e revisão final.

Agentes especializados produzem rascunhos e evidências: entrevistador, especificador, arquiteto/planejador, implementador, engenheiro de testes e segurança. O número exato não é princípio; fronteiras claras são. Um único agente pode assumir vários papéis em tarefas pequenas. Separar contextos ajuda quando revisão precisa ser independente ou quando especializações usam fontes diferentes.

Os três portões (*gates*) impedem avanço sem decisão humana proporcional:

1. **portão (*gate*) de intenção:** PO aprova spec, critérios, fora de escopo e riscos conhecidos.
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

Nem toda alteração precisa de oito documentos separados. O princípio é cobertura, não quantidade de arquivos. Uma mudança pequena pode reunir processo, requisitos e aceite no mesmo `spec.md`; ADR só nasce quando há decisão significativa; segurança pode ser checklist vinculada à spec. O erro oposto é invocar **YAGNI** — *You Aren't Gonna Need It*, a regra de não construir o que ainda não é exigido — para omitir risco que já existe. YAGNI dispensa a funcionalidade especulativa, não a análise de segurança de uma funcionalidade que vai para produção.
