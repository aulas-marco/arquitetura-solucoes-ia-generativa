# Avaliação e fitness functions

Medir recuperação e geração em camadas separadas, e transformar o que foi decidido em verificação contínua.

## Avaliação por camada e ponta a ponta

Um conjunto de avaliação precisa conter perguntas reais ou representativas, fonte e versão de referência, evidências relevantes, itens parcialmente relevantes, casos sem resposta, conflitos, mudanças temporais, grupos de permissão e consultas adversariais. Separe desenvolvimento e teste; estratifique por fonte, idioma, tipo, risco e dificuldade.

### Recuperação

- **Recall@k:** fração das evidências relevantes presentes nos k primeiros; importante quando perder um trecho crítico inviabiliza a resposta.
- **Precision@k:** fração dos k resultados que é relevante; aproxima desperdício do orçamento de contexto.
- **MRR:** valoriza a posição da primeira evidência relevante.
- **nDCG:** considera graus de relevância e posição.
- **cobertura de filtros:** itens autorizados recuperáveis e itens proibidos nunca materializados.

### Contexto, geração e citação

Meça precisão e cobertura do contexto, fidelidade das afirmações, relevância da resposta, correção e completude de citações, tratamento de conflito e calibração da abstenção. O artigo [RAGAs](https://aclanthology.org/2024.eacl-demo.16/) propõe dimensões automatizadas para avaliar RAG; avaliadores automáticos auxiliam escala, mas devem ser calibrados com julgamento humano e casos críticos.

### Sistema e resultado

Meça latência por etapa e percentis, custo por consulta, taxa de erro e timeout, atraso de atualização, violações de autorização, reconstrução de trace, utilidade para a tarefa, correções humanas e impacto no processo. Uma melhoria de recall que dobra latência pode não atender ao RAS. Uma resposta apoiada pode continuar inútil.

Execute testes offline antes de promover índice, canário ou shadow em mudanças de alto risco e monitoramento online após liberação. Mudanças em corpus, chunking, embedding, consulta, ranking, prompt ou modelo exigem pacote de versões e comparação reproduzível.

Na próxima página, essas decisões aparecem em uma arquitetura de referência sem fornecedor, com fluxos separados e uma consulta reconstruída passo a passo.

**Próxima página:** [Exemplo arquitetural de RAG](exemplo-arquitetural.md).

## Fitness functions de RAG

Fitness functions transformam características prioritárias em verificações contínuas que impedem promoção ou acionam revisão:

- **autorização:** nenhum item proibido é materializado no recuperador, reranker, cache ou contexto em testes por tenant e grupo;
- **atualidade:** publicação, revogação e exclusão atingem seus SLOs por fonte; falha bloqueia a promoção do índice;
- **recuperação:** Recall@k, nDCG e cobertura de evidência não caem abaixo dos limites acordados por segmento crítico;
- **proveniência:** toda afirmação material expõe fonte, versão, localização e transformação de contexto compatíveis com a política;
- **evolução:** alterações em chunking, embedding, ranking, prompt ou modelo produzem manifesto de versões e comparação reproduzível antes de canário ou troca gradual.

## Ferramentas no mercado

Compare papéis e condições no [Guia de ferramentas](../referencia/guia-de-ferramentas.md).

| Ferramenta | Quando ajuda | Pré-requisito | Limite arquitetural |
|---|---|---|---|
| LangChain | Compor recuperação. | Contratos de documentos e modelo. | Não prova autorização ou suficiência. |
| LlamaIndex | Estruturar índices e conectores. | Fontes e metadados classificados. | Não confere autoridade ou atualização. |
| Chroma | Testar coleção vetorial. | Embedding, persistência e metadados. | Similaridade exige validação de suporte e política de acesso. |
| Qdrant | Buscar vetores com filtros. | Serviço, embedding e acesso externos. | Filtros operam sob política de autorização. |

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
