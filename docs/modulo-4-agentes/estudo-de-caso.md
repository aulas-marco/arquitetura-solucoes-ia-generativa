# Estudo de caso: resolução controlada de solicitações

Caso curto, para cerca de 30 minutos de discussão em grupo com o material do módulo aberto. O dossiê fornece a situação, as restrições e as evidências; as decisões de arquitetura ficam por conta do grupo.

## Objetivo

Decidir **onde ficam as responsabilidades, quais atributos de qualidade prevalecem e como o sistema se recupera** quando parte do efeito já ocorreu. A discussão é de arquitetura: alocação de responsabilidade, acoplamento entre sistemas de propriedade distinta, limite de consistência e critério de evolução.

## Como trabalhar em grupo

Grupos de três a cinco pessoas. Leia o dossiê uma vez, sem tentar resolver nada, e depois trabalhe as cinco perguntas na ordem. Cada uma traz um cenário e três respostas possíveis: o grupo escolhe uma e justifica.

A justificativa vale mais do que a letra escolhida. O que o dossiê não permite decidir vira **incógnita**, com o experimento que a resolveria. Onde o grupo não chegar a acordo, registre a divergência e siga.

## Dossiê

A Vértice Varejo recebe pedidos de troca, cancelamento, alteração de entrega e informação sobre produtos. Atendentes alternam entre CRM, estoque, pedidos e políticas comerciais. A direção pede um "agente que resolva tudo".

**Restrições confirmadas.** Segurança exige identidade individual em cada chamada e logs sem documento e endereço em claro. Operações relata timeouts recorrentes no legado de pedidos, com equipe pequena de plantão. Comercial permite reserva temporária de item, mas desconto e cancelamento material dependem de limite por valor e aprovação de supervisor. CRM e estoque só são acessíveis por adaptadores; pedidos aceita precondição de versão e chave de idempotência. Auditoria precisa reconstruir proposta, decisão de política, aprovação, chamada, resultado e compensação.

**Classes de solicitação.** A arquitetura precisa governar o efeito de cada uma.

| Solicitação | Sistemas | Efeito |
|---|---|---|
| consultar status | pedidos | leitura |
| sugerir produto substituto | estoque + políticas | proposta |
| reservar substituto por 15 min | estoque/pedidos | escrita reversível |
| cancelar pedido aberto | pedidos + CRM | escrita material |
| conceder desconto excepcional | políticas + pedidos | impacto financeiro |
| alterar endereço após expedição | logística | alto risco de fraude |

**Evidências do piloto.** Já existe um copiloto com workflow determinístico: identifica intenção, consulta dados por ferramentas de leitura e prepara orientação para o atendente executar. Três semanas com 40 atendentes e 640 solicitações:

| Observação | Resultado |
|---|---:|
| tempo médio de resolução, troca simples (antes / com copiloto) | 11 min / 7 min |
| seleção correta da ferramenta de leitura | 94% |
| orientações com política desatualizada | 9 em 640 |
| falhas de integração com pedidos (timeout) | 23 em 640 |
| solicitações que exigiram consultar os sistemas fora da ordem prevista | 31% |

O workflow do copiloto segue uma ordem fixa com ramificações: consultar pedido, avaliar política, buscar estoque. Os 31% são casos que não couberam em nenhuma ramificação — o atendente precisou avaliar a política antes do estoque porque o cliente veio de outro canal, ou reconsultar o pedido depois da política porque o status mudou durante o atendimento.

**Capacidades expostas pelos adaptadores**, nenhuma delas ainda invocável fora do fluxo conduzido pelo atendente: `consultar_cliente`, `consultar_pedido`, `buscar_estoque`, `avaliar_politica`, `reservar_item`, `liberar_reserva`, `propor_cancelamento`, `registrar_interacao`. A política comercial é versionada e consultável por API.

**Incógnitas.** Sem medição de custo por atendimento, de carga de revisão do supervisor, nem de comportamento sob conteúdo malicioso no texto do cliente. A direção quer decisão em duas semanas.

## As cinco perguntas

Cada pergunta traz um cenário e três respostas possíveis. **Escolha uma e justifique em duas ou três frases**, citando a seção do módulo que sustenta a escolha. Nenhuma das opções é absurda. Cada uma é defensável sob alguma condição, e a justificativa precisa dizer qual.

As perguntas sobem os níveis da [taxonomia de Bloom](../comecar/taxonomia-de-bloom.md). Nenhuma delas se resolve escolhendo modelo, prompt ou plataforma.

### Pergunta 1 — Compreender

**Cenário.** No copiloto atual, o atendente lê a orientação e executa a reserva no sistema de pedidos. A proposta é o modelo passar a escolher o item substituto.

> **Quem passa a autorizar a reserva?**

- **a)** O componente que gera a proposta, porque conhece o caso.
- **b)** Um componente de política, que valida a chamada antes de o executor agir.
- **c)** O sistema de pedidos, que já rejeita gravação inválida.

