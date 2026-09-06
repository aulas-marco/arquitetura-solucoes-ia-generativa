# Que informação atravessa o sistema

Seis artefatos com ciclos de vida distintos circulam por uma solução generativa, e confundi-los é a origem de boa parte dos erros de projeto.

## Que informação atravessa o sistema

Informação entra no sistema como pedido, instrução, fonte, resultado intermediário ou registro operacional. O mesmo conteúdo não deve conservar automaticamente a mesma finalidade ao mudar de etapa. Um documento autorizado para consulta, por exemplo, pode ser usado como evidência sem se tornar memória de conversa ou conteúdo integral de telemetria.

### Artefatos com ciclos de vida diferentes

| Elemento | Função | Questão de ciclo de vida |
|---|---|---|
| Conhecimento | conteúdo mantido por uma fonte responsável | versão, vigência, autorização e descarte |
| Contexto | informação selecionada para uma execução | finalidade, minimização e expiração |
| Estado | posição e resultados intermediários de um fluxo | consistência, recuperação e concorrência |
| Memória | informação preservada entre interações | escopo, consentimento, retenção e correção |
| Evidência | registro que sustenta ou refuta uma afirmação ou decisão | origem, autoridade, transformação e uso |
| Trace | encadeamento de eventos e versões de uma execução | correlação, minimização, acesso e retenção |

**Proveniência** registra de onde a informação veio, por quais transformações passou e quais versões participaram do resultado. Ela permite reconstruir a cadeia de custódia, mas não prova sozinha que a fonte era correta, atual ou autorizada para aquela finalidade.

Recuperar um documento não o transforma em memória. Histórico de conversa não é fonte de verdade. Trace não autoriza armazenar todo o conteúdo. Essas distinções determinam fronteiras de acesso, retenção e responsabilidade.

### Embeddings e representação semântica

Um **embedding** é uma representação vetorial aprendida de um conteúdo. A proximidade entre vetores pode ajudar a localizar candidatos semanticamente relacionados, agrupar itens ou comparar representações.

O embedding preserva uma representação útil para cálculo, não a autoridade da fonte. Um mecanismo de recuperação ainda precisa de consulta, índices, metadados, filtros, ranking e avaliação. O [Módulo 3](../modulo-3-rag/index.md) mostrará como origem, versão e autorização atravessam ingestão e consulta.

Depois de identificar o que circula, o arquiteto pode decidir quem gera, quem julga e quem produz efeitos.
