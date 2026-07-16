from pathlib import Path
import re
import unittest

from scripts.validate_content import MODULES


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OFFICE = "oficina-de-ferramentas.md"


class AppliedLiteracyTest(unittest.TestCase):
    def test_every_module_has_an_accessible_tool_workshop(self):
        required = (
            "## Decisão arquitetural em foco",
            "## Roteiros equivalentes de acesso",
            "Essencial, sem cartão",
            "Institucional",
            "Comercial ou avançada",
            "## Atividade guiada",
            "## Evidência a entregar",
            "## Segurança e custo",
        )
        for slug in MODULES:
            text = (DOCS / slug / OFFICE).read_text(encoding="utf-8")
            with self.subTest(module=slug):
                for marker in required:
                    self.assertIn(marker, text)
                self.assertRegex(text, r"Bloom[^\n]*(Compreender|Aplicar|Analisar)")
                self.assertNotRegex(text, r"Bloom[^\n]*(Avaliar|Criar)")
                self.assertIn("não depende de cartão", text.casefold())

    def test_shared_guide_and_group_project_preserve_equity(self):
        guide = (DOCS / "referencia" / "guia-de-ferramentas.md").read_text(encoding="utf-8").casefold()
        project = (DOCS / "sobre" / "projeto-final.md").read_text(encoding="utf-8").casefold()

        for term in ("sem cartão", "institucional", "comercial", "sdk", "framework", "gateway", "aiaas"):
            self.assertIn(term, guide)
        for term in ("grupo", "duas opções", "evidências", "uso de ferramenta paga não acrescenta pontos"):
            self.assertIn(term, project)
