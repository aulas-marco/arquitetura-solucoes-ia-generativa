# Concept Infographics Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add six generated, accessible architectural infographics to the six concept pages and make them first-class validated assets of the course site.

**Architecture:** The content validator remains the source of truth for the repository image manifest. One new required PNG is added to each module manifest entry, then each `conceitos.md` renders its own infographic immediately after the title with complete alt text and an editorial caption. A focused regression test enforces placement, asset uniqueness, captioning, and pedagogical coverage independently of the generated pixels.

**Tech Stack:** Markdown, MkDocs Material, project CSS hooks, Python `unittest`, `scripts/validate_content.py`, built-in image generation.

## Global Constraints

- Generate exactly six new horizontal PNG assets under `docs/assets/images/`; do not overwrite existing images.
- Use the filenames defined in the approved design: `m01-mapa-comportamento-generativo.png`, `m02-mapa-da-oportunidade-ao-conops.png`, `m03-mapa-rag-dos-dois-pipelines.png`, `m04-mapa-autonomia-controlada.png`, `m05-mapa-confianca-sistemica.png`, and `m06-mapa-operacao-evidencia-continua.png`.
- Place each infographic immediately after the H1 of its matching `conceitos.md` page.
- Every image needs complete Portuguese alt text and an editorial caption; neither may depend on color alone.
- Preserve the existing Academia visual language: warm light background, deep blue/cobalt structure, amber decisions, coral risks, high contrast, short Portuguese labels, and no branding or watermark.
- Keep the existing validator rule that every PNG in `docs/assets/images/` is named in the required-image manifest and referenced exactly once.
- Do not alter exercises, case studies, curriculum structure, or existing architectural illustrations.

---

## File Structure

| Path | Responsibility |
| --- | --- |
| `scripts/validate_content.py` | Expand the authoritative required-image manifest from two to three images per module. |
| `tests/test_concept_infographics.py` | Assert the six concept-page image contracts, placement, captions, source assets, and exactly six distinct new filenames. |
| `tests/test_project.py` | Update the full-repository image-count assertion from 13 to 19. |
| `docs/assets/images/m01-mapa-comportamento-generativo.png`, `m02-mapa-da-oportunidade-ao-conops.png`, `m03-mapa-rag-dos-dois-pipelines.png`, `m04-mapa-autonomia-controlada.png`, `m05-mapa-confianca-sistemica.png`, `m06-mapa-operacao-evidencia-continua.png` | Six final generated infographic assets. |
| `docs/modulo-*/conceitos.md` | Render each asset after H1 with complete alt text and a caption. |

### Task 1: Extend the image manifest and lock the editorial contract

**Files:**
- Create: `tests/test_concept_infographics.py`
- Modify: `scripts/validate_content.py:22-28`
- Modify: `tests/test_project.py:29-38`
- Test: `tests/test_concept_infographics.py`

**Interfaces:**
- Consumes: `MODULES` from `scripts/validate_content.py` and the six source Markdown files.
- Produces: a 19-asset validator manifest and a regression suite that subsequent generation and Markdown tasks must satisfy.

- [ ] **Step 1: Write the failing image-contract test**

Create `tests/test_concept_infographics.py` with this complete test:

