from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.validate_content import Counts, ROOT, bloom_sections, validate_references


class ReferenceStyleMarkdownTest(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory(dir=ROOT)
        self.directory = Path(self.temporary_directory.name)
        self.page = self.directory / "page.md"

    def tearDown(self):
        self.temporary_directory.cleanup()

    def validate(self, text):
        errors = []
        counts = Counts()
        validate_references(self.page, text, errors, counts)
        return errors, counts

    def test_valid_reference_style_link_and_image(self):
        (self.directory / "target.md").write_text("# Destino\n", encoding="utf-8")
        (self.directory / "image.png").write_bytes(b"image")

        errors, counts = self.validate(
            "[texto][DOC]\n![diagrama][IMG]\n\n"
            "[doc]: target.md\n[img]: image.png \"Legenda\"\n"
        )

        self.assertEqual([], errors)
        self.assertEqual(1, counts.images)

    def test_broken_reference_style_targets_are_reported(self):
        errors, counts = self.validate(
            "[texto][doc]\n![diagrama][img]\n\n"
            "[doc]: missing.md\n[img]: missing.png\n"
        )

        self.assertTrue(any("missing.md" in error for error in errors), errors)
        self.assertTrue(any("missing.png" in error for error in errors), errors)
        self.assertEqual(1, counts.images)

    def test_reference_style_image_with_empty_alt_is_reported(self):
        (self.directory / "image.png").write_bytes(b"image")

        errors, counts = self.validate("![][img]\n\n[img]: image.png\n")

        self.assertTrue(any("texto alternativo vazio" in error for error in errors), errors)
        self.assertEqual(1, counts.images)

    def test_html_image_is_counted_and_checked(self):
        (self.directory / "image.png").write_bytes(b"image")

        errors, counts = self.validate('<img src="image.png" alt="Diagrama acessível">')

        self.assertEqual([], errors)
        self.assertEqual(1, counts.images)

    def test_html_image_without_src_is_reported_without_crashing(self):
        errors, counts = self.validate('<img alt="sem origem">')

        self.assertTrue(any("imagem HTML sem origem" in error for error in errors), errors)
        self.assertEqual(1, counts.images)

    def test_html_image_with_empty_src_is_reported_without_crashing(self):
        errors, counts = self.validate('<img src="" alt="sem origem">')

        self.assertTrue(any("imagem HTML sem origem" in error for error in errors), errors)
        self.assertEqual(1, counts.images)


class BloomSectionBoundaryTest(unittest.TestCase):
    def test_section_stops_at_next_heading_of_same_level(self):
        text = (
            "## Recordar\nPergunta.\n"
            "## Nota independente\n<details>não pertence a Recordar</details>\n"
            "## Compreender\nConteúdo.\n"
        )

        sections = bloom_sections(text)

        self.assertNotIn("<details>", sections["Recordar"])


class FullRepositoryMutationTest(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory(dir=ROOT)
        self.repository = Path(self.temporary_directory.name)
        shutil.copytree(ROOT / "docs", self.repository / "docs")
        shutil.copytree(ROOT / "scripts", self.repository / "scripts")

    def tearDown(self):
        self.temporary_directory.cleanup()

    def validate(self):
        return subprocess.run(
            [sys.executable, "scripts/validate_content.py", "--all"],
            cwd=self.repository,
            text=True,
            capture_output=True,
        )

    def test_duplicate_required_image_reference_is_rejected(self):
        page = self.repository / "docs/modulo-1-fundamentos/conceitos.md"
        page.write_text(
            page.read_text(encoding="utf-8")
            + "\n![repetida](../assets/images/m01-anatomia-solucao-generativa.png)\n",
            encoding="utf-8",
        )

        result = self.validate()

        self.assertNotEqual(0, result.returncode)
        self.assertIn("referenciada mais de uma vez", result.stderr)

    def test_unreferenced_required_image_is_rejected(self):
        page = self.repository / "docs/modulo-1-fundamentos/exemplo-arquitetural.md"
        page.write_text(
            re.sub(
                r"!\[[^]]+\]\(\.\./assets/images/m01-anatomia-solucao-generativa\.png\)",
                "", page.read_text(encoding="utf-8"),
            ),
            encoding="utf-8",
        )

        result = self.validate()

        self.assertNotEqual(0, result.returncode)
        self.assertIn("imagem obrigatória não referenciada", result.stderr)

    def test_fourteenth_png_is_rejected(self):
        (self.repository / "docs/assets/images/extra.png").write_bytes(b"png")

        result = self.validate()

        self.assertNotEqual(0, result.returncode)
        self.assertIn("PNG não previsto", result.stderr)

    def test_broken_local_anchor_is_rejected(self):
        page = self.repository / "docs/index.md"
        page.write_text(
            page.read_text(encoding="utf-8")
            + "\n[Âncora quebrada](comecar/como-usar.md#nao-existe)\n",
            encoding="utf-8",
        )

        result = self.validate()

        self.assertNotEqual(0, result.returncode)
        self.assertIn("âncora local inexistente", result.stderr)

    def test_explicit_heading_anchor_is_accepted(self):
        target = self.repository / "docs/comecar/como-usar.md"
        target.write_text(
            target.read_text(encoding="utf-8") + "\n## Seção estável {#secao-estavel}\n",
            encoding="utf-8",
        )
        page = self.repository / "docs/index.md"
        page.write_text(
            page.read_text(encoding="utf-8")
            + "\n[Âncora estável](comecar/como-usar.md#secao-estavel)\n",
            encoding="utf-8",
        )

        result = self.validate()

        self.assertEqual(0, result.returncode, result.stderr)

    def test_module_under_budget_is_rejected(self):
        module = self.repository / "docs/modulo-1-fundamentos"
        for page in module.glob("*.md"):
            page.write_text("# Curto\n", encoding="utf-8")

        result = self.validate()

        self.assertNotEqual(0, result.returncode)
        self.assertIn("fora do orçamento de 6.000–8.000", result.stderr)

    def test_module_over_budget_is_rejected(self):
        page = self.repository / "docs/modulo-1-fundamentos/conceitos.md"
        page.write_text(
            page.read_text(encoding="utf-8") + (" palavra" * 2_000),
            encoding="utf-8",
        )

        result = self.validate()

        self.assertNotEqual(0, result.returncode)
        self.assertIn("fora do orçamento de 6.000–8.000", result.stderr)

    def test_total_budget_is_rejected_independently(self):
        for slug in (
            "modulo-1-fundamentos", "modulo-2-desenho-conceitual", "modulo-3-rag",
            "modulo-4-agentes", "modulo-5-confianca", "modulo-6-operacao",
        ):
            page = self.repository / "docs" / slug / "conceitos.md"
            page.write_text(
                page.read_text(encoding="utf-8") + (" palavra" * 800),
                encoding="utf-8",
            )

        result = self.validate()

        self.assertNotEqual(0, result.returncode)
        self.assertIn("total fora do orçamento de 40.000–50.000", result.stderr)


if __name__ == "__main__":
    unittest.main()
