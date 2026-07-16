# Oficinas locais e executáveis — plano de implementação

> **Para agentes:** SUB-HABILIDADE OBRIGATÓRIA: usar `superpowers:subagent-driven-development` (recomendado) ou `superpowers:executing-plans` para executar este plano tarefa a tarefa. Os passos usam caixas de seleção (`- [ ]`) para acompanhamento.

**Objetivo:** transformar as seis oficinas em laboratórios locais e executáveis, removendo linguagem de acesso comercial e reconstruindo especialmente os módulos 2 e 3.

**Arquitetura:** as oficinas continuam em Markdown e apontam para artefatos pequenos e baixáveis em `docs/assets/labs/`. Cada laboratório usa dados sintéticos e uma ferramenta local open source. Os testes passam a garantir a estrutura pedagógica, os comandos e a ausência de termos de acesso/pagamento.

**Tecnologias:** MkDocs Material, Markdown, Python 3.10+, Ollama, LiteLLM Proxy, LangChain, Chroma, LangGraph, DeepEval e OpenTelemetry.

## Restrições globais

- Dados exclusivamente sintéticos; sem documentos, credenciais, URLs privadas ou dados pessoais/institucionais.
- Toda oficina terá objetivo, ferramenta, pré-requisitos, instalação, preparação, execução, resultado esperado, interpretação, entrega, limpeza e contingência.
- A ferramenta principal de cada oficina é local e open source; análise manual é somente contingência de falha local.
- Remover de oficinas e exercícios públicos: `cartão`, `crédito`, `cobrança`, `sem cartão`, `rota comercial` e `rota institucional`.
- Manter cada módulo entre 6.000 e 9.400 palavras e o conjunto entre 40.000 e 54.000 palavras.
- Antes de publicar: `python -m unittest discover -s tests -v`, `python scripts/validate_content.py --all` e `mkdocs build --strict`.

---

### Tarefa 1: estabelecer o novo contrato de oficina nos testes

**Arquivos:**

- Modificar: `tests/test_applied_literacy.py`
- Modificar: `README.md`

**Interfaces:** consome as seis páginas `oficina-de-ferramentas.md`; produz as garantias de que cada oficina é um laboratório local executável.

- [ ] **Passo 1: escrever o teste que falha para a estrutura comum**

Substituir o teste que exige “Roteiros equivalentes de acesso” por este contrato:

```python
def test_every_workshop_is_a_local_executable_lab(self):
    forbidden = re.compile(
        r"cart[ãa]o|crédito|cobrança|sem cart[ãa]o|rota comercial|rota institucional",
        re.IGNORECASE,
    )
    headings = (
        "## Ferramenta", "## Pré-requisitos", "## Instalação",
        "## Preparação do laboratório", "## Execução", "## Resultado esperado",
        "## Interpretação", "## Limpeza e contingência", "## Evidência a entregar",
    )
    for slug in MODULES:
        text = (DOCS / slug / OFFICE).read_text(encoding="utf-8")
        for heading in headings:
            self.assertIn(heading, text, f"{slug}: {heading}")
        self.assertIsNone(forbidden.search(text), slug)
        self.assertRegex(text, r"(?m)^```bash$")
```

- [ ] **Passo 2: executar o teste e confirmar a falha**

```bash
python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_every_workshop_is_a_local_executable_lab -v
```

Resultado esperado: falha porque as páginas ainda têm rotas antigas e títulos incompletos.

- [ ] **Passo 3: adicionar regressões específicas para os módulos 2 e 3**

```python
def test_module_two_uses_litellm_proxy_and_a_versioned_manifest(self):
    text = (DOCS / "modulo-2-desenho-conceitual" / OFFICE).read_text(encoding="utf-8")
    for term in ("LiteLLM Proxy", "Ollama", "litellm_config.yaml", "boreal-local",
                 "localhost:4000", "curl", "troca controlada"):
        self.assertIn(term, text)

def test_module_three_provides_files_ingestion_retrieval_and_abstention(self):
    text = (DOCS / "modulo-3-rag" / OFFICE).read_text(encoding="utf-8")
    for term in ("LangChain", "Chroma", "politica-reembolso.txt", "rag_local.py",
                 "chroma-boreal", "POL-17:v3", "revisão humana"):
        self.assertIn(term, text)
