from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "docs/assets/stylesheets/extra.css").read_text(encoding="utf-8")
MKDOCS = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")


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


class AcademiaAccessibilityTest(unittest.TestCase):
    def test_keyboard_motion_and_mobile_behaviors_are_preserved(self):
        for fragment in (
            ":focus-visible", "outline:", "prefers-reduced-motion",
            "overflow-x: auto", "max-width: 100%", "@media (max-width:",
            "scroll-margin-top",
        ):
            self.assertIn(fragment, CSS)
        self.assertNotRegex(CSS, r"outline\s*:\s*(?:0\s*;|none\b)")

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


if __name__ == "__main__":
    unittest.main()
