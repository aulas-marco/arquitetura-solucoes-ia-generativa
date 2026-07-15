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
        self.assertTrue(all(re.fullmatch(r"m0[1-6]-.+\.png", name) for name in filenames))


if __name__ == "__main__":
    unittest.main()
