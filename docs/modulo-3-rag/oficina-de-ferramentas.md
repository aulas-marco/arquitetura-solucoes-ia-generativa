# Oficina de ferramentas — investigar um RAG com evidências

**Objetivo Bloom:** Aplicar e Analisar.

Esta oficina não pede que você se lembre de uma passagem anterior para executar um comando. Ela reconstrói o problema a cada experimento: uma pergunta só pode receber resposta quando o sistema consegue mostrar evidência autorizada, atual e suficiente. Você começará com um corpus Boreal pequeno e, depois, testará recuperação lexical, vetorial e híbrida nos casos Lume e Aurora.

## Bússola da prática

Um RAG tem dois fluxos que se encontram na resposta:

- no **fluxo offline**, a **ingestão** lê a fonte, preserva ID, versão e metadados e publica um índice pesquisável;
- no **fluxo online**, a pergunta recupera candidatos, seleciona evidências e produz uma resposta com **citação** — ou declara **evidência insuficiente**.

| Experimento | Pergunta arquitetural                                 | Evidência que você coletará        |
| ----------- | ----------------------------------------------------- | ---------------------------------- |
| A           | O índice mantém o vínculo com a fonte?                | `RECUPERADO`, ID, versão e arquivo |
| B           | A resposta pode ser verificada?                       | trecho usado e citação na resposta |
| C           | O sistema para quando não há base para responder?     | `REVISÃO_HUMANA` e IDs ausentes    |
| D           | Qual estratégia encontra melhor a evidência rotulada? | ordem recuperada, MRR e nDCG@3     |

Ao final, você conseguirá localizar uma falha no caminho `fonte → ingestão → recuperação → contexto → resposta`, em vez de atribuí-la genericamente ao modelo.

## Ferramenta

Você usará **LangChain** para organizar componentes, **Chroma** como banco vetorial local, **Ollama** para embeddings e geração e **BM25** para a busca lexical do experimento comparativo. Todas as ferramentas rodam localmente com dados sintéticos.

**Decisão arquitetural em foco:** como o sistema registra fonte, versão, estratégia de recuperação e evidência antes de apresentar uma resposta como fundamentada?

## Pré-requisitos

- Python 3.10 ou superior, terminal e espaço em disco para ambiente virtual e índice local.
- Ollama instalado, com os modelos `llama3.2:3b` e `nomic-embed-text` baixados.
- Conexão temporária apenas para instalar bibliotecas e baixar modelos.
- Uma pasta de laboratório sem documentos reais. Os corpora Boreal, Lume e Aurora são integralmente sintéticos.

## Instalação

### macOS

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No Terminal, execute:

```bash
python3 --version
mkdir oficina-m3
cd oficina-m3
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install langchain langchain-chroma chromadb langchain-ollama rank-bm25
ollama pull llama3.2:3b
ollama pull nomic-embed-text
mkdir corpus
```

### Linux

