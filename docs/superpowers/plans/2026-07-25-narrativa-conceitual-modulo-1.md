# Narrativa conceitual do Módulo 1 — plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reescrever `conceitos.md` como uma progressão arquitetural coesa, preservando definições, links internos e a arquitetura da informação do Módulo 1.

**Architecture:** A página será organizada em cinco movimentos encadeados: mudança sistêmica, origem do comportamento, informação em trânsito, distribuição de responsabilidade e verificação. Termos técnicos permanecerão como subtítulos consultáveis dentro desses movimentos, e cada bloco terminará com uma consequência que conduz ao seguinte.

**Tech Stack:** Markdown, MkDocs Material, testes Python com `unittest` e `pytest`, validador editorial do repositório.

## Global Constraints

- Preservar as oito páginas da arquitetura da informação do módulo.
- Não criar uma página adicional nem deslocar conceitos para o exemplo arquitetural.
- Preservar as âncoras referenciadas por outras páginas ou atualizar todos os links afetados.
- Manter a distinção entre modelo, aplicação e sistema sociotécnico.
- Manter separados geração, decisão, autorização e efeito.
- Manter separados teste de software, avaliação comportamental e verificação arquitetural.
- Não antecipar o detalhamento de vistas, táticas, ADRs, RAG, agentes, ameaças ou LLMOps.
- Evitar frases sentenciosas, oposições artificiais e outros cacoetes de escrita de IA.

---

### Task 1: Fixar a progressão e proteger as âncoras

**Files:**
- Modify: `tests/test_module_one.py`
- Inspect: `docs/modulo-1-fundamentos/*.md`

**Interfaces:**
- Consumes: títulos e links existentes para `conceitos.md`.
- Produces: teste que codifica a ordem dos cinco movimentos e a preservação das âncoras públicas.

- [ ] **Step 1: Mapear links internos**

Run:

```bash
rg -n 'conceitos\.md#' docs tests
```

Expected: lista completa de âncoras que não podem desaparecer silenciosamente.

- [ ] **Step 2: Escrever o teste de ordem narrativa**

Adicionar a `ModuleOneReviewRegressionTest` um teste que leia `conceitos.md`, procure os cinco títulos principais aprovados e assegure que seus índices aparecem em ordem crescente.

- [ ] **Step 3: Escrever o teste de conceitos obrigatórios**

No mesmo teste, verificar a presença de `modelo`, `aplicação`, `sistema sociotécnico`, `superfície comportamental`, `conhecimento`, `contexto`, `estado`, `memória`, `evidência`, `trace`, `geração`, `decisão`, `autorização`, `efeito`, `Teste de software`, `Avaliação comportamental`, `Verificação arquitetural` e `fitness function`.

- [ ] **Step 4: Executar o teste e confirmar a falha**

Run:

```bash
python -m pytest tests/test_module_one.py -q
```

Expected: FAIL porque a página ainda não segue os cinco movimentos.

### Task 2: Reescrever a página em cinco movimentos

**Files:**
- Modify: `docs/modulo-1-fundamentos/conceitos.md`

**Interfaces:**
- Consumes: progressão e vocabulário protegidos pela Task 1.
- Produces: página conceitual coesa e compatível com os links do módulo.

- [ ] **Step 1: Manter a preparação e o mapa**

Preservar a abertura sobre o objetivo do arquiteto e `## Um mapa para orientar a leitura`. Usar a figura para antecipar modelo, contexto, variabilidade, controles e evidências, sem tratá-la como arquitetura pronta.

- [ ] **Step 2: Construir “O que muda no sistema”**

Fundir determinismo e probabilidade com modelo, aplicação e sistema sociotécnico. Encerrar mostrando que a variabilidade observada pertence à composição, não apenas ao modelo.

- [ ] **Step 3: Construir “De onde emerge o comportamento”**

Apresentar superfície comportamental como eixo. Integrar modelo fundacional, treinamento, inferência, tokens, janela, prompt, parâmetros, conhecimento paramétrico, variabilidade e alucinação como elementos que explicam essa superfície.

- [ ] **Step 4: Construir “Que informação atravessa o sistema”**

Relacionar contexto e embeddings ao ciclo da informação. Preservar a tabela que distingue conhecimento, contexto, estado, memória, evidência e trace, acrescentando transições sobre origem, finalidade, transformação, retenção e autorização.

- [ ] **Step 5: Construir “Como distribuir responsabilidade”**

Partir de atributos de qualidade, trade-offs e significância arquitetural. Conduzir à separação entre geração, decisão, autorização e efeito. Integrar multimodalidade como ampliação dos tipos de entrada, saída, risco e validação.

- [ ] **Step 6: Construir “Como verificar e governar”**

Relacionar teste de software, avaliação comportamental e verificação arquitetural às zonas determinísticas e probabilísticas. Definir fitness function como continuidade da verificação e fechar com o contrato arquitetural que prepara padrões e decisões e os módulos 2–6.

- [ ] **Step 7: Executar o teste do módulo**

Run:

```bash
python -m pytest tests/test_module_one.py -q
```

Expected: PASS.

### Task 3: Verificar links, estilo e publicação

**Files:**
- Modify if necessary: `docs/modulo-1-fundamentos/*.md`
- Modify if necessary: `tests/test_module_one.py`

**Interfaces:**
- Consumes: página reescrita da Task 2.
- Produces: módulo navegável, validado e sem regressões editoriais.

- [ ] **Step 1: Conferir âncoras após a renderização**

Run:

```bash
rg -n 'conceitos\.md#' docs tests
```

Comparar cada destino com os títulos finais. Atualizar somente links cujo título precisou mudar.

- [ ] **Step 2: Procurar fragmentação e cacoetes**

Run:

```bash
rg -n 'não é apenas|não é .* é|mais do que|em resumo|vale destacar|nesse sentido|fundamental|crucial|robusto' docs/modulo-1-fundamentos/conceitos.md
```

Expected: nenhuma ocorrência automática; qualquer ocorrência restante deve ser necessária ao argumento.

- [ ] **Step 3: Executar a validação completa**

Run:

```bash
python scripts/validate_content.py --all
python -m pytest -q
python -m mkdocs build --strict
git diff --check
```

Expected: validação sem erros, 132 testes e 312 subtestes ou contagens maiores, build concluído e diff sem problemas.

- [ ] **Step 4: Revisar o diff**

Run:

```bash
git diff -- docs/modulo-1-fundamentos/conceitos.md tests/test_module_one.py
```

Confirmar que nenhum conceito obrigatório foi perdido, que as cinco perguntas aparecem em sequência e que produtos continuam fora da página conceitual.
