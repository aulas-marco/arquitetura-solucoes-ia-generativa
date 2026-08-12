# Caso contínuo: Banco Lume — desenho conceitual

**Caso contínuo — Banco Lume.** [← Módulo 1: Antes da arquitetura](../modulo-1-fundamentos/caso-lume.md) · [Módulo 3: RAG →](../modulo-3-rag/caso-lume.md)

O desenho conceitual completo do Banco Lume **é** o [Exemplo arquitetural](exemplo-arquitetural.md) deste módulo — cinco visões, RAS, árvore de utilidade, matriz de alternativas e duas ADRs, resolvidas pelo professor. Esta página não duplica esse documento; ela resume as duas decisões que o restante do caso contínuo (Módulos 3 a 6) retoma, para quem está acompanhando o Lume de ponta a ponta.

## ADR-001 — Workflow assistivo, sem ferramentas autônomas

O Lume adota um **workflow assistivo**: o orquestrador segue consultas e transições definidas, e o modelo produz apenas o rascunho contextualizado a partir delas. Analista recomenda; supervisor aprova ou devolve antes do registro oficial. Um agente de leitura foi avaliado e rejeitado por ora — acrescentaria estado, contratos e orçamento de passos sem evidência de que a sequência (hoje conhecida e repetível) precise variar.

**Gatilho de revisão.** Reavaliar somente se uma atividade adicional demonstrar, em casos representativos, sequência não enumerável, benefício mensurável acima do workflow, autoridade clara por ferramenta e recuperação proporcional diante de falha. Ver como esse gatilho se comporta no [Módulo 4](../modulo-4-agentes/caso-lume.md).

## ADR-002 — Contexto selecionado antes de RAG

O primeiro incremento cobre uma categoria de contestação com doze políticas curtas, versionadas e mapeáveis manualmente. Em vez de RAG, adaptadores obtêm os campos permitidos e a política correspondente; o montador de contexto registra origem, versão e vigência — sem índice nem recuperação semântica.

**Gatilho de revisão.** Reavaliar se a cobertura de evidência ficar abaixo de 95% apesar de fontes disponíveis, ou se o corpus superar a seleção explícita. Ver como esse gatilho se cumpre no [Módulo 3](../modulo-3-rag/caso-lume.md).

## Continuidade

Os dois gatilhos acima — não o desejo de "ter RAG" ou "ter um agente" — são o que decide o próximo passo do Lume. O [Módulo 3](../modulo-3-rag/caso-lume.md) mostra o primeiro se cumprindo; o [Módulo 4](../modulo-4-agentes/caso-lume.md) mostra o segundo continuando **não** cumprido, por decisão deliberada.

A [Cooperativa Aurora](caso-aurora.md) tem, neste mesmo módulo, seu Documento de Arquitetura de Software completo resolvido do zero — ela parte de evidências e restrições diferentes das do Lume, e por isso não repete a mesma dupla de decisões.

---

**Continua:** [Módulo 3 — RAG](../modulo-3-rag/caso-lume.md)
