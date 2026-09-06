# Padrões e decisões

Esta página foi reorganizada. O conteúdo que estava aqui passou a viver em páginas temáticas, cada uma cobrindo uma decisão do começo ao fim. A tabela abaixo diz onde cada seção anterior está agora, e os endereços antigos continuam funcionando por este índice.

| Seção anterior | Onde está agora |
|---|---|
| <a id="agente-unico-versus-multiplos-agentes"></a>Agente único versus múltiplos agentes | [Onde está o controle](controle-e-autonomia.md#agente-unico-versus-multiplos-agentes) |
| <a id="comece-pelo-contrato-de-ferramenta"></a>Comece pelo contrato de ferramenta | [Ferramentas e contratos](ferramentas-e-contratos.md#comece-pelo-contrato-de-ferramenta) |
| <a id="reduzir-o-espaco-de-decisao-antes-de-trocar-o-modelo"></a>Reduzir o espaço de decisão antes de trocar o modelo | [Ferramentas e contratos](ferramentas-e-contratos.md#reduzir-o-espaco-de-decisao-antes-de-trocar-o-modelo) |
| <a id="apis-mensageria-eventos-e-adaptadores"></a>APIs, mensageria, eventos e adaptadores | [Ferramentas e contratos](ferramentas-e-contratos.md#apis-mensageria-eventos-e-adaptadores) |
| <a id="identidade-do-usuario-e-autorizacao-delegada"></a>Identidade do usuário e autorização delegada | [Efeito, identidade e recuperação](efeito-e-recuperacao.md#identidade-do-usuario-e-autorizacao-delegada) |
| <a id="idempotencia-concorrencia-e-prevencao-de-repeticao"></a>Idempotência, concorrência e prevenção de repetição | [Efeito, identidade e recuperação](efeito-e-recuperacao.md#idempotencia-concorrencia-e-prevencao-de-repeticao) |
| <a id="timeout-retry-e-circuit-breaker"></a>Timeout, retry e circuit breaker | [Efeito, identidade e recuperação](efeito-e-recuperacao.md#timeout-retry-e-circuit-breaker) |
| <a id="consistencia-transacoes-e-compensacao"></a>Consistência, transações e compensação | [Efeito, identidade e recuperação](efeito-e-recuperacao.md#consistencia-transacoes-e-compensacao) |
| <a id="auditoria-e-observabilidade"></a>Auditoria e observabilidade | [Efeito, identidade e recuperação](efeito-e-recuperacao.md#auditoria-e-observabilidade) |
| <a id="matriz-de-autonomia"></a>Matriz de autonomia | [Autonomia orçada](autonomia-orcada.md#matriz-de-autonomia) |
| <a id="orcamentos-interrupcao-e-fallback"></a>Orçamentos, interrupção e fallback | [Autonomia orçada](autonomia-orcada.md#orcamentos-interrupcao-e-fallback) |
| <a id="fitness-functions-para-autonomia"></a>Fitness functions para autonomia | [Autonomia orçada](autonomia-orcada.md#fitness-functions-para-autonomia) |
| <a id="plataforma-e-obtencao-de-capacidade"></a>Plataforma e obtenção de capacidade | [Autonomia orçada](autonomia-orcada.md#plataforma-e-obtencao-de-capacidade) |
| <a id="escolher-o-nivel-de-loop-e-a-condicao-de-parada"></a><a id="quando-nao-usar-laco"></a><a id="fitness-functions-de-um-laco"></a>Escolher o nível de loop e a condição de parada | [Loops](loops.md#escolher-o-nivel-de-loop-e-a-condicao-de-parada) |
| <a id="padrao-desenvolvimento-guiado-por-especificacao"></a>Padrão — Desenvolvimento guiado por especificação | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#padrao-desenvolvimento-guiado-por-especificacao) |
| <a id="decisao-1-escolher-a-profundidade-proporcional"></a>Decisão 1 — escolher a profundidade proporcional | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#decisao-1-escolher-a-profundidade-proporcional) |
| <a id="decisao-2-separar-o-que-de-como"></a>Decisão 2 — separar “o quê” de “como” | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#decisao-2-separar-o-que-de-como) |
| <a id="decisao-3-formular-criterios-antes-de-tarefas"></a>Decisão 3 — formular critérios antes de tarefas | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#decisao-3-formular-criterios-antes-de-tarefas) |
| <a id="decisao-4-fatiar-verticalmente"></a>Decisão 4 — fatiar verticalmente | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#decisao-4-fatiar-verticalmente) |
| <a id="decisao-5-escolher-seams-duraveis"></a>Decisão 5 — escolher seams duráveis | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#decisao-5-escolher-seams-duraveis) |
| <a id="decisao-6-usar-revisao-em-dois-eixos"></a>Decisão 6 — usar revisão em dois eixos | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#decisao-6-usar-revisao-em-dois-eixos) |
| <a id="decisao-7-tratar-seguranca-como-parte-da-transformacao"></a>Decisão 7 — tratar segurança como parte da transformação | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#decisao-7-tratar-seguranca-como-parte-da-transformacao) |
| <a id="decisao-8-manter-os-artefatos-coerentes"></a>Decisão 8 — manter os artefatos coerentes | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#decisao-8-manter-os-artefatos-coerentes) |
| <a id="adr-onde-colocar-os-gates-do-fluxo-sdd"></a>ADR — onde colocar os gates do fluxo SDD | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#adr-onde-colocar-os-gates-do-fluxo-sdd) |
| <a id="adr-spec-kit-como-fio-operacional-nao-como-metodologia-exclusiva"></a>ADR — Spec Kit como fio operacional, não como metodologia exclusiva | [Decisões, ADRs e limites do fluxo](sdd-decisoes.md#adr-spec-kit-como-fio-operacional-nao-como-metodologia-exclusiva) |

Comece pelo [mapa do módulo](index.md).
