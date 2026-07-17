# Exercícios guiados e critérios de avaliação — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Conduzir arquitetos iniciantes em IA nas atividades avançadas de Bloom e substituir linguagem de rubrica/pontuação por critérios de avaliação percentuais e explicados.

**Architecture:** As seis páginas de exercícios usarão uma estrutura textual uniforme para reduzir a ambiguidade inicial sem expor respostas canônicas. Um teste de política pedagógica exigirá condução, critérios percentuais e ausência de rubricas ou pontos; uma passagem editorial normalizará a terminologia em todo o conteúdo publicado.

**Tech Stack:** Markdown, MkDocs Material, Python `unittest`, `scripts/validate_content.py`.

## Global Constraints

- Altere apenas conteúdo publicado em `docs/`; não modifique `docs/superpowers/` além deste plano e da especificação aprovada.
- Preserve seis módulos, doze exercícios por módulo e respostas públicas apenas para Recordar e Compreender.
- Aplicar, Analisar, Avaliar e Criar não podem receber resposta-modelo, cálculo resolvido ou solução canônica.
- Cada atividade avançada terá: **Situação**, **Seu papel**, **Insumos disponíveis**, **Como conduzir**, **Entrega esperada** e **Critérios de avaliação**.
- Cada tabela de critérios totaliza 100%, explica resultados observáveis e não usa “ponto”, “pontuação”, “nota” ou “rubrica”.
- Use “critérios qualitativos de avaliação humana” para julgamento humano e “critérios de avaliação aplicados por modelo” para avaliação assistida.
- Antes de concluir, execute `python -m unittest discover -s tests -v`, `python scripts/validate_content.py --all` e `mkdocs build --strict --clean`.

---

## Estrutura de arquivos

| Arquivo | Responsabilidade após a mudança |
|---|---|
| `tests/test_pedagogical_shell.py` | Impede retorno de rubricas/pontos e exige condução e critérios percentuais. |
| `docs/modulo-*/exercicios.md` | Conduz as 30 atividades avançadas, preservando temas e níveis de Bloom. |
| `docs/sobre/projeto-final.md` | Expõe critérios percentuais detalhados para a entrega integradora. |
| Orientações, casos, conceitos, exemplos e referências da Tarefa 5 | Removem “rubrica” do conteúdo publicado sem alterar o significado técnico. |

## Convenção editorial

Use esta estrutura em cada questão avançada:

```markdown
**Situação**

Descreva um cenário sintético delimitado, sem fatos fora do alcance da atividade.

**Seu papel**

Declare a decisão que o aluno assume como arquiteto.

**Insumos disponíveis**

- Nomeie uma página, um artefato ou um resultado de oficina que o aluno pode consultar.
- Indique a evidência contida no enunciado que também pode ser usada.

**Como conduzir**

1. Comece por uma observação que possa ser registrada.
2. Separe fatos fornecidos, hipóteses e lacunas.
3. Compare alternativas ou tome a decisão solicitada.
4. Defina como verificar a decisão ou quando ela deve ser revista.

**Entrega esperada**

Informe o artefato, formato e limite proporcional de extensão.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Nome de um resultado observável | Percentual escolhido | Descreva a evidência que demonstra atendimento adequado. |
```

### Task 1: Criar a proteção automatizada da estrutura pedagógica

**Files:**
- Modify: `tests/test_pedagogical_shell.py:34-59`
- Test: `tests/test_pedagogical_shell.py`

**Interfaces:**
- Consumes: `MODULES` e `bloom_sections()` de `scripts.validate_content`.
- Produces: `PublicExerciseAnswerPolicyTest.test_advanced_sections_are_guided_and_use_percentual_criteria`.

- [ ] **Step 1: Escrever o teste inicialmente falho**

Substitua `test_advanced_sections_have_rubrics_but_no_public_answer_blocks` por:

```python
def test_advanced_sections_are_guided_and_use_percentual_criteria(self):
    required_blocks = (
        "**Situação**", "**Seu papel**", "**Insumos disponíveis**",
        "**Como conduzir**", "**Entrega esperada**",
        "**Critérios de avaliação**",
    )
    for slug in MODULES:
        text = (DOCS / slug / "exercicios.md").read_text(encoding="utf-8")
        sections = bloom_sections(text)
        for level in ("Aplicar", "Analisar", "Avaliar", "Criar"):
            body = sections[level]
            with self.subTest(module=slug, level=level):
                for block in required_blocks:
                    self.assertIn(block, body)
                self.assertRegex(body, r"\|[^\n]+\|\s*\d{1,3}%\s*\|")
                self.assertNotRegex(
                    body.casefold(), r"rubrica|\bpontos?\b|pontuação|\bnota\b"
                )
                self.assertNotIn("<details", body.casefold())
                self.assertNotRegex(
                    body.casefold(), r"resposta\s+(comentada|esperada|correta)"
                )
```

