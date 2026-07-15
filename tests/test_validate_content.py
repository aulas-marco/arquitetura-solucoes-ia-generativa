from pathlib import Path
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


class BloomSectionBoundaryTest(unittest.TestCase):
    def test_section_stops_at_next_heading_of_same_level(self):
        text = (
            "## Recordar\nPergunta.\n"
            "## Nota independente\n<details>não pertence a Recordar</details>\n"
            "## Compreender\nConteúdo.\n"
        )

        sections = bloom_sections(text)

        self.assertNotIn("<details>", sections["Recordar"])


if __name__ == "__main__":
    unittest.main()
