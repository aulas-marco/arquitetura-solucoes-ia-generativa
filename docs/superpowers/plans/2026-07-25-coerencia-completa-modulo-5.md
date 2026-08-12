# Coerência completa do Módulo 5 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Propagar decisões arquiteturais de confiança a todos os materiais do Módulo 5.

**Architecture:** Conceitos e padrões definem prioridades, fronteiras, fitness functions e decisão de plataforma. Os demais artefatos materializam os mesmos critérios em cenários, práticas, exercícios e checklist.

**Tech Stack:** Markdown, MkDocs, pytest e validador de conteúdo.

## Global Constraints

- Preservar os cenários, referenciais e progressão de Bloom existentes.
- Não apresentar uma métrica, guardrail ou fornecedor como garantia de confiança.
- Manter a independência de fornecedor e a aceitação formal de risco residual.

---

### Task 1: Alinhar conceitos e decisões

**Files:**
- Modify: `docs/modulo-5-confianca/conceitos.md`
- Modify: `docs/modulo-5-confianca/padroes-e-decisoes.md`

- [ ] Inserir matriz de características, fronteiras de responsabilidade, fitness functions e decisão de plataforma.

### Task 2: Propagar a lente ao restante do módulo

**Files:**
- Modify: `docs/modulo-5-confianca/index.md`
- Modify: `docs/modulo-5-confianca/exemplo-arquitetural.md`
- Modify: `docs/modulo-5-confianca/estudo-de-caso.md`
- Modify: `docs/modulo-5-confianca/oficina-de-ferramentas.md`
- Modify: `docs/modulo-5-confianca/exercicios.md`
- Modify: `docs/modulo-5-confianca/sintese-e-referencias.md`

- [ ] Inserir prioridade, tensão, responsável e fitness function nos artefatos de decisão, prática e avaliação.

### Task 3: Validar

- [ ] Run: `python scripts/validate_content.py --all && python -m pytest -q && mkdocs build --strict`
