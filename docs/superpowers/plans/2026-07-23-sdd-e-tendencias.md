# SDD e tendências curriculares Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrar Spec-Driven Development ao Módulo 4 e tendências ao Módulo 6, preservando os seis módulos e a esteira de publicação.

**Architecture:** O Spec Kit conduz SDD no M4; Matt Pocock, Kiro, BMAD, Tessl e Model Spec são comparações e apêndice. Tendências fecha o M6 conectando mudanças a capacidades arquiteturais duráveis.

**Tech Stack:** Python/unittest, MkDocs Material, Markdown, Mermaid 11, YAML.

## Global Constraints

- Não alterar seis módulos, oito páginas por módulo, 24h ou títulos-âncora.
- Não criar PNG; diagramas novos são Mermaid e possuem equivalente textual.
- Toda URL externa nova deve constar em `fontes.yml` e na bibliografia.
- Contagens de palavras e imagens permanecem informativas, sem bloquear validação.

---

### Task 1: Relaxar travas editoriais

**Files:**
- Modify: `scripts/validate_content.py`
- Modify: `tests/test_validate_content.py`
- Modify: `tests/test_project.py`
- Modify: `tests/test_module_five.py`
- Modify: `tests/test_module_six.py`
- Modify: `tests/test_concept_infographics.py`

- [ ] **Step 1: Escrever testes de contrato relaxado**

Remover os três testes de orçamento. Substituir testes de PNG obrigatório/extra por casos que confirmem retorno zero. Trocar `Imagens: 20` por regex de contagem. Tornar a checagem de infográfico condicional, preservando alt-text quando houver imagem.

- [ ] **Step 2: Rodar para confirmar falha**

Run: `python -m unittest tests.test_validate_content tests.test_project tests.test_concept_infographics tests.test_module_five tests.test_module_six -v`

- [ ] **Step 3: Implementar**

Remover em `main()` os limites `6_000..10_000` e `40_000..60_000`; remover `validate_required_images` e sua chamada. Não modificar `validate_references` ou a impressão de contagens.

- [ ] **Step 4: Rodar para confirmar sucesso**

Run: `python -m unittest tests.test_validate_content tests.test_project tests.test_concept_infographics tests.test_module_five tests.test_module_six -v`

- [ ] **Step 5: Commit**

Run: `git add scripts/validate_content.py tests/test_validate_content.py tests/test_project.py tests/test_module_five.py tests/test_module_six.py tests/test_concept_infographics.py && git commit -m "test: relax content volume and image inventory gates"`

### Task 2: Registrar fontes e apêndice SDD

**Files:**
- Modify: `docs/referencia/fontes.yml`
- Modify: `docs/referencia/bibliografia.md`
- Modify: `docs/modulo-4-agentes/sintese-e-referencias.md`
- Modify: `tests/test_module_four.py`

- [ ] **Step 1: Escrever teste de fontes**

Exigir ids para Spec Kit, documentação e anúncio GitHub, Microsoft, Matt Pocock, Kiro, BMAD, Tessl, Model Spec e Sean Grove; cada entrada deve incluir o módulo 4.

- [ ] **Step 2: Rodar para confirmar falha**

Run: `python -m unittest tests.test_module_four -v`

- [ ] **Step 3: Implementar**

Registrar todas as URLs aprovadas com o schema existente; criar seção bibliográfica de SDD; incluir na síntese `Materiais adicionais sobre SDD`, com Spec Kit como primário e os demais como comparativos.

- [ ] **Step 4: Verificar e commit**

Run: `python -m unittest tests.test_module_four tests.test_project -v`

Run: `git add docs/referencia/fontes.yml docs/referencia/bibliografia.md docs/modulo-4-agentes/sintese-e-referencias.md tests/test_module_four.py && git commit -m "docs: register spec driven development sources"`

### Task 3: Fazer SDD central no Módulo 4

**Files:**
- Modify: `docs/modulo-4-agentes/conceitos.md`
- Modify: `docs/modulo-4-agentes/padroes-e-decisoes.md`
- Modify: `docs/modulo-4-agentes/exemplo-arquitetural.md`
- Modify: `tests/test_module_four.py`

- [ ] **Step 1: Escrever testes de integração**

Exigir `vibe coding`, `spec-driven`, `constitution`, `spec`, `plan`, `tasks`, `implement`, `verify` e `arquiteto`; padrão completo de Desenvolvimento guiado por especificação; quatro Mermaid, Gates 1–3, dois papéis humanos, cinco agentes e equivalentes textuais.

- [ ] **Step 2: Rodar para confirmar falha**

Run: `python -m unittest tests.test_module_four -v`

- [ ] **Step 3: Implementar**

