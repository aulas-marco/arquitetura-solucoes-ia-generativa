# Padrões e decisões: integração, autonomia e recuperação

## Comece pelo contrato de ferramenta

Um **contrato de ferramenta** transforma uma capacidade corporativa em operação estreita, validável e auditável. “Acesso ao sistema de pedidos” é amplo demais. Prefira operações como `consultar_pedido`, `reservar_item` e `solicitar_cancelamento`, cada uma com efeito e política próprios.

O contrato mínimo declara:

| Campo | Pergunta que responde |
|---|---|
| nome, versão e finalidade | que capacidade está sendo invocada e por quê? |
| classe de efeito | é leitura, proposta, escrita reversível ou efeito irreversível? |
| esquema de entrada | tipos, obrigatoriedade, limites, enumerações e identificadores aceitos? |
| esquema de saída | dados, proveniência, versão do recurso e indicador de conclusão? |
| erros tipados | inválido, não autorizado, conflito, não encontrado, transitório ou definitivo? |
| identidade e autorização | quem age em nome de quem, com quais escopos e política? |
| idempotência e concorrência | qual chave evita duplicação e qual versão/precondição evita sobrescrita? |
| timeout e retry | quando desistir e quais erros permitem nova tentativa? |
| dados e auditoria | quais campos são sensíveis, mascarados, retidos e correlacionados? |
| compensação | como desfazer ou neutralizar o efeito, e quando isso é impossível? |

Descrições para o modelo incluem uso e não uso, mas o executor aplica as regras. O [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-11-25) oferece uma especificação oficial de interoperabilidade entre aplicações e servidores que expõem contexto e ferramentas. Um protocolo padroniza comunicação; não decide política corporativa, semântica de transação ou adequação da ferramenta.

## APIs, mensageria, eventos e adaptadores

Use **API síncrona** quando o agente precisa do resultado para escolher o próximo passo e a dependência responde dentro do orçamento. O contrato deve definir timeout menor que o prazo total, erros e correlação. Não mantenha uma interação bloqueada indefinidamente.

Use **mensageria** para comandos assíncronos, filas de trabalho e absorção de picos. O envio aceito não significa efeito concluído. Estado precisa distinguir `solicitado`, `aceito`, `processando`, `concluído` e `falhou`; uma resposta posterior correlaciona `execution_id` e `command_id`.

Use **eventos** para comunicar fatos ocorridos — `ReservaExpirada`, não “talvez reserve”. Consumidores assumem entrega pelo menos uma vez, ordenação limitada e evolução de esquema. Deduplicação é responsabilidade do consumidor. Evento não deve carregar dado sensível além do necessário.

Um **adaptador** protege o domínio de protocolos legados, campos instáveis e códigos opacos. Traduz contrato canônico para SOAP, arquivo, terminal ou API antiga; normaliza erros; aplica timeout; correlaciona chamadas; e impede que peculiaridades do legado entrem no prompt. Quando o legado não oferece idempotência, o adaptador pode usar registro transacional próprio, consulta de reconciliação e chave de negócio — ou classificar a ação como não repetível e exigir intervenção.

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

## Matriz de autonomia

Autonomia é atribuída por **ação e cenário**, não por produto inteiro. Os níveis abaixo não são uma escada obrigatória:

| Nível | Escolha do modelo | Efeito | Controle humano | Exemplo |
|---|---|---|---|---|
| A0 — sem autonomia | nenhuma | regra executa fluxo conhecido | responsável define processo | cálculo e consulta determinística |
| A1 — informar | gera resposta, sem ferramenta de efeito | nenhum | usuário interpreta | chatbot de políticas |
| A2 — recomendar | escolhe proposta ou ferramenta de leitura | pessoa executa | revisão antes de qualquer efeito | copiloto sugere troca |
| A3 — agir reversivelmente | escolhe leitura e escrita de baixo risco | reversível e limitada | aviso/contestação; amostra depois | criar reserva temporária |
| A4 — agir com aprovação | propõe ação material e aguarda | efeito após aprovação antes da ação | aprovador recebe evidência, parâmetros e prazo | cancelar pedido elegível |
| A5 — autonomia limitada | escolhe sequência e ações aprovadas por classe | efeitos dentro de limites estreitos | monitoramento e revisão humana depois da ação | ajuste operacional de baixo valor |

**Aprovação humana antes da ação** precisa ocorrer sobre objeto imutável: ferramenta, parâmetros, evidência, consequência, prazo e chave. Alterar parâmetros invalida aprovação. Aprovar “faça o necessário” não é controle.

**Revisão humana depois da ação** detecta desvio, corrige política e permite recurso; não retroativamente autoriza dano. Só serve quando o efeito é aceitável, reversível ou de baixo risco. Amostragem, alertas e prazo de contestação devem ser definidos. Ação crítica continua exigindo aprovação prévia, como pede o cenário de [Autonomia](../referencia/atributos-de-qualidade.md#autonomia).

## Orçamentos, interrupção e fallback

Um agente recebe **orçamento de etapas**, **orçamento de tempo** e **orçamento de custo**, além de limites de tokens, chamadas e ações de efeito. O contador é externo ao modelo e inclui retries, handoffs e compensações. Limites diferentes podem valer por classe de tarefa. Ao se aproximar do teto, o sistema resume estado, evita nova ação material e escolhe conclusão parcial, solicitação de dado, pausa ou escalonamento.

O fallback para **workflow determinístico** é uma rota projetada: por exemplo, coletar pedido e motivo, validar regras conhecidas e abrir tarefa humana. Não entregue silenciosamente a mesma ação a um modelo mais barato ou ferramenta alternativa com política diferente. Fallback preserva identidade, estado, idempotência e informação clara sobre o que não foi concluído.

## Agente único versus múltiplos agentes

Comece com agente único e ferramentas estreitas. Adote múltiplos agentes apenas se um experimento demonstrar benefício de especialização, isolamento de contexto/autoridade ou paralelismo. Compare taxa de conclusão, ações indevidas, handoffs, latência, custo e capacidade de reconstruir traces. Um supervisor não elimina falha: precisa de contrato de delegação, orçamento global, regra de consenso e autoridade para interromper. Nunca permita que subagentes ampliem escopo, criem credenciais ou deleguem indefinidamente.

Esses mecanismos aparecem juntos no [Exemplo arquitetural](exemplo-arquitetural.md).

## Padrão — Desenvolvimento guiado por especificação

**Contexto.** Um agente de codificação pode alterar múltiplos artefatos e executar ferramentas rapidamente.

**Problema.** Pedidos vagos transformam implementação em interpretação silenciosa; testes podem passar sem atender à necessidade original.

**Solução.** Manter constitution, spec, plan e tasks como contratos explícitos. Implementar em fatias verificáveis, testar nas interfaces acordadas e revisar separadamente padrões do repositório e aderência à spec.

**Consequências.** Há mais preparação e gates, mas decisões, critérios de aceite e riscos permanecem auditáveis. O modelo ganha autonomia limitada para implementar; não ganha autoridade para redefinir o objetivo.

> **Decisão arquitetural:** posicione gates humanos após a specification, após verify e antes da liberação. Um gate deve receber artefatos imutáveis, evidência de testes e o diff correspondente.
