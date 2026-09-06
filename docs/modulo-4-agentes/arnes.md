# Engenharia de arnês

Tudo o que cerca o modelo e o transforma em agente, e por que reconstruir esse conjunto costuma render mais do que trocar de modelo.

<a id="o-arnes-tudo-o-que-cerca-o-modelo"></a>

Catálogo de ferramentas, saída estruturada, estado, memória, contexto e política não são acessórios do modelo. Eles formam o sistema que transforma um modelo em agente. A engenharia deu um nome a esse sistema: *harness*, ou **arnês**, o mesmo termo do equipamento que prende um alpinista à parede e do arreio que atrela um animal ao carro. A formulação canônica aparece em [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness), de Vivek Trivedy: *"if you're not the model, you're the harness"*. Arnês é todo código, configuração e lógica de execução que não é o modelo. A equação que resume o campo é **agente = modelo + arnês**.

O curso já nomeou esse conjunto uma vez, de outro ângulo. A [superfície comportamental](../modulo-1-fundamentos/superficie-comportamental.md#de-onde-emerge-o-comportamento) do Módulo 1 é a configuração inteira que produz o comportamento observado numa execução, e inclui o modelo; o arnês é essa mesma superfície menos o modelo. A troca de lente não é cosmética: a superfície responde “por que a saída é esta”, e o arnês responde “o que eu posso reconstruir sem trocar de fornecedor”.

O nome importa menos que a consequência de medição. Trivedy relata que a mesma família de modelo sobe de fora das trinta primeiras posições para as cinco primeiras do Terminal Bench 2.0 quando apenas o arnês muda, e que um mesmo modelo pontua de forma diferente dentro e fora do arnês de um produto comercial. Rankings de *benchmark* envelhecem rápido e a posição específica não deve ser decorada; o resultado durável é a direção da relação. Trocar de modelo é uma decisão cara e visível; reconstruir o arnês é uma decisão barata e invisível, e frequentemente produz mais efeito. Addy Osmani sintetiza o mesmo achado em [Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/): um modelo mediano dentro de um bom arnês supera um bom modelo dentro de um arnês ruim.

## Erro composto: a aritmética da trajetória

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

A matemática também impõe um limite honesto. Reduzir o número de etapas é frequentemente mais eficaz que aumentar a confiabilidade de cada uma: um fluxo de dez passos com 99% é mais confiável que um de cinquenta passos com 99,5%. Essa é a versão quantitativa do [critério de entrada](controle-e-autonomia.md#o-criterio-de-entrada) discutido adiante.

## Os componentes do arnês

A lista abaixo reúne os componentes que aparecem de forma recorrente nos ensaios de Trivedy e Osmani e na documentação da Anthropic. A coluna da direita mostra que o curso já ensina cada um deles, disperso entre módulos; o vocabulário de arnês é o que permite tratá-los como um sistema único e projetá-los juntos.

| Componente | Pergunta que ele responde | Onde este curso já trata |
|---|---|---|
| *System prompt* | Que caráter, limites e convenções governam toda tarefa? | [Prompt como contrato](../modulo-1-fundamentos/superficie-comportamental.md) e [saída estruturada](ferramentas-e-contratos.md#uso-de-ferramentas-e-saidas-estruturadas) |
| Ferramentas | O que o agente pode fazer, e com que contrato? | [Contrato de ferramenta](ferramentas-e-contratos.md#comece-pelo-contrato-de-ferramenta) |
| Gestão de contexto | O que entra na janela agora, e o que é descartado? | [Estado, memória e contexto](estado-memoria-e-politica.md#estado-memoria-e-contexto) |
| Verificação | Como o agente confere o que fez antes de avançar? | [Fitness functions para autonomia](autonomia-orcada.md#fitness-functions-para-autonomia) e Módulo 6 |
| Memória | O que persiste entre execuções, com que autorização? | [Memória persistente](estado-memoria-e-politica.md#estado-memoria-e-contexto) |
| *Sandbox* | Onde o código roda sem alcançar produção nem dado real? | Oficinas locais e [ambientes](../modulo-7-operacao/pacote-e-promocao.md#ambientes-e-promocao) |
| *Hooks* | Em que ponto do ciclo um controle determinístico intervém? | [Políticas como fronteira executável](estado-memoria-e-politica.md#politicas-como-fronteira-executavel) |

Os dois primeiros itens costumam receber toda a atenção, e são os de menor retorno isolado. O quarto é o de maior retorno comprovado, tema da subseção seguinte.

Vale registrar de onde o vocabulário vem, para não importá-lo sem crítica. Ele nasceu na comunidade de agentes de codificação, onde o arnês é um produto de linha de comando e os componentes têm nomes de arquivo concretos. A Anthropic documenta essa camada de forma explícita em [Steering Claude Code](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more), que separa mecanismos que **guiam** o modelo, como arquivos de contexto e *skills*, de mecanismos que **impõem** comportamento, como *hooks* e permissões, com uma frase que este curso já defende desde o Módulo 1: uma proteção real precisa ser determinística. A generalização para sistemas corporativos é legítima, mas a tradução não é automática: num agente de atendimento, o *sandbox* não é um contêiner de código, é a fronteira entre ferramenta de leitura e ferramenta de escrita.

## Diagnosticar pelo tipo de falha

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

## Mais ferramentas não significa menos erro

A intuição diante de um agente que erra é ampliar sua capacidade. A evidência aponta para o contrário. A Vercel [removeu 80% das ferramentas](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools) de um agente de texto para SQL, trocando dezesseis ferramentas especializadas por acesso a um sistema de arquivos com execução de comandos, e relatou taxa de sucesso subindo de 80% para 100%, com 40% menos *tokens*, 40% menos passos e tempo médio de resposta caindo de 274 para 77 segundos.

A explicação é a mesma do erro composto. Cada ferramenta adicional amplia o espaço de decisão de cada etapa, e ferramentas com fronteiras parecidas criam pontos de decisão ambíguos. A orientação da Anthropic em [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) formula o critério de forma verificável: se uma pessoa da engenharia não consegue dizer com segurança qual ferramenta usar numa situação, não se pode esperar que o modelo decida melhor. O corolário arquitetural é consolidar ferramentas por fluxo de trabalho em vez de espelhar cada endpoint da API, e nomeá-las com prefixos que revelem a fronteira.

Existe um custo simétrico que a lição não deve esconder. Descrições de ferramenta ocupam contexto antes de qualquer requisição: a Anthropic relata, em [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp), um caso em que carregar definições sob demanda em vez de todas de uma vez reduziu o consumo de 150 mil para 2 mil *tokens*. Catálogo mínimo é, ao mesmo tempo, decisão de qualidade e decisão de custo.

Arnês, portanto, não é maximizar capacidade. É otimizar o caminho até o resultado certo, e a operação que mais frequentemente melhora esse caminho é uma remoção.

## O arnês é onde mora a autoridade

Há uma leitura arquitetural que o vocabulário de arnês torna nítida e que fecha esta seção. Tudo o que decide **se** uma ação acontece vive no arnês, não no modelo. O catálogo apresentado ao modelo é interface de descoberta; a política é avaliada no executor; a aprovação vincula pessoa, objeto e prazo; o *hook* interrompe num ponto definido pelo projeto. Quando alguém diz que "o agente decidiu escalar", ou o arnês define esse ponto explicitamente, ou não existe ponto de escalonamento e sim uma coincidência.

Isso também delimita o que um bom arnês não faz. Ele reduz a probabilidade de erro e limita o raio de impacto; não torna segura uma ação irreversível, não substitui aceitação de risco residual com dono nomeado e não produz autorização. As [fronteiras de componente](estado-memoria-e-politica.md#responsabilidades-e-fronteiras-de-componente) da próxima seção são a forma concreta de manter essa separação quando o arnês cresce.