Renomeie o segundo teste para `test_advanced_criteria_do_not_reveal_computed_or_canonical_answers` e faça-o inspecionar linhas de tabela (`line.startswith("|")`) em vez de linhas `**Rubrica`.

- [ ] **Step 2: Confirmar a falha**

Run: `python -m unittest tests.test_pedagogical_shell.PublicExerciseAnswerPolicyTest -v`  
Expected: FAIL porque ainda não existem os seis blocos e há rubricas.

- [ ] **Step 3: Commit do teste**

```bash
git add tests/test_pedagogical_shell.py
git commit -m "test: require guided advanced activities"
```

### Task 2: Guiar Aplicar, Analisar, Avaliar e Criar nos módulos 1 e 2

**Files:**
- Modify: `docs/modulo-1-fundamentos/exercicios.md:81-131`
- Modify: `docs/modulo-2-desenho-conceitual/exercicios.md:81-135`
- Test: `tests/test_pedagogical_shell.py`

**Interfaces:**
- Consumes: catálogo de atributos, exemplo arquitetural, padrões e oficina dos módulos 1 e 2.
- Produces: dez questões com o esqueleto editorial completo e critérios percentuais.

- [ ] **Step 1: Reescrever o Módulo 1**

Preserve as questões 8 a 12. Na questão 8, peça primeiro uma tabela das cinco ações antes de justificar fronteiras. Na 9, ofereça as seis partes do cenário de qualidade como lista de verificação. Na 10, peça matriz de atualização, proveniência, autorização, latência, custo e operação antes da escolha. Na 11, peça uma decisão provisória e só então as condições de revisão. Na 12, mantenha o template, limite a entrega a uma página, diagrama e uma hipótese verificável.

Use pesos como:

```markdown
| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Uso correto dos conceitos | 30% | Distingue responsabilidade probabilística de controle determinístico no caso. |
| Decisão e consequências | 35% | Relaciona fronteira, risco e consequência arquitetural. |
| Verificação | 35% | Define evidência, limite e condição de revisão proporcionais ao risco. |
```

- [ ] **Step 2: Reescrever o Módulo 2**

Preserve questões 8 a 12 e indique como insumos o CONOPS, estudo de caso, critérios probabilísticos, matriz de alternativas e oficina do gateway. Defina no próprio texto: baseline é medida atual; contramétrica é efeito indesejado; falha intolerável interrompe a liberação. Para a questão 12, delimite um fluxo administrativo e declare que não há decisão clínica automatizada. Distribua 100% entre formulação do problema, evidência/medida, trade-off, responsabilidade humana e gatilho de revisão.

- [ ] **Step 3: Executar o teste**

Run: `python -m unittest tests.test_pedagogical_shell.PublicExerciseAnswerPolicyTest -v`  
Expected: Módulos 1 e 2 não aparecem nas falhas; os demais podem falhar.

- [ ] **Step 4: Commit**

```bash
git add docs/modulo-1-fundamentos/exercicios.md docs/modulo-2-desenho-conceitual/exercicios.md
git commit -m "docs: guide Bloom activities in modules one and two"
```

### Task 3: Guiar Aplicar, Analisar, Avaliar e Criar nos módulos 3 e 4

**Files:**
- Modify: `docs/modulo-3-rag/exercicios.md:81-131`
- Modify: `docs/modulo-4-agentes/exercicios.md:81-149`
- Test: `tests/test_pedagogical_shell.py`

**Interfaces:**
- Consumes: corpus Boreal, saída `RECUPERADO`, `troca_boreal.py`, trace de reserva e padrões dos módulos.
- Produces: atividades que fazem o estudante ler evidência antes de propor mudanças.

- [ ] **Step 1: Reescrever o Módulo 3**

