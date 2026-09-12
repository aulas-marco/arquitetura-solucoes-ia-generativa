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

## O mesmo padrão, mecanismos diferentes

Os oito comandos acima são a implementação do Spec Kit, não o único jeito de fazer SDD. Três mecanismos resolvem o mesmo problema, transformar intenção em evidência, com formas bem diferentes de organizar o trabalho. Conhecê-los evita confundir o comando `/speckit.plan` com o princípio que ele serve.

### OpenSpec: a mudança como unidade, não o pipeline inteiro

O [OpenSpec](https://github.com/Fission-AI/OpenSpec) não parte de uma constitution nem percorre oito comandos em sequência. A unidade de trabalho é a mudança: uma pasta com proposta, especificação-delta, design e tarefas, que só é incorporada à especificação principal do sistema quando arquivada. Para a exportação de avaliações, isso significaria criar uma pasta `mudancas/exportacao-avaliacoes/` contendo só a diferença de comportamento (o cenário Gherkin desta página, o endpoint `POST /exportacoes`, a regra de autorização por unidade), sem declarar uma constitution nem passar pelos três portões completos.

Isso aproxima o OpenSpec da classe M da [Decisão 1](decisoes.md#decisao-1-escolher-a-profundidade-proporcional): comportamento novo, mais de um componente, mas sem o risco que justificaria a cerimônia completa de uma classe L. A especificação principal do sistema, o equivalente ao `spec.md` vivo, recebe só o delta aprovado, e a pasta arquivada preserva por que aquela mudança aconteceu, sem exigir uma constitution para funcionar.

### SPDD: a especificação inteira como um prompt estruturado único

O [Structured Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) (SPDD), publicado pela Thoughtworks, comprime constitution, spec e parte do plano num único artefato: o Painel REASONS, com sete dimensões (Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards). Na exportação de avaliações, a restrição de autorização por unidade que aqui vive na constitution, o critério de aceite que vive na spec, e a escolha de armazenamento que vive no plano, entrariam todos no mesmo painel, cada um em sua dimensão.

A diferença mais relevante para este módulo é a ordem da verificação. O SPDD roda testes de API antes da revisão de código, e testes unitários depois, o inverso da própria sequência ensinada na etapa 7 acima. A justificativa: quando a revisão humana acontece, requisitos e design já foram aprovados no painel, então a atenção do revisor vai para o que ainda importa naquele estágio, não para reconferir intenção que já foi validada. O painel também mantém um laço fechado entre prompt e código. Uma correção de lógica atualiza o painel antes do código. Uma refatoração legítima sincroniza o painel a partir do código, para que nenhum dos dois lados fique desatualizado silenciosamente ([Zhang & Xia, 2026](https://martinfowler.com/articles/structured-prompt-driven/), [OpenSPDD](https://github.com/gszhangwei/open-spdd)).

### Superpowers: disciplina automática em vez de comando explícito

O [Superpowers](https://github.com/obra/superpowers) muda outra variável. Em vez de comandos explícitos que alguém precisa lembrar de digitar, um conjunto de habilidades é acionado automaticamente conforme a situação exige. O ciclo de implementação (teste que falha, código mínimo, refatoração) é quase idêntico ao ensinado na etapa 7, mas levado a um extremo disciplinar: o próprio sistema apaga código escrito antes de seu teste correspondente existir. O trabalho roda numa cópia isolada do repositório, e a revisão também acontece em dois eixos, conformidade com o plano aprovado e qualidade da implementação, o mesmo princípio da etapa 8 deste módulo chegando por outro caminho.

A diferença estrutural importa. Superpowers não mantém uma especificação principal versionada como fonte de verdade do sistema, ao contrário de OpenSpec, Spec Kit e SPDD. Ele é melhor entendido como disciplina de execução adjacente ao SDD, que pode consumir uma spec produzida por outro processo, não como uma quarta forma de manter a spec viva.

### O que muda e o que não muda

As quatro implementações concordam no princípio e discordam no mecanismo. Todas separam intenção de execução. Todas preservam alguma forma de evidência antes de considerar o trabalho concluído. Todas dão à pessoa humana autoridade sobre decisões que o agente não deveria tomar sozinho. O que muda é onde o contrato mora (pasta de mudança, painel único, cadeia de artefatos sob constitution, ou plano dentro de um harness de execução), quantos portões existem, e se o comando é digitado ou disparado automaticamente. A pergunta que abre este módulo continua a mesma para qualquer uma das quatro: qual liberdade o modelo recebe, qual contrato orienta suas escolhas, e que evidência autoriza o próximo passo.

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
