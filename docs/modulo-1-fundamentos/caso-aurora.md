# Caso contínuo: Cooperativa Aurora — antes da arquitetura

**Caso contínuo — Cooperativa Aurora.** Próximo: [Módulo 2 — Desenho conceitual →](../modulo-2-desenho-conceitual/caso-aurora.md)

Este é o primeiro módulo de um caso que atravessa todo o curso. A **Cooperativa Aurora** (renegociação de crédito) tem uma irmã de percurso, o **Banco Lume** (contestação de transações), tratado em [sua própria página](caso-lume.md) — os dois partem da mesma pergunta, mas acumulam evidência diferente e chegam a decisões diferentes a cada módulo. Aqui, antes de qualquer arquitetura, a Aurora aparece na mesma forma do [caso Horizonte](estudo-de-caso.md) desta página: uma oportunidade, uma linha de base e quatro decisões ainda não separadas.

Não pressuponha RAG, agente ou qualquer composição. O objetivo deste módulo é reconhecer a superfície comportamental do caso e a diferença entre geração, decisão, autorização e efeito — antes de decidir o que construir.

## Cooperativa Aurora

**Situação.** Especialistas preparam propostas de renegociação de crédito consultando contratos, pagamentos, políticas de campanha e registros de contato. Uma demonstração de modelo convincente levou o patrocinador a chamar a iniciativa de “agente de renegociação” antes de qualquer desenho.

**Evidências iniciais.** Mediana de 31 minutos por solicitação (p90: 74); 42% do tempo classificado como busca e transcrição; 11% das propostas voltam por documento ausente ou política incorreta; concordância de 76% entre especialistas sobre “melhor proposta”. A amostra mistura três campanhas e não mede satisfação do cliente.

**Quatro decisões a separar.**

1. **Produção.** Parte do cálculo (elegibilidade, faixas) é regra estável; a redação da explicação ao cliente é o único ponto onde geração parece agregar valor hoje.
2. **Conhecimento.** Contratos e políticas de campanha vêm de sistemas legados heterogêneos, alguns só em lote — a pergunta de "como" recuperar essa evidência é mais restrita que no Lume, não mais ampla.
3. **Efeito.** Revisão humana obrigatória e segregação entre quem propõe e quem aprova são restrições já confirmadas; nenhuma gravação automática é cogitada.
4. **Operação e confiança.** Residência de dados, retenção de até 24 horas para conteúdo de inferência e continuidade do fluxo manual durante indisponibilidade dos sistemas legados são decisões independentes da composição escolhida.

**Classificação de evidências.**

| Tipo | O que mediria na Aurora |
|---|---|
| Teste de software | proposta nunca atravessa para aprovação sem passar por especialista distinto do autor |
| Avaliação comportamental | concordância entre especialistas sobre explicação e cálculo, com e sem apoio de geração |
| Verificação arquitetural | tempo de preparação, taxa de devolução e comportamento diante de sistema legado indisponível permanecem nos limites definidos |

## O que este caso compartilha com o Lume — e onde já diverge

A Aurora parte, como o [Lume](caso-lume.md), de uma demonstração convincente que antecipou uma solução ("agente que resolve tudo") antes de qualquer evidência representativa. Produção, conhecimento, efeito e operação são decisões distintas que podem evoluir em ritmos diferentes — esse princípio vale para os dois casos igualmente. A diferença já visível nesta etapa está no conhecimento: o corpus da Aurora depende de sistemas legados em lote e cresce por campanha, enquanto o do Lume é pequeno e mapeável por categoria. Essa diferença reaparece no [Módulo 3](../modulo-3-rag/caso-aurora.md) como o motivo pelo qual a Aurora adota RAG por um caminho diferente do Lume, e no [Módulo 4](../modulo-4-agentes/caso-aurora.md) como o motivo pelo qual só a Aurora justifica autonomia de agente.

---

**Continua:** [Módulo 2 — desenho conceitual completo](../modulo-2-desenho-conceitual/caso-aurora.md)
