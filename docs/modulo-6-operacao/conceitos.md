# Conceitos: comportamento operável e evidência contínua

![Ciclo: pacote comportamental passa por avaliação, promoção, entrega, observabilidade e aprendizado; métricas, privacidade e SLO atravessam-no](../assets/images/m06-mapa-operacao-evidencia-continua.png "Mapa da operação e evidência contínua")

*Figura — Operar IA requer evidência contínua.*

## O objeto operado é um pacote comportamental

Em IA generativa, a unidade de mudança excede a versão do código. Chamaremos de **ativo comportamental** qualquer artefato cuja alteração possa mudar resposta, decisão, custo, latência, acesso ou efeito: modelo e revisão do provedor; parâmetros de inferência; prompt e exemplos; política e guardrails; corpus, permissões e snapshot do índice; modelo de embedding e estratégia de recuperação; esquemas e versões de ferramentas; memória; código de orquestração; critérios de avaliação, avaliadores e conjuntos de referência; dependências e configuração de infraestrutura.

O manifesto de uma liberação registra versões, proprietário, finalidade, evidências, aprovação e compatibilidade. “Versão 2 do chatbot” não basta se ela não permite descobrir qual índice, modelo e política estavam ativos. Hashes ajudam a verificar integridade, mas precisam de metadados compreensíveis. Para provedores sem revisão fixável, registre identificador, região, data, parâmetros e testes sentinela: a variação é risco explícito.

## Ambientes e promoção

**Desenvolvimento** favorece velocidade e diagnóstico. Usa dados sintéticos ou minimizados, modelos econômicos quando adequados e credenciais sem efeito real. Ainda precisa reproduzir contratos essenciais: schemas, filtros de autorização e limites não podem existir apenas em produção.

**Homologação** aproxima topologia, identidade, políticas, cotas e dependências da produção. Executa conjunto de referência, testes adversariais, carga, recuperação e simulações de falha. Dados reais só entram com finalidade, minimização e acesso aprovados. A homologação não prova que produção será igual; ela reduz diferenças conhecidas e torna diferenças restantes visíveis.

**Produção** atende usuários e efeitos reais com acesso mínimo, telemetria, SLOs, alertas, runbooks e mudança controlada. Ambientes devem separar identidades, segredos, índices, quotas e trilhas. Copiar conversas ou credenciais de produção para desenvolvimento destrói a fronteira. Configuração comum pode ser promovida como artefato; segredo e dado sensível são fornecidos pelo ambiente.

A promoção segue o mesmo manifesto entre ambientes. Exceções emergenciais ficam registradas e depois reconciliadas com a fonte versionada. Se alguém “corrige o prompt direto” no console do fornecedor, cria divergência impossível de reproduzir e uma mudança fora dos portões.

## Reprodutibilidade sem promessa impossível

**Reprodutibilidade** significa reconstruir configuração, entradas, decisões observáveis e condições suficientes para comparar o comportamento. Ela não promete texto idêntico: amostragem, paralelismo, hardware e mudanças invisíveis do provedor podem gerar variação. Quando houver seed e inferência determinística, registre-as; quando não houver, execute repetições e compare distribuições, critérios e intervalos.

Um registro mínimo por execução liga `release_id`, modelo, parâmetros, prompt, política, snapshot de recuperação, contratos de ferramenta, identidade autorizada pseudonimizada, decisões de roteamento e resultado. O replay deve evitar repetir efeitos: ferramentas de escrita são substituídas por simuladores ou respostas capturadas, e dados que não podem ser retidos são representados por evidência mínima. Reproduzir não autoriza reprocessar dados para outra finalidade.

## Avaliação contínua e entrega controlada

**Avaliação contínua** reutiliza o framework do Módulo 5 ao longo do ciclo. Antes da integração, testes locais verificam schemas e regras determinísticas. No pull request, um subconjunto rápido detecta regressões conhecidas. Na homologação, o conjunto completo mede factualidade, relevância, fundamentação, segurança, utilidade, latência e custo por fatia. Em produção, canary e amostragem detectam mudança de distribuição, novas intenções e falhas de componentes. Periodicamente, casos de incidentes e feedback autorizado voltam ao conjunto.

Um resultado não passa apenas porque a média subiu. Critérios intoleráveis — vazamento, ação sem autorização, ausência de escalonamento obrigatório — bloqueiam. Métricas negociáveis usam faixa, orçamento e comparação com a versão vigente. Mudança no avaliador também é versão comportamental: deve ser calibrada contra julgamento humano e não pode redefinir retroativamente o sucesso sem explicação.

