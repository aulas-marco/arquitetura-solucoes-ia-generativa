# Oficina Instrumental com Ollama Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Converter a Oficina 1 em um laboratório linear, reproduzível e explicado com Ollama.

**Architecture:** Uma única página concentra a receita principal, corpus copiável, três experimentos, tabela de comparação e contingência final. O glossário fornece aprofundamento por links, sem interromper a execução do aluno.

**Tech Stack:** Markdown, links internos MkDocs, Python `unittest`, validador editorial.

## Global Constraints

- Abrir com Ollama como ferramenta open source, sem usar “Essencial, sem cartão”.
- Usar oito passos sequenciais, comandos e resultado observável.
- Explicar e linkar modelo, inferência, prompt, corpus, contexto, fundamentação, variabilidade e alucinação.
- Usar apenas corpus sintético, sem chave, API, conta ou dados reais.
- Deixar a contingência no final.

---

### Task 1: Definir o contrato do laboratório

**Files:**
- Modify: `tests/test_applied_literacy.py`

- [ ] **Step 1: Adicionar o teste específico do Módulo 1**

```python
def test_module_one_workshop_is_a_linear_ollama_lab(self):
    text = (DOCS / "modulo-1-fundamentos" / OFFICE).read_text(encoding="utf-8")
    self.assertIn("Ferramenta:** Ollama", text)
    self.assertNotIn("Essencial, sem cartão", text)
    for command in ("ollama --version", "ollama pull llama3.2:3b", "ollama run llama3.2:3b", "ollama rm llama3.2:3b"):
        self.assertIn(command, text)
    for step in range(1, 9):
        self.assertRegex(text, rf"(?m)^{step}\. ")
    for term in ("modelo", "inferência", "prompt", "corpus", "contexto", "fundamentação", "alucinação"):
        self.assertRegex(text.casefold(), rf"\[{term}[^]]*\]\([^)]*\)")
```

- [ ] **Step 2: Executar para confirmar a falha**

Run: `python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_module_one_workshop_is_a_linear_ollama_lab -v`  
Expected: FAIL porque a estrutura atual ainda declara rotas de acesso.

- [ ] **Step 3: Fazer commit**

```bash
git add tests/test_applied_literacy.py
git commit -m "test: define linear ollama workshop contract"
```

### Task 2: Reescrever a oficina como roteiro instrumental

**Files:**
- Modify: `docs/modulo-1-fundamentos/oficina-de-ferramentas.md`

- [ ] **Step 1: Substituir a abertura por contrato de laboratório**

Escrever `Ferramenta: Ollama — executor local de modelos open source`, objetivo, 35 minutos e resultado esperado. Remover toda a seção `Roteiros equivalentes de acesso`.

- [ ] **Step 2: Escrever os oito passos com blocos copiáveis**

Incluir comandos de instalação por link oficial, versão, pull, run e remoção; inserir o corpus Aurora num bloco copiável; fornecer os três experimentos e uma tabela a preencher após cada execução.

- [ ] **Step 3: Inserir explicações e links internos**

Definir cada termo novo na primeira ocorrência e linkar `conceitos.md` ou `../referencia/glossario.md`. Não usar links externos para conceitos.

- [ ] **Step 4: Encerrar com comparação e contingência**

Incluir três perguntas arquiteturais curtas e a contingência após a limpeza.

- [ ] **Step 5: Executar verificação**

Run: `python -m unittest tests.test_applied_literacy tests.test_module_one -v && python scripts/validate_content.py --all && mkdocs build --strict`  
Expected: PASS.

- [ ] **Step 6: Fazer commit**

```bash
git add docs/modulo-1-fundamentos/oficina-de-ferramentas.md
git commit -m "docs: make module one ollama workshop instrumental"
```

## Revisão do plano

- Task 1 protege o formato e Task 2 implementa todo o roteiro aprovado.
- A receita não amplia a dependência de ferramentas pagas nem altera as demais oficinas.
