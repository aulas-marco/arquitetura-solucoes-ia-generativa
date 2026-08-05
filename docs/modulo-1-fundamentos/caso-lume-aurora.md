# Caso contínuo: Banco Lume e Cooperativa Aurora — antes da arquitetura

Este módulo apresenta dois casos que atravessam todo o curso: o **Banco Lume** (contestação de transações) e a **Cooperativa Aurora** (renegociação de crédito). Eles são tratados em detalhe a partir do [Módulo 2](../modulo-2-desenho-conceitual/caso-lume-aurora.md); aqui aparecem apenas na forma anterior a qualquer arquitetura — a mesma forma do [caso Horizonte](estudo-de-caso.md) desta página: uma oportunidade, uma linha de base e quatro decisões ainda não separadas.

Não pressuponha RAG, agente ou qualquer composição. O objetivo deste módulo é reconhecer, nos dois casos, a superfície comportamental e a diferença entre geração, decisão, autorização e efeito — antes de decidir o que construir.

## Banco Lume

**Situação.** Analistas preparam contestações de compra não reconhecida consultando casos, cadastro e políticas. A liderança quer reduzir o tempo de análise sem abrir mão de revisão humana e rastreabilidade.

**Evidências iniciais.** Mediana de 22 minutos por caso; 8% dos casos voltam por evidência incompleta; 4% ultrapassam o prazo interno. A amostra mistura casos de complexidade desigual e não isola causa — parte do tempo pode ser busca evitável, parte pode ser julgamento necessário.

**Quatro decisões a separar.**

1. **Produção.** Regras e templates já respondem a parte do fluxo (dados cadastrais, prazos). Geração poderia reformular políticas e preparar rascunho de justificativa — mas isso ainda não decide se deve.
2. **Conhecimento.** O problema central é localizar a política vigente e o dado autorizado do caso, não necessariamente “buscar” num sentido amplo — o corpus inicial é pequeno e mapeável.
3. **Efeito.** Nenhum efeito automático é cogitado neste incremento: abrir, alterar ou registrar decisão continuam humanos.
4. **Operação e confiança.** Hospedagem, retenção e fallback diante de indisponibilidade permanecem decisões próprias, independentes de qual composição de geração for escolhida.

**Classificação de evidências.**

| Tipo | O que mediria no Lume |
|---|---|
| Teste de software | o rascunho nunca inclui campo fora da finalidade de contestação |
| Avaliação comportamental | proporção de rascunhos com afirmação sustentada por política vigente |
| Verificação arquitetural | tempo, cobertura de evidência e comportamento sob indisponibilidade do modelo permanecem nos limites do modo sombra |

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

## O que os dois casos compartilham — e onde já divergem

Os dois partem de uma demonstração convincente que antecipou uma solução ("agente que resolve tudo") antes de qualquer evidência representativa. Nos dois, produção, conhecimento, efeito e operação são decisões distintas que podem evoluir em ritmos diferentes. A diferença já visível nesta etapa está no conhecimento: o corpus do Lume é pequeno e mapeável por categoria; o da Aurora depende de sistemas legados em lote e cresce por campanha. Essa diferença reaparece no [Módulo 3](../modulo-3-rag/caso-lume-aurora.md) como o motivo pelo qual as duas soluções adotam RAG em momentos e formas diferentes, e no [Módulo 4](../modulo-4-agentes/caso-lume-aurora.md) como o motivo pelo qual apenas uma delas justifica autonomia de agente.

**Continuação:** [Módulo 2 — desenho conceitual completo dos dois casos](../modulo-2-desenho-conceitual/caso-lume-aurora.md).
