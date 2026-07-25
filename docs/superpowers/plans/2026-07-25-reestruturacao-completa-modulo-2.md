# Reestruturação completa do Módulo 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reestruturar o Módulo 2 como fundamento de decisão arquitetural para os módulos 3–6.

**Architecture:** O dossiê conceitual organiza o módulo inteiro como convenção didática. Conceitos separam entradas, vistas, análise, decisões e evidências; padrões ligam RAS a táticas, mecanismos e estruturas; exemplo e caso verificam correspondências entre vistas; oficina, exercícios e síntese exigem a mesma rastreabilidade.

**Tech Stack:** Markdown, MkDocs, pytest e validador de conteúdo.

## Global Constraints

- Usar Banco Lume como caso condutor e Aurora como caso de transferência identificado.
- Reter detalhes de implementação para os módulos 3–6.
- Preservar progressão de Bloom, fontes e independência de fornecedor.

---

### Task 1: Reestruturar abertura, conceitos e decisões

**Files:**
- Modify: `docs/modulo-2-desenho-conceitual/index.md`
- Modify: `docs/modulo-2-desenho-conceitual/conceitos.md`
- Modify: `docs/modulo-2-desenho-conceitual/padroes-e-decisoes.md`

- [ ] Explicitar a taxonomia de descrição arquitetural: preocupações, pontos de vista, vistas, modelos, cenários, ADRs e evidências.
- [ ] Acrescentar vistas de informação e implantação e regras de correspondência entre todas as vistas.
- [ ] Separar tática, mecanismo, padrão, estilo e ADR; incluir composição e conflitos entre táticas.
- [ ] Introduzir árvore de utilidade reduzida e registro de riscos, premissas e incertezas.

### Task 2: Reestruturar aplicação pedagógica

**Files:**
- Modify: `docs/modulo-2-desenho-conceitual/exemplo-arquitetural.md`
- Modify: `docs/modulo-2-desenho-conceitual/estudo-de-caso.md`
- Modify: `docs/modulo-2-desenho-conceitual/oficina-de-ferramentas.md`
- Modify: `docs/modulo-2-desenho-conceitual/exercicios.md`
- Modify: `docs/modulo-2-desenho-conceitual/sintese-e-referencias.md`

- [ ] Fazer o exemplo construir as cinco vistas, aplicar regras de correspondência e registrar sensibilidades, trade-offs e riscos.
- [ ] Fazer caso, oficina e exercícios construir, testar ou revisar os mesmos elementos.
- [ ] Atualizar síntese, autoavaliação e referências para refletir a taxonomia.

### Task 3: Validar

- [ ] Ampliar `tests/test_module_two.py` com regressões para taxonomia, cinco vistas, correspondências, análise de trade-offs e distinção entre táticas e ADRs.
- [ ] Run: `python scripts/validate_content.py --all`
- [ ] Run: `python -m pytest -q`
- [ ] Run: `mkdocs build --strict`
