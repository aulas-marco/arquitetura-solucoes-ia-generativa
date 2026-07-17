from pathlib import Path
import re
import unittest

from scripts.validate_content import MODULES, PAGES, bloom_sections


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


class PedagogicalShellTest(unittest.TestCase):
    def test_every_module_states_approved_reading_time(self):
        for slug in MODULES:
            text = (DOCS / slug / "index.md").read_text(encoding="utf-8")
            with self.subTest(module=slug):
                self.assertRegex(text, r"\*\*Tempo estimado de leitura:\*\* 60[–-]90 minutos")

    def test_modules_four_to_six_link_complete_eight_page_maps(self):
        for slug in tuple(MODULES)[3:]:
            text = (DOCS / slug / "index.md").read_text(encoding="utf-8")
            with self.subTest(module=slug):
                for page in (*PAGES, "oficina-de-ferramentas.md"):
                    self.assertRegex(text, rf"\[[^]]+\]\({re.escape(page)}\)")

    def test_every_module_links_to_the_applied_workshop(self):
        for slug in MODULES:
            text = (DOCS / slug / "index.md").read_text(encoding="utf-8")
            with self.subTest(module=slug):
                self.assertIn("[Oficina de ferramentas](oficina-de-ferramentas.md)", text)

    def test_modules_five_and_six_end_with_self_assessment_questions(self):
        for slug in ("modulo-5-confianca", "modulo-6-operacao"):
            text = (DOCS / slug / "sintese-e-referencias.md").read_text(encoding="utf-8")
            section = re.search(
                r"(?ms)^## Autoavaliação\s*(.*?)(?=^## |\Z)", text
            )
            with self.subTest(module=slug):
                self.assertIsNotNone(section)
                self.assertGreaterEqual(len(re.findall(r"(?m)^\d+\. .+\?$", section.group(1))), 5)


class PublicExerciseAnswerPolicyTest(unittest.TestCase):
    def test_advanced_sections_have_criteria_but_no_public_answer_blocks(self):
        for slug in MODULES:
            text = (DOCS / slug / "exercicios.md").read_text(encoding="utf-8")
            sections = bloom_sections(text)
            for level in ("Aplicar", "Analisar", "Avaliar", "Criar"):
                body = sections[level]
                with self.subTest(module=slug, level=level):
                    self.assertIn("Critérios de avaliação", body)
                    self.assertNotIn("<details", body.casefold())
                    self.assertNotRegex(body.casefold(), r"resposta\s+(comentada|esperada|correta)")

    def test_advanced_criteria_do_not_reveal_computed_or_canonical_answers(self):
        forbidden = (
            r"recall@\d+\s*=", r"precision@\d+\s*=",
            r"hipótese da primeira reserva ter concluído",
            r"timeout não significa falha",
            r"completed[^.;\n]*incorreto",
        )
        for slug in MODULES:
            text = (DOCS / slug / "exercicios.md").read_text(encoding="utf-8")
            sections = bloom_sections(text)
            advanced = "\n".join(sections[level] for level in ("Aplicar", "Analisar", "Avaliar", "Criar"))
            criteria = "\n".join(
                line for line in advanced.splitlines() if line.startswith("**Critérios de avaliação")
            ).casefold()
            with self.subTest(module=slug):
                for pattern in forbidden:
                    self.assertNotRegex(criteria, pattern)
