# Caso contínuo: Banco Lume — antes da arquitetura

**Caso contínuo — Banco Lume.** Próximo: [Módulo 2 — Desenho conceitual →](../modulo-2-desenho-conceitual/caso-lume.md)

Este é o primeiro módulo de um caso que atravessa todo o curso. O **Banco Lume** (contestação de transações) tem uma irmã de percurso, a **Cooperativa Aurora** (renegociação de crédito), tratada em [sua própria página](caso-aurora.md) — os dois partem da mesma pergunta, mas acumulam evidência diferente e chegam a decisões diferentes a cada módulo. Aqui, antes de qualquer arquitetura, o Lume aparece na mesma forma do [caso Horizonte](estudo-de-caso.md) desta página: uma oportunidade, uma linha de base e quatro decisões ainda não separadas.

Não pressuponha RAG, agente ou qualquer composição. O objetivo deste módulo é reconhecer a superfície comportamental do caso e a diferença entre geração, decisão, autorização e efeito — antes de decidir o que construir.

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

## O que este caso compartilha com a Aurora — e onde já diverge

O Lume parte, como a Aurora, de uma demonstração convincente que antecipou uma solução ("a IA resolve isso") antes de qualquer evidência representativa. Produção, conhecimento, efeito e operação são decisões distintas que podem evoluir em ritmos diferentes — esse princípio vale para os dois casos igualmente. A diferença já visível nesta etapa está no conhecimento: o corpus do Lume é pequeno e mapeável por categoria, enquanto o da [Aurora](caso-aurora.md) depende de sistemas legados em lote e cresce por campanha. Essa diferença reaparece no [Módulo 3](../modulo-3-rag/caso-lume.md) como o motivo pelo qual o Lume adota RAG num momento e por um caminho diferente da Aurora, e no [Módulo 4](../modulo-4-agentes/caso-lume.md) como o motivo pelo qual só a Aurora justifica autonomia de agente.

---

**Continua:** [Módulo 2 — desenho conceitual completo](../modulo-2-desenho-conceitual/caso-lume.md)