Inserir a seção conceitual, padrão e decisão de gates. Adicionar dois Mermaid: `Constitution → Specification → Gate 1 → Plan → Tasks → Implement → Verify → Gate 2 → Gate 3` e squad híbrida; escrever legenda e equivalente textual para cada um.

- [ ] **Step 4: Verificar e commit**

Run: `python -m unittest tests.test_module_four -v && mkdocs build --strict`

Run: `git add docs/modulo-4-agentes/conceitos.md docs/modulo-4-agentes/padroes-e-decisoes.md docs/modulo-4-agentes/exemplo-arquitetural.md tests/test_module_four.py && git commit -m "docs: make spec driven development central to module four"`

### Task 4: Oficina e exercícios SDD

**Files:**
- Modify: `docs/modulo-4-agentes/oficina-de-ferramentas.md`
- Modify: `docs/modulo-4-agentes/exercicios.md`
- Modify: `tests/test_module_four.py`

- [ ] **Step 1: Escrever testes**

Exigir os quatro comandos `/speckit.*`, dados sintéticos, limpeza e alternativa demonstrativa. Exigir SDD e critérios de aceite nos exercícios e preservar as contagens e a política Bloom.

- [ ] **Step 2: Rodar para confirmar falha**

Run: `python -m unittest tests.test_module_four -v`

- [ ] **Step 3: Implementar e verificar**

Adicionar feature sintética, artefatos, teste, limpeza e caminho sem CLI; distribuir perguntas SDD nos seis níveis Bloom.

Run: `python -m unittest tests.test_module_four -v`

- [ ] **Step 4: Commit**

Run: `git add docs/modulo-4-agentes/oficina-de-ferramentas.md docs/modulo-4-agentes/exercicios.md tests/test_module_four.py && git commit -m "docs: add Spec Kit workshop and SDD exercises"`

### Task 5: Fechar Módulo 6 com tendências

**Files:**
- Modify: `docs/modulo-6-operacao/sintese-e-referencias.md`
- Modify: `tests/test_module_six.py`

- [ ] **Step 1: Escrever teste da seção**

Exigir `Tendências e futuro da arquitetura com GenAI`, contexto longo, multimodalidade, modelos abertos/hospedados, desenvolvimento agêntico, SDD, gateways, multimodelo, regulação, sinal, hype e arquiteto.

- [ ] **Step 2: Rodar para confirmar falha**

Run: `python -m unittest tests.test_module_six -v`

- [ ] **Step 3: Implementar e verificar**

Descrever consequência arquitetural e evidência para cada direção, ligando SDD ao M4 e distinguindo sinal de hype.

Run: `python -m unittest tests.test_module_six -v`

- [ ] **Step 4: Commit**

Run: `git add docs/modulo-6-operacao/sintese-e-referencias.md tests/test_module_six.py && git commit -m "docs: close module six with architecture trends"`

### Task 6: Atualizar espinha curricular compartilhada

**Files:**
- Modify: `docs/sobre/plano-da-disciplina.md`
- Modify: `docs/sobre/projeto-final.md`
- Modify: `docs/referencia/glossario.md`
- Modify: `docs/referencia/catalogo-de-padroes.md`
- Modify: `README.md`
- Modify: `tests/test_project.py`

- [ ] **Step 1: Escrever testes**

Exigir SDD no Encontro 4 e tendências no Encontro 6 e matriz, sem alterar títulos; entradas SDD, spec, constitution, EARS, vibe coding e agente de codificação com `#modulo-4`; padrão completo e método SDD no projeto final.

- [ ] **Step 2: Rodar para confirmar falha**

Run: `python -m unittest tests.test_project -v`

- [ ] **Step 3: Implementar e verificar**

Atualizar ementa, resultados, leituras e matriz; acrescentar método SDD ao projeto final, verbetes, padrão e a progressão no README.

Run: `python -m unittest tests.test_project -v`

- [ ] **Step 4: Commit**

Run: `git add docs/sobre/plano-da-disciplina.md docs/sobre/projeto-final.md docs/referencia/glossario.md docs/referencia/catalogo-de-padroes.md README.md tests/test_project.py && git commit -m "docs: connect SDD and trends across course backbone"`

### Task 7: Verificação final

- [ ] **Step 1: Executar validações integrais**

Run: `python -m unittest discover -s tests -v && python scripts/validate_content.py --all && mkdocs build --strict`

Expected: suíte verde, `Validação concluída sem erros.` e build estrito sem erro.

- [ ] **Step 2: Verificar ausência de PNG novo**

Run: `git diff --name-only HEAD~6..HEAD | rg 'docs/assets/images/.*\\.png'`

Expected: nenhuma saída.
