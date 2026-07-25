# Exercícios do desenho conceitual Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reescrever os exercícios do Módulo 2 para aplicar os novos conceitos e padrões de decisão sem alterar sua estrutura ou extensão aproximada.

**Architecture:** Uma única página de exercícios preservará os seis níveis de Bloom e os doze itens. Questões iniciais atualizarão o vocabulário de recuperação; atividades avançadas conservarão os blocos instrucionais e transformarão os novos padrões em decisões arquiteturais justificadas.

**Tech Stack:** Markdown, MkDocs e verificações de links locais.

## Global Constraints

- Modificar apenas `docs/modulo-2-desenho-conceitual/exercicios.md`.
- Preservar 12 exercícios, classificação de Bloom, respostas públicas nos níveis iniciais e tabelas de critérios.
- Usar somente âncoras presentes em `conceitos.md` e `padroes-e-decisoes.md`.
- Não incluir respostas-modelo para atividades avançadas.

---

### Task 1: Reescrever os exercícios

**Files:**
- Modify: `docs/modulo-2-desenho-conceitual/exercicios.md`
- Reference: `docs/modulo-2-desenho-conceitual/conceitos.md`
- Reference: `docs/modulo-2-desenho-conceitual/padroes-e-decisoes.md`

**Interfaces:**
- Consumes: títulos e conceitos das duas páginas atualizadas.
- Produces: doze enunciados alinhados ao conteúdo, prontos para renderização no MkDocs.

- [ ] **Step 1: Inventariar os títulos de destino e a estrutura atual**

Run: `rg '^#{1,3} ' docs/modulo-2-desenho-conceitual/{conceitos,padroes-e-decisoes,exercicios}.md`

Expected: títulos que permitam substituir todas as referências obsoletas e confirmar os doze exercícios.

- [ ] **Step 2: Reescrever Recordar e Compreender**

Atualizar as sete questões e respostas para cobrir oportunidade versus requisito, IA como componente, atributos de qualidade, ADRs e critérios probabilísticos, sem alterar os blocos `details`.

- [ ] **Step 3: Reescrever Aplicar a Criar**

Atualizar os cinco cenários para exercitar escolha entre contexto, RAG e fine-tuning; workflow, agente e mediador; filters de validação; gateway/chassi; modelos; e ADRs, preservando blocos, rubricas percentuais e escopo das entregas.

- [ ] **Step 4: Verificar a página**

Run: `rg '^### [0-9]+' docs/modulo-2-desenho-conceitual/exercicios.md | wc -l && wc -w docs/modulo-2-desenho-conceitual/exercicios.md && git diff --check -- docs/modulo-2-desenho-conceitual/exercicios.md`

Expected: 12 exercícios, extensão próxima de 1.988 palavras e nenhuma falha de whitespace no arquivo alterado.

- [ ] **Step 5: Verificar destinos de links locais**

Run: `rg -o '\]\(([^)#]+)(#[^)]+)?\)' docs/modulo-2-desenho-conceitual/exercicios.md`

Expected: referências para páginas existentes e âncoras legíveis que correspondem aos títulos atualizados.