**Consulte:** [geração, decisão e ação](conceitos.md#geracao-decisao-e-acao) e [políticas como fronteira executável](conceitos.md#politicas-como-fronteira-executavel).

**Armadilha.** Tratar "o legado rejeita" como autorização. Rejeitar gravação inválida verifica o dado; a permissão já foi decidida antes disso, em outro lugar.

### Pergunta 2 — Aplicar

**Cenário.** Auditoria quer reconstruir cada atendimento: proposta, política aplicada, chamada e resultado. Segurança proíbe documento e endereço em claro nos logs. Operações tem três pessoas de plantão.

> **Qual par de atributos de qualidade está em conflito, e qual você atende primeiro?**

- **a)** Observabilidade e privacidade. Registrar o suficiente para reconstruir sem reter dado pessoal.
- **b)** Latência e custo. Cada consulta a mais encarece e atrasa o atendimento.
- **c)** Confiabilidade e manutenibilidade. Mais táticas de recuperação, mais código para sustentar.

**Consulte:** o [catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md).

**Entrega adicional.** Um cenário mensurável para o atributo priorizado, no formato do catálogo.

**Armadilha.** Escolher um par cujas medidas melhoram juntas.

### Pergunta 3 — Analisar

**Cenário.** O sistema de pedidos é o que mais dá timeout e é o único que aceita precondição de versão. CRM e estoque só respondem por adaptadores. A política comercial é versionada e consultável por API.

> **Como integrar o sistema de pedidos?**

- **a)** Chamada síncrona com timeout curto, precondição de versão e chave de idempotência.
- **b)** Mensageria: o pedido de reserva entra numa fila e é processado quando o legado responder.
- **c)** Evento de domínio: o estoque publica a reserva e pedidos reage por conta própria.

**Consulte:** [APIs, mensageria, eventos e adaptadores](padroes-e-decisoes.md#apis-mensageria-eventos-e-adaptadores) e [identidade do usuário e autorização delegada](padroes-e-decisoes.md#identidade-do-usuario-e-autorizacao-delegada).

**Entrega adicional.** Na opção escolhida, como a identidade do atendente atravessa a fronteira sem virar credencial compartilhada.

**Armadilha.** Escolher desacoplamento assíncrono e manter a expectativa de confirmação imediata na tela do atendente.

### Pergunta 4 — Avaliar

**Cenário.** A reserva foi enviada ao sistema de pedidos e o timeout expirou sem resposta. Não se sabe se o item foi reservado. O cliente está na linha esperando.

> **O que o sistema faz?**

- **a)** Repete a chamada com a mesma chave de idempotência.
- **b)** Consulta o legado pela chave para descobrir o estado real antes de qualquer nova escrita.
- **c)** Interrompe o fluxo, registra compensação pendente e encaminha para tratamento humano.

**Consulte:** [idempotência, concorrência e prevenção de repetição](padroes-e-decisoes.md#idempotencia-concorrencia-e-prevencao-de-repeticao) e [consistência, transações e compensação](padroes-e-decisoes.md#consistencia-transacoes-e-compensacao).

**Entrega adicional.** O que se afirma ao cliente enquanto o estado é desconhecido. O que ele ouvir precisa distinguir duas situações que ele confunde: **a troca ainda não está concluída**, mas **a reserva temporária já pode estar ativa** e indisponibilizar o item até expirar ou ser liberada.

**Armadilha.** Justificar a repetição pela existência da chave de idempotência sem verificar se o legado a honra na condição de timeout.

### Pergunta 5 — Criar

**Cenário.** A direção quer decisão em duas semanas. O piloto reduziu o tempo de resolução de 11 para 7 minutos, e 31% das solicitações exigiram consultar os sistemas fora da ordem prevista pelo workflow.

> **Que estrutura o grupo recomenda?**

- **a)** Manter o copiloto e ampliar apenas as consultas de leitura.
- **b)** Um componente com autoridade para reservar, sob política, com aprovação humana para efeito material.
- **c)** Um componente por domínio (CRM, estoque, pedidos, política) coordenando entre si.

**Consulte:** [agente único e múltiplos agentes](conceitos.md#agente-unico-e-multiplos-agentes) e [fitness functions para autonomia](padroes-e-decisoes.md#fitness-functions-para-autonomia).

**Entrega adicional.** Meia página no formato do [template de ADR](../referencia/template-adr.md): a decisão, a opção descartada com o motivo, a evidência do dossiê que a sustenta e uma fitness function com limite numérico e ação automática de recuo.

**Armadilha.** Escolher a opção (c) porque existem quatro sistemas. Fronteira de componente se justifica por autoridade sobre o dado e por ritmo de mudança.

## Plenária

Cada grupo diz o que escolheu nas cinco perguntas e por quê. Quando dois grupos escolhem opções opostas com a mesma evidência, vale perguntar qual incógnita do dossiê separa as duas leituras.

Para aprofundar depois da aula, ver [Classificação de autonomia](exercicios.md#11-classificacao-de-autonomia), [Diagnóstico de trace](exercicios.md#14-diagnostico-de-trace) e [Arquitetura de agente controlado](exercicios.md#18-arquitetura-de-agente-controlado) em [Exercícios](exercicios.md).