```

- [ ] **Passo 4: atualizar a descrição do repositório**

No `README.md`, substituir a frase sobre rotas de acesso por:

```markdown
As seis oficinas são laboratórios locais com ferramentas open source e dados sintéticos. Cada roteiro informa o que instalar, os arquivos a preparar, os comandos a executar, o resultado esperado e como limpar o ambiente ao terminar.
```

- [ ] **Passo 5: executar e registrar o teste**

```bash
python -m unittest tests.test_applied_literacy -v
git add tests/test_applied_literacy.py README.md
git commit -m "test: define executable local workshop contract"
```

### Tarefa 2: adicionar artefatos didáticos baixáveis

**Arquivos:**

- Criar: `docs/assets/labs/modulo-2/litellm_config.yaml`
- Criar: `docs/assets/labs/modulo-2/request.json`
- Criar: `docs/assets/labs/modulo-3/politica-reembolso.txt`
- Criar: `docs/assets/labs/modulo-3/politica-campanha.txt`
- Criar: `docs/assets/labs/modulo-3/portal-estorno.txt`
- Criar: `docs/assets/labs/modulo-3/rag_local.py`
- Criar: `docs/assets/labs/modulo-4/troca_boreal.py`
- Criar: `docs/assets/labs/modulo-5/casos_confianca.json`
- Criar: `docs/assets/labs/modulo-5/avaliar_confianca.py`
- Criar: `docs/assets/labs/modulo-6/telemetria_local.py`

**Interfaces:** os arquivos leem e produzem apenas conteúdo de treinamento, e podem ser baixados pelas páginas Markdown.

- [ ] **Passo 1: escrever o manifesto e a requisição do M2**

`litellm_config.yaml` deve ser exatamente:

```yaml
model_list:
  - model_name: boreal-local
    litellm_params:
      model: ollama/llama3.2:3b
      api_base: http://localhost:11434
