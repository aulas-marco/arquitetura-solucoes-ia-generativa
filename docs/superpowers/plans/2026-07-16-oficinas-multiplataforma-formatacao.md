# Oficinas multiplataforma e legíveis — plano de implementação

> **Para agentes:** SUB-HABILIDADE OBRIGATÓRIA: usar `superpowers:subagent-driven-development` (recomendado) ou `superpowers:executing-plans` para executar este plano tarefa a tarefa. Os passos usam caixas de seleção (`- [ ]`) para acompanhamento.

**Objetivo:** tornar os experimentos visualmente escaneáveis e as seis instalações utilizáveis em macOS, Linux e Windows.

**Arquitetura:** o conteúdo permanece em Markdown. Os experimentos usam blocos rotulados em parágrafos separados; todas as oficinas passam a seguir uma sequência comum de verificação, instruções por sistema operacional e instalação da ferramenta.

**Tecnologias:** MkDocs Material, Markdown, Python 3, Ollama, LiteLLM, LangChain/Chroma, LangGraph, DeepEval e OpenTelemetry.

## Restrições globais

- Não exigir Homebrew, `apt`, `dnf` ou uma distribuição Linux específica.
- Usar `python3` em macOS/Linux, `python` em Windows, `source .venv/bin/activate` em macOS/Linux e `.venv\Scripts\Activate.ps1` em PowerShell.
- Só pedir Ollama nos módulos 1, 2, 3, 5 e 6.
- Manter dados sintéticos, exercícios Bloom, links válidos e orçamentos editoriais atuais.
- Validar com testes, validador de conteúdo e `mkdocs build --strict`.

---

### Tarefa 1: criar regressões para legibilidade e plataformas

**Arquivos:**

- Modificar: `tests/test_applied_literacy.py`

**Interfaces:** consome `docs/modulo-*/oficina-de-ferramentas.md`; produz uma garantia de estrutura visual e instruções por sistema operacional.

- [ ] **Passo 1: escrever o teste que falha**

Adicionar este método à classe `AppliedLiteracyTest`:

```python
def test_every_workshop_has_platform_instructions_and_block_experiments(self):
    for slug in MODULES:
        text = (DOCS / slug / OFFICE).read_text(encoding="utf-8")
        for platform in ("### macOS", "### Linux", "### Windows"):
            self.assertIn(platform, text, f"{slug}: {platform}")
        self.assertIn("**Objetivo**\n\n", text, slug)
        self.assertIn("**Pré-requisito**\n\n", text, slug)
        self.assertIn("**Execute**\n\n", text, slug)
        self.assertIn("**Observe**\n\n", text, slug)
        self.assertIn("**Compare**\n\n", text, slug)
```

- [ ] **Passo 2: executar para confirmar a falha**

```bash
python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_every_workshop_has_platform_instructions_and_block_experiments -v
```

Resultado esperado: falha porque os experimentos ainda combinam rótulos e macOS/Linux não aparecem em todas as oficinas.

- [ ] **Passo 3: registrar a nova regressão**

```bash
git add tests/test_applied_literacy.py
git commit -m "test: require readable multiplatform workshops"
```

### Tarefa 2: padronizar a instalação multiplataforma nas seis oficinas

**Arquivos:**

- Modificar: `docs/modulo-1-fundamentos/oficina-de-ferramentas.md`
- Modificar: `docs/modulo-2-desenho-conceitual/oficina-de-ferramentas.md`
- Modificar: `docs/modulo-3-rag/oficina-de-ferramentas.md`
- Modificar: `docs/modulo-4-agentes/oficina-de-ferramentas.md`
- Modificar: `docs/modulo-5-confianca/oficina-de-ferramentas.md`
- Modificar: `docs/modulo-6-operacao/oficina-de-ferramentas.md`

**Interfaces:** cada página apresenta `### macOS`, `### Linux` e `### Windows`; macOS/Linux compartilham comandos POSIX e Windows usa PowerShell.

- [ ] **Passo 1: inserir a verificação comum antes da instalação da ferramenta**

Em macOS/Linux, publicar:

```bash
python3 --version
```

Em Windows PowerShell, publicar:

