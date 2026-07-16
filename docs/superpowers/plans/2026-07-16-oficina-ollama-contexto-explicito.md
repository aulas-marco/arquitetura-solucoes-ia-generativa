# Contexto Explícito na Oficina Ollama Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fazer a Oficina 1 explicar cenário, corpus e cada ação de copiar, colar, executar e registrar.

**Architecture:** Um teste editorial protege as explicações obrigatórias; a página passa a ordenar cenário → conceitos → instalação → experimentos guiados → comparação → contingência.

**Tech Stack:** Markdown, MkDocs e Python `unittest`.

## Global Constraints

- Aurora e a Política Aurora são explicitamente fictícias.
- Corpus e contexto são definidos antes de qualquer uso e têm links internos.
- Experimentos informam local, cópia, colagem, tecla, resultado e registro.
- A frase “acrescente o corpus” não aparece.

### Task 1: Proteger e reescrever a oficina

**Files:**
- Modify: `tests/test_applied_literacy.py`
- Modify: `docs/modulo-1-fundamentos/oficina-de-ferramentas.md`

- [ ] **Step 1: Escrever o teste de instrução explícita**

```python
def test_module_one_explains_fictional_corpus_and_copy_paste_actions(self):
    text = (DOCS / "modulo-1-fundamentos" / OFFICE).read_text(encoding="utf-8").casefold()
    for phrase in ("empresa fictícia aurora", "documento fictício", "corpus é", "contexto é", "copie o bloco inteiro", "cole", "pressione `enter`", "registre"):
        self.assertIn(phrase, text)
    self.assertNotIn("acrescente o corpus", text)
```

- [ ] **Step 2: Executar o teste e confirmar a falha**

Run: `python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_module_one_explains_fictional_corpus_and_copy_paste_actions -v`  
Expected: FAIL na oficina atual.

- [ ] **Step 3: Reordenar a página**

Antes do passo 1, escrever o cenário fictício, definir corpus e contexto, e explicar que a Política Aurora é o único documento da prática. Em A, B e C, declarar Terminal/cursor `>>>`, bloco integral, comando de colar, Enter, espera e registro. O bloco B inclui instrução, política e pergunta em uma única caixa.

- [ ] **Step 4: Validar e fazer commit**

Run: `python -m unittest tests.test_applied_literacy tests.test_module_one -v && python scripts/validate_content.py --all && mkdocs build --strict`  
Expected: PASS.

```bash
git add tests/test_applied_literacy.py docs/modulo-1-fundamentos/oficina-de-ferramentas.md
git commit -m "docs: clarify ollama corpus lab instructions"
```
