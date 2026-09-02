# Estudo de caso: resolução controlada de solicitações

Caso curto, para 30 minutos de discussão em grupo com o material do módulo aberto. O dossiê fornece situação, restrições e evidências; as decisões de arquitetura ficam por conta do grupo.

## Objetivo

Decidir **quanta autonomia conceder, a que ação, sob qual autoridade e com qual recuperação** na Vértice Varejo. As cinco perguntas pedem respostas curtas — uma tabela, um contrato, uma mensagem, meia página de ADR — e usam as [quatro formas de controle operacional](conceitos.md#quatro-formas-de-controle-operacional), a [matriz de autonomia](padroes-e-decisoes.md#matriz-de-autonomia), o [contrato de ferramenta](padroes-e-decisoes.md#comece-pelo-contrato-de-ferramenta) e as [fitness functions](padroes-e-decisoes.md#fitness-functions-para-autonomia).

## Como trabalhar em grupo

Grupos de três a cinco pessoas, 30 minutos cronometrados.

**Papéis.** Distribua quatro papéis e mantenha-os até o fim, porque as tensões do caso só aparecem se alguém as defender: **arquitetura**, **segurança e privacidade**, **operações** e **comercial**. Em grupos de três, arquitetura acumula comercial.

**Ritmo.** 4 min de leitura do dossiê · 3 min na Pergunta 1 · 5 min na 2 · 4 min na 3 · 6 min na 4 · 5 min na 5 · 3 min de plenária.

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

A coluna de autonomia foi removida de propósito: preenchê-la é a Pergunta 1.

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

## As cinco perguntas

As perguntas sobem os níveis da [taxonomia de Bloom](../comecar/taxonomia-de-bloom.md): compreender, aplicar, analisar, avaliar e criar. Cada uma indica o que consultar antes de responder, o tempo e a entrega esperada. Não há bloco de resposta: de Aplicar para cima, o feedback é do professor, sobre critérios, coerência e evidência.

### Pergunta 1 — Compreender · 3 min

> **Que nível de autonomia cada classe de solicitação admite, e por que a matriz não pode ser uniforme?**
>
> O piloto que já roda hoje é chatbot, copiloto, workflow determinístico ou agente — e qual evidência do dossiê sustenta essa classificação?

**Consulte:** [quatro formas de controle operacional](conceitos.md#quatro-formas-de-controle-operacional) e a [matriz de autonomia](padroes-e-decisoes.md#matriz-de-autonomia).

**Entrega esperada.** A coluna de autonomia preenchida nas seis linhas (A1 a A4, ou "fora do agente"), com meia linha de justificativa por efeito e reversibilidade, mais uma frase classificando o piloto.

**Armadilha.** Nível uniforme nas seis linhas — sinal de que o grupo classificou a solução, não as ações.

### Pergunta 2 — Aplicar · 5 min

> **Que contrato permite recusar uma chamada inválida de `reservar_item` antes de executá-la?**
>
> Quem valida a precondição, o modelo ou a política? O que impede que duas chamadas reservem o item duas vezes? Com qual identidade a reserva chega ao sistema de pedidos? E quais ferramentas da lista **não** devem ser expostas à escolha do modelo neste incremento?

**Consulte:** [contrato de ferramenta](padroes-e-decisoes.md#comece-pelo-contrato-de-ferramenta), [autorização delegada](padroes-e-decisoes.md#identidade-do-usuario-e-autorizacao-delegada) e [idempotência](padroes-e-decisoes.md#idempotencia-concorrencia-e-prevencao-de-repeticao).

**Entrega esperada.** O contrato de `reservar_item` — parâmetros, precondições, identidade e finalidade, chave de idempotência, expiração, erros e retorno — e a lista de exclusões com o motivo de cada uma.

**Armadilha.** Descrever a ferramenta em linguagem natural ("reserva o item se possível"). Isso não é contrato: não dá para recusar nada com ele.

### Pergunta 3 — Analisar · 4 min

> **Onde vive cada dado deste atendimento, e o que acontece quando a autorização desaparece no meio da trajetória?**
>
> O cliente menciona uma preferência de canal de contato: ela pode ficar no estado de execução, na memória de trabalho, na memória persistente, no trace? Quem é o sistema dono desse dado? E se o acesso do atendente for revogado com uma reserva ativa, o que ocorre com o estado, com a reserva e com o que já foi registrado?

**Consulte:** [estado, memória e contexto](conceitos.md#estado-memoria-e-contexto) e [auditoria e observabilidade](padroes-e-decisoes.md#auditoria-e-observabilidade).

**Entrega esperada.** Resposta aos dois casos, dizendo em cada um o que entra e o que é proibido em cada lugar.

**Armadilha.** Deixar o agente "aprender" a preferência a partir da conversa.

### Pergunta 4 — Avaliar · 6 min

> **Quando o legado de pedidos não responde, o efeito ocorreu ou não — e o que se pode afirmar ao cliente?**
>
> Diante de timeout na escrita da reserva, cabe repetir a chamada? Se a reserva foi efetivada e o pedido mudou por outro canal em seguida, quem compensa, e para onde vai a falha da compensação? Que orçamento de passos, ações de efeito, tempo e custo você defende para a trajetória, e o que acontece ao esgotá-lo?

**Consulte:** [timeout, retry e circuit breaker](padroes-e-decisoes.md#timeout-retry-e-circuit-breaker), [consistência, transações e compensação](padroes-e-decisoes.md#consistencia-transacoes-e-compensacao) e [orçamentos, interrupção e fallback](padroes-e-decisoes.md#orcamentos-interrupcao-e-fallback).

**Entrega esperada.** Tratamento das duas situações, o orçamento em uma linha e a mensagem ao cliente para o caso do timeout de escrita. A mensagem precisa distinguir dois estados que ele confunde: **a troca ainda não está concluída**, mas **a reserva temporária já pode estar ativa** e indisponibilizar o item até expirar ou ser liberada.

**Armadilha.** Tratar timeout de escrita como timeout de leitura e repetir a chamada.

### Pergunta 5 — Criar · 5 min

> **Que decisão o grupo leva à direção em duas semanas, e sob que condição ela se reverte?**
>
> A reserva deve ser exposta à escolha do modelo? Por que descartar múltiplos agentes por domínio e por que não comprar um serviço hospedado de planejamento e política? Que número, medido em produção, obrigaria a reduzir a autonomia depois de concedida?

**Consulte:** [fitness functions para autonomia](padroes-e-decisoes.md#fitness-functions-para-autonomia), [agente único versus múltiplos agentes](padroes-e-decisoes.md#agente-unico-versus-multiplos-agentes) e [plataforma e obtenção de capacidade](padroes-e-decisoes.md#plataforma-e-obtencao-de-capacidade).

**Entrega esperada.** Meia página no formato do [template de ADR](../referencia/template-adr.md): decisão, duas opções descartadas, evidência do dossiê que a sustenta, duas fitness functions com limite numérico e ação automática, e o gatilho de redução de autonomia.

**Armadilha.** Justificar a promoção pela variação de 31% sem verificar em que classes de solicitação ela ocorre — pode estar concentrada em leituras que já são A2.

## Plenária

Três minutos: cada grupo diz o nível concedido, a ação exposta e a fitness function que dispararia redução de autonomia. O confronto útil está nos grupos que chegaram a decisões opostas com a mesma evidência — aí a pergunta é qual incógnita do dossiê separa as duas leituras.

Para aprofundar depois da aula, ver [Classificação de autonomia](exercicios.md#11-classificacao-de-autonomia), [Diagnóstico de trace](exercicios.md#14-diagnostico-de-trace) e [Arquitetura de agente controlado](exercicios.md#18-arquitetura-de-agente-controlado) em [Exercícios](exercicios.md).