```powershell
python --version
```

Explicar que a versão deve ser 3.10 ou superior e que o próprio instalador oficial da ferramenta é a fonte de instalação quando o comando não existir.

- [ ] **Passo 2: descrever macOS e Linux sem dependência de distribuição**

Nos módulos com Ollama, indicar [instalador oficial do Ollama](https://ollama.com/download), `ollama --version` e o `ollama pull` correspondente. No Linux, indicar que o site oficial oferece o procedimento atualizado e que o aluno deve executar os comandos no terminal da distribuição. Homebrew e gerenciadores de pacotes aparecem somente como nota opcional.

- [ ] **Passo 3: descrever Windows PowerShell**

Manter a ativação:

```powershell
.venv\Scripts\Activate.ps1
```

Explicar que, se a política de execução bloquear a ativação, o aluno deve consultar o suporte local/professor, sem usar uma alternativa insegura.

- [ ] **Passo 4: aplicar os requisitos específicos**

- M1: Ollama, `llama3.2:3b` e `curl`.
- M2: Ollama, `llama3.2:3b` e `litellm[proxy]`.
- M3: Ollama, `llama3.2:3b`, `nomic-embed-text`, LangChain, Chroma e integração Ollama.
- M4: apenas Python, ambiente virtual e LangGraph.
- M5: Ollama, `llama3.2:3b` e DeepEval.
- M6: Ollama, `llama3.2:3b`, LiteLLM Proxy e OpenTelemetry.

- [ ] **Passo 5: verificar o teste de plataformas**

```bash
python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_every_workshop_has_platform_instructions_and_block_experiments -v
```

Resultado esperado: PASS.

### Tarefa 3: reformatar todos os experimentos

**Arquivos:** os mesmos seis arquivos de oficina da Tarefa 2.

**Interfaces:** cada título de experimento é seguido por blocos separados de Objetivo, Pré-requisito, Execute, Observe e Compare, e depois por questões exploratórias.

- [ ] **Passo 1: reformular os quatro experimentos do M1**

Trocar cada linha compacta por:

```markdown
**Objetivo**

Identificar o limite de uma resposta sem documento de referência.

**Pré-requisito**

Preparação local concluída.
```

Repetir para `Execute`, `Observe` e `Compare`, preservando os comandos e os quatro experimentos.

- [ ] **Passo 2: reformular os três experimentos de cada módulo 2–6**

Aplicar o mesmo padrão de blocos aos 15 experimentos restantes. Não modificar classificação, perguntas exploratórias, comandos, variáveis controladas ou evidências de entrega.

- [ ] **Passo 3: testar leitura e estrutura completa**

```bash
python -m unittest tests.test_applied_literacy -v
python scripts/validate_content.py --all
```

Resultado esperado: PASS, sem quebrar as contagens de Bloom, links ou orçamento de palavras.

- [ ] **Passo 4: commit das oficinas**

```bash
git add docs/modulo-*/oficina-de-ferramentas.md
git commit -m "docs: improve workshop layout and platform guidance"
```

### Tarefa 4: verificação e publicação

**Arquivos:** verificar o repositório completo e `.github/workflows/publicar-site.yml`.

- [ ] **Passo 1: rodar a suíte e construir o site**

```bash
python -m unittest discover -s tests -v
python scripts/validate_content.py --all
mkdocs build --strict
```

Resultado esperado: testes, validação e build sem erros.

- [ ] **Passo 2: revisar a visualização local**

```bash
mkdocs serve
```

Abrir ao menos as oficinas dos módulos 1, 2, 3 e 6; verificar que rótulos não se unem em parágrafos e que as três plataformas estão fáceis de localizar. Encerrar com `Ctrl+C`.

- [ ] **Passo 3: enviar a publicação**

```bash
git push origin main
```

## Revisão do plano

- A Tarefa 1 fixa a regressão visual e multiplataforma; a Tarefa 2 atende instalação; a Tarefa 3 atende leitura dos 19 experimentos; a Tarefa 4 valida e publica.
- Não há requisito de gerenciador de pacote ou distribuição Linux; a única diferença de comando é explicitada por sistema operacional.
