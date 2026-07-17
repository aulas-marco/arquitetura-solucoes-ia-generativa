# Enunciados explícitos para exercícios de arquitetura de IA — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Revisar os exercícios dos seis módulos para que cada tarefa avançada explique o artefato pedido, indique onde estudá-lo, conduza a produção e forneça uma verificação de completude.

**Architecture:** A alteração será editorial e orientada por contrato. Cada módulo manterá a estrutura de Bloom, o contexto, o papel, os insumos, a entrega e os critérios percentuais; as instruções receberão definições locais, referências e passos observáveis. Um teste de contrato verificará a presença dos blocos de orientação nos seis arquivos sem publicar gabaritos.

**Tech Stack:** Markdown, MkDocs Material, Python `unittest`, `scripts/validate_content.py`.

## Global Constraints

- Revisar os seis arquivos `docs/modulo-*/exercicios.md`.
- Priorizar Aplicar, Analisar, Avaliar e Criar sem remover Recordar e Compreender.
- Para cada objeto pedido, explicar o que é, onde encontrar, como produzir e como verificar.
- Reutilizar conceitos, exemplos, oficinas, glossário e templates existentes.
- Manter critérios de avaliação em percentuais e não publicar respostas canônicas para níveis avançados.
- Não trocar ferramentas locais das oficinas, exigir serviços pagos ou usar dados reais.
- Não publicar a documentação interna em `docs/superpowers/` na navegação do curso.

---

### Task 1: Criar o contrato de clareza dos enunciados

**Files:**
- Modify: `tests/test_applied_literacy.py`
- Test: `tests/test_applied_literacy.py`

**Interfaces:**
- Consumes: seis arquivos `docs/modulo-*/exercicios.md` e a função `section` já existente.
- Produces: teste que exige orientação explícita em cada nível avançado e rejeita instruções sem referência ou procedimento.

- [x] **Step 1: Write the failing test**

Adicionar um teste que, para cada módulo e nível em `Aplicar`, `Analisar`, `Avaliar` e `Criar`, exija:

```python
for marker in (
    "**Situação**",
    "**Seu papel**",
    "**Insumos disponíveis**",
    "**Como conduzir**",
    "**Entrega esperada**",
    "**Critérios de avaliação**",
):
    self.assertIn(marker, advanced)
self.assertRegex(advanced, r"(?i)(o que é|significa)")
self.assertRegex(advanced, r"\[[^\]]+\]\([^\)]+\)")
self.assertRegex(advanced, r"(?m)^\d+\. ")
self.assertRegex(advanced, r"(?i)(verifique|confira|revis[eã]o|complet) ")
```

O teste deve isolar cada seção Bloom para que uma explicação de outro nível não satisfaça o contrato por acidente.

- [x] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_advanced_exercises_explain_artifacts_and_procedure -v`

Expected: FAIL porque os exercícios atuais têm contexto e critérios, mas nem todos explicam o objeto, a referência e a verificação no próprio nível.

- [x] **Step 3: Commit the failing test**

```bash
git add tests/test_applied_literacy.py
git commit -m "test: require explicit exercise instructions"
```

### Task 2: Tornar explícitos os exercícios dos módulos 1 e 2

**Files:**
- Modify: `docs/modulo-1-fundamentos/exercicios.md`
- Modify: `docs/modulo-2-desenho-conceitual/exercicios.md`

**Interfaces:**
- Consumes: `conceitos.md`, `padroes-e-decisoes.md`, `exemplo-arquitetural.md`, `estudo-de-caso.md`, oficinas locais e `docs/referencia/template-adr.md`.
- Produces: quatro atividades avançadas por módulo com definição, localização, procedimento, entrega e checagem claros.

- [x] **Step 1: Map each artifact before editing**

Para cada atividade, listar no próprio enunciado os objetos que o aluno deve produzir. No módulo 1, cobrir classificação, cenário de qualidade, comparação arquitetural, ADR e diagrama. No módulo 2, cobrir problema observável, critério probabilístico, matriz de escolhas, decisão de agente e arquitetura-alvo.

- [x] **Step 2: Rewrite the local guidance**

Substituir instruções genéricas por frases no formato:

```markdown
**O que é:** [definição curta do artefato].

**Onde encontrar:** [link para conceito, exemplo ou template].

**Como conduzir:**
1. [ação concreta com campos, caixas ou linhas a preencher].
2. [ação que relaciona o resultado ao caso].
3. [ação que registra hipótese, limite ou responsável].

