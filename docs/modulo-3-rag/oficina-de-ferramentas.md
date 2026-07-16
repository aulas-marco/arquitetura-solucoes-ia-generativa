# Oficina de ferramentas — observar um RAG fundamentado

**Objetivo Bloom:** Aplicar e Analisar.

Esta oficina constrói um RAG local pequeno para observar, na ordem correta, corpus, ingestão, recuperação, evidência e resposta. O resultado não é uma demonstração de “chat inteligente”; é uma forma de verificar quais documentos sustentaram uma resposta.

## Ferramenta

Você usará **LangChain** para organizar os componentes, **Chroma** como banco vetorial local e **Ollama** para gerar embeddings e a resposta. As três ferramentas são open source e rodam no computador do aluno.

**Decisão arquitetural em foco:** como a arquitetura registra versão e trecho recuperado antes de permitir uma resposta apresentada como fundamentada?

## Pré-requisitos

- Python 3.10 ou superior, terminal e espaço em disco para ambiente virtual e índice local.
- Ollama instalado, com os modelos `llama3.2:3b` e `nomic-embed-text` baixados.
- Conexão temporária apenas para instalar bibliotecas e baixar modelos.
- Uma pasta de laboratório sem documentos reais: o corpus Boreal abaixo é integralmente sintético.

## Instalação

### macOS

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No Terminal, execute:

```bash
python3 --version
mkdir oficina-m3
cd oficina-m3
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install langchain langchain-chroma chromadb langchain-ollama
ollama pull llama3.2:3b
ollama pull nomic-embed-text
mkdir corpus
```

### Linux

