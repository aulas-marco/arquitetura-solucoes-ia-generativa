# Conceitos: comportamento operável e evidência contínua

## O objeto operado é um pacote comportamental

Em software convencional, uma versão do código costuma identificar grande parte do comportamento. Em uma solução generativa, a unidade de mudança é maior. Chamaremos de **ativo comportamental** qualquer artefato cuja alteração possa mudar resposta, decisão, custo, latência, acesso ou efeito: modelo e revisão do provedor; parâmetros de inferência; prompt e exemplos; política e guardrails; corpus, permissões e snapshot do índice; modelo de embedding e estratégia de recuperação; esquemas e versões de ferramentas; memória; código de orquestração; rubricas, avaliadores e conjuntos de referência; dependências e configuração de infraestrutura.

O manifesto de uma liberação relaciona versões imutáveis desses ativos, proprietário, finalidade, data, evidências, aprovação e compatibilidade. “Versão 2 do chatbot” não basta se ela não permite descobrir qual índice, modelo e política estavam ativos. Hashes ajudam a verificar integridade, mas precisam de metadados compreensíveis. Para serviços externos que não permitem fixar uma revisão, registre o identificador declarado, região, data, parâmetros e resultado de testes sentinela; a incapacidade de fixação é risco explícito.

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

## Trace: reconstruir a composição

Um trace distribuído conecta a solicitação às etapas de **prompt**, **contexto**, **recuperação**, **ferramenta** e **resposta**. Cada span registra tempo, resultado, versão, política aplicada e relação causal. Por padrão, o span de recuperação registra classificação, tamanho, identificador controlado ou hash e metadados de recuperação: índice, filtros de autorização, quantidade, latência e identificadores controlados dos documentos. A consulta derivada em texto bruto só pode aparecer em amostra explicitamente autorizada, segregada e com retenção limitada; não pertence à telemetria operacional padrão. O span de ferramenta registra contrato, operação, decisão de política, idempotência e status; o de resposta registra validações e rota de entrega.

As [convenções semânticas do OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/) oferecem um vocabulário oficial em evolução. As convenções específicas de GenAI são **prática viva**: campos e estabilidade mudam, portanto a organização deve fixar a versão adotada, mapear seu schema interno e revisar migrações. Adotar uma convenção melhora correlação; não define sozinho o que é seguro registrar.

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

## Logs com preservação de privacidade

**Logs com preservação de privacidade** aplicam minimização antes da coleta. Por padrão, registre identificadores pseudonimizados, tamanhos, versões, categorias, hashes controlados, decisões e métricas. Mascare campos sensíveis antes do coletor; separe telemetria operacional de conteúdo para avaliação; criptografe e controle acesso; defina retenção por classe; audite consultas; descarte também exportações e backups.

Amostras de prompt ou resposta exigem base, finalidade, seleção, acesso e prazo explícitos. Sampling deve ser estratificado para não esconder grupos raros, mas nenhum objetivo analítico justifica coletar indiscriminadamente. Hashes de texto previsível podem permitir reidentificação; use técnicas e chaves adequadas ao risco. Em incidente, acesso excepcional tem aprovação e trilha.

## SLO para serviço útil

Um **SLO** define uma meta sobre um indicador de nível de serviço em uma janela. O capítulo oficial de [SLOs do livro de SRE do Google](https://sre.google/sre-book/service-level-objectives/) orienta selecionar poucos indicadores relevantes ao usuário. Para IA generativa, disponibilidade HTTP é necessária, porém insuficiente: uma resposta 200 sem fonte ou uma ação duplicada não é sucesso.

Exemplos: “99% das consultas elegíveis em 28 dias recebem resposta validada em até 8 segundos”; “99,9% das ações confirmadas não produzem duplicidade”; “95% das respostas amostradas sobre políticas vigentes atingem fundamentação 3 ou 4”. O primeiro pode ser observado continuamente; o terceiro depende de amostragem e julgamento, portanto deve declarar atraso e incerteza.

O orçamento de erro orienta ritmo de mudança, mas não compra permissão para eventos intoleráveis. Vazamento de dado sensível ou ação fora de autoridade aciona incidente mesmo se a média do SLO estiver dentro da meta. SLO, guardrail e risco residual são instrumentos complementares.

Com o ciclo definido, avance para [Padrões e decisões](padroes-e-decisoes.md).