```

`request.json` deve ser exatamente:

```json
{"model":"boreal-local","messages":[{"role":"user","content":"Resuma: cliente fictício não consegue acessar o portal."}],"temperature":0.2}
```

- [ ] **Passo 2: criar o corpus e o script do M3**

`rag_local.py` deve ler os três `.txt` em `corpus/`, criar `chroma-boreal`, inserir metadados `id` e `versao`, imprimir `RECUPERADO <id>:<versao>` antes da resposta e produzir `REVISÃO_HUMANA` se faltarem data e tipo de compra. Deve aceitar `--pergunta` e `--excluir`.

- [ ] **Passo 3: criar os scripts dos M4–M6**

- `troca_boreal.py`: grafo LangGraph, estados `aguardando_aprovacao`, `reservado` e `outcome_unknown`, argumentos `--aprovado` e `--repetir`.
- `casos_confianca.json`: os cinco casos sintéticos da oficina.
- `avaliar_confianca.py`: executa DeepEval com Ollama e grava `relatorio-confianca.json` com caso, decisão esperada, decisão observada e justificativa.
- `telemetria_local.py`: configura `TracerProvider` e `ConsoleSpanExporter`, emite spans `entrada`, `modelo` e `saida` e imprime duração, resultado e `trace_id`.

- [ ] **Passo 4: validar sintaxe antes de documentar os comandos**

```bash
python -m py_compile docs/assets/labs/modulo-3/rag_local.py docs/assets/labs/modulo-4/troca_boreal.py docs/assets/labs/modulo-5/avaliar_confianca.py docs/assets/labs/modulo-6/telemetria_local.py
python -m json.tool docs/assets/labs/modulo-2/request.json >/dev/null
python -m json.tool docs/assets/labs/modulo-5/casos_confianca.json >/dev/null
git add docs/assets/labs
git commit -m "feat: add local workshop lab assets"
```

### Tarefa 3: padronizar o Módulo 1 e reconstruir o Módulo 2

**Arquivos:**

- Modificar: `docs/modulo-1-fundamentos/oficina-de-ferramentas.md`
- Modificar: `docs/modulo-2-desenho-conceitual/oficina-de-ferramentas.md`
- Usar: `docs/assets/labs/modulo-2/litellm_config.yaml`
- Usar: `docs/assets/labs/modulo-2/request.json`

**Interfaces:** M1 usa Ollama e `llama3.2:3b`; M2 consome Ollama em `localhost:11434` e oferece `boreal-local` em `localhost:4000/v1/chat/completions`.

- [ ] **Passo 1: adequar o M1 aos títulos comuns**

Preservar seus quatro experimentos e acrescentar os nove títulos da Tarefa 1. Mover instalação e comandos existentes às seções adequadas. Remover qualquer frase sobre conta, cartão ou acesso; manter somente o aviso de dados sintéticos.

- [ ] **Passo 2: substituir a fixture isolada do M2 por gateway local**

Explicar LiteLLM Proxy como adaptador que preserva o contrato enquanto o manifesto escolhe o destino. Oferecer downloads de `litellm_config.yaml` e `request.json`, descrevendo cada campo.

- [ ] **Passo 3: incluir os comandos literais e a alternativa Windows**

```bash
mkdir oficina-m2 && cd oficina-m2
python -m venv .venv
source .venv/bin/activate
python -m pip install 'litellm[proxy]'
ollama pull llama3.2:3b
litellm --config litellm_config.yaml --port 4000
curl http://localhost:4000/v1/chat/completions -H 'Content-Type: application/json' --data @request.json
```

Incluir `.venv\Scripts\Activate.ps1` como ativação PowerShell, explicando que proxy e chamada são feitos em terminais diferentes.

- [ ] **Passo 4: tornar a variação e entrega do M2 controladas**

Trocar apenas `model: ollama/llama3.2:3b` por outro modelo já baixado, reenviar o mesmo JSON e registrar alias, modelo, entrada, resposta e mini-ADR. Reescrever A, B e C como contrato pelo gateway, troca de destino e decisão reversível, cada qual com Objetivo, Pré-requisito, Execute, Observe, Compare e questões exploratórias.

- [ ] **Passo 5: verificar e registrar a entrega**

```bash
python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_module_one_workshop_is_an_exploratory_ollama_lab tests.test_applied_literacy.AppliedLiteracyTest.test_module_one_temperature_experiment_uses_the_local_ollama_api tests.test_applied_literacy.AppliedLiteracyTest.test_module_two_uses_litellm_proxy_and_a_versioned_manifest -v
git add docs/modulo-1-fundamentos/oficina-de-ferramentas.md docs/modulo-2-desenho-conceitual/oficina-de-ferramentas.md docs/assets/labs/modulo-2
git commit -m "docs: standardize local foundations and LiteLLM labs"
```

### Tarefa 4: reconstruir o Módulo 3 como RAG local observável

**Arquivos:**

- Modificar: `docs/modulo-3-rag/oficina-de-ferramentas.md`
- Usar: `docs/assets/labs/modulo-3/`

**Interfaces:** recebe o corpus Boreal e uma pergunta; produz `chroma-boreal`, IDs/versões recuperados e uma resposta citada ou `REVISÃO_HUMANA`.

- [ ] **Passo 1: introduzir corpus, ingestão e recuperação antes de executar**

Definir corpus como conjunto de arquivos consultáveis, ingestão como leitura/indexação e recuperação como seleção de trechos. Ligar cada conceito ao arquivo ou etapa executada.

- [ ] **Passo 2: escrever a receita completa**

```bash
mkdir oficina-m3 && cd oficina-m3
python -m venv .venv
source .venv/bin/activate
python -m pip install langchain langchain-chroma chromadb langchain-ollama
mkdir corpus
python rag_local.py --pergunta 'Qual é o prazo para solicitar reembolso em uma compra regular?'
```

Explicar exatamente onde copiar os três documentos e o script; incluir a alternativa PowerShell.

- [ ] **Passo 3: expor evidência e abstenção**

Exigir `RECUPERADO POL-17:v3` antes da resposta. A segunda execução é:

```bash
python rag_local.py --pergunta 'Não sei a data nem se a compra era promocional; qual prazo devo informar?'
```

Resultado esperado: encaminhamento a revisão humana. A variação usa `--excluir POL-17:v3`, compara IDs e explica que se trata de falha simulada de ingestão/filtro.

- [ ] **Passo 4: manter os três experimentos e a entrega**

A: ingestão e evidência; B: recuperação e resposta fundamentada; C: falha e abstenção. A entrega transcreve IDs/versões e compara as duas execuções.

- [ ] **Passo 5: validar e registrar**

```bash
python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_module_three_provides_files_ingestion_retrieval_and_abstention -v
git add docs/modulo-3-rag/oficina-de-ferramentas.md docs/assets/labs/modulo-3
git commit -m "docs: rebuild module three as a local RAG lab"
```

### Tarefa 5: reconstruir os laboratórios dos Módulos 4, 5 e 6

**Arquivos:**

- Modificar: `docs/modulo-4-agentes/oficina-de-ferramentas.md`
- Modificar: `docs/modulo-5-confianca/oficina-de-ferramentas.md`
- Modificar: `docs/modulo-6-operacao/oficina-de-ferramentas.md`
- Usar: `docs/assets/labs/modulo-4/`, `docs/assets/labs/modulo-5/`, `docs/assets/labs/modulo-6/`

**Interfaces:** M4 imprime estado da troca; M5 cria relatório de avaliação; M6 imprime trace, duração e atributos minimizados.

- [ ] **Passo 1: aplicar a mesma estrutura de nove seções**

Remover `## Roteiros equivalentes de acesso` das três páginas. Em cada contingência, orientar diagnóstico/limpeza do mesmo laboratório instalado, sem trocar a atividade por análise manual.

