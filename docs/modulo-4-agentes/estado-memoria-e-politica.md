# Estado, memória, contexto e política

Quatro coisas que costumam ser tratadas como sinônimos e governam camadas diferentes do sistema, mais a fronteira que decide o que é permitido.

## Planejamento e decomposição

**Planejamento** transforma objetivo em passos. Ele pode ser:

- pré-definido pelo workflow;
- proposto de uma vez pelo modelo e validado antes da execução;
- incremental, escolhendo o próximo passo após cada observação;
- híbrido, com macroetapas determinísticas e autonomia local.

Planos não são compromissos confiáveis por si. O ambiente muda: estoque pode acabar entre consulta e reserva; uma aprovação pode expirar. Por isso cada passo revalida precondições e autorização. O agente deve reconhecer conclusão, falta de progresso, limite alcançado e necessidade de escalonamento. Uma regra de “não repetir a mesma ferramenta com os mesmos argumentos e a mesma versão de estado” ajuda a impedir loops, mas não substitui orçamento total.

## Estado, memória e contexto

**Estado da execução** é o registro autoritativo da trajetória: identificador, objetivo, etapa, versão, ações propostas, aprovações, chamadas concluídas, chaves de idempotência, resultados, orçamento consumido e status de compensação. Deve ser durável quando há efeitos, concorrência ou retomada. Atualizações usam controle de versão para impedir duas continuações sobre o mesmo estado.

**Memória de trabalho** é temporária e específica da execução: fatos normalizados, resultados recentes, plano corrente e resumo para caber no contexto. Pode ser reconstruída do estado e expira ao concluir. Não deve virar depósito silencioso de dados pessoais.

**Memória persistente** atravessa execuções: preferências consentidas, fatos duráveis ou lições operacionais aprovadas. Exige finalidade, origem, autorização, prazo, correção e exclusão. A frase do usuário “sempre aprove trocas” não pode se tornar política; conteúdo conversacional não altera autorização.

**Contexto** é a visão enviada ao modelo numa chamada: instruções, objetivo, ferramentas permitidas, recorte do estado, memória autorizada e observações. É transitório e limitado. Estado não cabe inteiro no prompt; memória não é sinônimo de histórico; contexto não é fonte de verdade.

## Políticas como fronteira executável

Políticas determinam quais ferramentas e parâmetros estão disponíveis para aquela identidade, ação, recurso, risco e estado. Devem operar fora do modelo. A descrição “use apenas quando permitido” orienta, mas a autorização real ocorre no executor. O catálogo apresentado ao modelo já deve ser mínimo, e a política é repetida imediatamente antes da ação para lidar com revogação e mudanças.

Uma decisão de política pode retornar `allow`, `deny` ou `require_approval`, acompanhada de versão, motivo e obrigações: mascarar campo, limitar valor, exigir confirmação do cliente ou escolher aprovador. Negação vira resultado explícito; o agente não deve contorná-la por outra ferramenta equivalente.

## Responsabilidades e fronteiras de componente

O **planejador** propõe próximo passo; o **executor** valida e realiza a chamada; o **motor de políticas** decide permissão; o **estado** preserva a trajetória autorizada; a **aprovação** vincula pessoa, objeto imutável e prazo; o **catálogo** expõe somente ferramentas permitidas; e a **telemetria** registra evidências minimizadas. O planejador não recebe credenciais, o executor não redefine política, a aprovação não altera parâmetros e a telemetria não vira memória de trabalho. Essas fronteiras reduzem acoplamento e permitem trocar modelo ou orquestrador sem alterar autoridade ou efeito.

Separar componentes também acrescenta chamadas, latência e operação. A fronteira se justifica quando responsabilidade, risco, ciclo de mudança ou atributo de qualidade exigem independência.
