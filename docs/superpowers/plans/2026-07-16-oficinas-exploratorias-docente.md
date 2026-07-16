# Oficinas Exploratórias e Roteiro Docente Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Criar laboratórios GenAI selecionáveis pelo professor, com exploração guiada e material docente privado.

**Architecture:** As oficinas públicas adotam blocos de experimento independentes; `material-professor/` contém a condução por encontro e permanece ignorado pelo Git. O M1 acrescenta comparações reais de temperatura por API local do Ollama.

**Tech Stack:** Markdown, Ollama API local, `curl`, MkDocs e Python `unittest`.

## Global Constraints

- Cada experimento informa objetivo, pré-requisito, execute, observe, compare e questões exploratórias.
- Experimentos são rotulados essencial em aula, exploração em dupla ou extensão.
- O material docente não entra no Git nem no site.
- Ferramentas obrigatórias usam dados sintéticos, execução local e nenhuma credencial.

### Task 1: Contrato e laboratório de temperatura do Módulo 1

**Files:** `tests/test_applied_literacy.py`, `docs/modulo-1-fundamentos/oficina-de-ferramentas.md`

1. Testar a presença de Experimento D, `http://localhost:11434/api/generate`, temperaturas `0.1` e `0.9`, e questões exploratórias.
2. Inserir dois comandos `curl` com o mesmo modelo, prompt e corpus; mudar somente `options.temperature`.
3. Pedir comparação entre diversidade, fundamentação e correção; declarar que temperatura não prova factualidade.
4. Rodar testes, validador e build; commitar.

### Task 2: Padronizar oficinas 2–6

**Files:** `docs/modulo-{2..6}-*/oficina-de-ferramentas.md`, `tests/test_applied_literacy.py`

1. Inserir roteiro sugerido para aula e rótulos Essencial, Exploração e Extensão.
2. Separar as receitas atuais em experimentos independentes.
3. Adicionar ao menos três questões exploratórias por módulo, ligadas a decisão arquitetural, atributo de qualidade e risco.
4. Executar testes e build; commitar.

### Task 3: Criar roteiro privado do professor

**Files:** `material-professor/oficinas-exploratorias.md`

1. Criar roteiro por encontro: duração, experimento essencial, alternativas, perguntas, resposta esperada e contingência.
2. Confirmar que `material-professor/` continua ignorado e não aparece no site.
3. Executar suíte completa, validador e build; commitar somente arquivos públicos.
