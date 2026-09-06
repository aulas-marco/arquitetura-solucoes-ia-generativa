# Observabilidade e métricas

Relacionar as fases de uma solicitação, escolher o que registrar sem acumular dado sensível e transformar sinal em objetivo de serviço.

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

## Logs com preservação de privacidade

**Logs com preservação de privacidade** aplicam minimização antes da coleta. Por padrão, registre identificadores pseudonimizados, tamanhos, versões, categorias, hashes controlados, decisões e métricas. Mascare campos sensíveis antes do coletor; separe telemetria operacional de conteúdo para avaliação; criptografe e controle acesso; defina retenção por classe; audite consultas; descarte também exportações e backups.

Amostras de prompt ou resposta exigem base, finalidade, seleção, acesso e prazo explícitos. Sampling deve ser estratificado para não esconder grupos raros, mas nenhum objetivo analítico justifica coletar indiscriminadamente. Hashes de texto previsível podem permitir reidentificação; use técnicas e chaves adequadas ao risco. Em incidente, acesso excepcional tem aprovação e trilha.

## SLO para serviço útil

Um **SLO** define uma meta sobre um indicador de nível de serviço em uma janela. O capítulo oficial de [SLOs do livro de SRE do Google](https://sre.google/sre-book/service-level-objectives/) orienta selecionar poucos indicadores relevantes ao usuário. Para IA generativa, disponibilidade HTTP é necessária, porém insuficiente: uma resposta 200 sem fonte ou uma ação duplicada não é sucesso.

Exemplos: “99% das consultas elegíveis em 28 dias recebem resposta validada em até 8 segundos”; “99,9% das ações confirmadas não produzem duplicidade”; “95% das respostas amostradas sobre políticas vigentes atingem fundamentação 3 ou 4”. O primeiro pode ser observado continuamente; o terceiro depende de amostragem e julgamento, portanto deve declarar atraso e incerteza.

O orçamento de erro orienta ritmo de mudança, mas não compra permissão para eventos intoleráveis. Vazamento de dado sensível ou ação fora de autoridade aciona incidente mesmo se a média do SLO estiver dentro da meta. SLO, guardrail e risco residual são instrumentos complementares.
