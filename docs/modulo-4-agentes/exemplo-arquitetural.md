# Exemplo arquitetural: agente de atendimento com CRM e pedidos

## Cenário e limites

Um cliente autenticado pede: “troque o item P10 pelo P20 no pedido 845 e mantenha a data”. O sistema pode consultar cadastro e pedido, verificar elegibilidade, criar reserva temporária e propor a alteração. O cancelamento do item original exige confirmação do cliente; diferença acima de R$ 200 exige supervisor. O agente não muda endereço, concede crédito, escolhe credenciais nem ignora política.

O objetivo não é mostrar uma biblioteca específica. É localizar decisões probabilísticas dentro de uma malha determinística de identidade, contratos, política, estado, aprovação e recuperação.

![O agente propõe ferramentas de um catálogo mínimo; chamadas seguem pelo plano de controle até os adaptadores, e resultados tipados retornam por auditoria e estado ao orquestrador antes de chegar ao canal](../assets/images/m04-agente-ferramentas.png)
*Figura 1 — O modelo propõe; o plano de controle valida e executa com autoridade limitada. Sistemas corporativos nunca recebem diretamente texto livre do modelo.*

## Vista de componentes

```mermaid
flowchart LR
    U["Cliente / atendente"] --> UI["Canal autenticado"]
    UI --> ORQ["Orquestrador de execução"]
    ORQ --> LLM["Modelo: propõe próximo passo"]
    ORQ --> CAT["Catálogo e esquemas de ferramentas"]
    ORQ --> POL["Política e autorização delegada"]
    ORQ --> ST["Estado, orçamento e idempotência"]
    ORQ --> APR["Fila e interface de aprovação"]
    ORQ --> EXE["Executor determinístico"]
    EXE --> ACRM["Adaptador CRM"]
    EXE --> APED["Adaptador de pedidos"]
    ACRM --> CRM["CRM corporativo"]
    APED --> PED["Pedidos e reservas"]
    CRM -- "resultado tipado" --> ACRM
    PED -- "resultado / evento" --> APED
    ORQ --> AUD["Trace e auditoria"]
    POL --> AUD
    ST --> AUD
    EXE --> AUD
    APR --> AUD
```

**Equivalente textual 1.** O canal autentica cliente ou atendente e envia objetivo ao orquestrador. O modelo só propõe próximo passo usando um catálogo mínimo. Antes da execução, o orquestrador consulta política e autorização delegada, reserva orçamento e verifica estado/idempotência. Ações condicionadas seguem para uma interface de aprovação. O executor chama adaptadores de CRM e pedidos com credenciais fora do modelo. Resultados tipados retornam ao orquestrador. Proposta, política, estado, aprovação, chamada e resultado compõem um trace auditável.

## Dois contratos conceituais

```yaml
tool: consultar_pedido
version: 1
effect: read
input:
  order_id: string
  customer_id: string
output:
  order_version: string
  status: [open, shipped, cancelled]
  items: array
  promised_date: date
authorization: order belongs to delegated customer or attendant scope
timeout_ms: 1200
retry: up to 2 for transient errors
audit: actor, subject, order_id, policy_decision_id, result_code
```

```yaml
tool: reservar_substituicao
version: 2
effect: reversible_write
input:
  order_id: string
  expected_order_version: string
  old_sku: string
  new_sku: string
  quantity: integer, 1..5
  idempotency_key: string
output:
  reservation_id: string
  expires_at: timestamp
  price_delta: decimal
errors: [invalid, denied, conflict, unavailable, transient, unknown_outcome]
authorization: delegated order scope plus commercial policy
execution_boundary: deterministic executor and orders adapter only
timeout_ms: 1800
on_timeout:
  local_state: outcome_unknown
  reconciliation: query destination by idempotency key or consume correlated event
retry: only after destination proves no effect; reuse the stable key
after_human_wait: revalidate identity, policy, approval and resource version
compensation: liberar_reserva(reservation_id, idempotency_key)
audit: actor, subject, approval_id, policy_version, before/after references
```

Os esquemas não recebem `approved=true` produzido pelo modelo. A política calcula necessidade de aprovação. `expected_order_version` impede alteração sobre pedido que mudou; `idempotency_key` impede duas reservas lógicas. Timeout deixa o estado local em `outcome_unknown`: somente uma consulta ao destino pela mesma chave, ou um evento correlacionado emitido por ele, pode confirmar o resultado. A compensação é uma ferramenta independente e autorizada, e também atravessa política, estado, executor e adaptador.

![Fronteiras de autonomia mostrando ações informativas, leituras, escritas reversíveis e ações materiais condicionadas a aprovação](../assets/images/m04-fronteiras-autonomia.png)
*Figura 2 — A autonomia varia por ação: conversar, consultar, reservar e confirmar uma troca pertencem a níveis e controles diferentes.*

