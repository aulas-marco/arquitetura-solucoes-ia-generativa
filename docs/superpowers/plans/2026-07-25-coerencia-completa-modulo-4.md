# Coerência completa do Módulo 4 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Propagar decisões arquiteturais de autonomia a todos os materiais do Módulo 4.

**Architecture:** Conceitos e padrões definem responsabilidades, tensões, plataforma e fitness functions. Abertura, exemplo, caso, oficina, exercícios e síntese exigem as mesmas evidências em seus próprios formatos.

**Tech Stack:** Markdown, MkDocs, pytest e validador de conteúdo.

## Global Constraints

- Preservar matriz de autonomia, SDD, cenários e progressão de Bloom.
- Não apresentar agente como solução universal.
- Manter decisões independentes de fornecedor.

---

### Task 1: Alinhar conceitos e padrões

**Files:**
- Modify: `docs/modulo-4-agentes/conceitos.md`
- Modify: `docs/modulo-4-agentes/padroes-e-decisoes.md`

- [ ] Inserir matriz de características, responsabilidades de componentes, decisão de plataforma e fitness functions.

### Task 2: Propagar a lente ao restante do módulo

**Files:**
- Modify: `docs/modulo-4-agentes/index.md`
- Modify: `docs/modulo-4-agentes/exemplo-arquitetural.md`
- Modify: `docs/modulo-4-agentes/estudo-de-caso.md`
- Modify: `docs/modulo-4-agentes/oficina-de-ferramentas.md`
- Modify: `docs/modulo-4-agentes/exercicios.md`
- Modify: `docs/modulo-4-agentes/sintese-e-referencias.md`

- [ ] Inserir prioridade, tensão, responsável e fitness function nos artefatos de decisão, prática e avaliação.

### Task 3: Validar

- [ ] Run: `python scripts/validate_content.py --all && python -m pytest -q && mkdocs build --strict`