**Como verificar antes de entregar:** [checklist observável].
```

Para o exemplo do recibo, declarar que a fronteira separa responsabilidades, nomear as caixas “Extração do recibo”, “Regra de limite”, “Proposta de despesa” e “Lançamento financeiro”, indicar o dado em cada seta e exigir autorização no efeito financeiro.

- [x] **Step 3: Run focused checks**

Run: `python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_advanced_exercises_explain_artifacts_and_procedure tests.test_module_one tests.test_module_two -v`

Expected: PASS for modules 1 and 2.

- [x] **Step 4: Commit the module pair**

```bash
git add docs/modulo-1-fundamentos/exercicios.md docs/modulo-2-desenho-conceitual/exercicios.md
git commit -m "docs: clarify foundational and conceptual exercises"
```

### Task 3: Tornar explícitos os exercícios dos módulos 3 e 4

**Files:**
- Modify: `docs/modulo-3-rag/exercicios.md`
- Modify: `docs/modulo-4-agentes/exercicios.md`

**Interfaces:**
- Consumes: conceitos, padrões, estudos de caso, oficinas locais, scripts e templates dos módulos 3 e 4.
- Produces: instruções executáveis para métricas RAG, chunking, autorização, seleção de padrão, contratos de ferramentas, autonomia, diagnóstico de trace e arquitetura de agente.

- [x] **Step 1: Explain retrieval artifacts in place**

Definir chunk, conjunto de referência, `Recall@5`, `Precision@5`, proveniência, cache e citação. Linkar para os padrões e para a oficina local. Mostrar numerador, denominador, fonte da lista de relevantes e formato da tabela esperada.

- [x] **Step 2: Explain agent artifacts in place**

Definir contrato de ferramenta, idempotência, timeout, estado desconhecido, nível A0–A5 e trace. Linkar para o catálogo e para a oficina. Nomear os campos a preencher e indicar como diferenciar fato observado, hipótese, contenção e reconciliação.

- [x] **Step 3: Add verification checklists**

Em cada atividade avançada, incluir uma checagem que confirme autorização antes da materialização, ausência de chamada proibida, identidade e versão, ou coerência entre fluxo, efeito e aprovação.

- [x] **Step 4: Run focused checks and commit**

Run: `python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_advanced_exercises_explain_artifacts_and_procedure tests.test_module_three tests.test_module_four -v`

```bash
git add docs/modulo-3-rag/exercicios.md docs/modulo-4-agentes/exercicios.md
git commit -m "docs: clarify retrieval and agent exercises"
```

### Task 4: Tornar explícitos os exercícios dos módulos 5 e 6

**Files:**
- Modify: `docs/modulo-5-confianca/exercicios.md`
- Modify: `docs/modulo-6-operacao/exercicios.md`

**Interfaces:**
- Consumes: modelos de ameaça, pipeline de avaliação, conceitos de operação, manifesto, traces, SLOs, padrões de plataforma e projeto final.
- Produces: instruções guiadas para controles, ameaças, avaliação multidimensional, risco residual, ciclo de operação, métricas, portabilidade e arquitetura final.

- [x] **Step 1: Explain trust and governance artifacts**

Definir ativo, ameaça, controle em profundidade, teste negativo, fatia, critério de avaliação, portão e risco residual. Apontar o diagrama, o estudo de caso, a oficina de confiança e o catálogo de qualidade.

- [x] **Step 2: Explain operational artifacts**

Definir ativo comportamental, manifesto, span, SLO, indicador, janela, canary, rollback, fallback, runbook, ADR e fronteira de propriedade. Apontar exemplos e nomear os campos que o aluno deve preencher.

- [x] **Step 3: Add vertical and horizontal verification**

Para o projeto do módulo 6, explicar como seguir uma mudança de corpus de versão a incidente e uma ação de usuário até auditoria, com uma tabela de etapas, responsável, evidência e decisão.

- [x] **Step 4: Run focused checks and commit**

Run: `python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_advanced_exercises_explain_artifacts_and_procedure tests.test_module_five tests.test_module_six -v`

```bash
git add docs/modulo-5-confianca/exercicios.md docs/modulo-6-operacao/exercicios.md
git commit -m "docs: clarify trust and operations exercises"
```

### Task 5: Verificar linguagem, referências e limites editoriais

**Files:**
- Modify: `tests/test_applied_literacy.py` only if the contract needs a precise assertion.
- Modify: `docs/modulo-*/exercicios.md` only for residual hermetic terms found by review.

**Interfaces:**
- Consumes: seis páginas revisadas e o contrato de clareza.
- Produces: nenhum termo operacional sem definição ou referência na primeira ocorrência relevante.

- [x] **Step 1: Search for residual opaque directives**

Run:

```bash
rg -n "Desenhe|Preencha|Calcule|Defina|Compare|Relacione|Separe|Marque|Trace|SLO|ADR|baseline|fronteira|proveniência|chunk|portão|canary|rollback|runbook" docs/modulo-*/exercicios.md
```

Para cada ocorrência, confirmar que a seção contém definição, link e critério de verificação; reescrever somente quando faltar um deles.

- [x] **Step 2: Check link targets and answer policy**

Run: `python scripts/validate_content.py --all`

Expected: no broken local references, no missing Bloom levels, no public answer blocks in advanced sections and no forbidden editorial markers.

- [x] **Step 3: Commit residual fixes**

```bash
git add docs/modulo-*/exercicios.md tests/test_applied_literacy.py
git commit -m "docs: remove remaining hermetic exercise prompts"
```

### Task 6: Verificação final e publicação

**Files:**
- Verify: `tests/`, `scripts/validate_content.py`, `mkdocs.yml`, `docs/modulo-*/exercicios.md`

**Interfaces:**
- Consumes: todos os commits anteriores.
- Produces: site MkDocs estrito sem erros e evidência registrada para integração.

- [x] **Step 1: Run the complete test suite**

Run: `python -m unittest discover -s tests`

Expected: all tests pass.

- [x] **Step 2: Run the content validator**

Run: `python scripts/validate_content.py --all`

Expected: validation completes without errors.

- [x] **Step 3: Build MkDocs strictly**

Run: `mkdocs build --strict --site-dir /tmp/arquitetura-solucoes-ia-generativa-final`

Expected: exit code 0. The Material for MkDocs advisory about MkDocs 2.0 is informational and does not fail the build.

- [x] **Step 4: Review the diff and commit if needed**

Run: `git diff --check && git status -sb && git log --oneline -8`

Expected: no whitespace errors and only intended files changed.