```python
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "docs" / "assets" / "images"

INFOGRAPHICS = {
    "modulo-1-fundamentos": (
        "m01-mapa-comportamento-generativo.png",
        "Mapa do comportamento generativo",
        "Do determinístico ao probabilístico",
    ),
    "modulo-2-desenho-conceitual": (
        "m02-mapa-da-oportunidade-ao-conops.png",
        "Mapa da oportunidade ao CONOPS",
        "Oportunidade não é solução",
    ),
    "modulo-3-rag": (
        "m03-mapa-rag-dos-dois-pipelines.png",
        "Mapa RAG dos dois pipelines",
        "Conhecimento paramétrico não é repositório corporativo",
    ),
    "modulo-4-agentes": (
        "m04-mapa-autonomia-controlada.png",
        "Mapa da autonomia controlada",
        "Quatro formas que não devem ser confundidas",
    ),
    "modulo-5-confianca": (
        "m05-mapa-confianca-sistemica.png",
        "Mapa da confiança sistêmica",
        "Confiança é uma relação, não uma característica absoluta",
    ),
    "modulo-6-operacao": (
        "m06-mapa-operacao-evidencia-continua.png",
        "Mapa da operação e evidência contínua",
        "O objeto operado é um pacote comportamental",
    ),
}


class ConceptInfographicsTest(unittest.TestCase):
    def test_every_concept_page_introduces_one_accessible_infographic(self):
        for slug, (filename, title, first_heading) in INFOGRAPHICS.items():
            with self.subTest(module=slug):
                page = (ROOT / "docs" / slug / "conceitos.md").read_text(encoding="utf-8")
                image = f"![{title}](../assets/images/{filename}"
                self.assertIn(image, page)
                self.assertEqual(1, page.count(filename))
                self.assertTrue((IMAGES / filename).is_file())
                self.assertLess(page.index(image), page.index(f"## {first_heading}"))
                self.assertIn("*Figura —", page)

    def test_infographic_assets_are_six_distinct_pngs(self):
        filenames = [contract[0] for contract in INFOGRAPHICS.values()]
        self.assertEqual(6, len(filenames))
        self.assertEqual(6, len(set(filenames)))
        self.assertTrue(all(re.fullmatch(r"m0[1-6]-.+\\.png", name) for name in filenames))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the new test and verify it fails because the assets and references do not yet exist**

Run:

```bash
python3 -m unittest tests.test_concept_infographics -v
```

Expected: six subtests fail at the missing image reference assertion.

- [ ] **Step 3: Add each new filename to the validator manifest**

Replace the `MODULES` declaration in `scripts/validate_content.py` with:

```python
MODULES = {
    "modulo-1-fundamentos": ("Fundamentos", ("m01-deterministico-probabilistico.png", "m01-anatomia-solucao-generativa.png", "m01-mapa-comportamento-generativo.png")),
    "modulo-2-desenho-conceitual": ("Desenho conceitual", ("m02-oportunidade-arquitetura.png", "m02-paisagem-decisoes.png", "m02-mapa-da-oportunidade-ao-conops.png")),
    "modulo-3-rag": ("RAG", ("m03-dois-fluxos-rag.png", "m03-pergunta-evidencia.png", "m03-mapa-rag-dos-dois-pipelines.png")),
    "modulo-4-agentes": ("Agentes", ("m04-agente-ferramentas.png", "m04-fronteiras-autonomia.png", "m04-mapa-autonomia-controlada.png")),
    "modulo-5-confianca": ("Confiança", ("m05-defesas-profundidade.png", "m05-prisma-avaliacao.png", "m05-mapa-confianca-sistemica.png")),
    "modulo-6-operacao": ("Operação", ("m06-ciclo-llmops.png", "m06-plataforma-corporativa.png", "m06-mapa-operacao-evidencia-continua.png")),
}
```

Change the assertion in `tests/test_project.py` to:

```python
self.assertIn("Imagens: 19", result.stdout)
```

- [ ] **Step 4: Run the changed validation tests and verify expected failure**

Run:

```bash
python3 -m unittest tests.test_concept_infographics tests.test_project.ProjectTest.test_full_validator_counts_the_cover_and_module_illustrations -v
```

Expected: failures report the six required PNG assets as missing; this confirms the manifest blocks unknown or absent assets before image generation.

- [ ] **Step 5: Commit the test-first manifest work**

```bash
git add scripts/validate_content.py tests/test_concept_infographics.py tests/test_project.py
git commit -m "test: define concept infographic asset contract"
```

### Task 2: Generate and inspect the six infographic assets

**Files:**
- Create: `docs/assets/images/m01-mapa-comportamento-generativo.png`
- Create: `docs/assets/images/m02-mapa-da-oportunidade-ao-conops.png`
- Create: `docs/assets/images/m03-mapa-rag-dos-dois-pipelines.png`
- Create: `docs/assets/images/m04-mapa-autonomia-controlada.png`
- Create: `docs/assets/images/m05-mapa-confianca-sistemica.png`
- Create: `docs/assets/images/m06-mapa-operacao-evidencia-continua.png`
- Test: `tests/test_concept_infographics.py`

**Interfaces:**
- Consumes: approved design in `docs/superpowers/specs/2026-07-15-infograficos-conceitos-design.md` and the filenames locked by Task 1.
- Produces: six inspectable PNGs exactly at the paths consumed by the validator and Markdown pages.

- [ ] **Step 1: Generate M1 — mapa do comportamento generativo**

Use the built-in image generator with this prompt:

```text
Use case: infographic-diagram
Asset type: horizontal course infographic for a postgraduate architecture course website
Primary request: a precise educational architecture map titled only with short Portuguese labels, showing how a generative AI system changes a deterministic architecture into a probabilistic one
Scene/backdrop: warm near-white editorial background, no texture
Subject: left-to-right flow Entrada e contexto -> Prompt, tokens e parâmetros -> Modelo fundacional -> Saída variável; surround this flow with the named architectural safeguards Conhecimento paramétrico, Avaliação, Segurança, Observabilidade
Style/medium: polished editorial systems diagram, clean flat vector-like shapes, thin deep-blue connection lines, cobalt structural blocks, amber decision markers, coral risk markers
Composition/framing: 16:9 landscape, generous margins, one central flow and one clearly separated protective ring
Text (verbatim): "Entrada e contexto", "Prompt, tokens e parâmetros", "Modelo fundacional", "Saída variável", "Conhecimento paramétrico", "Avaliação", "Segurança", "Observabilidade"
Constraints: Brazilian Portuguese labels only, large legible typography, high contrast, no paragraph text, no logos, no watermark, no people, no photorealism
Avoid: fabricated technical terms, tiny text, crowded tables, gradients that reduce legibility
```

- [ ] **Step 2: Generate M2 — mapa da oportunidade ao CONOPS**

Use the built-in image generator with this prompt:

```text
Use case: infographic-diagram
Asset type: horizontal course infographic for a postgraduate architecture course website
Primary request: a decision map that turns an AI opportunity into an operable concept of operations
Scene/backdrop: warm near-white editorial background
Subject: a staged left-to-right path Oportunidade -> Hipótese de valor -> Hipótese de capacidade -> Adequação ou rejeição da IA -> CONOPS -> Requisitos significativos; under CONOPS, show Stakeholders, Modos operacionais and Responsabilidade humano–IA as connected operating views
Style/medium: rigorous architectural decision diagram, deep-blue and cobalt structure, amber gate for the adequação/rejeição decision, coral exit for rejection
Composition/framing: 16:9 landscape, one clearly labeled decision gate, short labels only
Text (verbatim): "Oportunidade", "Hipótese de valor", "Hipótese de capacidade", "Adequação da IA", "Rejeitar", "CONOPS", "Stakeholders", "Modos operacionais", "Responsabilidade humano–IA", "Requisitos significativos"
Constraints: Brazilian Portuguese, large type, no logos, no watermark, no paragraphs, no people
Avoid: generic chatbot imagery, dense tables, tiny labels, invented English text
```

- [ ] **Step 3: Generate M3 — mapa RAG dos dois pipelines**

Use the built-in image generator with this prompt:

```text
Use case: infographic-diagram
Asset type: horizontal course infographic for a postgraduate architecture course website
Primary request: an architecture map showing two distinct but connected RAG pipelines: governed ingestion and authorized consultation
Scene/backdrop: warm near-white editorial background
Subject: upper offline route Fontes governadas -> Extração e fragmentação -> Metadados e permissões -> Índice versionado; lower online route Pergunta autorizada -> Recuperação -> Evidências -> Resposta citada ou Abstenção; connect both routes through Proveniência and Atualidade
Style/medium: technical editorial diagram, cobalt routes, deep-blue stores, amber evidence markers, coral abstention marker
Composition/framing: 16:9 landscape, two visibly separate lanes with arrows and a shared provenance spine
Text (verbatim): "Fontes governadas", "Extração e fragmentação", "Metadados e permissões", "Índice versionado", "Pergunta autorizada", "Recuperação", "Evidências", "Resposta citada", "Abstenção", "Proveniência", "Atualidade"
Constraints: Brazilian Portuguese, short labels, high contrast, no logo, no watermark, no paragraph copy
Avoid: database brands, tiny typography, a single collapsed pipeline, ungrounded answer as the final output
```

- [ ] **Step 4: Generate M4 — mapa da autonomia controlada**

Use the built-in image generator with this prompt:

```text
Use case: infographic-diagram
Asset type: horizontal course infographic for a postgraduate architecture course website
Primary request: a controlled-autonomy map distinguishing dialogue, workflow, agent and multi-agent collaboration, and showing where tools and policy boundaries constrain action
Scene/backdrop: warm near-white editorial background
Subject: a continuum Diálogo -> Workflow -> Agente -> Múltiplos agentes; below it, a controlled action loop Planejamento -> Ferramentas tipadas -> Estado e contexto -> Resultado; overlay a policy boundary with approval required before material actions
Style/medium: systems architecture infographic, cobalt autonomy continuum, deep-blue control plane, amber approval checkpoint, coral material-action risk marker
Composition/framing: 16:9 landscape, explicit boundary line around policies, short labels
Text (verbatim): "Diálogo", "Workflow", "Agente", "Múltiplos agentes", "Planejamento", "Ferramentas tipadas", "Estado e contexto", "Políticas", "Aprovação", "Ação material"
Constraints: Brazilian Portuguese, high contrast, large type, no logo, no watermark, no robots or humanoid figures
Avoid: autonomous action bypassing policy, tiny labels, generic sci-fi aesthetic
```

- [ ] **Step 5: Generate M5 — mapa da confiança sistêmica**

Use the built-in image generator with this prompt:

```text
Use case: infographic-diagram
Asset type: horizontal course infographic for a postgraduate architecture course website
Primary request: a systemic trust map showing how risk is reduced by layered controls and evidenced by multidimensional evaluation
Scene/backdrop: warm near-white editorial background
Subject: a left-to-right transformation Perigo -> Risco inerente -> Controles em camadas -> Risco residual -> Evidências; show four risk families Segurança, Privacidade, Comportamento, Operação around the left; show Rastreabilidade, Papéis e responsabilidades, and Avaliação multidimensional around the right
Style/medium: disciplined governance infographic, deep-blue structure, coral risk zone, cobalt controls, amber evidence markers
Composition/framing: 16:9 landscape, layered defense visual without a target or weapon metaphor, all relationships readable from the flow
Text (verbatim): "Perigo", "Risco inerente", "Controles em camadas", "Risco residual", "Evidências", "Segurança", "Privacidade", "Comportamento", "Operação", "Rastreabilidade", "Papéis e responsabilidades", "Avaliação multidimensional"
Constraints: Brazilian Portuguese, large high-contrast labels, no logos, no watermark, no paragraphs
Avoid: compliance seals, security shields as the only explanation, tiny text, invented scores
```

- [ ] **Step 6: Generate M6 — mapa da operação e evidência contínua**

Use the built-in image generator with this prompt:

```text
Use case: infographic-diagram
Asset type: horizontal course infographic for a postgraduate architecture course website
Primary request: an operational lifecycle map for a generative AI system treated as a versioned behavioral package
Scene/backdrop: warm near-white editorial background
Subject: a cycle Pacote comportamental versionado -> Avaliação contínua -> Promoção de ambiente -> Entrega controlada -> Observabilidade e traces -> Aprendizado; show Métricas, Privacidade and SLO as transversal guardrails touching the cycle
Style/medium: polished LLMOps systems diagram, cobalt lifecycle arrows, deep-blue assets, amber promotion gate, coral incident/rollback marker used sparingly
Composition/framing: 16:9 landscape, circular operational loop with three transversal rails, short labels only
Text (verbatim): "Pacote comportamental versionado", "Avaliação contínua", "Promoção de ambiente", "Entrega controlada", "Observabilidade e traces", "Aprendizado", "Métricas", "Privacidade", "SLO"
Constraints: Brazilian Portuguese, high contrast, no brands, no watermark, no paragraphs, no dashboards full of tiny values
Avoid: a linear lifecycle with no feedback loop, tiny typography, vendor logos, generic cloud icons
```

- [ ] **Step 7: Inspect every generated image before accepting it**

For each asset, open the output and confirm all five acceptance checks:

1. all required labels are present, readable, and in Portuguese;
2. the named flow or boundary matches the prompt and the approved design;
3. no fabricated claims, vendor logos, watermark, or dense unreadable text appears;
4. the composition is legible at website-column width;
5. the file is a valid PNG at the exact Task 2 path.

Regenerate only the failing asset with a prompt that corrects the single failed criterion; do not overwrite any pre-existing repository asset.

- [ ] **Step 8: Run the asset existence portion of the regression suite**

Run:

```bash
python3 -m unittest tests.test_concept_infographics.ConceptInfographicsTest.test_infographic_assets_are_six_distinct_pngs -v
```

Expected: PASS. The page-reference test remains red until Task 3.

- [ ] **Step 9: Commit the inspected generated assets**

```bash
git add docs/assets/images/m01-mapa-comportamento-generativo.png docs/assets/images/m02-mapa-da-oportunidade-ao-conops.png docs/assets/images/m03-mapa-rag-dos-dois-pipelines.png docs/assets/images/m04-mapa-autonomia-controlada.png docs/assets/images/m05-mapa-confianca-sistemica.png docs/assets/images/m06-mapa-operacao-evidencia-continua.png
git commit -m "feat: add concept synthesis infographics"
```

### Task 3: Integrate the infographics into the six concept pages

**Files:**
- Modify: `docs/modulo-1-fundamentos/conceitos.md:1-3`
- Modify: `docs/modulo-2-desenho-conceitual/conceitos.md:1-5`
- Modify: `docs/modulo-3-rag/conceitos.md:1-5`
- Modify: `docs/modulo-4-agentes/conceitos.md:1-3`
- Modify: `docs/modulo-5-confianca/conceitos.md:1-3`
- Modify: `docs/modulo-6-operacao/conceitos.md:1-3`
- Test: `tests/test_concept_infographics.py`

**Interfaces:**
- Consumes: the six final PNG assets from Task 2 and the filenames locked by Task 1.
- Produces: six rendered Markdown figures, each recognized once by the validator and placed before the module’s first H2.

- [ ] **Step 1: Insert M1 and M2 figures after their H1 headings**

Insert after the H1 in `docs/modulo-1-fundamentos/conceitos.md`:

```md
![Mapa do comportamento generativo: entrada e contexto atravessam prompt, tokens e parâmetros até um modelo fundacional e uma saída variável; conhecimento paramétrico, avaliação, segurança e observabilidade circundam esse comportamento probabilístico](../assets/images/m01-mapa-comportamento-generativo.png "Mapa do comportamento generativo")

