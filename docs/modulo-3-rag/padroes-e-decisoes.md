# Padrões e decisões: recuperar, autorizar e sustentar

Cada mecanismo de RAG responde a uma falha possível. A decisão não é “qual banco vetorial usar?”, mas “qual evidência precisa ser encontrada, sob quais direitos, com que atualidade, custo e capacidade de explicação?”. Esta página segue o encadeamento do [framework de decisão](../modulo-2-desenho-conceitual/padroes-e-decisoes.md): direcionador → alternativa → consequência → evidência → gatilho de revisão.

## Antes da busca: transformar sem perder a intenção

Perguntas humanas raramente coincidem com o vocabulário do corpus. “Posso cancelar sem multa?” pode depender de “resilição antecipada”, um número de contrato, jurisdição e data. A **transformação da consulta** pode:

- normalizar grafia e expandir siglas conhecidas;
- extrair entidades e filtros explícitos, como contrato, unidade e vigência;
- produzir uma consulta lexical e outra semântica;
- gerar múltiplas reformulações para aumentar cobertura;
- decompor uma questão composta em subconsultas;
- pedir esclarecimento quando uma entidade essencial está ausente.

Quanto mais livre a transformação, maior o risco de mudar o pedido. Preserve a pergunta original, registre versões, limite o número de consultas e avalie se entidades, negações e temporalidade foram mantidas. Não permita que texto do usuário defina tenant, grupo ou permissão; filtros de segurança vêm de identidade e política confiáveis.

## Estratégias de recuperação

### Busca lexical

A busca lexical encontra correspondência de termos e pondera sua importância no corpus. É forte para códigos, números de cláusula, nomes próprios, siglas e expressões raras. É previsível e explicável, mas pode perder paráfrases e equivalências sem vocabulário compartilhado.

### Busca vetorial

