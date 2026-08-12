# Coerência completa do Módulo 3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Alinhar todos os artefatos didáticos restantes do Módulo 3 à arquitetura de RAG orientada por evidências, características e trade-offs.

**Architecture:** A abertura anuncia o mesmo vocabulário que caso, exemplo, oficina, exercícios e síntese praticam. Cada artefato acrescenta proveniência, responsabilidades, prioridade, tensão e fitness functions sem alterar seu formato pedagógico.

**Tech Stack:** Markdown, MkDocs, pytest e validador de conteúdo.

## Global Constraints

- Não alterar `conceitos.md` ou `padroes-e-decisoes.md` nesta etapa.
- Manter cenários, formatos de entrega e independência de fornecedor.
- Preservar 12 exercícios e progressão de Bloom.

---

### Task 1: Propagar decisões arquiteturais no material didático

**Files:**
- Modify: `docs/modulo-3-rag/index.md`
- Modify: `docs/modulo-3-rag/exemplo-arquitetural.md`
- Modify: `docs/modulo-3-rag/estudo-de-caso.md`
- Modify: `docs/modulo-3-rag/oficina-de-ferramentas.md`
- Modify: `docs/modulo-3-rag/exercicios.md`
- Modify: `docs/modulo-3-rag/sintese-e-referencias.md`

**Interfaces:**
- Consumes: proveniência, responsabilidades, matriz de características e fitness functions das páginas revisadas.
- Produces: atividades e referências coerentes com o vocabulário arquitetural do módulo.

- [ ] **Step 1: Alinhar abertura, exemplo e caso**

Inserir prioridades, tensões, responsáveis, decisão de plataforma e evidências de promoção nos pontos em que cada artefato apresenta arquitetura ou escolha.

- [ ] **Step 2: Alinhar oficina, exercícios e síntese**

Exigir proveniência, responsabilidade de componente e fitness functions nas entregas, critérios e checklists, sem mudar a classificação de Bloom.

- [ ] **Step 3: Validar**

Run: `python scripts/validate_content.py --all && python -m pytest -q && mkdocs build --strict`

Expected: validação sem erros, testes aprovados e build estrito concluído.