*Figura — O modelo transforma contexto em uma saída provável, não garantida; por isso avaliação, segurança e observabilidade pertencem à arquitetura desde a primeira decisão.*
```

Insert after the H1 in `docs/modulo-2-desenho-conceitual/conceitos.md`:

```md
![Mapa da oportunidade ao CONOPS: uma oportunidade é testada por hipóteses de valor e capacidade, passa por uma decisão de adequação da IA e se converte em CONOPS, stakeholders, modos operacionais, responsabilidade humano–IA e requisitos significativos; a rejeição da IA é uma saída válida](../assets/images/m02-mapa-da-oportunidade-ao-conops.png "Mapa da oportunidade ao CONOPS")

*Figura — A decisão arquitetural começa antes do modelo: uma oportunidade só merece solução depois que seu valor, sua capacidade e seu modo de operação podem ser defendidos.*
```

- [ ] **Step 2: Insert M3 and M4 figures after their H1 headings**

Insert after the H1 in `docs/modulo-3-rag/conceitos.md`:

```md
![Mapa RAG dos dois pipelines: no fluxo offline, fontes governadas passam por extração, fragmentação, metadados e permissões até um índice versionado; no fluxo online, uma pergunta autorizada recupera evidências para uma resposta citada ou para abstenção, ligadas por proveniência e atualidade](../assets/images/m03-mapa-rag-dos-dois-pipelines.png "Mapa RAG dos dois pipelines")

