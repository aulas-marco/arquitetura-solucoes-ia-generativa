from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProjectTest(unittest.TestCase):
    def test_required_project_files_exist(self):
        required = [
            "mkdocs.yml",
            "requirements.txt",
            ".gitignore",
            "docs/index.md",
            "docs/assets/stylesheets/extra.css",
            "scripts/validate_content.py",
        ]
        self.assertEqual([], [name for name in required if not (ROOT / name).exists()])

    def test_validator_help_runs(self):
        result = subprocess.run(
            ["python3", "scripts/validate_content.py", "--help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)

    def test_full_validator_counts_the_cover_and_module_illustrations(self):
        result = subprocess.run(
            ["python3", "scripts/validate_content.py", "--all"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("Imagens: 19", result.stdout)

    def test_homepage_cover_has_an_editorial_caption(self):
        homepage = (ROOT / "docs/index.md").read_text(encoding="utf-8")

        self.assertIn("*Capa — Cartografia da solução generativa", homepage)

    def test_homepage_links_directly_to_six_modules_and_separately_to_plan(self):
        homepage = (ROOT / "docs/index.md").read_text(encoding="utf-8")

        for slug in (
            "modulo-1-fundamentos", "modulo-2-desenho-conceitual", "modulo-3-rag",
            "modulo-4-agentes", "modulo-5-confianca", "modulo-6-operacao",
        ):
            self.assertEqual(1, homepage.count(f"({slug}/index.md)"), slug)
        self.assertIn("[Plano da disciplina](sobre/plano-da-disciplina.md)", homepage)

    def test_opentelemetry_semconv_year_is_consistently_2026(self):
        registry = (ROOT / "docs/referencia/fontes.yml").read_text(encoding="utf-8")
        entry = re.search(
            r"- id: opentelemetry-semconv-1-43\n(.*?)(?=\n- id:|\Z)",
            registry,
            re.DOTALL,
        )
        self.assertIsNotNone(entry)
        self.assertIn("\n  year: 2026\n", entry.group(0))

        bibliography = (ROOT / "docs/referencia/bibliografia.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "OpenTelemetry Authors (2026). [*OpenTelemetry Semantic Conventions 1.43.0*]",
            bibliography,
        )

    def test_every_external_markdown_url_is_in_the_source_registry(self):
        registry = (ROOT / "docs/referencia/fontes.yml").read_text(encoding="utf-8")
        registered_urls = set(re.findall(r"(?m)^  url: (https?://\S+)$", registry))
        markdown = "\n".join(
            path.read_text(encoding="utf-8") for path in (ROOT / "docs").rglob("*.md")
        )
        used_urls = set(re.findall(r"https?://[^) >]+", markdown))

        self.assertEqual([], sorted(used_urls - registered_urls))


if __name__ == "__main__":
    unittest.main()
