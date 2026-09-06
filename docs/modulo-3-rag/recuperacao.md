# Busca e recuperação

Transformar a pergunta sem perder a intenção, escolher entre busca lexical, vetorial e híbrida, e fazer a autorização participar da recuperação em vez de vir depois dela.

Cada mecanismo de RAG responde a uma falha possível. A decisão central é: “qual evidência precisa ser encontrada, sob quais direitos, com que atualidade, custo e capacidade de explicação?”. Esta página segue o encadeamento do [framework de decisão](../modulo-2-desenho-conceitual/alternativas-e-registro.md): direcionador → alternativa → consequência → evidência → gatilho de revisão.

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

![Diagrama: uma pergunta e três trechos de políticas são convertidos pelo modelo nomic-embed-text em vetores; em uma projeção didática bidimensional, a pergunta fica próxima do trecho sobre atraso superior a 90 dias; os dois trechos mais próximos seguem como contexto para a LLM](../assets/images/m03-busca-vetorial.png "Da pergunta aos trechos semanticamente próximos")

*Figura — O embedding real tem 768 dimensões; o mapa em duas dimensões é apenas uma projeção para visualizar proximidade semântica. A recuperação seleciona os trechos mais próximos para compor o contexto da LLM.*

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
