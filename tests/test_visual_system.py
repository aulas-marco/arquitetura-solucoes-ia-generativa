from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "docs/assets/stylesheets/extra.css").read_text(encoding="utf-8")
MKDOCS = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
MERMAID_JS = ROOT / "docs/assets/javascripts/mermaid.mjs"


class AcademiaTokenSystemTest(unittest.TestCase):
    def test_six_approved_colors_and_semantic_roles_are_tokens(self):
        for value in ("#16243A", "#254DB8", "#5FC0D1", "#F2F6FB", "#FFFFFF", "#F2B84B"):
            self.assertIn(value.casefold(), CSS.casefold())
        for token in (
            "--color-text", "--color-text-muted", "--color-surface",
            "--color-border", "--space-1", "--space-8", "--reading-width",
            "--radius-sm", "--radius-md", "--shadow-plate",
        ):
            self.assertIn(token, CSS)

    def test_typography_uses_approved_resilient_stacks(self):
        for family in ("Charter", "Georgia", "Inter", "Segoe UI", "IBM Plex Mono", "Consolas"):
            self.assertIn(family, CSS)


class AcademiaSemanticComponentsTest(unittest.TestCase):
    def test_recurring_course_components_have_explicit_styles(self):
        selectors = (
            ".module-opening", ".objective-card", ".learning-spine",
            ".decision-callout", ".risk-callout", ".bloom-label",
            ".architecture-figure", ".comparison-table", ".adr-block",
            ".md-typeset details", ".rubric",
        )
        for selector in selectors:
            self.assertIn(selector, CSS)

    def test_bloom_levels_keep_their_text_labels(self):
        for slug in ("recordar", "compreender", "aplicar", "analisar", "avaliar", "criar"):
            self.assertRegex(CSS, rf"h2#{slug}\b")

    def test_mkdocs_activates_academia_theme_and_semantic_markdown_extensions(self):
        self.assertRegex(MKDOCS, r"(?m)^\s+primary:\s+custom\s*$")
        self.assertIn("attr_list", MKDOCS)
        self.assertIn("md_in_html", MKDOCS)
        self.assertIn("assets/stylesheets/extra.css", MKDOCS)

    def test_semantic_components_are_added_by_a_project_hook(self):
        self.assertIn("course_semantics", MKDOCS)
        extension = (ROOT / "course_semantics.py").read_text(encoding="utf-8")
        for class_name in (
            "module-opening", "objectives-grid", "objective-card",
            "learning-spine", "decision-callout", "risk-callout",
            "bloom-label", "architecture-figure", "figure-caption",
            "comparison-table", "adr-block", "answer-details", "rubric",
        ):
            self.assertIn(class_name, extension)

    def test_no_broad_strong_lead_in_selector_remains(self):
        self.assertNotIn(".md-typeset p > strong:first-child", CSS)


