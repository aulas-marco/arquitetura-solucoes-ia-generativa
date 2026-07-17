# Exercícios guiados e critérios de avaliação Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reescrever as atividades avançadas dos seis módulos para conduzir o arquiteto iniciante em IA por contexto, evidências, procedimento, entrega e critérios percentuais, eliminando pontos e o termo “rubrica” do conteúdo publicado.

**Architecture:** A alteração será editorial e estruturada por página. Cada exercício de Aplicar, Analisar, Avaliar e Criar receberá seis blocos padronizados — Situação, Seu papel, Insumos disponíveis, Como conduzir, Entrega esperada e Critérios de avaliação — sem criar um gabarito. Um teste de contrato verificará os blocos, os pesos percentuais e a ausência de pontuação e “rubrica” no conteúdo publicado; o projeto final e as páginas de orientação usarão o mesmo vocabulário.

**Tech Stack:** Markdown, MkDocs Material, Python `unittest`, `scripts/validate_content.py`.

## Global Constraints

- Preservar a quantidade, a ordem e os temas dos exercícios existentes.
- Manter respostas públicas somente em Recordar e Compreender.
- Nas atividades avançadas, conduzir o raciocínio sem publicar solução-modelo.
- Cada tabela de critérios deve totalizar 100% e usar critérios observáveis.
- Remover “rubrica”, “pontos”, “pontuação” e faixas de pontos do conteúdo publicado; não alterar documentos internos em `docs/superpowers/`.
- Usar somente cenários sintéticos e referências às páginas, oficinas e artefatos já existentes.
- Executar `python -m unittest discover -s tests -v`, `python scripts/validate_content.py --all` e `mkdocs build --strict --clean` antes da integração.

## Arquivos e responsabilidades

- Modificar `docs/modulo-1-fundamentos/exercicios.md`: guiar decisões sobre modelo, contexto, qualidade e sistema sociotécnico.
- Modificar `docs/modulo-2-desenho-conceitual/exercicios.md`: guiar oportunidade, aceitação, alternativas e ADR.
- Modificar `docs/modulo-3-rag/exercicios.md`: guiar recuperação, proveniência, autorização e escolha de padrão.
- Modificar `docs/modulo-4-agentes/exercicios.md`: guiar ferramentas, autonomia, trace, aprovação e efeitos.
- Modificar `docs/modulo-5-confianca/exercicios.md`: guiar ameaças, controles, regressão e risco residual.
- Modificar `docs/modulo-6-operacao/exercicios.md`: guiar manifesto, telemetria, rollout, plataforma e operação.
- Modificar `docs/sobre/projeto-final.md`: substituir a matriz de pontos por critérios percentuais explicados.
- Modificar `docs/comecar/como-usar.md`: explicar ao aluno como ler e usar os critérios.
- Modificar `docs/comecar/taxonomia-de-bloom.md`: explicar a progressão e o apoio esperado em cada nível.
- Modificar `docs/modulo-2-desenho-conceitual/estudo-de-caso.md`, `docs/modulo-5-confianca/estudo-de-caso.md`, `docs/modulo-5-confianca/exemplo-arquitetural.md`, `docs/modulo-5-confianca/index.md`, `docs/modulo-5-confianca/padroes-e-decisoes.md`, `docs/modulo-6-operacao/estudo-de-caso.md`, `docs/modulo-6-operacao/conceitos.md`, `docs/modulo-2-desenho-conceitual/padroes-e-decisoes.md`, `docs/modulo-2-desenho-conceitual/sintese-e-referencias.md` e `docs/referencia/atributos-de-qualidade.md`: trocar o termo técnico por vocabulário contextual equivalente, sem remover o conceito.
- Modificar `tests/test_pedagogical_shell.py` ou `tests/test_applied_literacy.py`: verificar o contrato editorial de blocos, percentuais e vocabulário.

### Task 1: Criar os testes de contrato editorial

**Files:**
- Modify: `tests/test_applied_literacy.py`

