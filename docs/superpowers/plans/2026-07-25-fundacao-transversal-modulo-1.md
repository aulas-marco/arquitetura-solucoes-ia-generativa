# Fundação transversal do Módulo 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorientar o Módulo 1 como fundação conceitual equilibrada dos módulos 2–6.

**Architecture:** A abertura apresenta o mapa do curso; conceitos definem a superfície comportamental e tipos de verificação; padrões comparam composições; exemplo, caso, oficina e exercícios aplicam o mesmo vocabulário. O detalhamento de descrição arquitetural, RAG, agentes, confiança e operação permanece nos módulos próprios.

**Tech Stack:** Markdown, MkDocs, unittest/pytest e validador editorial.

## Global Constraints

- Preservar oito páginas e os seis níveis da Taxonomia de Bloom.
- Manter o laboratório local com dados sintéticos e alternativa sem instalação.
- Não transformar o Módulo 1 em implementação antecipada dos módulos 2–6.
- Evitar afirmações absolutas e cacoetes de contraste sem função conceitual.

---

### Task 1: Fixar regressões conceituais

**Files:**
- Modify: `tests/test_module_one.py`

- [ ] Adicionar testes para superfície comportamental, geração–decisão–autorização–efeito, três tipos de verificação, fitness function, mapa de responsabilidades e pontes aos módulos 2–6.
- [ ] Remover a regressão que exige detalhes históricos de Transformer.
- [ ] Executar `python -m pytest tests/test_module_one.py -q` e confirmar que as novas expectativas falham antes da reescrita.

### Task 2: Reescrever abertura, conceitos e decisões

**Files:**
- Modify: `docs/modulo-1-fundamentos/index.md`
- Modify: `docs/modulo-1-fundamentos/conceitos.md`
- Modify: `docs/modulo-1-fundamentos/padroes-e-decisoes.md`

- [ ] Corrigir definições de decisão arquitetural, prompt, contexto, embedding e conhecimento paramétrico.
- [ ] Introduzir superfície comportamental, ciclos de vida, tipos de verificação e fitness functions.
- [ ] Substituir a ADR completa por ficha de decisão inicial, incorporar o mapa de responsabilidades na página e distribuir igualmente as pontes para os módulos 2–6.

### Task 3: Remodelar aplicação pedagógica

**Files:**
- Modify: `docs/modulo-1-fundamentos/exemplo-arquitetural.md`
- Modify: `docs/modulo-1-fundamentos/estudo-de-caso.md`
- Modify: `docs/modulo-1-fundamentos/oficina-de-ferramentas.md`
- Modify: `docs/modulo-1-fundamentos/exercicios.md`
- Modify: `docs/modulo-1-fundamentos/sintese-e-referencias.md`

- [ ] Aplicar o mapa de responsabilidades ao exemplo Horizonte sem criar nova categoria de página.
- [ ] Cobrir no exemplo concreto o fluxo de evidência, falhas, superfície comportamental e verificações.
- [ ] Fazer caso e exercícios avaliar conhecimento, efeito, confiança e mudança.
- [ ] Relacionar a oficina ao pacote comportamental e aos limites da evidência produzida.

### Task 4: Verificar

- [ ] Executar `python -m pytest tests/test_module_one.py -q`.
- [ ] Executar `python scripts/validate_content.py --all`.
- [ ] Executar `python -m pytest -q`.
- [ ] Executar `mkdocs build --strict`.
- [ ] Executar `git diff --check` e revisar o diff do Módulo 1.