- [ ] **Passo 2: instrumentar o M4 com LangGraph**

Documentar `python -m pip install langgraph langchain-ollama`, depois executar `troca_boreal.py` com `--aprovado false`, `--aprovado true` e `--aprovado true --repetir`. Observar, respectivamente, parada, reserva e idempotência.

- [ ] **Passo 3: instrumentar o M5 com DeepEval**

Documentar `python -m pip install deepeval langchain-ollama`, a cópia de `casos_confianca.json` e `python avaliar_confianca.py`. A saída deve mostrar caso, decisão esperada, decisão observada e justificativa; a variação altera uma regra sintética e mede a diferença no relatório.

- [ ] **Passo 4: instrumentar o M6 com OpenTelemetry**

Documentar `python -m pip install opentelemetry-api opentelemetry-sdk 'litellm[proxy]'`, a inicialização do LiteLLM Proxy do M2 e `python telemetria_local.py`. Observar `trace_id`, duração e atributos. A variação muda só uma entrada sintética e compara duração, erro e metadados, sem inferir causalidade de um único trace.

- [ ] **Passo 5: executar a suíte e criar o commit**

```bash
python -m unittest tests.test_applied_literacy -v
git add docs/modulo-4-agentes/oficina-de-ferramentas.md docs/modulo-5-confianca/oficina-de-ferramentas.md docs/modulo-6-operacao/oficina-de-ferramentas.md docs/assets/labs/modulo-4 docs/assets/labs/modulo-5 docs/assets/labs/modulo-6
git commit -m "docs: make advanced workshops locally executable"
```

### Tarefa 6: alinhar exercícios, guia e validação final

**Arquivos:**

- Modificar: `docs/modulo-*/exercicios.md`
- Modificar: `docs/referencia/guia-de-ferramentas.md`
- Modificar: `docs/sobre/projeto-final.md`
- Modificar, se necessário: `docs/referencia/fontes.yml`, `docs/referencia/bibliografia.md`

**Interfaces:** os exercícios passam a referenciar as saídas dos laboratórios locais sem mudar os níveis ou rubricas Bloom existentes.

- [ ] **Passo 1: localizar e remover a linguagem de acesso**

```bash
rg -n -i 'cartão|crédito|cobrança|sem cartão|rota comercial|rota institucional' docs --glob '*.md' --glob '!superpowers/**'
```

Substituir menções em exercícios por referências à execução correspondente, como “use a saída do laboratório de RAG local”. Não alterar quantidade de questões ou rubricas Bloom.

- [ ] **Passo 2: alinhar guia e projeto final**

Apresentar ferramenta local por módulo e a regra “a evidência é a execução e a interpretação arquitetural”. Remover classificações de acesso, comparação de modalidades e mérito por plataforma.

- [ ] **Passo 3: registrar links oficiais novos**

Se forem adicionados links novos das ferramentas, incluir cada um em `fontes.yml` e `bibliografia.md` no formato vigente antes de colocar o URL em Markdown.

- [ ] **Passo 4: rodar todas as validações**

```bash
python -m unittest discover -s tests -v
python scripts/validate_content.py --all
mkdocs build --strict
rg -n -i 'cartão|crédito|cobrança|sem cartão|rota comercial|rota institucional' site || true
```

Resultado esperado: todos os testes passam, a construção não emite avisos e a busca em `site/` não retorna páginas públicas.

- [ ] **Passo 5: revisar e publicar**

```bash
mkdocs serve
```

Conferir as seis páginas de oficina, os links de download, os blocos de comando e as quebras de linha; encerrar com `Ctrl+C`. Em seguida:

```bash
git add docs tests README.md
git commit -m "feat: deliver executable local course workshops"
git push origin main
```

## Revisão do plano

- A Tarefa 1 substitui a política antiga por um contrato testável; a Tarefa 2 cria os artefatos; as Tarefas 3–5 entregam os seis laboratórios; a Tarefa 6 limpa os exercícios, valida e publica.
- LiteLLM é introduzido no M2 e observado no M6; `POL-17:v3` é preservado nos arquivos e na saída do M3; todos os scripts têm caminho definido.
- O plano não inclui implantação, serviços externos, modelos distribuídos ou dados reais.
