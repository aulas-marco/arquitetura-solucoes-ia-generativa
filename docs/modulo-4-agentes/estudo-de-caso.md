# Estudo de caso: resolução controlada de solicitações

Caso curto, para 30 minutos de discussão em grupo com o material do módulo aberto. O dossiê fornece situação, restrições e evidências; as decisões de arquitetura ficam por conta do grupo.

## Objetivo

Decidir **quanta autonomia conceder, a que ação, sob qual autoridade e com qual recuperação** na Vértice Varejo. As cinco questões pedem respostas curtas — uma tabela, um contrato, uma mensagem, meia página de ADR — e usam as [quatro formas de controle operacional](conceitos.md#quatro-formas-de-controle-operacional), a [matriz de autonomia](padroes-e-decisoes.md#matriz-de-autonomia), o [contrato de ferramenta](padroes-e-decisoes.md#comece-pelo-contrato-de-ferramenta) e as [fitness functions](padroes-e-decisoes.md#fitness-functions-para-autonomia).

## Como trabalhar em grupo

Grupos de três a cinco pessoas, 30 minutos cronometrados.

**Papéis.** Distribua quatro papéis e mantenha-os até o fim, porque as tensões do caso só aparecem se alguém as defender: **arquitetura**, **segurança e privacidade**, **operações** e **comercial**. Em grupos de três, arquitetura acumula comercial.

**Ritmo.** 4 min de leitura do dossiê · 3 min na Q1 · 5 min na Q2 · 4 min na Q3 · 6 min na Q4 · 5 min na Q5 · 3 min de plenária.

**Regra.** Toda decisão cita a seção do módulo que a sustenta. Decisão sem evidência no dossiê vira **incógnita** com o experimento que a resolveria, não suposição silenciosa. Não há tempo para consenso em tudo: registre a divergência e siga.

## Dossiê

A Vértice Varejo recebe pedidos de troca, cancelamento, alteração de entrega e informação sobre produtos. Atendentes alternam entre CRM, estoque, pedidos e políticas comerciais. A direção pede um "agente que resolva tudo".

**Restrições confirmadas.** Segurança exige identidade individual em cada chamada e logs sem documento e endereço em claro. Operações relata timeouts recorrentes no legado de pedidos, com equipe pequena de plantão. Comercial permite reserva temporária de item, mas desconto e cancelamento material dependem de limite por valor e aprovação de supervisor. CRM e estoque só são acessíveis por adaptadores; pedidos aceita precondição de versão e chave de idempotência. Auditoria precisa reconstruir proposta, decisão de política, aprovação, chamada, resultado e compensação.

**Classes de solicitação.**

| Solicitação | Sistemas | Efeito |
|---|---|---|
| consultar status | pedidos | leitura |
| sugerir produto substituto | estoque + políticas | proposta |
| reservar substituto por 15 min | estoque/pedidos | escrita reversível |
| cancelar pedido aberto | pedidos + CRM | escrita material |
| conceder desconto excepcional | políticas + pedidos | impacto financeiro |
| alterar endereço após expedição | logística | alto risco de fraude |

A coluna de autonomia foi removida de propósito: preenchê-la é a Q1.

**Evidências do piloto.** Já existe um copiloto com workflow determinístico: identifica intenção, consulta dados por ferramentas de leitura e prepara orientação para o atendente executar. Três semanas com 40 atendentes e 640 solicitações:

| Observação | Resultado |
|---|---:|
| tempo médio de resolução, troca simples (antes / com copiloto) | 11 min / 7 min |
| seleção correta da ferramenta de leitura | 94% |
| orientações com política desatualizada | 9 em 640 |
| falhas de integração com pedidos (timeout) | 23 em 640 |
| solicitações em que a sequência de consulta variou de forma não prevista | 31% |

**Ferramentas no adaptador**, nenhuma exposta ainda à escolha do modelo: `consultar_cliente`, `consultar_pedido`, `buscar_estoque`, `avaliar_politica`, `reservar_item`, `liberar_reserva`, `propor_cancelamento`, `registrar_interacao`. A política comercial é versionada e consultável por API.

**Incógnitas.** Sem medição de custo por atendimento, de carga de revisão do supervisor, nem de comportamento sob conteúdo malicioso no texto do cliente. A direção quer decisão em duas semanas.

## As cinco questões

### Q1 — Classificar autonomia por ação e risco (3 min)

**Consulte:** [quatro formas de controle operacional](conceitos.md#quatro-formas-de-controle-operacional) e a [matriz de autonomia](padroes-e-decisoes.md#matriz-de-autonomia).

**Tarefa.** Atribua um nível (A1 a A4, ou "fora do agente") a cada linha da tabela de classes, com justificativa de meia linha por efeito e reversibilidade. Diga também se o piloto atual é chatbot, copiloto, workflow determinístico ou agente.

**Armadilha.** Nível uniforme nas seis linhas — sinal de que o grupo classificou a solução, não as ações.

### Q2 — Especificar o contrato da primeira ação de efeito (5 min)

**Consulte:** [contrato de ferramenta](padroes-e-decisoes.md#comece-pelo-contrato-de-ferramenta), [autorização delegada](padroes-e-decisoes.md#identidade-do-usuario-e-autorizacao-delegada) e [idempotência](padroes-e-decisoes.md#idempotencia-concorrencia-e-prevencao-de-repeticao).

**Tarefa.** Escreva o contrato de `reservar_item`: parâmetros, precondições validadas pela política (não pelo modelo), identidade e finalidade exigidas, chave de idempotência, expiração, erros e retorno. Aponte quais ferramentas da lista ficam **fora** do catálogo exposto ao modelo neste incremento.

**Armadilha.** Descrever a ferramenta em linguagem natural. Contrato que não permite recusar chamada inválida antes de executá-la não é contrato.

### Q3 — Separar estado, memória e dado pessoal (4 min)

**Consulte:** [estado, memória e contexto](conceitos.md#estado-memoria-e-contexto) e [auditoria e observabilidade](padroes-e-decisoes.md#auditoria-e-observabilidade).

**Tarefa.** Resolva dois casos concretos de um atendimento de troca com reserva: (a) o cliente menciona uma preferência de canal de contato — onde ela pode e não pode ficar? (b) o acesso do atendente é revogado no meio da trajetória, com reserva ativa — o que acontece com estado, reserva e trace?

**Armadilha.** Deixar o agente "aprender" a preferência a partir da conversa. Nomeie o sistema dono do dado e o fluxo autorizado a alterá-lo.

### Q4 — Falha, compensação e o que se diz ao cliente (6 min)

**Consulte:** [timeout, retry e circuit breaker](padroes-e-decisoes.md#timeout-retry-e-circuit-breaker), [consistência, transações e compensação](padroes-e-decisoes.md#consistencia-transacoes-e-compensacao) e [orçamentos, interrupção e fallback](padroes-e-decisoes.md#orcamentos-interrupcao-e-fallback).

**Tarefa.** Defina o tratamento de duas situações: timeout na escrita da reserva sem resposta do legado; reserva efetivada e pedido alterado por outro canal em seguida. Para cada uma, diga o que se faz (retry, consulta por chave, bloqueio, compensação) e onde vai a falha de compensação. Especifique em uma linha o orçamento da trajetória — passos, ações de efeito, tempo, custo — e o que ocorre ao esgotá-lo.

Escreva a mensagem ao cliente no caso do timeout de escrita, distinguindo dois estados que ele confunde: **a troca ainda não está concluída**, mas **a reserva temporária já pode estar ativa** e indisponibilizar o item até expirar ou ser liberada.

**Armadilha.** Tratar timeout de escrita como timeout de leitura e repetir a chamada.

### Q5 — Decidir a promoção e registrar o ADR (5 min)

**Consulte:** [fitness functions para autonomia](padroes-e-decisoes.md#fitness-functions-para-autonomia), [agente único versus múltiplos agentes](padroes-e-decisoes.md#agente-unico-versus-multiplos-agentes) e [plataforma e obtenção de capacidade](padroes-e-decisoes.md#plataforma-e-obtencao-de-capacidade).

**Tarefa.** Meia página no formato do [template de ADR](../referencia/template-adr.md): expor ou não a reserva ao modelo; duas opções descartadas, entre elas múltiplos agentes por domínio e serviço hospedado de planejamento e política; a evidência do dossiê que sustenta a decisão; duas fitness functions com limite numérico e ação automática; e o gatilho que reduz autonomia depois de concedida.

**Armadilha.** Justificar a promoção pela variação de 31% sem verificar em que classes de solicitação ela ocorre — pode estar concentrada em leituras que já são A2.

## Plenária

Três minutos: cada grupo diz o nível concedido, a ação exposta e a fitness function que dispararia redução de autonomia. O confronto útil está nos grupos que chegaram a decisões opostas com a mesma evidência — aí a pergunta é qual incógnita do dossiê separa as duas leituras.

Para aprofundar depois da aula, ver [Classificação de autonomia](exercicios.md#11-classificacao-de-autonomia), [Diagnóstico de trace](exercicios.md#14-diagnostico-de-trace) e [Arquitetura de agente controlado](exercicios.md#18-arquitetura-de-agente-controlado) em [Exercícios](exercicios.md).
