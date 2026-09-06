# Integração e resiliência

A partir do momento em que existe efeito sobre um sistema real, identidade, idempotência, tempo limite e compensação deixam de ser detalhe de implementação.

## Identidade do usuário e autorização delegada

A ação precisa preservar **identidade do usuário**, aplicação, executor e aprovador. Evite uma conta técnica onipotente apresentada ao modelo. Na **autorização delegada**, a aplicação recebe autoridade limitada para agir em nome do usuário, com escopos reduzidos, recurso, finalidade e duração. Tokens e segredos ficam no executor, nunca no contexto do modelo.

Em cada chamada:

1. autentique usuário e serviço;
2. derive um token delegado de curta duração ou decisão equivalente;
3. reduza escopo à ferramenta e ao recurso;
4. avalie política com identidade, risco, parâmetros, estado e consentimento;
5. execute usando credencial fora do prompt;
6. registre ator, sujeito, delegador, aprovador, política e resultado.

Revalide na execução, não apenas quando o plano foi criado. Uma permissão pode ser revogada durante espera por aprovação. Delegação não transfere responsabilidade para o modelo; torna a cadeia explícita e revogável.

## Idempotência, concorrência e prevenção de repetição

**Idempotência** faz repetições equivalentes produzirem um único efeito lógico. O orquestrador gera uma chave estável a partir da execução e da intenção de ação, persiste-a antes da chamada e reutiliza-a em retry. O sistema de destino armazena chave e resultado. Não crie nova chave a cada tentativa.

Idempotência não resolve tudo. Para atualizar um pedido, envie a versão observada (`if-match` ou precondição) para detectar concorrência. Para impedir loops, registre uma assinatura de ferramenta, argumentos canônicos e versão de estado. Se a mesma chamada já concluiu, devolva o resultado persistido; se está em andamento, aguarde ou reconcilie; se falhou definitivamente, não repita por reformulação textual.

## Timeout, retry e circuit breaker

Todo limite local deve caber no **orçamento de tempo** da execução. Um **timeout** encerra a espera, não prova que o destino não executou. Após timeout de escrita, consulte por chave de idempotência antes de tentar novamente.

**Retry** é apropriado para falhas transitórias e operações idempotentes, com número limitado, backoff e jitter. Erro de validação, autorização, conflito de negócio ou saldo insuficiente é definitivo até mudança de estado; repetir consome custo e pode amplificar incidente.

O **circuit breaker** abre após padrão de falhas, evita pressão sobre uma dependência degradada e testa recuperação de forma controlada. Quando aberto, o agente não procura um endpoint equivalente para contornar a proteção. Ele usa fallback aprovado, pausa ou encaminha.

## Consistência, transações e compensação

Uma trajetória entre CRM, estoque e pedidos raramente participa de transação ACID única. Modele uma saga: cada efeito local confirma e produz estado durável; falhas posteriores acionam **compensação** na ordem apropriada. Liberar uma reserva pode compensar a criação da reserva. Não é “rollback” perfeito: uma mensagem enviada ou produto despachado pode ser irreversível. Nesses casos, compense por neutralização, correção ou processo humano e registre efeito residual.

Defina precondição e compensação antes de oferecer uma ferramenta de escrita. A compensação tem contrato, autorização, idempotência, timeout e observabilidade próprios. Se ela falhar, a execução entra em `compensation_pending`, alerta operações e não é marcada como resolvida.

## Auditoria e observabilidade

**Auditoria** preserva evidência de responsabilidade; **observabilidade** ajuda a entender comportamento e saúde. Um trace correlaciona solicitação, versões de modelo/prompt/política, catálogo oferecido, saída estruturada, validações, decisão de autorização, aprovação, chamada, tentativas, resultado, custo e compensação. Registre parâmetros minimizados ou hashes quando o conteúdo for sensível.

As [convenções semânticas de IA generativa do OpenTelemetry](https://github.com/open-telemetry/semantic-conventions-genai) são uma referência oficial para telemetria. Padronizar nomes não autoriza copiar prompts e dados pessoais. Retenção, acesso e mascaramento continuam sob política.