A busca vetorial compara embeddings da consulta e dos chunks. É forte quando pergunta e fonte expressam a mesma ideia com palavras diferentes. Pode aproximar conteúdo apenas genericamente relacionado e não é naturalmente superior em identificadores exatos. O trabalho de [Karpukhin et al.](https://aclanthology.org/2020.emnlp-main.550/) é uma base primária para recuperação densa; ele não implica que toda coleção corporativa deva usar apenas esse sinal.

### Recuperação híbrida

A **recuperação híbrida** executa busca lexical e vetorial, reúne candidatos e combina rankings. Uma técnica de fusão baseada em posição evita comparar diretamente escores de escalas incompatíveis; outra opção aprende pesos com dados rotulados. Híbrido melhora cobertura em corpus misto, mas duplica índices, latência, ajuste e observabilidade. Deve demonstrar ganho em consultas representativas, especialmente termos exatos e paráfrases.

### Recuperação estruturada

Dados tabulares e relacionais pedem consulta com esquema, tipos, junções e autorização por linha ou coluna. A saída deve preservar unidades, tempo de referência e significado dos campos. O modelo pode ajudar a formular uma intenção, mas uma camada determinística valida e executa a consulta. Não transforme uma tabela inteira em chunks se a necessidade é obter o valor vigente de um registro.

## Autorização participa da recuperação

**Recuperar e depois esconder** é uma fronteira fraca: o conteúdo proibido já pode ter chegado ao serviço de ranking, cache, log ou modelo. A recuperação consciente de autorização propaga identidade e finalidade até o mecanismo que decide o conjunto elegível.

Há três estratégias frequentes:

1. **índices fisicamente separados:** isolamento forte por tenant ou domínio; aumenta custo, replicação e operação;
2. **particionamento ou namespace:** reduz mistura e permite escala compartilhada; exige controles contra seleção incorreta;
3. **filtro por metadados no momento da busca:** flexível para grupos e atributos; depende da correção, atualização e capacidade do mecanismo.

Em muitos sistemas, combina-se separação grossa com filtros finos. O motor de políticas deriva predicados de atributos confiáveis, e o recuperador os aplica antes de materializar conteúdo. O reranker recebe somente candidatos autorizados. Cache inclui identidade ou classe de política na chave; caso contrário, uma resposta autorizada para uma pessoa pode vazar para outra.

Metadado de permissão é dado crítico. Mudança de grupo, revogação ou confidencialidade deve propagar-se segundo SLO menor ou igual ao da fonte. Falha ao obter política resulta em negar acesso ou degradar para um corpus público conhecido, nunca em liberar tudo.

## Reranking: qualidade com custo delimitado

A primeira recuperação privilegia velocidade e cobertura. O **reranking** aplica um avaliador mais caro a poucas dezenas de candidatos e estima relevância conjunta entre pergunta e trecho. Depois, deduplica versões, impõe diversidade e seleciona o contexto final.

Reranking pode elevar precisão nas primeiras posições, mas acrescenta latência, custo e outra versão probabilística. Meça ganho em MRR, nDCG ou precisão no orçamento de contexto; estabeleça timeout e fallback para o ranking inicial. Um reranker nunca deve desfazer autorização ou usar conteúdo que a pessoa não poderia receber.

## Montagem de contexto

Contexto não é concatenação cega dos primeiros resultados. O montador precisa:

- reservar orçamento para instruções, pergunta e resposta;
- preservar título, versão, vigência, seção e identificador de citação;
- agrupar chunks vizinhos quando a unidade recuperada depende do entorno;
- remover duplicatas e versões superadas;
- equilibrar relevância e diversidade de fontes;
- sinalizar autoridade e conflitos, sem inventar precedência;
- separar claramente evidência de instrução;
- limitar dados à finalidade da consulta.

Ordenação pode influenciar a atenção do modelo. Avalie casos em que a evidência principal está no início, meio e fim. Compressão de contexto pode resumir candidatos antes da geração, porém cria uma transformação que também precisa preservar suporte e proveniência.

Conteúdo recuperado é entrada não confiável. Um documento pode conter frases como “ignore as instruções anteriores”. Isolamento estrutural, rotulagem, minimização de ferramentas e validação posterior reduzem risco de injeção indireta. O [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) é orientação de segurança registrada para tratar essa superfície; conteúdo nunca recebe autoridade para mudar política ou executar ação.

## Citações e suporte

Uma citação útil liga uma afirmação material a um trecho que realmente a sustenta. O pipeline deve produzir identificadores estáveis, e a interface deve permitir abrir fonte, versão e localização dentro da autorização vigente.

Valide ao menos:

- **correção:** a fonte citada implica a afirmação;
- **completude:** afirmações verificáveis importantes possuem citação;
- **qualidade da fonte:** a origem é adequada e vigente;
- **atribuição:** a citação está próxima da afirmação correspondente;
- **acessibilidade:** o usuário consegue consultar o material citado.

Mostrar três links no rodapé não demonstra suporte. Uma resposta pode citar fonte relevante ao tema, mas não à proposição. Citação também não transforma opinião, inferência ou política conflitante em fato; essas categorias devem ser rotuladas.

## Evidência insuficiente e abstenção

**Evidência insuficiente** ocorre quando falta cobertura, os resultados são fracos, há conflito não resolvido, uma fonte exigida está indisponível, a pergunta está fora do escopo ou a autorização remove todo suporte. O sistema precisa distinguir “não existe”, “não foi encontrado” e “você não pode acessar”. A mensagem não deve revelar a existência de documento confidencial.

O controle de suficiência combina sinais: presença de fonte obrigatória, limiar calibrado, cobertura das partes da pergunta, vigência, diversidade, conflito e verificações de suporte. Escores de similaridade variam por coleção e consulta; não use um valor universal.

Respostas seguras incluem:

- pedir dado essencial que falta;
- responder parcialmente e nomear o limite;
- indicar canal oficial ou revisão humana;
- declarar que as fontes disponíveis não sustentam a resposta;
- bloquear quando a finalidade ou identidade não autoriza.

Avalie **abstenção correta** e **abstenção indevida**. Recusar sempre é seguro, mas inútil; responder sempre é fluente, mas arriscado.

## Padrões de RAG e seus trade-offs

### RAG básico com dois fluxos

Uma ingestão prepara chunks e um fluxo online recupera top-k, monta contexto e gera. É o ponto de partida quando uma coleção homogênea e perguntas simples demonstram cobertura suficiente.

**Acrescenta:** atualização externa e proveniência. **Cobra:** operação de pipeline, índice e avaliação. **Evite quando:** o contexto necessário já é pequeno e selecionável por regra.

### RAG híbrido

Combina busca lexical e busca vetorial, frequentemente com reranking. É apropriado para coleções com códigos exatos e paráfrases.

**Acrescenta:** cobertura e robustez entre tipos de consulta. **Cobra:** dois sinais, fusão, calibração e latência. **Evidência necessária:** ganho segmentado sobre cada estratégia isolada.

### RAG hierárquico

Recupera primeiro uma representação de documento, tema ou resumo e depois trechos filhos; ou encontra o filho e expande para o pai. Serve a documentos longos cuja estrutura carrega significado.

**Acrescenta**

Navegação entre visão ampla e detalhe.

**Cobra**

Hierarquia consistente, propagação de metadados e mais etapas.

**Risco**

Resumo pai esconder exceção presente no trecho.

### RAG adaptativo

Classifica a consulta e escolhe caminho: resposta sem recuperação para conversa geral, lexical para código, híbrida para política ou decomposição para questão composta. Também ajusta top-k e orçamento.

**Acrescenta**

Custo e qualidade proporcionais à necessidade.

**Cobra**

Roteador, políticas de decisão e avaliação por rota.

**Risco**

Roteamento incorreto impedir acesso à evidência necessária.

### RAG corretivo

Avalia os resultados recuperados e, se forem insuficientes, reformula a consulta, amplia fontes, muda estratégia ou recusa. A correção deve ter orçamento e limite de tentativas.

**Acrescenta**

Recuperação diante de primeira tentativa fraca.

**Cobra**

Latência, variabilidade e caminhos adicionais.

**Risco**

Ciclos de reformulação alterarem intenção ou buscarem fora da autorização.

### RAG multisource

Consulta fontes com semânticas e autoridades diferentes — por exemplo, políticas, contratos e registros estruturados — e compõe resultados preservando origem. Um orquestrador determina quais fontes são necessárias; cada adaptador mantém contrato e política próprios.

**Acrescenta**

Cobertura de perguntas que cruzam domínios.

**Cobra**

Resolução de identidade, tempo e conflito.

**Risco**

Combinar informação de momentos ou entidades diferentes.

### RAG com dados estruturados

Traduz parte da intenção em consulta validada sobre banco, API ou grafo, e usa o resultado tipado como evidência. Pode coexistir com recuperação documental.

**Acrescenta**

Precisão para fatos operacionais e agregações.

**Cobra**

Catálogo semântico, validação de consulta e autorização de linha/coluna.

**Risco**

Consulta sintaticamente válida, mas semanticamente errada ou excessiva.

## Como escolher sem acumular padrões

Comece com a menor composição que satisfaz o cenário de qualidade. Uma matriz simples ajuda:

| Direcionador | Alternativa inicial | Escale quando houver evidência |
|---|---|---|
| termos e códigos exatos | busca lexical | paráfrases relevantes ficam ausentes |
| perguntas conceituais | busca vetorial | códigos e entidades perdem cobertura |
| mistura dos dois | recuperação híbrida | ganho compensa latência e operação |
| documentos longos e estruturados | pai–filho | chunks isolados perdem definição ou exceção |
| tipos de consulta muito diferentes | RAG adaptativo | rotas têm critérios e dados suficientes |
| primeira busca frequentemente fraca | RAG corretivo limitado | reformulação melhora sem mudar intenção |
| fatos em sistemas diferentes | RAG multisource | identidade, temporalidade e autoridade são reconciliáveis |
| agregação e estado atual | consulta estruturada validada | texto não representa o fato com segurança |

Registre em ADR: população de perguntas, fontes, restrições, métrica-base, alternativa rejeitada, risco residual, custo e gatilho de revisão. “Mais avançado” não é atributo de qualidade.

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
