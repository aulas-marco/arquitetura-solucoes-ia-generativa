from pathlib import Path
import re
import unittest

from scripts.validate_content import MODULES


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OFFICE = "oficina-de-ferramentas.md"


class AppliedLiteracyTest(unittest.TestCase):
    @staticmethod
    def section(text, heading):
        match = re.search(
            rf"^{re.escape(heading)}\\s*$\\n(?P<body>.*?)(?=^## |\\Z)",
            text,
            flags=re.MULTILINE | re.DOTALL,
        )
        if match is None:
            return None
        return match.group("body").strip()

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

                bloom_lines = re.findall(r"^.*objetivo\s+Bloom.*$", text, flags=re.MULTILINE | re.IGNORECASE)
                self.assertEqual(1, len(bloom_lines), "a oficina deve declarar um único objetivo Bloom")
                bloom_declaration = bloom_lines[0].split(":", maxsplit=1)[-1]
                bloom_declaration = re.sub(r"[*_`]", "", bloom_declaration)
                self.assertRegex(
                    bloom_declaration,
                    r"^\s*(?:Compreender|Aplicar|Analisar)"
                    r"(?:\s*(?:,|e)\s*(?:Compreender|Aplicar|Analisar))*\.?\s*$",
                )

                essential = self.section(text, "### Essencial, sem cartão")
                institutional = self.section(text, "### Institucional")
                commercial = self.section(text, "### Comercial ou avançada")
                activity = self.section(text, "## Atividade guiada")
                evidence = self.section(text, "## Evidência a entregar")
                security_cost = self.section(text, "## Segurança e custo")
                for heading, content in (
                    ("### Essencial, sem cartão", essential),
                    ("### Institucional", institutional),
                    ("### Comercial ou avançada", commercial),
                    ("## Atividade guiada", activity),
                    ("## Evidência a entregar", evidence),
                    ("## Segurança e custo", security_cost),
                ):
                    self.assertTrue(content, f"{heading} deve conter orientação utilizável")

                self.assertIn("não depende de cartão", essential.casefold())
                self.assertRegex(
                    activity,
                    r"(?is)obrigat.ria.*essencial, sem cart.o|essencial, sem cart.o.*obrigat.ria",
                )
                self.assertIn("não depende de cartão", activity.casefold())
                for route_name, route in (
                    ("institucional", institutional),
                    ("comercial", commercial),
                ):
                    self.assertIn(
                        "não acrescenta pontos",
                        route.casefold(),
                        f"a rota {route_name} não pode dar vantagem avaliativa",
                    )

                self.assertRegex(activity, r"(?i)decis.o arquitetural")
                self.assertRegex(activity, r"(?i)evid.ncia")
                self.assertRegex(evidence, r"(?i)atividade")
                self.assertRegex(evidence, r"(?i)seguran.a|custo")
                self.assertRegex(security_cost, r"(?i)decis.o arquitetural")
                self.assertRegex(security_cost, r"(?i)atividade|evid.ncia")

    def test_shared_guide_and_group_project_preserve_equity(self):
        guide = (DOCS / "referencia" / "guia-de-ferramentas.md").read_text(encoding="utf-8").casefold()
        project = (DOCS / "sobre" / "projeto-final.md").read_text(encoding="utf-8").casefold()

        for term in ("sem cartão", "institucional", "comercial", "sdk", "framework", "gateway", "aiaas"):
            self.assertIn(term, guide)
        for term in ("grupo", "duas opções", "evidências", "uso de ferramenta paga não acrescenta pontos"):
            self.assertIn(term, project)
