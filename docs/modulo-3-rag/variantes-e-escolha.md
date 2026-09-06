# Variantes de RAG

Sete variantes, o que cada uma compra e cobra, e o critério para escolher uma em vez de acumular todas.

## Padrões de RAG e seus trade-offs

As opções abaixo são estratégias de recuperação e composição, não estilos arquiteturais completos. Um mesmo sistema pode usar mais de uma; a escolha continua subordinada às características arquiteturais, ao domínio e às restrições.

### RAG básico com dois fluxos

Uma ingestão prepara chunks e um fluxo online recupera top-k, monta contexto e gera. É o ponto de partida quando uma coleção homogênea e perguntas simples demonstram cobertura suficiente.

**Acrescenta:** atualização externa e possibilidade de preservar proveniência. **Cobra:** operação de pipeline, índice e avaliação. **Evite quando:** o contexto necessário já é pequeno e selecionável por regra.

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

Registre em ADR: população de perguntas, fontes, restrições, métrica-base, alternativa rejeitada, risco residual, custo e gatilho de revisão. A sofisticação da solução só se justifica quando atende a uma característica priorizada.

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

## Prioridades, plataforma e evolução

| Característica | Prioridade no caso | Tensão aceita | Medida e responsável |
|---|---|---|---|
| Autorização e privacidade | Não negociável | filtros antecipados podem reduzir cobertura aparente | item proibido nunca materializado; Segurança e Privacidade |
| Proveniência e atualidade | Alta | metadados, versionamento e validação adicionam latência | fonte, versão e vigência por afirmação; dono do conhecimento |
| Qualidade de recuperação | Alta | híbrido e reranking elevam custo e operação | Recall@k e nDCG por segmento; produto e arquitetura |
| Confiabilidade | Alta | fallback pode reduzir qualidade | SLO de atualização e modo degradado; Operações |
| Latência e custo | Importante | limites podem restringir top-k, reranking ou contexto | p95 e custo por consulta; plataforma |
| Modificabilidade | Importante | adaptadores e contratos adicionam componentes | troca localizada e teste de contrato; arquitetura |

**Hospedado versus autogerido:** um serviço hospedado de índice, embedding ou reranking acelera capacidade e elasticidade, mas cria fronteiras de fornecedor para dados, versões, disponibilidade e portabilidade. Operação autogerida aumenta controle e também assume capacidade, atualização, segurança, escala e plantão. Compare custo total e risco residual no volume esperado.

**Construir, comprar ou compor:** compre uma capacidade padronizada quando a diligência e a saída forem proporcionais ao risco; construa onde contrato, política ou diferenciação exigirem; componha índice, conectores, políticas e avaliação quando as responsabilidades forem distintas. Preserve manifestos, métricas e conjuntos de avaliação para substituir componentes sem perder evidência.
