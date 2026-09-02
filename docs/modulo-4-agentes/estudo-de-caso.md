# Estudo de caso: resolução controlada de solicitações

Caso curto, para 30 minutos de discussão em grupo com o material do módulo aberto. O dossiê fornece situação, restrições e evidências; as decisões de arquitetura ficam por conta do grupo.

## Objetivo

Decidir **onde ficam as responsabilidades, quais atributos de qualidade prevalecem e como o sistema se recupera** quando parte do efeito já ocorreu. A discussão é de arquitetura: alocação de responsabilidade, acoplamento entre sistemas de propriedade distinta, limite de consistência e critério de evolução. As respostas são curtas — uma tabela, um cenário mensurável, meia página de ADR.

## Como trabalhar em grupo

Grupos de três a cinco pessoas, 30 minutos cronometrados.

**Papéis.** Distribua quatro papéis e mantenha-os até o fim, porque as tensões do caso só aparecem se alguém as defender: **arquitetura**, **segurança e privacidade**, **operações** e **comercial**. Em grupos de três, arquitetura acumula comercial.

**Ritmo.** 4 min de leitura do dossiê · 3 min na Pergunta 1 · 5 min na 2 · 4 min na 3 · 6 min na 4 · 5 min na 5 · 3 min de plenária.

**Regra.** Toda decisão cita a seção do módulo que a sustenta. Decisão sem evidência no dossiê vira **incógnita** com o experimento que a resolveria, não suposição silenciosa. Não há tempo para consenso em tudo: registre a divergência e siga.

## Dossiê

A Vértice Varejo recebe pedidos de troca, cancelamento, alteração de entrega e informação sobre produtos. Atendentes alternam entre CRM, estoque, pedidos e políticas comerciais. A direção pede um "agente que resolva tudo".

**Restrições confirmadas.** Segurança exige identidade individual em cada chamada e logs sem documento e endereço em claro. Operações relata timeouts recorrentes no legado de pedidos, com equipe pequena de plantão. Comercial permite reserva temporária de item, mas desconto e cancelamento material dependem de limite por valor e aprovação de supervisor. CRM e estoque só são acessíveis por adaptadores; pedidos aceita precondição de versão e chave de idempotência. Auditoria precisa reconstruir proposta, decisão de política, aprovação, chamada, resultado e compensação.

**Classes de solicitação.** O efeito de cada uma é o que a arquitetura precisa governar.

| Solicitação | Sistemas | Efeito |
|---|---|---|
| consultar status | pedidos | leitura |
| sugerir produto substituto | estoque + políticas | proposta |
| reservar substituto por 15 min | estoque/pedidos | escrita reversível |
| cancelar pedido aberto | pedidos + CRM | escrita material |
| conceder desconto excepcional | políticas + pedidos | impacto financeiro |
| alterar endereço após expedição | logística | alto risco de fraude |

Nenhuma das seis linhas tem hoje autoridade definida em componente: é isso que a Pergunta 1 endereça.

**Evidências do piloto.** Já existe um copiloto com workflow determinístico: identifica intenção, consulta dados por ferramentas de leitura e prepara orientação para o atendente executar. Três semanas com 40 atendentes e 640 solicitações:

| Observação | Resultado |
|---|---:|
| tempo médio de resolução, troca simples (antes / com copiloto) | 11 min / 7 min |
| seleção correta da ferramenta de leitura | 94% |
| orientações com política desatualizada | 9 em 640 |
| falhas de integração com pedidos (timeout) | 23 em 640 |
| solicitações em que a sequência de consulta variou de forma não prevista | 31% |

**Capacidades expostas pelos adaptadores**, nenhuma delas ainda invocável fora do fluxo conduzido pelo atendente: `consultar_cliente`, `consultar_pedido`, `buscar_estoque`, `avaliar_politica`, `reservar_item`, `liberar_reserva`, `propor_cancelamento`, `registrar_interacao`. A política comercial é versionada e consultável por API.

**Incógnitas.** Sem medição de custo por atendimento, de carga de revisão do supervisor, nem de comportamento sob conteúdo malicioso no texto do cliente. A direção quer decisão em duas semanas.

## As cinco perguntas

São perguntas de arquitetura: alocação de responsabilidades, atributos de qualidade em tensão, estilos de integração e acoplamento, limites de consistência e recuperação, estrutura e evolução. O modelo de linguagem é um elemento do sistema, não o assunto — nenhuma pergunta se resolve escolhendo modelo, prompt ou plataforma.

As perguntas sobem os níveis da [taxonomia de Bloom](../comecar/taxonomia-de-bloom.md): compreender, aplicar, analisar, avaliar e criar. De Aplicar para cima não há bloco de resposta; o feedback é do professor, sobre critérios, coerência e evidência.

### Pergunta 1 — Compreender · 3 min

> **Como as responsabilidades de gerar, decidir, autorizar e executar efeito estão hoje distribuídas entre os componentes da Vértice?**
>
> Se a escolha da reserva deixar de ser do atendente, qual dessas quatro responsabilidades muda de componente — e quais permanecem onde estão?