class AcademiaAccessibilityTest(unittest.TestCase):
    def test_keyboard_motion_and_mobile_behaviors_are_preserved(self):
        for fragment in (
            ":focus-visible", "outline:", "prefers-reduced-motion",
            "overflow-x: auto", "max-width: 100%", "@media (max-width:",
            "scroll-margin-top",
        ):
            self.assertIn(fragment, CSS)
        self.assertNotRegex(CSS, r"outline\s*:\s*(?:0\s*;|none\b)")

    def test_focus_uses_cobalt_and_keeps_material_skip_link_positioning(self):
        focus_rule = re.search(r":focus-visible\s*\{([^}]+)\}", CSS)
        self.assertIsNotNone(focus_rule)
        self.assertIn("var(--course-cobalt)", focus_rule.group(1))
        self.assertNotIn("var(--course-amber)", focus_rule.group(1))
        self.assertNotIn(".md-skip:focus", CSS)

        def luminance(hex_color):
            channels = [int(hex_color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
            channels = [
                value / 12.92 if value <= 0.04045
                else ((value + 0.055) / 1.055) ** 2.4
                for value in channels
            ]
            return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]

        def contrast(first, second):
            light, dark = sorted((luminance(first), luminance(second)), reverse=True)
            return (light + 0.05) / (dark + 0.05)

        for background in ("#FFFFFF", "#F2F6FB"):
            self.assertGreaterEqual(contrast("#254DB8", background), 3.0)

    def test_visual_labels_use_text_or_symbols_in_addition_to_color(self):
        self.assertIn('content: "DECISÃO"', CSS)
        self.assertIn('content: "RISCO"', CSS)
        self.assertIn('content: "RUBRICA"', CSS)


class DirectGithubFallbackTest(unittest.TestCase):
    def test_representative_modules_keep_standard_markdown_structure(self):
        for slug in ("modulo-1-fundamentos", "modulo-3-rag", "modulo-5-confianca"):
            opening = (ROOT / "docs" / slug / "index.md").read_text(encoding="utf-8")
            example = (ROOT / "docs" / slug / "exemplo-arquitetural.md").read_text(encoding="utf-8")
            exercises = (ROOT / "docs" / slug / "exercicios.md").read_text(encoding="utf-8")
            self.assertRegex(opening, r"(?m)^# .+")
            self.assertRegex(opening, r"(?m)^> ")
            self.assertRegex(opening + example, r"(?m)^\|.+\|$")
            self.assertRegex(example, r"!\[[^\]]+\]\([^\)]+\)")
            self.assertRegex(example, r"(?m)^\*Figura \d+ — .+\*$")
            self.assertRegex(example, r"\[[^\]]+\]\([^\)]+\)")
            self.assertIn("<details>", exercises)
            self.assertRegex(exercises, r"<summary>(?:Ver resposta|Resposta comentada)</summary>")
            self.assertRegex(exercises, r"(?m)^\*\*Rubrica")

    def test_decision_and_risk_callouts_are_standard_markdown_blockquotes(self):
        decision = (ROOT / "docs/modulo-2-desenho-conceitual/padroes-e-decisoes.md").read_text(encoding="utf-8")
        risk = (ROOT / "docs/modulo-5-confianca/conceitos.md").read_text(encoding="utf-8")
        self.assertRegex(decision, r"(?m)^> \*\*Decisão arquitetural:")
        self.assertRegex(risk, r"(?m)^> \*\*Risco arquitetural:")


class BuiltSiteRuntimeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        result = subprocess.run(
            [sys.executable, "-m", "mkdocs", "build", "--strict"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if result.returncode:
            raise AssertionError(result.stdout + result.stderr)

    def built(self, relative_path):
        return (ROOT / "site" / relative_path / "index.html").read_text(encoding="utf-8")

    def test_mermaid_fence_has_pinned_runtime_and_instant_navigation_initializer(self):
        self.assertTrue(MERMAID_JS.is_file())
        initializer = MERMAID_JS.read_text(encoding="utf-8")
        self.assertRegex(initializer, r"mermaid@11\.\d+\.\d+")
        self.assertIn("startOnLoad: false", initializer)
        self.assertIn("document$.subscribe", initializer)
        self.assertIn("mermaid.run", initializer)

        page = self.built("modulo-1-fundamentos/exemplo-arquitetural")
        self.assertIn('<pre class="mermaid"><code>', page)
        self.assertRegex(
            page,
            r'<script src="\.\./\.\./assets/javascripts/mermaid\.mjs" type="module"></script>',
        )

    def test_representative_pages_emit_all_semantic_component_classes(self):
        module = self.built("modulo-1-fundamentos")
        self.assertRegex(module, r'<h1[^>]*class="[^"]*module-opening')
        self.assertRegex(module, r'<ol[^>]*class="[^"]*objectives-grid')
        self.assertRegex(module, r'<li[^>]*class="[^"]*objective-card')
        self.assertRegex(module, r'<table[^>]*class="[^"]*comparison-table')

        how_to = self.built("comecar/como-usar")
        self.assertRegex(how_to, r'<ol[^>]*class="[^"]*learning-spine')

        exercises = self.built("modulo-1-fundamentos/exercicios")
        self.assertRegex(exercises, r'<h2[^>]*class="[^"]*bloom-label')
        self.assertRegex(exercises, r'<details[^>]*class="[^"]*answer-details')
        self.assertRegex(exercises, r'<p[^>]*class="[^"]*rubric')

        concepts = self.built("modulo-1-fundamentos/conceitos")
        self.assertRegex(concepts, r'<p[^>]*class="[^"]*architecture-figure')
        self.assertRegex(concepts, r'<em[^>]*class="[^"]*figure-caption')

        rag_figures = self.built("modulo-3-rag/exemplo-arquitetural")
        self.assertGreaterEqual(rag_figures.count("architecture-figure"), 2)
        self.assertGreaterEqual(rag_figures.count("figure-caption"), 2)

        decisions = self.built("modulo-2-desenho-conceitual/padroes-e-decisoes")
        self.assertRegex(decisions, r'<blockquote[^>]*class="[^"]*decision-callout')
        adr = self.built("modulo-2-desenho-conceitual/exemplo-arquitetural")
        self.assertRegex(adr, r'<h3[^>]*class="[^"]*adr-block')
        risks = self.built("modulo-5-confianca/conceitos")
        self.assertRegex(risks, r'<blockquote[^>]*class="[^"]*risk-callout')


if __name__ == "__main__":
    unittest.main()
