# Coesão arquitetural do Módulo 3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tornar RAG explicitamente governado por características arquiteturais, trade-offs e evidências contínuas.

**Architecture:** Conceitos delimita proveniência e fronteiras de componentes. Padrões apresenta estratégias de recuperação como decisões de composição, prioriza características e define opções de plataforma e fitness functions.

**Tech Stack:** Markdown, MkDocs, pytest e validador de conteúdo.

## Global Constraints

- Modificar apenas `docs/modulo-3-rag/conceitos.md` e `docs/modulo-3-rag/padroes-e-decisoes.md`.
- Preservar os dois pipelines, padrões existentes e independência de fornecedor.
- Não apresentar estratégia de RAG como solução universal.

---

### Task 1: Reforçar decisões arquiteturais de RAG

**Files:**
- Modify: `docs/modulo-3-rag/conceitos.md`
- Modify: `docs/modulo-3-rag/padroes-e-decisoes.md`

**Interfaces:**
- Consumes: fluxos offline/online, proveniência e padrões de recuperação existentes.
- Produces: decisões priorizadas com responsabilidades, consequências e verificações contínuas.

- [ ] **Step 1: Ajustar conceitos de proveniência e componentes**

Corrigir a promessa de proveniência e inserir responsabilidades coesas para política, recuperador, ranking, contexto, validação e adaptadores.

- [ ] **Step 2: Ajustar padrões e trade-offs**

Inserir matriz de prioridade, hospedado/autogerido, construir/comprar/compor e distinção entre estratégia de recuperação e estilo arquitetural.

- [ ] **Step 3: Adicionar governança contínua**

Definir fitness functions para autorização, atualidade, recuperação e promoção de versões.

- [ ] **Step 4: Validar publicação**

Run: `python scripts/validate_content.py --all && python -m pytest -q && mkdocs build --strict`

Expected: validação sem erros, testes aprovados e build estrito concluído.