Instale o Ollama pelo procedimento oficial em [ollama.com/download](https://ollama.com/download). Em seguida, execute:

```bash
python3 --version
mkdir oficina-m3
cd oficina-m3
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install langchain langchain-chroma chromadb langchain-ollama rank-bm25
ollama pull llama3.2:3b
ollama pull nomic-embed-text
mkdir corpus
```

### Windows

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No PowerShell, execute:

```powershell
python --version
mkdir oficina-m3
cd oficina-m3
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install langchain langchain-chroma chromadb langchain-ollama rank-bm25
ollama pull llama3.2:3b
ollama pull nomic-embed-text
mkdir corpus
```

> **Ao retomar a prática:** volte para `oficina-m3` e reative o ambiente: no macOS/Linux, `source .venv/bin/activate`; no Windows/PowerShell, `.venv\Scripts\Activate.ps1`.

## Preparação do laboratório

O primeiro roteiro usa três fontes Boreal e um script. Baixe os arquivos abaixo; salve os `.txt` em `corpus/` e `rag_local.py` na raiz de `oficina-m3/`.

- [politica-reembolso.txt](../assets/labs/modulo-3/politica-reembolso.txt)
- [politica-campanha.txt](../assets/labs/modulo-3/politica-campanha.txt)
- [portal-estorno.txt](../assets/labs/modulo-3/portal-estorno.txt)
- [rag_local.py](../assets/labs/modulo-3/rag_local.py)

Confirme o ponto de partida:

```bash
ls corpus
ls rag_local.py
```

Os campos `ID: POL-17-REG`, `ID: POL-17-CAMP` e `VERSAO: v3` são metadados de **[proveniência](conceitos.md#proveniencia-de-ponta-a-ponta)**. Eles distinguem as duas políticas e, junto ao nome do arquivo, permitem reconstruir qual fonte e versão sustentaram a resposta.

Para o Experimento D, baixe também [rag_lume_aurora.py](../assets/labs/modulo-3/rag_lume_aurora.py), [avaliar_recuperacao_lume_aurora.py](../assets/labs/modulo-3/avaliar_recuperacao_lume_aurora.py), [casos_recuperacao_lume_aurora.json](../assets/labs/modulo-3/casos_recuperacao_lume_aurora.json) e estas políticas, mantendo tudo na raiz de `oficina-m3/`:

- Lume: [contestação](../assets/labs/modulo-3/lume-politica-contestacao.txt), [estorno parcial](../assets/labs/modulo-3/lume-politica-estorno-parcial.txt), [compra internacional](../assets/labs/modulo-3/lume-politica-compra-internacional.txt), [cobrança duplicada](../assets/labs/modulo-3/lume-politica-cobranca-duplicada.txt) e [produto não entregue](../assets/labs/modulo-3/lume-politica-produto-nao-entregue.txt).
- Aurora: [campanha](../assets/labs/modulo-3/aurora-politica-campanha.txt), [carência](../assets/labs/modulo-3/aurora-politica-carencia.txt), [atraso prolongado](../assets/labs/modulo-3/aurora-politica-atraso-prolongado.txt), [parcelamento](../assets/labs/modulo-3/aurora-politica-parcelamento.txt) e [restrição judicial](../assets/labs/modulo-3/aurora-politica-restricao-judicial.txt).

## Execução

Você executará cada comando dentro de `oficina-m3/`, com o ambiente virtual ativo. O script Boreal recria `chroma-boreal` a cada execução: assim, cada comparação começa com o corpus que o comando declara.

## Receita principal

Siga os experimentos em ordem quando estiver conhecendo RAG: A torna a proveniência visível; B separa evidência de fluência; C força uma parada segura; D mede a recuperação. Em uma aula curta, execute A e C em grupo e escolha uma pergunta de D para as duplas. O bloco de cada experimento repete cenário, pergunta, comando e critério de leitura para que possa ser realizado de forma independente.

## Resultado esperado

Você produzirá quatro rastros comparáveis: índice e proveniência, resposta citada, abstenção por falta de evidência e comparação de estratégias de recuperação. Eles demonstram o comportamento destes corpora e parâmetros; não medem recall geral, autorização real ou qualidade de produção.

## Interpretação

Leia a saída em duas camadas. Primeiro, verifique a evidência determinística — IDs, versões, arquivos, ordem e marcador de parada. Depois, avalie se a resposta do modelo respeita essa evidência. Uma resposta fluente não corrige uma recuperação errada, uma fonte ausente ou uma versão inválida.

## Roteiro sugerido para aula

### Experimento A — do corpus ao índice (Essencial em aula)

**Situação**

Você precisa responder ao prazo de uma compra regular. A política pode mudar; por isso, a resposta precisa apontar para a fonte e a versão, não apenas repetir um prazo.

**Pergunta de investigação**

Após a ingestão, como provar que o índice ainda preserva o vínculo com `POL-17-REG:v3`?

**Objetivo**

Observar o fluxo offline: corpus, ingestão, índice e proveniência.

**Pré-requisito**

Os três arquivos Boreal estão em `corpus/` e `rag_local.py` está na raiz da oficina.

**Execute**

```bash
python rag_local.py --pergunta 'Qual é o prazo para solicitar reembolso em uma compra regular?'
```

**Observe**

Antes de `RESPOSTA`, localize `RECUPERADO POL-17-REG:v3`, o nome de `politica-reembolso.txt` e a criação de `chroma-boreal`.

**Interprete**

`RECUPERADO` é a evidência de que a recuperação recebeu um item com ID e versão. A pasta do Chroma é o índice local; ela não substitui o arquivo de origem, que continua sendo a fonte de verdade.

**Compare**

Compare o texto de `politica-reembolso.txt` com o trecho impresso. O prazo pode coincidir, mas a evidência verificável inclui também ID, versão e arquivo.

**Questões exploratórias:**

- Que componente precisa registrar o manifesto que liga fonte, estratégia de chunking, embedding e índice?
- O que se perde se o trecho é recuperado sem versão?
- Que verificação bloquearia a promoção de um índice que não contém uma política obrigatória?

### Experimento B — evidência antes da resposta (Exploração em dupla)

**Situação**

Um assistente pode produzir uma frase plausível sobre reembolso. O aluno precisa distinguir uma frase que parece correta de uma resposta cuja base pode ser conferida.

**Pergunta de investigação**

Qual parte da saída permite verificar a resposta e qual parte ainda exige julgamento sobre suficiência?

**Objetivo**

Separar recuperação, montagem de contexto, citação e geração.

**Pré-requisito**

A execução do Experimento A está disponível no terminal ou registrada na tabela de evidências.

**Execute**

Rode novamente o comando completo para produzir uma saída nova e compare as duas partes indicadas:

```bash
python rag_local.py --pergunta 'Qual é o prazo para solicitar reembolso em uma compra regular?'
```

**Observe**

Copie o trecho após `RECUPERADO POL-17-REG:v3` e, na linha `RESPOSTA`, marque a citação ao ID, à versão e ao arquivo.

**Interprete**

A [citação](padroes-e-decisoes.md#citacoes-e-suporte) permite voltar à fonte; ela não prova sozinha que todos os casos foram cobertos. A suficiência depende de a pergunta, o trecho, a vigência e as exceções estarem alinhados.

**Compare**

Compare uma resposta sem ID/versão/arquivo, que não é auditável, com a resposta citada. Depois, compare `POL-17-REG:v3` (compra regular) com `POL-17-CAMP:v3` (campanha): são fontes diferentes com condições diferentes.

**Questões exploratórias:**

- Em que componente a arquitetura deve limitar o contexto a trechos elegíveis?
- Como uma citação correta pode continuar insuficiente para uma pergunta com exceção?
- Em que ponto a fonte deve aparecer para o usuário final?

### Experimento C — ausência de evidência e parada segura (Extensão)

**Situação**

Há duas regras de prazo: 15 dias para compra regular e 7 dias para campanha. Sem data e tipo de compra, escolher uma delas seria inventar uma condição. Além disso, uma política pode ter falhado na ingestão.

**Pergunta de investigação**

Quando a arquitetura deve pedir informação, encaminhar para revisão humana ou bloquear uma resposta por ausência da fonte necessária?

**Objetivo**

Tratar [evidência insuficiente e abstenção](padroes-e-decisoes.md#evidencia-insuficiente-e-abstencao) como decisões explícitas.

**Pré-requisito**

Experimentos A e B executados ao menos uma vez.

**Execute**

Execute os dois cenários, um de cada vez:

```bash
python rag_local.py --pergunta 'Não sei a data nem se a compra era promocional; qual prazo devo informar?'
python rag_local.py --excluir POL-17-REG:v3 --pergunta 'Qual é o prazo para solicitar reembolso em uma compra regular?'
```

**Observe**

No primeiro comando, confirme `REVISÃO_HUMANA` e a explicação de que faltam dados. No segundo, confirme que `POL-17-REG:v3` não aparece entre os recuperados e que a resposta declara: “a evidência obrigatória `POL-17-REG:v3` não foi recuperada”. Registre os IDs que aparecem em seu lugar.

**Interprete**

O primeiro caso mostra abstenção por ambiguidade da pergunta. O segundo isola uma falha no corpus publicado e interrompe a geração antes de chamar o modelo: a política obrigatória está ausente. Falha de recuperação não é sinônimo de alucinação; ela é uma causa anterior que o trace torna investigável.

**Compare**

Compare três saídas possíveis: prazo sem condição (arriscado), pergunta de esclarecimento (quando a informação pode ser obtida) e `REVISÃO_HUMANA` (quando a regra não pode ser aplicada com segurança).

**Questões exploratórias:**

- Qual fitness function impediria publicar um índice sem `POL-17-REG:v3`?
- Que dado adicional reduziria a abstenção no primeiro caso?
- Quem deve responder pelo alerta quando uma fonte obrigatória deixa de ser recuperável?

### Experimento D — comparar estratégias e avaliar recuperação (Extensão)

**Situação**

O Boreal mostrou um único caminho de recuperação. Em um corpus maior, termos exatos e paráfrases podem favorecer estratégias diferentes. Lume e Aurora fornecem perguntas rotuladas: para cada uma, o arquivo JSON declara o ID que deveria aparecer como evidência relevante.

**Pergunta de investigação**

Como busca lexical, vetorial e recuperação híbrida alteram a posição da evidência relevante — e como MRR e nDCG@3 tornam essa diferença observável?

**Objetivo**

Comparar [busca lexical, vetorial e recuperação híbrida](padroes-e-decisoes.md#estrategias-de-recuperacao) e relacionar ranking a avaliação.

**Pré-requisito**

Os dois scripts, o JSON e os dez arquivos Lume/Aurora foram baixados para a raiz da oficina; `rank-bm25` está instalado.

**Execute**

Primeiro, faça uma pergunta Lume e leia a ordem completa. Em seguida, execute a avaliação para os dois casos:

```bash
python rag_lume_aurora.py --caso lume --modo lexical --pergunta 'A compra foi cobrada duas vezes no meu cartão, como contesto?'
python rag_lume_aurora.py --caso lume --modo vetorial --pergunta 'A compra foi cobrada duas vezes no meu cartão, como contesto?'
python rag_lume_aurora.py --caso lume --modo hibrido --pergunta 'A compra foi cobrada duas vezes no meu cartão, como contesto?'
python avaliar_recuperacao_lume_aurora.py --caso lume --k 3
python avaliar_recuperacao_lume_aurora.py --caso aurora --k 3
```

**Observe**

Em cada consulta, a seta `→` marca os dois itens enviados ao contexto; a posição `1.` é o primeiro candidato. Na avaliação, registre MRR e nDCG@3 para cada modo, sem supor que o mesmo modo vencerá em todos os corpora.

**Interprete**

Busca lexical favorece termos compartilhados; vetorial favorece proximidade semântica; a recuperação híbrida combina as duas ordens por Reciprocal Rank Fusion. MRR valoriza a posição do primeiro item relevante; nDCG@3 mede ganho por posição nos três primeiros. Métrica alta não elimina a necessidade de filtros de autorização, vigência, citação e teste com casos críticos.

**Compare**

Compare o ID relevante do JSON com o ranking de cada modo. Se ele não estiver nas duas posições marcadas com `→`, a resposta teria recebido contexto insuficiente mesmo que o documento apareça mais abaixo.

**Questões exploratórias:**

- Em que tipo de pergunta um código exato pode favorecer a busca lexical?
- Qual mudança de chunking, embedding ou fusão você testaria se o ID relevante ficasse abaixo do top 2?
- Que conjunto de casos precisa ser acrescentado antes de promover uma nova configuração?

## Evidência a entregar

Entregue a tabela preenchida, as duas linhas de avaliação e uma conclusão de até oito linhas.

| Experimento | Pergunta ou caso                  | Evidência observada | Decisão arquitetural ou hipótese |
| ----------- | --------------------------------- | ------------------- | -------------------------------- |
| A           | Compra regular                    |                     |                                  |
| B           | Compra regular                    |                     |                                  |
| C           | Dados insuficientes               |                     |                                  |
| C           | `POL-17-REG:v3` excluído          |                     |                                  |
| D           | Lume: lexical, vetorial e híbrido |                     |                                  |
| D           | Aurora: MRR e nDCG@3              |                     |                                  |

Na conclusão, responda: quando responder, quando pedir informação e quando encaminhar para revisão humana? Declare que os corpora são sintéticos; registre os modelos de embedding e chat; e escreva uma **fitness function** verificável, por exemplo: “nenhuma resposta sobre reembolso é exibida sem ID, versão e fonte recuperada”. Indique qual equipe de **operação** verificaria esse sinal antes de uma promoção e qual ação tomaria se ele falhasse.

## Limpeza e contingência

Encerre a execução, saia do ambiente com `deactivate` e apague `.venv`, `chroma-boreal` e `chroma-lume-aurora` se não precisar mais deles. Para remover modelos que não serão usados, execute `ollama rm nomic-embed-text` e `ollama rm llama3.2:3b`.

Se houver falha, confirme `python --version`, `ollama list`, a ativação do ambiente, os nomes dos arquivos e `python -m pip show rank-bm25`. Registre a mensagem de erro e peça apoio ao professor. Não substitua os corpora sintéticos por políticas reais, contratos ou dados de atendimento.

## Ferramentas adicionais

O laboratório combinou LangChain, Chroma, Ollama e BM25 para tornar visíveis ingestão, recuperação, proveniência e avaliação. Investigação livre, fora do escopo avaliado desta oficina.

| Ferramenta    | Site                                                                               | Propósito                                                            |
| ------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Qdrant        | [qdrant.tech](https://qdrant.tech)                                                 | Banco vetorial open source em Rust para recuperação por similaridade |
| Weaviate      | [weaviate.io](https://weaviate.io)                                                 | Banco vetorial com busca híbrida e esquema tipado                    |
| pgvector      | [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector)               | Extensão vetorial para PostgreSQL                                    |
| LlamaIndex    | [llamaindex.ai](https://www.llamaindex.ai)                                         | Framework especializado em indexação e recuperação                   |
| Cohere Rerank | [cohere.com/rerank](https://cohere.com/rerank)                                     | Serviço de reranking de trechos candidatos                           |
| RAGAs         | [github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas) | Framework de avaliação de fidelidade, relevância e recuperação       |