**Consulte:** [geração, decisão e ação](conceitos.md#geracao-decisao-e-acao), [responsabilidades e fronteiras de componente](conceitos.md#responsabilidades-e-fronteiras-de-componente) e [políticas como fronteira executável](conceitos.md#politicas-como-fronteira-executavel).

**Entrega esperada.** Uma tabela de quatro linhas — geração, decisão, autorização, efeito — com o componente responsável hoje e o componente responsável na proposta. Componentes, não ferramentas.

**Armadilha.** Concentrar decisão e autorização no mesmo componente. Se quem propõe é quem permite, a política deixou de ser fronteira.

### Pergunta 2 — Aplicar · 5 min

> **Quais atributos de qualidade entram em conflito nesta situação, e como se mede o conflito?**
>
> Segurança e latência, confiabilidade e custo, observabilidade e privacidade: escolha um par que a Vértice não consegue maximizar ao mesmo tempo. Que medida revela a tensão, e qual valor você aceitaria?

**Consulte:** o [catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md) e [características e tensões da autonomia](conceitos.md#caracteristicas-e-tensoes-da-autonomia).

**Entrega esperada.** Um cenário mensurável para um dos dois atributos do par, no formato Fonte/Estímulo/Ambiente/Artefato/Resposta/Medida, e uma frase dizendo o que se perde no outro atributo ao atender essa medida.

**Armadilha.** Escolher um par que não compete de verdade. Se as duas medidas melhoram juntas, não há decisão de arquitetura ali.

### Pergunta 3 — Analisar · 4 min

> **Que estilo de integração cada sistema exige, e onde ficam as fronteiras de confiança?**
>
> CRM, estoque, pedidos e política têm consistência, disponibilidade e propriedade diferentes. Onde chamada síncrona é adequada, onde mensageria ou evento reduz acoplamento, e onde o adaptador está encobrindo uma dependência que continua indisponível? Como a identidade do atendente atravessa cada fronteira sem virar credencial compartilhada?

**Consulte:** [APIs, mensageria, eventos e adaptadores](padroes-e-decisoes.md#apis-mensageria-eventos-e-adaptadores), [identidade do usuário e autorização delegada](padroes-e-decisoes.md#identidade-do-usuario-e-autorizacao-delegada) e o atributo [Segurança](../referencia/atributos-de-qualidade.md#seguranca).

**Entrega esperada.** Tabela de quatro linhas, uma por sistema, com estilo de integração escolhido, motivo em meia linha e como a identidade é propagada.

**Armadilha.** Adotar mensageria pelo desacoplamento e manter a expectativa de resposta imediata na experiência do atendente.

### Pergunta 4 — Avaliar · 6 min

> **Onde termina o limite transacional, e que invariante o sistema preserva quando um passo falha no meio?**
>
> Estoque e pedidos não compartilham transação. Diante de escrita sem confirmação no legado, que táticas você defende — idempotência, precondição de versão, consulta por chave, compensação, interrupção do fluxo — e a que preço em latência, complexidade operacional e carga de plantão? Que estado o sistema é obrigado a tornar visível para fora enquanto a inconsistência existe?

**Consulte:** [idempotência, concorrência e prevenção de repetição](padroes-e-decisoes.md#idempotencia-concorrencia-e-prevencao-de-repeticao), [consistência, transações e compensação](padroes-e-decisoes.md#consistencia-transacoes-e-compensacao), [timeout, retry e circuit breaker](padroes-e-decisoes.md#timeout-retry-e-circuit-breaker) e o atributo [Confiabilidade](../referencia/atributos-de-qualidade.md#confiabilidade).

**Entrega esperada.** O invariante enunciado em uma frase, as táticas escolhidas com o custo de cada uma, e o destino de uma compensação que falha. O estado visível para fora precisa distinguir duas situações que o cliente confunde: **a troca ainda não está concluída**, mas **a reserva temporária já pode estar ativa** e indisponibilizar o item até expirar ou ser liberada.

**Armadilha.** Tratar escrita sem confirmação como leitura sem resposta e repetir a chamada.

### Pergunta 5 — Criar · 5 min

> **Que estrutura você recomenda à direção em duas semanas, e sob que evidência ela se reverte?**
>
> Autoridade concentrada em um componente ou distribuída por domínio, com o custo de coordenação que isso implica? Capacidade padronizada comprada de um fornecedor ou construída, considerando fronteira de dados, versionamento e saída? E que medida em produção obrigaria a arquitetura a recuar da opção escolhida?

**Consulte:** [agente único e múltiplos agentes](conceitos.md#agente-unico-e-multiplos-agentes), [plataforma e obtenção de capacidade](padroes-e-decisoes.md#plataforma-e-obtencao-de-capacidade) e [fitness functions para autonomia](padroes-e-decisoes.md#fitness-functions-para-autonomia).

**Entrega esperada.** Meia página no formato do [template de ADR](../referencia/template-adr.md): decisão estrutural, duas opções descartadas com o motivo, a evidência do dossiê que sustenta a escolha, duas fitness functions com limite numérico e ação automática, e o gatilho de recuo.

**Armadilha.** Distribuir por domínio porque há quatro sistemas. Fronteira de componente se justifica por autoridade, dado e ritmo de mudança — não pelo número de integrações.

## Plenária

Três minutos: cada grupo diz onde colocou a autorização, qual atributo de qualidade sacrificou e qual medida obrigaria a arquitetura a recuar. O confronto útil está nos grupos que chegaram a decisões opostas com a mesma evidência — aí a pergunta é qual incógnita do dossiê separa as duas leituras.

Para aprofundar depois da aula, ver [Classificação de autonomia](exercicios.md#11-classificacao-de-autonomia), [Diagnóstico de trace](exercicios.md#14-diagnostico-de-trace) e [Arquitetura de agente controlado](exercicios.md#18-arquitetura-de-agente-controlado) em [Exercícios](exercicios.md).