*Figura — RAG não é uma busca acoplada ao prompt: ingestão governada e consulta autorizada são pipelines distintos unidos por evidência, atualização e proveniência.*
```

Insert after the H1 in `docs/modulo-4-agentes/conceitos.md`:

```md
![Mapa da autonomia controlada: diálogo, workflow, agente e múltiplos agentes formam um continuum; planejamento usa ferramentas tipadas e estado sob políticas, enquanto ações materiais passam por aprovação explícita](../assets/images/m04-mapa-autonomia-controlada.png "Mapa da autonomia controlada")

*Figura — Autonomia não é uma propriedade binária: ela cresce com a capacidade de decidir e agir, e deve encontrar políticas e aprovação antes de cruzar fronteiras materiais.*
```

- [ ] **Step 3: Insert M5 and M6 figures after their H1 headings**

Insert after the H1 in `docs/modulo-5-confianca/conceitos.md`:

```md
![Mapa da confiança sistêmica: perigo se torna risco inerente nas famílias de segurança, privacidade, comportamento e operação; controles em camadas reduzem o risco residual, que é demonstrado por rastreabilidade, papéis identificáveis e avaliação multidimensional](../assets/images/m05-mapa-confianca-sistemica.png "Mapa da confiança sistêmica")

*Figura — Confiança não é um selo do modelo: é uma relação demonstrável entre riscos, controles, responsabilidades e evidências de comportamento aceitável.*
```

Insert after the H1 in `docs/modulo-6-operacao/conceitos.md`:

```md
![Mapa da operação e evidência contínua: um pacote comportamental versionado passa por avaliação contínua, promoção de ambiente, entrega controlada, observabilidade e traces, e aprendizado; métricas, privacidade e SLO atravessam todo o ciclo](../assets/images/m06-mapa-operacao-evidencia-continua.png "Mapa da operação e evidência contínua")