Nas questões 8 a 12, comece pelo corpus Boreal e pela saída da oficina. Defina recall como encontrar o trecho correto e precisão como evitar trecho irrelevante. Na falha de permissão, ordene: delimitar dados expostos, localizar fronteiras, formular hipótese, conter e testar. Na escolha de padrão, ofereça tabela tipo de fonte/pergunta, estratégia, consequência e gatilho. Na criação, delimite arquitetura para documentos e tabelas sintéticos, em vez de plataforma corporativa completa.

Distribua 100% entre rastreabilidade de fontes, separação recuperação/geração, autorização, decisão e experimento de revisão.

- [ ] **Step 2: Reescrever o Módulo 4**

Referencie `troca_boreal.py` e o trace. Defina “estado autoritativo” como registro que confirma o efeito e “idempotência” como prevenção de repetição de efeito. No diagnóstico, conduza: fatos observados, incertezas do timeout, violação de contrato, contenção, reconciliação e teste. Na crítica, comece pela alternativa mínima e só então compare agente único, múltiplos agentes e workflow.

Distribua 100% entre leitura de evidências, fronteiras de autoridade, falha/recuperação, alternativa mínima e verificação.

- [ ] **Step 3: Executar o teste**

Run: `python -m unittest tests.test_pedagogical_shell.PublicExerciseAnswerPolicyTest -v`  
Expected: Módulos 1 a 4 passam; 5 e 6 podem falhar.

- [ ] **Step 4: Commit**

```bash
git add docs/modulo-3-rag/exercicios.md docs/modulo-4-agentes/exercicios.md
git commit -m "docs: guide Bloom activities in RAG and agents"
```

### Task 4: Guiar Aplicar, Analisar, Avaliar e Criar nos módulos 5 e 6

**Files:**
- Modify: `docs/modulo-5-confianca/exercicios.md:74-119`
- Modify: `docs/modulo-6-operacao/exercicios.md:74-122`
- Test: `tests/test_pedagogical_shell.py`

**Interfaces:**
- Consumes: casos sintéticos, relatório da oficina, trace/manifesto local, conceitos de risco residual e métricas.
- Produces: critérios de avaliação compreensíveis, sem pontos e sem terminologia hermética.

- [ ] **Step 1: Reescrever o Módulo 5**

Defina ameaça, ativo, precondição, risco inerente e risco residual na primeira exigência. Na regressão: listar fatos, separar camadas, verificar fatias, questionar independência do avaliador e decidir portão. No parecer, explique os tratamentos reduzir, aceitar temporariamente com controle, transferir e suspender. Na criação, troque “rubrica de avaliação” por “critérios qualitativos de avaliação humana em quatro níveis”, pedindo tabela com dimensão, descritores e evidência.

Converta regras de desconto em critérios percentuais explícitos de modelo de ameaças, causalidade, impacto, controles/limites, responsabilidade e verificação.

- [ ] **Step 2: Reescrever o Módulo 6**

Defina ativo comportamental, portão de regressão, canary, rollback, SLO e trace na primeira instrução que os exige, ligando às definições existentes. Para o manifesto, conduza versão de ativos, tabela de evidências e portão. No rollout, peça hipótese por camada; na plataforma, classificação comum/específica/adiada; no capstone, divida a entrega em três incrementos, começando por consulta fundamentada ou ação aprovada.

Distribua 100% entre fronteiras, evidências, operação segura, responsabilidades, riscos residuais e evolução. Troque “rubricas, instrumentos” por “critérios qualitativos, instrumentos”.

- [ ] **Step 3: Executar o teste**

Run: `python -m unittest tests.test_pedagogical_shell.PublicExerciseAnswerPolicyTest -v`  
Expected: PASS.

- [ ] **Step 4: Commit**

```bash
git add docs/modulo-5-confianca/exercicios.md docs/modulo-6-operacao/exercicios.md
git commit -m "docs: guide Bloom activities in trust and operations"
```

### Task 5: Reformular projeto final e normalizar a linguagem publicada

**Files:**
- Modify: `docs/sobre/projeto-final.md:38-48`
- Modify: `docs/comecar/{como-usar.md,taxonomia-de-bloom.md}`
- Modify: `docs/sobre/plano-da-disciplina.md:527,696,716,774`
- Modify: `docs/modulo-2-desenho-conceitual/{estudo-de-caso.md,padroes-e-decisoes.md,sintese-e-referencias.md}`
- Modify: `docs/modulo-5-confianca/{index.md,estudo-de-caso.md,exemplo-arquitetural.md,padroes-e-decisoes.md}`
- Modify: `docs/modulo-6-operacao/{conceitos.md,estudo-de-caso.md}`
- Modify: `docs/referencia/atributos-de-qualidade.md`
- Test: `tests/test_pedagogical_shell.py`

