# Conceitos: conhecimento externo e os dois pipelines

![Mapa RAG dos dois pipelines: no fluxo offline, fontes governadas passam por extração, fragmentação, metadados e permissões até um índice versionado; no fluxo online, uma pergunta autorizada recupera evidências para uma resposta citada ou para abstenção, ligadas por proveniência e atualidade](../assets/images/m03-mapa-rag-dos-dois-pipelines.png "Mapa RAG dos dois pipelines")

*Figura — RAG combina dois pipelines: ingestão governada e consulta autorizada, unidos por evidência, atualização e proveniência.*

RAG conecta uma pergunta a evidências externas antes da geração. Para projetá-lo, precisamos distinguir quatro objetos que interfaces de chat costumam misturar: o que o modelo aprendeu, o que a organização declara como fonte, o que a recuperação seleciona e o que a geração afirma.

## Conhecimento paramétrico e fontes corporativas

**Conhecimento paramétrico** é a regularidade incorporada aos parâmetros durante treinamento. Ele apoia linguagem, padrões gerais e tarefas amplas; fontes corporativas exigem mecanismos separados de versão, autorização e consulta:

- o corte temporal e a cobertura podem não corresponder ao momento da consulta;
- uma afirmação não traz, automaticamente, fonte, versão ou autorização;
- atualizar um contrato não altera imediatamente os parâmetros;
- ausência de evidência não impede que o modelo complete uma resposta plausível;
- conteúdo aprendido não oferece consulta determinística por registro.

Fine-tuning pode modificar comportamento, formato ou desempenho numa tarefa. Para fatos que mudam diariamente ou exigem exclusão auditável, o conhecimento precisa permanecer em fonte versionada e consultável durante a execução. RAG reduz o tempo entre publicação e disponibilidade, mantendo visíveis os riscos de recuperação e geração.

## Quatro planos do sistema RAG

### Plano de conhecimento

Contém fontes sob governança: políticas, contratos, manuais, decisões, tabelas, registros e dados operacionais. Cada fonte tem dono, finalidade, classificação, vigência, versão e regra de retenção. “Documento disponível” não significa “documento autorizado para toda pergunta”.

### Plano de preparação e recuperação

Transforma fontes em representações pesquisáveis e, durante a consulta, produz um conjunto ordenado de candidatos. Embeddings, índices vetoriais e índices lexicais vivem aqui, assim como filtros, fusão e reranking. O resultado segue para validação de suficiência, vigência e suporte antes da resposta.

### Plano de geração

Recebe instruções, pergunta e contexto delimitado. O modelo sintetiza, compara ou explica. Deve distinguir conteúdo recuperado de instruções do sistema, referenciar identificadores e não preencher lacunas como se fossem fatos.

### Plano de controle e evidência

Aplica identidade, autorização, segurança, validação, observabilidade, avaliação e auditoria. Ele atravessa os demais planos. Sem esse plano, é possível recuperar corretamente o conteúdo errado para a pessoa errada.

### Responsabilidades e acoplamentos

O **motor de políticas** decide o universo autorizado; o **recuperador** localiza candidatos apenas nesse universo; o **reranker** reordena candidatos permitidos; o **montador de contexto** conserva limite, versão e proveniência; a **validação** verifica suporte e política de saída; e **adaptadores** isolam conectores, índices e provedores. Cada componente deve mudar por uma razão dominante: trocar o índice não deve reescrever política, e trocar o modelo não deve alterar a proveniência da fonte. Separar componentes sem necessidade também acrescenta chamadas, latência e operação; a fronteira se justifica por risco, mudança independente ou característica arquitetural.

## Fontes e formatos

O corpus pode combinar:

- **documentos não estruturados:** texto corrido, e-mails aprovados, atas e páginas;
- **documentos semiestruturados:** contratos com cláusulas, manuais com seções, formulários e catálogos;
- **dados estruturados:** tabelas, cadastros e registros consultados com semântica explícita;
- **conteúdo multimodal:** documentos digitalizados, tabelas em imagem, gráficos ou áudio transcrito;
- **fontes externas controladas:** normas e manuais públicos cuja origem e atualização são verificadas.

Nem tudo deve ser convertido em texto e colocado no mesmo índice. Um saldo atual, uma data de vigência ou uma lista de centros de custo pode exigir consulta estruturada e validação de esquema. Um contrato pede preservação de hierarquia e numeração. Um documento digitalizado exige OCR e indicador de qualidade. O desenho começa pela semântica e pelo risco da fonte.

