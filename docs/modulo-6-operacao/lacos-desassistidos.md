# Operação de loops

Quando a unidade operada deixa de ser a solicitação e passa a ser o laço, o gargalo não é o modelo: é o verificador.

## Loop desassistido: o verificador é o gargalo

O Módulo 4 apresentou a [escada de quatro níveis de loop](../modulo-4-agentes/loops.md#quatro-niveis-de-loop) e o critério de subida. Do terceiro degrau em diante não há pessoa presente no momento do disparo, e a unidade operada deixa de ser a solicitação: passa a ser o **laço**. Isso muda o que precisa ser versionado, medido e interrompido.

Um laço acrescenta cinco itens à lista de ativos comportamentais desta página: o *prompt* que ele reinjeta, a **condição de parada**, o **orçamento** de iterações e de custo, o **verificador** e o gatilho que o aciona. Nenhum deles é parâmetro de execução. Mudar a condição de parada altera o comportamento do sistema tanto quanto trocar o modelo, e mudar o verificador invalida retroativamente a evidência das execuções anteriores, porque "passou" passa a significar outra coisa. O manifesto de uma liberação que inclui laço precisa registrar os cinco, ou a execução não é reconstruível.

O gargalo de um laço desassistido não é o modelo, é o verificador. Enquanto uma pessoa está presente, ela é o verificador implícito de última instância: lê a saída, percebe o disparate e interrompe. Ao remover a pessoa, essa função precisa existir em outro lugar, escrita e executável. Se ela não existir, o laço não vira automação, vira consumo de orçamento sem condição de término, e o pior desfecho não é a fatura: é o **falso positivo**, quando o sistema declara conclusão, encerra e ninguém confere.

### Modos de falha próprios de laço

| Modo de falha | Sintoma observável | Controle no arnês |
|---|---|---|
| Falso positivo de conclusão | laço encerra com sucesso declarado e o artefato não satisfaz o critério | condição de parada externa ao modelo, conferida por comando determinístico |
| Estagnação | duas ou mais iterações com resultado de verificação idêntico | detecção de repetição que aciona diversificação, escalonamento ou interrupção |
| Convergência para a métrica | o critério passa e o requisito continua descumprido | conjunto de verificação revisado por pessoa, com casos que o laço não pode editar |
| Efeito duplicado | a mesma ação externa acontece duas vezes entre iterações | chave de idempotência por objetivo, não por iteração |
| Deriva do gatilho | o laço continua disparando depois que a condição que o justificava sumiu | prazo de validade do agendamento e reconciliação periódica com o dono |
| Consumo silencioso | custo cresce sem resultado correspondente | orçamento com teto rígido e alerta em custo por resultado, não em custo total |

A convergência para a métrica merece destaque, porque é a falha que a instrumentação não pega. Um laço que otimiza contra um conjunto de testes tende a satisfazer exatamente aquele conjunto, e um agente com permissão de escrita sobre o próprio verificador transforma a condição de parada em variável de folga. A regra prática é simples de enunciar e precisa ser aplicada com rigor: **o laço não escreve o verificador**. Quando o mesmo processo produz o artefato e o critério que o aprova, não existe verificação, existe autoavaliação.

### Medir um laço

Os [quatro planos de métricas](observabilidade.md#quatro-planos-de-metricas) continuam valendo, com leituras específicas. No plano de operação, iterações por objetivo, *tokens* por objetivo e proporção de execuções que terminam por esgotamento de orçamento são os sinais primários; custo total isolado engana, porque um laço barato que nunca converge é pior que um caro que converge. No plano de produto, a taxa de objetivos concluídos sem intervenção humana é o indicador que justifica o degrau em que o laço opera. No plano de modelo, a taxa de falso positivo do verificador é o número que decide se é seguro subir de degrau.

Duas execuções de um mesmo laço com a mesma entrada não produzem necessariamente o mesmo número de iterações nem o mesmo custo. Isso não é defeito de instrumentação, é a natureza do objeto: a [reprodutibilidade possível](pacote-e-promocao.md#reprodutibilidade-sem-promessa-impossivel) aqui é sobre configuração, decisões e critérios, não sobre trajetória idêntica. A consequência de planejamento é que orçamento de laço se dimensiona por distribuição observada, com percentil, e não por média.

### O que permanece humano num laço

Três coisas não descem para o laço, mesmo no quarto degrau. A **definição do critério de sucesso**, porque é ela que codifica a intenção. A **aceitação do risco residual** de um laço rodar sem supervisão, que é decisão de governança com dono nomeado. E o **desligamento**, que precisa ser acessível a quem está de plantão, não só a quem escreveu o laço. Um laço cujo desligamento depende de conhecimento não documentado é um risco operacional independentemente da qualidade do verificador.

## Portões de um loop autônomo

Um laço que roda sem pessoa presente atravessa os mesmos portões de qualquer pacote comportamental, e mais quatro específicos. Eles são cumulativos: nenhum substitui o anterior.

**Portão de critério.** A condição de parada existe, é executável por comando determinístico e está versionada junto ao pacote. O portão verifica também o negativo: existe pelo menos um caso conhecido em que a condição de parada **não** é satisfeita, comprovando que ela discrimina. Uma condição que nunca reprova não é critério, é decoração.

**Portão de orçamento.** Existem dois tetos independentes, iterações e custo, cada um com dono e com comportamento definido no esgotamento. O portão rejeita o pacote se o comportamento no esgotamento for "encerrar em silêncio". O desfecho mínimo aceitável é registrar o que foi tentado, o que bloqueou e qual é o estado do artefato, e encaminhar a uma pessoa.

**Portão de isolamento.** O laço executa com identidade própria, escopo menor que o de qualquer pessoa, credenciais de prazo curto e um ambiente sem alcance a produção nem a dado real enquanto a natureza do efeito não estiver classificada. Ferramentas de escrita entram por último e uma de cada vez, na ordem da [matriz de autonomia](../modulo-4-agentes/autonomia-orcada.md#matriz-de-autonomia).

**Portão de interrupção.** Existe um desligamento acessível fora do processo do laço, documentado em *runbook*, testado no ensaio e conhecido por quem está de plantão. O portão inclui o teste: interromper o laço no meio de uma iteração não pode deixar efeito parcial sem compensação nem estado que impeça a retomada.

### Verificação independente

O melhor verificador de um laço é determinístico. Quando o critério é difuso e a única opção é um segundo modelo como avaliador, três condições reduzem o risco de conluio. O avaliador roda com **contexto limpo**, sem o histórico de raciocínio de quem produziu o artefato, o que a Anthropic recomenda em [Getting started with loops](https://claude.com/blog/getting-started-with-loops) ao tratar revisão por segundo agente: um revisor com contexto novo é menos enviesado porque não foi influenciado pelo raciocínio do agente principal. O avaliador é **versionado e calibrado** contra julgamento humano, como qualquer avaliador do Módulo 5. E o avaliador **não é editável pelo laço**, o que na prática significa repositório, permissão e trilha separados.

Essa combinação tem consequência de custo. Um laço com verificação independente executa pelo menos duas inferências por iteração, e o desenho econômico razoável usa um verificador barato para o filtro grosso e reserva o caro para a decisão de encerramento.

### Fitness functions de operação de laço

- todo laço em execução tem, no catálogo, dono, gatilho, condição de parada, tetos e procedimento de desligamento;
- nenhum laço possui permissão de escrita sobre o artefato que define seu próprio critério de sucesso;
- toda execução registra `release_id`, condição de parada declarada, condição que encerrou, iterações e custo;
- laços que terminam por esgotamento de orçamento acima de um limiar por janela abrem revisão do critério, não aumento do teto;
- o procedimento de desligamento é ensaiado na mesma cadência do ensaio de rollback, com resultado registrado.

Falha em qualquer uma dessas verificações rebaixa o laço para o degrau anterior da escada até a correção. Rebaixar é uma ação operacional normal, e deve ser mais fácil de executar do que promover.