**Interfaces:**
- Consumes: vocabulário aprovado e seis critérios do projeto final.
- Produces: conteúdo publicado sem “rubrica” e projeto com critérios percentuais legíveis.

- [ ] **Step 1: Reescrever a tabela do projeto final**

Renomeie `## Rubrica` para `## Critérios de avaliação` e use:

```markdown
| Critério | Peso | Evidência e qualidade esperadas |
|---|---:|---|
| Problema e requisitos | 15% | Delimita usuários, processo, hipótese, fora de escopo e atributos verificáveis; não começa pela ferramenta. |
| Arquitetura e ADRs | 20% | Mostra fronteiras, contratos, responsabilidades e decisões rastreáveis às consequências e gatilhos. |
| Comparação de ferramentas | 15% | Compara duas opções no mesmo caso e explica a escolha sem preferência por marca. |
| Evidências reproduzíveis | 20% | Permite repetir execução local com dados sintéticos, versões, entrada, saída, critério qualitativo e limite. |
| Segurança e governança | 15% | Trata dados, identidade, autorização, riscos, responsabilidade humana e interrupção de modo específico. |
| Operação e custo | 15% | Define sinais, falhas, recuperação, capacidade, custo potencial e remoção com proprietário e ação. |
| **Total** | **100%** |  |
```

Acrescente que pesos orientam a revisão, sem substituir devolutiva qualitativa.

- [ ] **Step 2: Substituir vocabulário técnico**

Use “critérios qualitativos de avaliação humana” para o julgamento de saídas, “critérios de avaliação aplicados por modelo” para o avaliador assistido e “métrica ou critério qualitativo” no Módulo 2. Preserve a escala de quatro níveis de utilidade, mas apresente-a como escala de critérios humanos.

- [ ] **Step 3: Comprovar remoção**

Run: `rg -n -i 'rubrica|\\bpontos?\\b|pontuação|\\bnota\\b' docs --glob '*.md' -g '!superpowers/**'`  
Expected: nenhum resultado.

- [ ] **Step 4: Executar teste e commit**

Run: `python -m unittest tests.test_pedagogical_shell -v`  
Expected: PASS.

```bash
git add docs/sobre/projeto-final.md docs/comecar docs/sobre/plano-da-disciplina.md docs/modulo-2-desenho-conceitual docs/modulo-5-confianca docs/modulo-6-operacao docs/referencia/atributos-de-qualidade.md
git commit -m "docs: clarify evaluation criteria"
```

### Task 6: Verificar a entrega integrada

**Files:**
- Verify: `tests/test_pedagogical_shell.py`
- Verify: `docs/modulo-*/exercicios.md`
- Verify: `docs/sobre/projeto-final.md`

**Interfaces:**
- Consumes: tarefas 1 a 5.
- Produces: site estático válido e política pedagógica protegida.

- [ ] **Step 1: Inspecionar os seis blocos**

Run: `rg -n '^\\*\\*(Situação|Seu papel|Insumos disponíveis|Como conduzir|Entrega esperada|Critérios de avaliação)\\*\\*$' docs/modulo-*/exercicios.md`  
Expected: cada rótulo aparece em cada bloco Aplicar, Analisar, Avaliar e Criar dos seis módulos.

- [ ] **Step 2: Executar todas as verificações**

```bash
python -m unittest discover -s tests -v
python scripts/validate_content.py --all
mkdocs build --strict --clean
```

Expected: todos passam sem erros.

- [ ] **Step 3: Revisar e registrar somente correções necessárias**

Run: `git diff --check && git status --short`  
Expected: sem erro de espaço e diretório limpo depois dos commits das tarefas. Se uma verificação exigir correção, registre apenas essa correção:

```bash
git add docs tests
git commit -m "fix: align guided evaluation criteria"
```

## Revisão do plano

- Cobertura: Tarefas 2–4 reescrevem as 30 atividades avançadas; Tarefa 5 cobre projeto e terminologia publicada; Tarefa 1 protege a política; Tarefa 6 valida a integração.
- Não há respostas-modelo: os passos orientam processo e evidência, sem concluir os cenários.
- Não há dependências novas, mudanças de quantidade de exercícios ou alterações em documentos históricos internos.