Instale o Ollama pelo procedimento oficial em [ollama.com/download](https://ollama.com/download). Em seguida, execute no terminal Linux:

```bash
python3 --version
mkdir oficina-m3
cd oficina-m3
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install langchain langchain-chroma chromadb langchain-ollama
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
python -m pip install langchain langchain-chroma chromadb langchain-ollama
ollama pull llama3.2:3b
ollama pull nomic-embed-text
mkdir corpus
```

> **Ao retomar a prática:** se você fechar o terminal, volte para `oficina-m3` e reative o ambiente: no macOS/Linux, `source .venv/bin/activate`; no Windows/PowerShell, `.venv\Scripts\Activate.ps1`. Com o ambiente ativo, `python` funciona nos três sistemas.

## Preparação do laboratório

Um **[corpus](conceitos.md#fontes-e-formatos)** é o conjunto de documentos que o sistema pode consultar. Aqui ele terá três arquivos. **Ingestão** é a leitura desses arquivos, a preservação de seus metadados e sua indexação no Chroma. **Recuperação** é a seleção dos trechos candidatos para uma pergunta.

Baixe os quatro arquivos abaixo. Salve os três `.txt` dentro da pasta `corpus/`; salve `rag_local.py` diretamente em `oficina-m3/`.

- [politica-reembolso.txt](../assets/labs/modulo-3/politica-reembolso.txt)
- [politica-campanha.txt](../assets/labs/modulo-3/politica-campanha.txt)
- [portal-estorno.txt](../assets/labs/modulo-3/portal-estorno.txt)
- [rag_local.py](../assets/labs/modulo-3/rag_local.py)

Ao terminar, confirme os arquivos:

```bash
ls corpus
ls rag_local.py
```

Os metadados `ID: POL-17` e `VERSAO: v3` fazem parte do corpus. Eles não são detalhes decorativos: serão impressos antes da resposta e permitem discutir proveniência.

## Execução

Execute a primeira pergunta, sobre compra regular:

```bash
python rag_local.py --pergunta 'Qual é o prazo para solicitar reembolso em uma compra regular?'
```

O script cria a pasta `chroma-boreal`, faz a ingestão, recupera até dois trechos e imprime linhas que começam por `RECUPERADO`. Só depois ele pede uma resposta ao modelo local.

## Receita principal

Procure na saída por `RECUPERADO POL-17:v3`. Esse é o sinal de que a resposta tem evidência do corpus correto. Em seguida, execute uma pergunta com informação insuficiente:

```bash
python rag_local.py --pergunta 'Não sei a data nem se a compra era promocional; qual prazo devo informar?'
```

**Resultado esperado:** `REVISÃO_HUMANA`. O script interrompe a geração nessa condição porque o corpus exige data e tipo de compra para escolher entre 15 e 7 dias. Essa parada é uma regra arquitetural explícita, não uma limitação a esconder do usuário.

## Resultado esperado

Após a primeira execução, devem existir:

- a pasta `chroma-boreal`, que contém o índice local;
- pelo menos uma linha `RECUPERADO POL-17:v3` antes da resposta;
- uma resposta que cite o ID e a versão usados;
- na segunda pergunta, a indicação `REVISÃO_HUMANA` em vez de um prazo inventado.

Uma execução só mostra o comportamento desse corpus e desses parâmetros. Ela não mede recall geral, cobertura de um acervo real, qualidade de produção ou autorização de acesso.

## Interpretação

Simule uma falha de ingestão ou filtro removendo o documento de política da coleção:

```bash
python rag_local.py --excluir POL-17:v3 --pergunta 'Qual é o prazo para solicitar reembolso em uma compra regular?'
```

Compare os IDs recuperados, a resposta e sua confiança em apresentá-la ao usuário. A variável alterada é a presença de `POL-17:v3`; o experimento não compara “modelos melhores”, mas localiza uma hipótese de falha entre ingestão, metadado, recuperação e montagem de contexto.

## Roteiro sugerido para aula

### Experimento A — ingestão e proveniência (Essencial em aula)

**Objetivo**

Ver como o corpus se transforma em índice.

**Pré-requisito**

Arquivos copiados.

**Execute**

Rode a primeira pergunta.

**Observe**

`chroma-boreal`, IDs e versões.

**Compare**

Arquivo de origem e trecho recuperado.

**Questões exploratórias:**

- Que componente preserva `POL-17:v3` quando o texto entra no índice?
- Qual risco aparece se o trecho é recuperado sem versão?
- Que evidência torna uma atualização do corpus auditável?

### Experimento B — resposta com fonte (Exploração em dupla)

**Objetivo**

Separar resposta fluente de resposta fundamentada.

**Pré-requisito**

Primeira execução concluída.

**Execute**

Localize o ID antes da resposta.

**Observe**

Citação e conteúdo recuperado.

**Compare**

Resposta sem trecho versus resposta com evidência.

**Questões exploratórias:**

- O que a citação permite verificar e o que ela não garante?
- Como o ranking pode recuperar um trecho plausível, mas insuficiente?
- Em que ponto da arquitetura a fonte deve ser apresentada ao usuário?

### Experimento C — falha e abstenção (Extensão)

**Objetivo**

Tratar ausência de evidência como sinal de parada.

**Pré-requisito**

Experimento B.

**Execute**

Use `--excluir POL-17:v3` e a pergunta sem data.

**Observe**

IDs ausentes e `REVISÃO_HUMANA`.

**Compare**

Abstenção, resposta inventada e encaminhamento.

**Questões exploratórias:**

- Que teste evitaria publicar um índice sem o documento obrigatório?
- Qual é a diferença entre falha de recuperação e alucinação?
- Que dado adicional seria necessário para reduzir a abstenção com segurança?

## Evidência a entregar

Entregue a tabela preenchida e uma conclusão de até cinco linhas.

| Pergunta | IDs e versões recuperados | Resposta | Fonte citada? | Hipótese de correção ou decisão |
|---|---|---|---|---|
| Compra regular |  |  |  |  |
| Dados insuficientes |  |  |  |  |
| `POL-17:v3` excluído |  |  |  |  |

Na conclusão, responda: quando a arquitetura deve responder, quando deve pedir informação e quando deve encaminhar para revisão humana? Declare que o corpus é sintético e registre o modelo de embedding e o modelo de chat usados.

## Limpeza e contingência

Encerre a execução, saia do ambiente com `deactivate` e apague `.venv` e `chroma-boreal` se não precisar mais deles. Para remover modelos que não serão usados, execute `ollama rm nomic-embed-text` e `ollama rm llama3.2:3b`.

Se houver falha, primeiro confirme `python --version`, `ollama list`, a existência de `corpus/` e os nomes dos quatro arquivos. Registre a mensagem de erro e peça apoio ao professor para corrigir a instalação local. Não substitua o corpus por políticas reais, contratos ou dados de atendimento.
