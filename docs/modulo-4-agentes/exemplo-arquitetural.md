# Exemplo arquitetural: agente de atendimento com CRM e pedidos

## Cenário e limites

Um cliente autenticado pede: “troque o item P10 pelo P20 no pedido 845 e mantenha a data”. O sistema pode consultar cadastro e pedido, verificar elegibilidade, criar reserva temporária e propor a alteração. O cancelamento do item original exige confirmação do cliente; diferença acima de R$ 200 exige supervisor. O agente não muda endereço, concede crédito, escolhe credenciais nem ignora política.

O objetivo não é mostrar uma biblioteca específica. É localizar decisões probabilísticas dentro de uma malha determinística de identidade, contratos, política, estado, aprovação e recuperação.

![Agente controlado conectado a um catálogo mínimo de ferramentas, executor de políticas, estado, auditoria, CRM e sistema de pedidos](../assets/images/m04-agente-ferramentas.png)
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
timeout_ms: 1800
retry: reconcile by idempotency key, then at most 1 transient retry
compensation: liberar_reserva(reservation_id, idempotency_key)
audit: actor, subject, approval_id, policy_version, before/after references
```

Os esquemas não recebem `approved=true` produzido pelo modelo. A política calcula necessidade de aprovação. `expected_order_version` impede alteração sobre pedido que mudou; `idempotency_key` impede duas reservas lógicas; `unknown_outcome` força reconciliação. A compensação é uma ferramenta independente e autorizada.

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
    participant R as CRM
    participant D as Pedidos

    C->>O: Solicita troca (pedido 845, P10→P20)
    O->>S: Cria execução e orçamento
    O->>M: Objetivo + ferramentas permitidas + estado
    M-->>O: consultar_cliente e consultar_pedido
    O->>P: Autorizar leituras com identidade delegada
    P-->>O: allow (política v31)
    O->>R: Consultar cliente
    R-->>O: Segmento e preferências autorizadas
    O->>D: Consultar pedido
    D-->>O: Pedido v17 e itens
    O->>M: Observações tipadas
    M-->>O: reservar_substituicao(P20, expected=v17)
    O->>P: Avaliar ação, parâmetros e risco

    alt Caminho feliz: reversível e dentro do limite
        P-->>O: allow + exige confirmação do cliente antes da troca
        O->>S: Persistir intenção e chave K-845-1
        O->>D: Reservar P20 com K-845-1
        D-->>O: Reserva R9, expira 15:30, diferença R$ 40
        O-->>C: Exibe termos e solicita confirmação
        C->>O: Confirma objeto aprovado
        O->>D: Confirmar troca com chave K-845-2
        D-->>O: Troca concluída, pedido v18
        O->>R: Registrar resolução com K-845-3
        R-->>O: Registro concluído
        O-->>C: Confirma conclusão e protocolo
    else Ação rejeitada pela política
        P-->>O: deny (pedido já despachado)
        O->>S: Registrar negação e encerrar ações
        O-->>C: Informa limite e oferece atendimento humano
    else Prevenção de chamada repetida após timeout
        P-->>O: allow
        O->>S: Encontrar K-845-1 como concluída
        S-->>O: Reutilizar resultado Reserva R9
        Note over O,D: Nenhuma segunda reserva é enviada
        O-->>C: Retoma a partir da reserva existente
    else Compensação após falha posterior
        P-->>O: allow
        O->>D: Reservar P20 com K-845-1
        D-->>O: Reserva R9 criada
        O->>D: Confirmar troca com K-845-2
        D-->>O: Conflito: pedido mudou para v18
        O->>P: Autorizar compensação da reserva R9
        P-->>O: allow
        O->>D: Liberar R9 com chave C-K-845-1
        D-->>O: Reserva liberada
        O->>S: Marcar compensada e preservar conflito
        O-->>C: Informa não conclusão e encaminha revisão
    end
```

**Equivalente textual 2.** A execução começa com identidade e orçamento. O modelo escolhe leituras; a política autoriza; CRM e pedidos devolvem resultados tipados. No **caminho feliz**, uma reserva reversível é criada com chave idempotente, o cliente confirma exatamente a proposta e a troca é concluída antes de registrar o CRM. Na **ação rejeitada**, a política nega porque o pedido foi despachado; o orquestrador encerra efeitos e oferece atendimento. Na **prevenção de chamada repetida**, o estado encontra a mesma chave já concluída após timeout e reutiliza o resultado, sem enviar segunda reserva. No caminho de **compensação**, uma mudança concorrente impede confirmar a troca; o sistema autoriza e executa a liberação idempotente da reserva, preserva o conflito e informa que a solicitação não foi concluída.

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
4. timeout de escrita produz reconciliação antes de retry;
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
| resultado desconhecido | bloquear nova intenção equivalente | reconciliar por chave e recurso |
| compensação falha | marcar `compensation_pending`, alertar e limitar novas ações | operação repete com chave ou corrige manualmente |
| orçamento esgotado | persistir estado e impedir novo efeito | resposta parcial, retomada autorizada ou encaminhamento |

Esse desenho é deliberadamente assimétrico: o modelo tem flexibilidade para propor; controles mantêm autoridade para negar, pausar, deduplicar e compensar. A seguir, aplicamos o desenho a uma operação mais ampla em [Estudo de caso](estudo-de-caso.md).
