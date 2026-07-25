# Coesão arquitetural do Módulo 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tornar o Módulo 2 coerente com a prática de decisões arquiteturais contextuais, orientadas por características e trade-offs.

**Architecture:** A abertura promete o mesmo conjunto de decisões que a página de padrões ensina. Conceitos definem proveniência e modularidade; padrões apresentam uma sequência de perguntas, tensões e consequências; o exemplo, o caso e os exercícios exigem essas evidências.

**Tech Stack:** Markdown, MkDocs, validador de conteúdo e pytest.

## Global Constraints

- Preservar cenários, exemplo Banco Lume e estrutura de exercícios.
- Não apresentar estilo, padrão ou produto como solução universal.
- Modificar somente conteúdo necessário em `docs/modulo-2-desenho-conceitual/`.
- Definir proveniência como cadeia verificável de origem, transformação, versão, autorização e uso da evidência.

---

### Task 1: Alinhar conceitos e decisões

**Files:**
- Modify: `docs/modulo-2-desenho-conceitual/conceitos.md`
- Modify: `docs/modulo-2-desenho-conceitual/padroes-e-decisoes.md`

**Interfaces:**
- Consumes: RAS, atributos de qualidade, CONOPS, ADR e decisões atuais do módulo.
- Produces: vocabulário de proveniência e um processo de decisão que explicita alternativas, trade-offs, consequências e evidências.

- [ ] **Step 1: Atualizar as definições arquiteturais**

Definir proveniência com os cinco elementos exigidos e associá-la a fronteira de dados, auditoria e evidência. Substituir a comparação imprecisa entre monólito, distribuído e infraestrutura por distinção entre estilo, granularidade e capacidade compartilhada.

- [ ] **Step 2: Reestruturar os padrões como decisões contextuais**

Apresentar perguntas sobre geração, conhecimento, ação, autonomia, hospedagem e obtenção de capacidade; em cada uma, declarar direcionadores, alternativas e consequências. Restaurar hospedado versus autogerido e construir, comprar ou compor.

- [ ] **Step 3: Tornar trade-offs e modularidade explícitos**

Adicionar matriz de características com prioridade, tensão, medida e dono. Explicar coesão e acoplamento entre orquestrador, adaptador, gateway, contexto e validação; incluir custos de gateway e chassi.

### Task 2: Propagar a lente aos artefatos didáticos

**Files:**
- Modify: `docs/modulo-2-desenho-conceitual/index.md`
- Modify: `docs/modulo-2-desenho-conceitual/exemplo-arquitetural.md`
- Modify: `docs/modulo-2-desenho-conceitual/estudo-de-caso.md`
- Modify: `docs/modulo-2-desenho-conceitual/exercicios.md`
- Modify: `docs/modulo-2-desenho-conceitual/sintese-e-referencias.md`

**Interfaces:**
- Consumes: definições e decisões da Task 1.
- Produces: objetivos, exemplo, caso, exercícios e checklist consistentes com o processo revisto.

- [ ] **Step 1: Revisar promessa e exemplo**

Alinhar objetivo e roteiro da abertura às decisões ensinadas. Adicionar ao Banco Lume a tensão priorizada e a proveniência de evidências sem ampliar o escopo da arquitetura.

- [ ] **Step 2: Revisar caso, exercícios e síntese**

Exigir proveniência e trade-offs explícitos nas entregas. Ajustar exercícios e checklist para tratar prioridade de características, consequências e fronteiras de componente.

- [ ] **Step 3: Validar conteúdo e publicação**

Run: `python scripts/validate_content.py --all && python -m pytest -q && mkdocs build --strict`

Expected: validação sem erros, todos os testes aprovados e build estrito concluído.