*Figura — Operar IA generativa significa promover e observar um pacote comportamental completo, produzindo evidência para evoluir com segurança e não apenas liberar uma nova versão de código.*
```

- [ ] **Step 4: Run the focused regression suite and make it green**

Run:

```bash
python3 -m unittest tests.test_concept_infographics tests.test_project.ProjectTest.test_full_validator_counts_the_cover_and_module_illustrations -v
```

Expected: PASS, including the `Imagens: 19` contract.

- [ ] **Step 5: Build the site and inspect representative rendered pages**

Run:

```bash
python3 scripts/validate_content.py --all
mkdocs build --strict
```

Expected: validator reports `Imagens: 19` with no errors and MkDocs completes with exit code 0.

Open these generated pages and confirm the infographic appears directly below H1, is not clipped, and its caption remains attached:

```text
site/modulo-1-fundamentos/conceitos/index.html
site/modulo-3-rag/conceitos/index.html
site/modulo-5-confianca/conceitos/index.html
```

- [ ] **Step 6: Commit the six Markdown integrations**

```bash
git add docs/modulo-1-fundamentos/conceitos.md docs/modulo-2-desenho-conceitual/conceitos.md docs/modulo-3-rag/conceitos.md docs/modulo-4-agentes/conceitos.md docs/modulo-5-confianca/conceitos.md docs/modulo-6-operacao/conceitos.md
git commit -m "feat: add infographics to concept pages"
```

### Task 4: Run full quality gates and prepare the publication handoff

**Files:**
- Modify: none unless a validation failure identifies a concrete defect.
- Test: full `tests/` suite, content validator, strict MkDocs build, and a visual inspection of the generated pages.

**Interfaces:**
- Consumes: the manifest, assets, and Markdown integrations completed by Tasks 1–3.
- Produces: a clean, publication-ready working tree with evidence that the new assets are valid and the site is buildable.

- [ ] **Step 1: Run the full regression suite**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: every test passes, including `ConceptInfographicsTest`, the updated 19-image count, and existing validator mutation tests.

- [ ] **Step 2: Run the final content and build gates**

Run:

```bash
python3 scripts/validate_content.py --all
mkdocs build --strict
git diff --check
git status --short
```

Expected: no validator errors, a successful strict build, no whitespace errors, and only intended tracked changes before the final commit.

- [ ] **Step 3: Resolve only a concrete failed check, if one occurs**

If a validation command fails, return to the task that owns the failing file: Task 1 for the manifest or tests, Task 2 for a named asset, and Task 3 for a concept page. Make the smallest correction, rerun the exact failed command and then repeat Steps 1–2 of this task. Do not introduce unrelated changes.

- [ ] **Step 4: Report the publication-ready result**

Record: six final asset paths, six updated concept pages, the full test count, validator image count of 19, and strict-build result. Do not push or publish without a separate instruction to do so.

## Plan self-review

- **Spec coverage:** Tasks 1–4 cover the six named assets, individual concept-page placement, complete alternative text, captions, approved visual language, explicit inspection, validator registration, local-link checks, strict build, and scope exclusions.
- **Placeholder scan:** The plan contains no `TODO`, `TBD`, omitted prompts, unspecified file paths, or incomplete commands.
- **Consistency:** All filenames, page slugs, alt-text titles, required manifest entries, expected image count, and validation commands match across tasks.
