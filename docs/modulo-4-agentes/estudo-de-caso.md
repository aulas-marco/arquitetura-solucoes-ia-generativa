# Estudo de caso: resolução controlada de solicitações

A Vértice Varejo recebe pedidos de troca, cancelamento, alteração de entrega e informação sobre produtos. Atendentes alternam entre CRM, estoque, pedidos e políticas comerciais. A direção pede um “agente que resolva tudo”. Segurança exige identidade individual; Operações relata timeouts no legado; Comercial permite reservas temporárias, mas descontos e cancelamentos materiais dependem de limites e aprovação.

## Antes da arquitetura: classes de solicitação

| Solicitação | Sistemas | Efeito | Autonomia inicial |
|---|---|---|---|
| consultar status | pedidos | leitura | A2: agente pode selecionar leitura e explicar |
| sugerir produto substituto | estoque + políticas | proposta | A2: cliente decide |
| reservar substituto por 15 min | estoque/pedidos | escrita reversível | A3, com confirmação clara e limite de quantidade |
| cancelar pedido aberto | pedidos + CRM | escrita material | A4, aprovação antes da ação conforme valor/status |
| conceder desconto excepcional | políticas + pedidos | impacto financeiro | fora do agente; supervisor em workflow |
| alterar endereço após expedição | logística | alto risco/fraude | negado e encaminhado |

A matriz impede autonomia uniforme. O mesmo agente informa livremente, propõe algumas ações, reserva dentro de limites e jamais concede exceção comercial.

## Arquitetura incremental

O primeiro incremento é um copiloto com workflow: identifica intenção, consulta dados por ferramentas de leitura e prepara orientação com evidências. O atendente executa. Esse baseline mede tempo, erro de seleção, cobertura de políticas e falhas de integração.

Somente depois, reservas temporárias entram como ação A3. A sequência pode variar entre consultar pedido, política e estoque; o agente escolhe leituras e candidato, mas política valida SKU, quantidade, propriedade do pedido, prazo e diferença. A reserva usa idempotência, expira automaticamente e pode ser liberada. Cancelamento permanece A4. Descontos excepcionais ficam fora do catálogo, em workflow determinístico de supervisor.

As ferramentas são estreitas: `consultar_cliente`, `consultar_pedido`, `buscar_estoque`, `avaliar_politica`, `reservar_item`, `liberar_reserva`, `propor_cancelamento` e `registrar_interacao`. A política comercial é consultada por versão; não é copiada como instrução persistente. CRM e estoque usam adaptadores. Pedidos recebe identidade delegada, precondição de versão e chave de idempotência.

## Estado, memória e privacidade

O estado autoritativo guarda objetivo, recursos envolvidos, versões, propostas, aprovações, chamadas, orçamento e compensações. A memória de trabalho conserva somente fatos necessários à solicitação. Preferência persistente de contato só é lida do CRM e só é alterada por fluxo específico com consentimento; o agente não aprende permanentemente de toda conversa. Logs mascaram documento e endereço, preservando identificadores correlacionáveis sob acesso restrito.

## Aprovações e experiência humana

Ao cliente, a confirmação mostra item anterior/novo, preço, prazo, duração da reserva e que nada foi concluído ainda. Ao supervisor, o objeto de aprovação inclui pedido, regra aplicada, diferença financeira, efeito, reversibilidade, evidências e expiração. Mudança de preço ou versão invalida a aprovação.

Revisão humana depois da ação cobre amostra de reservas A3 e todos os alertas de repetição, compensação ou política negada várias vezes. Ela calibra limites; não substitui aprovação antes de cancelamento crítico. O cliente recebe protocolo, estado real e caminho de contestação.

## Falhas, fallback e responsabilidade

Timeout de leitura admite retry limitado. Timeout de escrita aciona consulta por chave. Circuit breaker aberto no sistema de pedidos bloqueia novas reservas. O fallback coleta pedido, motivo e contato por workflow determinístico, abre tarefa humana e informa que a mudança não foi realizada. Se estoque foi reservado e o pedido mudou, a liberação compensa; se falhar, Operações recebe fila `compensation_pending`.

O orçamento inicial permite oito passos, duas ações de efeito, 20 segundos online e custo máximo por classe. Uma aprovação pausada não consome chamadas de modelo. Retomada revalida identidade, política, pedido, estoque e validade. Múltiplos agentes foram rejeitados no início: os quatro domínios já estão encapsulados em ferramentas, e handoffs acrescentariam custo e autorização sem benefício medido. A decisão será revista se equipes distintas precisarem operar contextos e credenciais isolados ou se paralelismo reduzir latência sem piorar ações indevidas.

## Avaliação e gatilhos

O conjunto de teste cruza intenção, status do pedido, valor, estoque, identidade, revogação, conflito, timeout e conteúdo malicioso. Mede seleção correta de ferramentas, parâmetros válidos, conclusão, negação apropriada, aprovação correta, duplicação zero, compensação, passos, latência e custo. Falhas intoleráveis: agir em pedido alheio, executar ferramenta fora do catálogo, duplicar efeito ou ultrapassar aprovação.

Promova A3 somente se superar o workflow em tempo de resolução sem falha intolerável e com traces reconstruíveis. Reduza autonomia quando compensações, revisões ou loops ultrapassarem limites. Expanda ferramenta ou nível apenas com hipótese, teste e ADR. O resultado desejado não é “mais autonomia”; é resolução útil com autoridade e recuperação proporcionais.

Pratique as decisões em [Exercícios](exercicios.md).