## Fluxo offline: da fonte ao conhecimento pesquisável

“Offline” significa fora do caminho síncrono da pergunta, não necessariamente processamento em lote. Um evento pode disparar ingestão em segundos.

**LangChain** e **LlamaIndex** organizam recuperação; **Chroma** e **Qdrant** armazenam e buscam vetores. Não substituem fonte, autorização ou evidência.

1. **Aquisição:** conectores leem fontes aprovadas com identidade de serviço, escopo mínimo e registro de origem. O pipeline captura exclusões e alterações, não apenas inclusões.
2. **Extração:** conteúdo, estrutura, tabelas e atributos são obtidos. Falhas de OCR, páginas ilegíveis e seções vazias tornam-se estados explícitos.
3. **Normalização:** codificação, espaços, cabeçalhos, datas e formatos são padronizados sem apagar significado jurídico ou operacional. A versão bruta permanece rastreável.
4. **Classificação e validação:** tipo, sensibilidade, dono, vigência e qualidade mínima são verificados. Um item inválido vai para quarentena, não para produção.
5. **Segmentação:** a fonte é dividida em chunks por estrutura, semântica, tamanho e tarefa. Cada chunk preserva título, seção, posição e vínculo com vizinhos.
6. **Enriquecimento de metadados:** fonte, versão, validade, tenant, grupos, jurisdição, idioma e identificadores são anexados. Metadados usados em autorização precisam vir de autoridade confiável.
7. **Representação:** embeddings são calculados para busca semântica; termos e campos alimentam busca lexical; relações ou resumos podem alimentar níveis hierárquicos.
8. **Indexação:** representações e conteúdo autorizado são publicados de forma consistente. Um manifesto liga versão da fonte, extrator, estratégia de chunking, modelo de embedding e índice.
9. **Promoção:** testes de qualidade, cobertura, autorização e recuperação aprovam uma versão candidata antes da troca atômica ou gradual.
10. **Atualização e exclusão:** eventos, reconciliação periódica e validade temporal propagam mudanças. Reprocessamento deve ser idempotente e permitir rollback.
11. **Monitoramento:** atraso de ingestão, falhas por fonte, chunks órfãos, divergência entre origem e índice e crescimento anormal geram alertas.

### Segmentação é decisão de recuperação

Um chunk pequeno pode localizar a frase correta, mas perder definição, exceção ou sujeito. Um chunk grande preserva contexto, porém mistura assuntos, ocupa janela e reduz precisão. Estratégias comuns incluem tamanho fixo com sobreposição, divisão por parágrafo ou seção, segmentação semântica e estruturas pai–filho. A escolha deve ser testada com perguntas reais, não decidida apenas por número de tokens.

Um bom identificador de chunk é estável o bastante para citação e reprocessamento, mas incorpora a versão que altera seu conteúdo. Ele permite voltar ao documento, à seção e ao intervalo original.

### Embeddings, recuperação e autorização

