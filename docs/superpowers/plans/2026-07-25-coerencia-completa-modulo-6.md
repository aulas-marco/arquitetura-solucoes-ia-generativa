# Coerência completa do Módulo 6 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Propagar decisões arquiteturais operacionais a todos os materiais do Módulo 6.

**Architecture:** Conceitos e padrões estabelecem prioridades, fronteiras, fitness functions e escolha de plataforma. Os demais artefatos usam os mesmos critérios para prática, caso, capstone e checklist de produção.

**Tech Stack:** Markdown, MkDocs, pytest e validador de conteúdo.

## Global Constraints

- Preservar cenários, progressão de Bloom e independência de fornecedor.
- Não tratar mecanismos de plataforma como autoridade de domínio.
- Manter a promoção por manifesto, a recuperação proporcional e o risco residual.

---

### Task 1: Alinhar conceitos e decisões

**Files:**
- Modify: `docs/modulo-6-operacao/conceitos.md`
- Modify: `docs/modulo-6-operacao/padroes-e-decisoes.md`

- [ ] Inserir matriz de características, fronteiras de plataforma, fitness functions e decisão de obtenção de capacidade.

### Task 2: Propagar a lente ao restante do módulo

**Files:**
- Modify: `docs/modulo-6-operacao/index.md`
- Modify: `docs/modulo-6-operacao/exemplo-arquitetural.md`
- Modify: `docs/modulo-6-operacao/estudo-de-caso.md`
- Modify: `docs/modulo-6-operacao/oficina-de-ferramentas.md`
- Modify: `docs/modulo-6-operacao/exercicios.md`
- Modify: `docs/modulo-6-operacao/sintese-e-referencias.md`

- [ ] Inserir prioridade, tensão, responsável e fitness function nos artefatos de operação e avaliação.

### Task 3: Validar

- [ ] Run: `python scripts/validate_content.py --all && python -m pytest -q && mkdocs build --strict`