## Sequência com quatro caminhos obrigatórios

```mermaid
sequenceDiagram
    autonumber
    actor C as Cliente
    participant O as Orquestrador
    participant M as Modelo
    participant P as Política/Aprovação
    participant S as Estado/Idempotência
    participant X as Executor/Adaptadores
    participant R as CRM
    participant D as Pedidos

    C->>O: Solicita troca (pedido 845, P10→P20)
    O->>S: Cria execução e orçamento
    O->>M: Objetivo + ferramentas permitidas + estado
    M-->>O: consultar_cliente e consultar_pedido
    O->>P: Autorizar leituras com identidade delegada
    P-->>O: allow (política v31)
    O->>X: Executar consultas autorizadas
    X->>R: Consultar cliente
    R-->>X: Segmento e preferências autorizadas
    X->>D: Consultar pedido
    D-->>X: Pedido v17 e itens
    X-->>O: Observações tipadas e versões
    O->>M: Observações tipadas
    M-->>O: reservar_substituicao(P20, expected=v17)
    O->>P: Avaliar identidade, política, parâmetros, pedido v17 e risco

    alt Caminho feliz: reversível e dentro do limite
        P-->>O: allow + exige confirmação do cliente antes da troca
        O->>P: Revalidar identidade, política e pedido v17 para reserva
        P-->>O: allow (política v31, pedido v17)
        O->>S: Persistir intenção reservar + K-845-1
        O->>X: Executor: reservar P20, expected=v17, K-845-1
        X->>D: Adaptador invoca reserva
        D-->>X: Reserva R9, reserva-v1, expira 15:30
        X-->>O: R9, diferença R$ 40
        O->>S: Persistir completed, versões e auditoria before/after
        O-->>C: Exibe termos e solicita confirmação
        C->>O: Confirma objeto aprovado
        O->>P: Revalidar identidade, política, aprovação e pedido v17
        P-->>O: allow (aprovação íntegra e vigente)
        O->>S: Persistir intenção confirmar + K-845-2
        O->>X: Executor: confirmar troca, expected=v17, K-845-2
        X->>D: Adaptador invoca confirmação
        D-->>X: Troca concluída, pedido v18
        X-->>O: Pedido v18 e auditoria before/after
        O->>S: Persistir confirmação completed e pedido v18
        O->>P: Revalidar identidade, política e CRM v12
        P-->>O: allow para registro do resultado
        O->>S: Persistir intenção registrar + K-845-3
        O->>X: Executor: registrar resolução, pedido v18, K-845-3
        X->>R: Adaptador grava com expected=CRM-v12
        R-->>X: Registro concluído, CRM-v13
        X-->>O: CRM-v13 e auditoria before/after
        O->>S: Persistir registro completed
        O-->>C: Confirma conclusão e protocolo
    else Ação rejeitada pela política
        P-->>O: deny (pedido já despachado)
        O->>S: Registrar negação e encerrar ações
        O-->>C: Informa limite e oferece atendimento humano
    else Prevenção de chamada repetida após timeout
        P-->>O: allow
        O->>S: Persistir intenção reservar + K-845-1
        O->>X: Executor: reservar P20, expected=v17, K-845-1
        X->>D: Adaptador invoca reserva com K-845-1
        D-->>X: Reserva R9 criada no destino
        X--xO: Timeout; confirmação não chega
        O->>S: Marcar K-845-1 como outcome_unknown
        O->>X: Reconciliar K-845-1 no destino
        X->>D: Consultar operação por K-845-1
        D-->>X: R9, completed, reserva-v1
        X-->>O: Confirmar R9 como resultado autoritativo
        O->>S: Persistir completed e resultado R9
        Note over O,D: Só após reconciliação; nenhuma segunda reserva é enviada
        O-->>C: Retoma a partir da reserva existente
    else Compensação após falha posterior
        P-->>O: allow
        O->>P: Revalidar identidade, política e pedido v17 para reserva
        P-->>O: allow (pedido v17)
        O->>S: Persistir intenção reservar + K-845-1
        O->>X: Executor: reservar P20, expected=v17, K-845-1
        X->>D: Adaptador invoca reserva
        D-->>X: Reserva R9 criada, reserva-v1
        X-->>O: R9, reserva-v1
        O->>S: Persistir reserva completed e auditoria before/after
        O-->>C: Informa reserva ativa e solicita confirmação
        C->>O: Confirma objeto aprovado
        O->>P: Revalidar identidade, política, aprovação e pedido v17
        P-->>O: allow
        O->>S: Persistir intenção confirmar + K-845-2
        O->>X: Executor: confirmar troca, expected=v17, K-845-2
        X->>D: Adaptador invoca confirmação
        D-->>X: Conflito: pedido atual v18
        X-->>O: conflict, expected=v17, actual=v18
        O->>S: Persistir conflito e compensation_required
        O->>P: Revalidar identidade, política e reserva-v1; autorizar compensação
        P-->>O: allow para liberar R9
        O->>S: Persistir compensação C-K-845-1 e estado compensation_pending
        O->>X: Executor: liberar R9, expected=reserva-v1, C-K-845-1
        X->>D: Adaptador invoca liberação idempotente
        D-->>X: Reserva liberada, reserva-v2
        X-->>O: Compensação concluída e auditoria before/after
        O->>S: Marcar compensada, guardar reserva-v2 e preservar conflito
        O-->>C: Informa não conclusão e encaminha revisão
    end
```