Embeddings representam itens num espaço onde proximidade pode refletir semântica. [Sentence-BERT](https://aclanthology.org/D19-1410/) é uma fonte primária sobre embeddings de sentenças; [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/) demonstra recuperação densa de passagens. A autorização continua sob responsabilidade da política de acesso, e buscas lexicais complementam a recuperação para termos exatos, números de cláusula, códigos e datas.

## Fluxo online: da pergunta à resposta apoiada

1. **Autenticação e contexto de finalidade:** o sistema recebe identidade validada, tenant, grupos, atributos e finalidade permitida.
2. **Validação da entrada:** limites de tamanho, idioma, escopo e conteúdo abusivo são verificados. A pergunta não recebe poder para alterar políticas.
3. **Transformação da consulta:** o orquestrador pode corrigir termos, expandir siglas, produzir filtros temporais, decompor questões ou gerar consultas lexical e semântica. A transformação é observável e limitada.
4. **Determinação do universo autorizado:** o motor de políticas calcula quais fontes e atributos são elegíveis. A autorização acompanha a recuperação e usa política negadora por padrão.
5. **Recuperação de candidatos:** busca lexical, vetorial, estruturada ou combinações retornam itens com identificadores e escores próprios.
6. **Fusão e reranking:** resultados são normalizados, deduplicados e reordenados por relevância para a pergunta, sem reintroduzir item proibido.
7. **Verificação de suficiência:** cobertura, diversidade, vigência, conflito e limiar de relevância determinam se há base para responder. A decisão combina esses sinais, em vez de depender de um escore isolado.
8. **Montagem de contexto:** trechos são organizados com título, versão, data, seção e marcador de confiança dentro do orçamento de tokens. Instruções e evidências ficam separadas.
9. **Geração:** o modelo recebe contrato para responder apenas com apoio, explicitar limites e associar afirmações materiais a identificadores.
10. **Validação:** estrutura, citações, suporte, política de saída e exposição de dados são verificados. Algumas checagens são determinísticas; outras usam modelos ou revisão humana.
11. **Resposta ou abstenção:** o usuário recebe resposta citada, pergunta de esclarecimento, resultado parcial ou declaração de evidência insuficiente.
12. **Telemetria e feedback:** o trace registra versões e decisões sem copiar conteúdo sensível desnecessário. Feedback vira hipótese para avaliação, não rótulo automático.

## Proveniência de ponta a ponta

Proveniência é a cadeia que permite reconstruir origem e transformação. No mínimo, cada evidência deve ligar:

`fonte → versão → localização → aquisição → extração → chunk → metadados → representação → índice → consulta → contexto → citação`.

Também é preciso versionar política de acesso, transformador de consulta, modelo de embedding, algoritmo de fusão, reranker, template de contexto, prompt e modelo gerador. Um trace completo pode registrar identificadores, hashes, versões, tempos e decisões, em lugar do conteúdo integral, conforme retenção e privacidade.

RAG preserva essa cadeia quando o pipeline registra origem, autoridade, versão, transformação e uso verificáveis. Índice vetorial, citação na interface e trace precisam compor esse registro, cada qual com sua responsabilidade.

## Atualidade, consistência e temporalidade

“Atual” precisa de medida. Uma política publicada às 10h pode ter SLO de disponibilidade até 10h15; uma exclusão por incidente pode exigir propagação em dois minutos. Defina atraso máximo por fonte, comportamento durante reindexação e regra para consultas no intervalo. Índices azul–verde, manifestos e troca atômica evitam misturar versões incompatíveis.

Vigência difere de data de ingestão. A consulta “qual política valia em janeiro?” requer recuperação temporal, enquanto “qual vale agora?” deve excluir versões expiradas. Conflitos entre fontes não devem ser resolvidos por similaridade: autoridade, jurisdição e precedência pertencem à governança do conhecimento.

## Propriedades que o desenho precisa assegurar

RAG oferece mecanismos para projetar e avaliar qualidade de fonte, recuperação relevante, autorização, orçamento de contexto, fidelidade da geração e suporte de citações. Cada propriedade depende de decisões, controles e evidências próprios.

Essa separação orienta o diagnóstico:

- **fonte ausente:** corrigir cobertura e aquisição;
- **conteúdo mal extraído:** corrigir parser ou OCR;
- **evidência existe, mas não aparece:** revisar segmentação, consulta e recuperação;
- **candidato correto perde posição:** revisar fusão e reranking;
- **contexto correto, resposta infiel:** revisar montagem, prompt, modelo e validação;
- **conteúdo correto, acesso indevido:** interromper, conter e corrigir autorização antes de otimizar qualidade.

Os dois pipelines formam um único produto operacional. A próxima página transforma suas etapas em decisões: quando combinar sinais, onde filtrar, como montar contexto, quando recusar e qual variante de RAG acrescenta valor.

## Ferramentas no mercado

Compare papéis e condições no [Guia de ferramentas](../referencia/guia-de-ferramentas.md).

| Ferramenta | Quando ajuda | Pré-requisito | Limite arquitetural |
|---|---|---|---|
| LangChain | Compor recuperação. | Contratos de documentos e modelo. | Não prova autorização ou suficiência. |
| LlamaIndex | Estruturar índices e conectores. | Fontes e metadados classificados. | Não confere autoridade ou atualização. |
| Chroma | Testar coleção vetorial. | Embedding, persistência e metadados. | Similaridade exige validação de suporte e política de acesso. |
| Qdrant | Buscar vetores com filtros. | Serviço, embedding e acesso externos. | Filtros operam sob política de autorização. |

**Próxima página:** [Padrões e decisões de recuperação](padroes-e-decisoes.md).