**Entrega controlada** transforma evidência em exposição gradual. O pacote aprovado entra em canary para uma parcela delimitada, com critérios de continuação e interrupção definidos antes. Só então amplia. Liberação e mudança de configuração compartilham trilha. A velocidade sustentável vem de automatizar evidências repetíveis, não de dispensar decisão.

## Loop desassistido: o verificador é o gargalo

O Módulo 4 apresentou a [escada de quatro níveis de loop](../modulo-4-agentes/conceitos.md#quatro-niveis-de-loop) e o critério de subida. Do terceiro degrau em diante não há pessoa presente no momento do disparo, e a unidade operada deixa de ser a solicitação: passa a ser o **laço**. Isso muda o que precisa ser versionado, medido e interrompido.

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

Os [quatro planos de métricas](#quatro-planos-de-metricas) continuam valendo, com leituras específicas. No plano de operação, iterações por objetivo, *tokens* por objetivo e proporção de execuções que terminam por esgotamento de orçamento são os sinais primários; custo total isolado engana, porque um laço barato que nunca converge é pior que um caro que converge. No plano de produto, a taxa de objetivos concluídos sem intervenção humana é o indicador que justifica o degrau em que o laço opera. No plano de modelo, a taxa de falso positivo do verificador é o número que decide se é seguro subir de degrau.

Duas execuções de um mesmo laço com a mesma entrada não produzem necessariamente o mesmo número de iterações nem o mesmo custo. Isso não é defeito de instrumentação, é a natureza do objeto: a [reprodutibilidade possível](#reprodutibilidade-sem-promessa-impossivel) aqui é sobre configuração, decisões e critérios, não sobre trajetória idêntica. A consequência de planejamento é que orçamento de laço se dimensiona por distribuição observada, com percentil, e não por média.

### O que permanece humano num laço

Três coisas não descem para o laço, mesmo no quarto degrau. A **definição do critério de sucesso**, porque é ela que codifica a intenção. A **aceitação do risco residual** de um laço rodar sem supervisão, que é decisão de governança com dono nomeado. E o **desligamento**, que precisa ser acessível a quem está de plantão, não só a quem escreveu o laço. Um laço cujo desligamento depende de conhecimento não documentado é um risco operacional independentemente da qualidade do verificador.

## Trace: reconstruir a composição

Um trace distribuído conecta a solicitação às etapas de **prompt**, **contexto**, **recuperação**, **ferramenta** e **resposta**. Cada span registra tempo, resultado, versão, política aplicada e relação causal. Por padrão, o span de recuperação registra classificação, tamanho, identificador controlado ou hash e metadados de recuperação: índice, filtros de autorização, quantidade, latência e identificadores controlados dos documentos. A consulta derivada em texto bruto só pode aparecer em amostra explicitamente autorizada, segregada e com retenção limitada; não pertence à telemetria operacional padrão. O span de ferramenta registra contrato, operação, decisão de política, idempotência e status; o de resposta registra validações e rota de entrega.

As [convenções semânticas do OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/) oferecem um vocabulário oficial em evolução. As convenções específicas de GenAI são **prática viva**: campos e estabilidade mudam, portanto a organização deve fixar a versão adotada, mapear seu schema interno e revisar migrações. Adotar uma convenção melhora correlação; não define sozinho o que é seguro registrar.

**LiteLLM Proxy** concentra rotas; **OpenTelemetry** transporta telemetria. Ambos exigem identidade, minimização e retenção; gateway não é controle de domínio.

Trace não deve guardar cadeia de pensamento privada como explicação. Registre entradas autorizadas, evidências, decisões externas e saídas necessárias. Justificativas de política vêm de regras auditáveis; texto do modelo sobre seu “raciocínio” não é prova causal.

## Quatro planos de métricas

Métricas formam uma cadeia de hipóteses, não um placar único:

| Plano | Perguntas e exemplos | Decisão possível |
|---|---|---|
| **produto** | tarefa concluída, abandono, reconsulta, aceitação, escalonamento, feedback por jornada | corrigir experiência, escopo ou fluxo |
| **modelo** | factualidade, fundamentação, recusa adequada, aderência a schema, segurança por fatia | trocar prompt, modelo, contexto ou avaliador |
| **operação** | disponibilidade, **latência**, **tokens**, **erros**, saturação, filas, retries, **custo** | escalar, conter, rotear, degradar ou reverter |
| **negócio** | tempo poupado validado, resolução, receita, perda evitada, satisfação, risco e custo por resultado | ampliar, redesenhar ou encerrar o caso |

Correlação não prova causa. Mais tokens podem acompanhar melhor resolução porque casos difíceis são longos. Um experimento controlado, com guardrails equivalentes, é necessário para inferir contribuição. Métrica de negócio também precisa de contrafactual: “10 mil respostas” mede atividade, não valor.

## Prioridades e tensões operacionais

| Característica | Prioridade | Tensão aceita | Medida e responsável |
|---|---|---|---|
| Segurança, privacidade e autorização | Não negociável | bloqueio e segregação podem reduzir disponibilidade | acesso indevido ou ação sem política: zero; Segurança e Privacidade |
| Confiabilidade e recuperação | Alta | redundância, ensaios e reconciliação aumentam custo e operação | recuperação dentro da janela e efeitos duplicados: zero; Operação e Plataforma |
| Auditabilidade | Alta | traces preservam metadados sob retenção limitada | execução crítica reconstruível por `release_id`; Auditoria e Operação |
| Latência, custo e utilidade | Importante | orçamento e degradação podem encaminhar ou limitar jornadas | p95, custo por resultado e abandono por rota; Produto e FinOps |
| Modificabilidade e portabilidade | Importante | adaptadores, contratos e regressão elevam complexidade | mudança localizada e ensaio de saída; Arquitetura e Plataforma |

Operação sustentável atende a essas prioridades no cenário. Não maximiza simultaneamente disponibilidade, autonomia, coleta de telemetria, velocidade de mudança e opcionalidade.

## Logs com preservação de privacidade

**Logs com preservação de privacidade** aplicam minimização antes da coleta. Por padrão, registre identificadores pseudonimizados, tamanhos, versões, categorias, hashes controlados, decisões e métricas. Mascare campos sensíveis antes do coletor; separe telemetria operacional de conteúdo para avaliação; criptografe e controle acesso; defina retenção por classe; audite consultas; descarte também exportações e backups.

Amostras de prompt ou resposta exigem base, finalidade, seleção, acesso e prazo explícitos. Sampling deve ser estratificado para não esconder grupos raros, mas nenhum objetivo analítico justifica coletar indiscriminadamente. Hashes de texto previsível podem permitir reidentificação; use técnicas e chaves adequadas ao risco. Em incidente, acesso excepcional tem aprovação e trilha.

## SLO para serviço útil

Um **SLO** define uma meta sobre um indicador de nível de serviço em uma janela. O capítulo oficial de [SLOs do livro de SRE do Google](https://sre.google/sre-book/service-level-objectives/) orienta selecionar poucos indicadores relevantes ao usuário. Para IA generativa, disponibilidade HTTP é necessária, porém insuficiente: uma resposta 200 sem fonte ou uma ação duplicada não é sucesso.

Exemplos: “99% das consultas elegíveis em 28 dias recebem resposta validada em até 8 segundos”; “99,9% das ações confirmadas não produzem duplicidade”; “95% das respostas amostradas sobre políticas vigentes atingem fundamentação 3 ou 4”. O primeiro pode ser observado continuamente; o terceiro depende de amostragem e julgamento, portanto deve declarar atraso e incerteza.

O orçamento de erro orienta ritmo de mudança, mas não compra permissão para eventos intoleráveis. Vazamento de dado sensível ou ação fora de autoridade aciona incidente mesmo se a média do SLO estiver dentro da meta. SLO, guardrail e risco residual são instrumentos complementares.

## Ferramentas no mercado

Veja comparações no [Guia de ferramentas](../referencia/guia-de-ferramentas.md).

| Ferramenta | Quando ajuda | Pré-requisito | Limite arquitetural |
|---|---|---|---|
| LiteLLM Proxy | Centralizar rotas e limites. | Provedores, identidade, segredos e fallback. | Não remove custo ou valida produto. |
| OpenTelemetry | Correlacionar sinais. | Convenções, coletor e retenção. | Não substitui investigação. |
| Langfuse | Acompanhar liberação. | Instrumentação e acesso controlado. | Não define SLO ou incidente. |

Com o ciclo definido, avance para [Padrões e decisões](padroes-e-decisoes.md).