**Equivalente textual 2.** A execução começa com identidade e orçamento. O modelo escolhe leituras; política, executor e adaptadores mediam CRM e pedidos. No **caminho feliz**, antes de cada escrita o sistema revalida identidade, política e versão do recurso, persiste intenção e chave estável e só então o executor chama o adaptador. Depois da espera humana, a confirmação não reutiliza autorização antiga: revalida a aprovação e o pedido v17. Confirmar a troca e registrar o CRM repetem a fronteira determinística e preservam precondições e auditoria. Na **ação rejeitada**, a política nega porque o pedido foi despachado; nenhuma ferramenta de efeito é executada. Na **prevenção de chamada repetida**, o timeout deixa K-845-1 em `outcome_unknown`; o executor consulta o sistema de pedidos pela chave, recebe R9 como resultado autoritativo e só então o estado reutiliza o resultado, sem segunda reserva. No caminho de **compensação**, reserva e confirmação atravessam a mesma fronteira. O conflito de versão exige nova autorização para compensar, intenção `compensation_pending` e chave estável; executor e adaptador liberam R9 com precondição `reserva-v1`, e estado/auditoria preservam versões e efeito residual.

## Estado e invariantes

O registro da execução pode ser resumido assim:

```text
execution_id, objective, actor_id, subject_id, delegated_scopes
status, state_version, current_step, tool_catalog_version
policy_version, proposed_actions[], approval_objects[]
tool_calls[idempotency_key, signature, attempt, outcome, resource_version]
budget[steps, elapsed_ms, tokens, cost, effectful_actions]
compensations[required, status, residual_effect]
trace_id, retention_class
```

Invariantes testáveis:

1. nenhuma chamada ocorre sem decisão de política vigente;
2. nenhuma credencial aparece no contexto do modelo;
3. uma intenção de escrita possui uma chave persistida antes da chamada;
4. timeout de escrita persiste `outcome_unknown`; antes de reutilizar resultado ou fazer retry, o executor reconcilia no destino por chave de idempotência ou evento correlacionado autoritativo;
5. aprovação vincula ferramenta, parâmetros, evidência e validade;
6. orçamento inclui tentativas, handoffs e compensações;
7. execução só termina `completed` quando efeitos e registros obrigatórios concluem;
8. compensação pendente mantém alerta e dono explícito.

## Falhas e modos degradados

| Falha | Contenção | Recuperação |
|---|---|---|
| política indisponível | negar escrita; permitir apenas informação pública aprovada | restaurar serviço e reavaliar, sem reutilizar autorização antiga |
| CRM indisponível | não inferir segmento nem preferência | workflow abre tarefa com dados mínimos |
| pedidos com circuito aberto | interromper chamadas e não procurar rota paralela | retomar após half-open ou atendimento humano |
| resposta do modelo inválida | rejeitar esquema e permitir uma correção dentro do orçamento | fallback determinístico coleta campos |
| aprovação expirada | não executar | gerar novo objeto após revalidar estado e preço |
| resultado desconhecido | persistir `outcome_unknown` e bloquear nova intenção equivalente | reconciliar no destino por chave ou evento correlacionado; reutilizar só após confirmação autoritativa e repetir apenas se o destino provar ausência de efeito |
| compensação falha | marcar `compensation_pending`, alertar e limitar novas ações | operação repete com chave ou corrige manualmente |
| orçamento esgotado | persistir estado e impedir novo efeito | resposta parcial, retomada autorizada ou encaminhamento |

Esse desenho é deliberadamente assimétrico: o modelo tem flexibilidade para propor; controles mantêm autoridade para negar, pausar, deduplicar e compensar. A seguir, aplicamos o desenho a uma operação mais ampla em [Estudo de caso](estudo-de-caso.md).