**Interfaces:**
- Consumes: `MODULES`, `DOCS` e os seis arquivos de exercícios já usados pelos testes existentes.
- Produces: testes que falham antes da reescrita e passam quando cada atividade avançada estiver orientada.

- [ ] **Step 1: Write the failing tests**

Adicionar testes que, para cada página de exercícios, verifiquem:

```python
for level in ("Aplicar", "Analisar", "Avaliar", "Criar"):
    assert f"## {level}" in text
advanced = text.split("## Aplicar", 1)[1]
for label in ("Situação", "Seu papel", "Insumos disponíveis", "Como conduzir", "Entrega esperada", "Critérios de avaliação"):
    assert f"**{label}**" in advanced
assert "Rubrica" not in text
assert "pontos" not in advanced.lower()
assert re.search(r"\|[^\n]*\|\s*\d+%\s*\|", advanced)
```

Adicionar um teste para `docs/sobre/projeto-final.md` que exija o título `## Critérios de avaliação`, percentuais em seis linhas e ausência de `pontos` e `Rubrica`.

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m unittest tests.test_applied_literacy tests.test_pedagogical_shell -v`

Expected: FAIL, porque os exercícios ainda usam `Rubrica (N pontos)` e não possuem os seis blocos de condução.

- [ ] **Step 3: Commit the test contract**

```bash
git add tests/test_applied_literacy.py
git commit -m "test: define guided exercise assessment contract"
```

### Task 2: Reescrever os exercícios dos módulos 1 e 2

**Files:**
- Modify: `docs/modulo-1-fundamentos/exercicios.md`
- Modify: `docs/modulo-2-desenho-conceitual/exercicios.md`

**Interfaces:**
- Consumes: conceitos, exemplos, oficinas e padrões dos módulos 1 e 2.
- Produces: dez atividades avançadas guiadas, sem solução pública, com tabelas percentuais.

- [ ] **Step 1: Reescrever a abertura de cada página**

Trocar a instrução que manda usar “rubricas” por uma explicação: Recordar e Compreender servem para autocorreção; nos níveis avançados, o aluno deve seguir o roteiro, declarar pressupostos e usar os critérios como guia de qualidade.

- [ ] **Step 2: Reestruturar Aplicar**

Para cada questão, explicar o caso sintético, nomear o papel do arquiteto, apontar exatamente a página ou artefato de entrada, numerar três passos de análise e definir uma entrega curta. Usar quatro critérios percentuais, por exemplo evidência 25%, decisão 30%, verificação 25% e clareza 20%, ajustando os pesos ao objetivo da questão.

- [ ] **Step 3: Reestruturar Analisar e Avaliar**

Para Analisar, conduzir a separação de fatos, hipóteses, causas e consequências antes da recomendação. Para Avaliar, exigir comparação de alternativas, critérios explícitos, condição de reversão e limites da evidência. Usar no máximo cinco critérios percentuais por questão, com frases observáveis.

- [ ] **Step 4: Reestruturar Criar**

Dividir o artefato em partes mínimas — escopo, componentes, responsabilidades, riscos, experimento e evolução — e referenciar o template de ADR ou diagrama existente. Usar no máximo seis critérios percentuais, sem revelar a arquitetura que o aluno deve escolher.

- [ ] **Step 5: Verificar conteúdo dos módulos 1 e 2**

Run: `python -m unittest tests.test_applied_literacy -v`

Expected: os testes de contrato dos módulos 1 e 2 passam; os módulos restantes continuam falhando até as tarefas seguintes.

- [ ] **Step 6: Commit**

```bash
git add docs/modulo-1-fundamentos/exercicios.md docs/modulo-2-desenho-conceitual/exercicios.md
git commit -m "docs: guide foundational and conceptual exercises"
```

### Task 3: Reescrever os exercícios dos módulos 3 e 4

**Files:**
- Modify: `docs/modulo-3-rag/exercicios.md`
- Modify: `docs/modulo-4-agentes/exercicios.md`

**Interfaces:**
- Consumes: corpus, scripts locais, traces, diagramas, padrões e templates dos módulos 3 e 4.
- Produces: oito atividades avançadas guiadas com evidência de recuperação, autorização, estado e efeito.

- [ ] **Step 1: Reescrever Aplicar**

No módulo 3, começar pelo corpus e pela tabela de referência antes de pedir métricas, chunking ou evidência. No módulo 4, começar pelo trace e pelo contrato de ferramenta antes de pedir autonomia. Indicar comandos ou arquivos quando a oficina já fornecer a evidência.

- [ ] **Step 2: Reescrever Analisar**

Explicar como reconstruir a sequência causal: entrada, decisão, acesso, efeito e resultado. Pedir que o aluno marque o que o trace prova, o que apenas sugere e qual dado falta.

- [ ] **Step 3: Reescrever Avaliar e Criar**

Para Avaliar, exigir recomendação condicionada e gatilho de revisão. Para Criar, exigir diagrama, fluxo textual, ADR, autorização, abstenção ou aprovação e experimento mínimo. Referenciar os artefatos existentes sem criar resposta-modelo.

- [ ] **Step 4: Verificar e commit**

Run: `python -m unittest tests.test_applied_literacy -v`

Expected: contratos dos módulos 1 a 4 passam.

```bash
git add docs/modulo-3-rag/exercicios.md docs/modulo-4-agentes/exercicios.md
git commit -m "docs: guide retrieval and agent exercises"
```

### Task 4: Reescrever os exercícios dos módulos 5 e 6

**Files:**
- Modify: `docs/modulo-5-confianca/exercicios.md`
- Modify: `docs/modulo-6-operacao/exercicios.md`

**Interfaces:**
- Consumes: casos sintéticos, relatórios locais, traces, métricas, SLOs e padrões dos módulos 5 e 6.
- Produces: oito atividades avançadas guiadas sobre risco, controles, regressão, operação e plataforma.

- [ ] **Step 1: Reescrever Aplicar**

Apresentar o cenário, o conjunto de casos e a tabela ou relatório que o aluno deve inspecionar. Explicar como registrar ativo, ator, ameaça, sinal, controle ou manifesto antes de pedir julgamento.

- [ ] **Step 2: Reescrever Analisar**

Conduzir a decomposição causal de regressão e rollout: separar métrica de qualidade, latência, custo, falha de segurança e efeito por fatia. Pedir hipótese, teste que pode refutá-la, decisão provisória e ação de contenção.

- [ ] **Step 3: Reescrever Avaliar e Criar**

Explicar como comparar plataforma comum e autonomia local, e como montar o capstone em partes. Exigir responsabilidade, privacidade, recuperação e critérios de liberação, sem induzir uma solução única.

- [ ] **Step 4: Verificar e commit**

Run: `python -m unittest tests.test_applied_literacy -v`

Expected: todos os contratos dos seis módulos passam.

```bash
git add docs/modulo-5-confianca/exercicios.md docs/modulo-6-operacao/exercicios.md
git commit -m "docs: guide trust and operations exercises"
```

### Task 5: Converter projeto final e orientações de avaliação

**Files:**
- Modify: `docs/sobre/projeto-final.md`
- Modify: `docs/comecar/como-usar.md`
- Modify: `docs/comecar/taxonomia-de-bloom.md`

**Interfaces:**
- Consumes: os seis módulos e o desenho pedagógico aprovado.
- Produces: vocabulário uniforme e critérios percentuais compreensíveis antes do aluno iniciar os exercícios.

- [ ] **Step 1: Reescrever a matriz do projeto**

Trocar a coluna “pontos” por “peso” e usar `15%`, `20%`, `15%`, `20%`, `15%` e `15%`. Para cada critério, explicar evidência mínima, qualidade esperada e falha frequente.

- [ ] **Step 2: Explicar como usar critérios**

Em `como-usar.md`, explicar que o percentual é peso relativo, não pontuação automática; o aluno deve usar a coluna de evidência para revisar a entrega antes de enviar.

- [ ] **Step 3: Atualizar Bloom**

Explicar em linguagem direta o que o aluno faz em Aplicar, Analisar, Avaliar e Criar, incluindo o apoio fornecido pelo enunciado e o tipo de artefato esperado.

- [ ] **Step 4: Verificar e commit**

Run: `rg -n -i "rubrica|pontos|pontuação" docs/sobre/projeto-final.md docs/comecar/como-usar.md docs/comecar/taxonomia-de-bloom.md`

Expected: nenhum resultado de avaliação estudantil.

```bash
git add docs/sobre/projeto-final.md docs/comecar/como-usar.md docs/comecar/taxonomia-de-bloom.md
git commit -m "docs: explain percentage assessment criteria"
```

### Task 6: Ajustar vocabulário técnico publicado

**Files:**
- Modify: `docs/modulo-2-desenho-conceitual/estudo-de-caso.md`
- Modify: `docs/modulo-2-desenho-conceitual/padroes-e-decisoes.md`
- Modify: `docs/modulo-2-desenho-conceitual/sintese-e-referencias.md`
- Modify: `docs/modulo-5-confianca/estudo-de-caso.md`
- Modify: `docs/modulo-5-confianca/exemplo-arquitetural.md`
- Modify: `docs/modulo-5-confianca/index.md`
- Modify: `docs/modulo-5-confianca/padroes-e-decisoes.md`
- Modify: `docs/modulo-6-operacao/estudo-de-caso.md`
- Modify: `docs/modulo-6-operacao/conceitos.md`
- Modify: `docs/referencia/atributos-de-qualidade.md`

**Interfaces:**
- Consumes: conceitos de avaliação humana, avaliação assistida e aceitação comportamental.
- Produces: explicações tecnicamente equivalentes sem depender do termo “rubrica”.

- [ ] **Step 1: Substituir o termo conforme o contexto**

Usar “critérios qualitativos de avaliação humana” para julgamento humano, “critérios de avaliação aplicados por modelo” para avaliação assistida e “critério qualitativo” quando a alternativa atual disser “métrica ou rubrica”. Em diagramas, substituir o rótulo do nó por `Critérios humanos versionados`.

- [ ] **Step 2: Preservar a precisão conceitual**

Manter a explicação de níveis observáveis, calibração, divergência, viés, proveniência, avaliação por fatia e portões. Somente a terminologia muda; o mecanismo não pode ser simplificado para uma nota única.

- [ ] **Step 3: Verificar e commit**

Run: `rg -n -i "rubrica" docs --glob '*.md' -g '!superpowers/**'`

Expected: nenhum resultado em conteúdo publicado.

```bash
git add docs/modulo-2-desenho-conceitual docs/modulo-5-confianca docs/modulo-6-operacao docs/referencia/atributos-de-qualidade.md
git commit -m "docs: use architecture assessment vocabulary"
```

### Task 7: Rodar gates de conteúdo e revisar a publicação

**Files:**
- Modify: `tests/test_applied_literacy.py` only if a contract assertion needs correction.

- [ ] **Step 1: Run the complete test suite**

Run: `python -m unittest discover -s tests -v`

Expected: todos os testes passam.

- [ ] **Step 2: Run content validation**

Run: `python scripts/validate_content.py --all`

Expected: `Validação concluída sem erros.`

- [ ] **Step 3: Build the site strictly**

Run: `mkdocs build --strict --clean`

Expected: build concluído sem erro.

- [ ] **Step 4: Inspect representative rendered pages**

Open the locally built pages for Módulos 1, 3, 5 and the project final. Confirm that each advanced question shows visual separation between the six blocks, that percentage tables render correctly and that no points language remains.

- [ ] **Step 5: Commit test adjustments if needed**

```bash
git add tests/test_applied_literacy.py
git commit -m "test: enforce assessment terminology and guidance"
```

- [ ] **Step 6: Re-run all three gates after the final commit**

Run: `python -m unittest discover -s tests -v && python scripts/validate_content.py --all && mkdocs build --strict --clean`

Expected: exit code 0 for the complete chain.
