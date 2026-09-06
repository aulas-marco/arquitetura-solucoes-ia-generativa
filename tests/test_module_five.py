from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "modulo-5-especificacao"


class ModuleFiveContentRegressionTest(unittest.TestCase):
    def test_sdd_is_a_module_not_a_sidebar(self):
        pages = {
            path.name: path.read_text(encoding="utf-8")
            for path in MODULE.glob("*.md")
        }
        combined = "\n".join(pages.values()).casefold()

        for concept in (
            "specification-driven development",
            "constitution",
            "ledger epistemológico",
            "ears",
            "bdd",
            "fatias verticais",
            "módulos profundos",
            "seams",
            "revisão de spec",
            "revisão de standards",
            "gate 1",
            "gate 2",
            "gate 3",
            "feedback de produção",
        ):
            self.assertIn(concept, combined, concept)

        for page in (
            "index.md",
            "modos-de-trabalho.md",
            "fluxo.md",
            "decisoes.md",
            "exemplo-arquitetural.md",
            "oficina-de-ferramentas.md",
            "exercicios.md",
            "sintese-e-referencias.md",
        ):
            folded = pages[page].casefold()
            self.assertTrue(
                "sdd" in folded or "desenvolvimento guiado por especificação" in folded,
                page,
            )

        syllabus = (
            ROOT / "docs" / "sobre" / "plano-da-disciplina.md"
        ).read_text(encoding="utf-8").casefold()
        capstone = (
            ROOT / "docs" / "sobre" / "projeto-final.md"
        ).read_text(encoding="utf-8").casefold()
        for evidence in ("constitution", "spec", "fatias verticais", "gates"):
            self.assertIn(evidence, syllabus, evidence)
            self.assertIn(evidence, capstone, evidence)


    def test_module_has_the_standard_shell_and_its_own_cases(self):
        nomes = {p.name for p in MODULE.glob("*.md")}
        for page in ("index.md", "exemplo-arquitetural.md", "estudo-de-caso.md",
                     "oficina-de-ferramentas.md", "exercicios.md", "sintese-e-referencias.md",
                     "caso-lume.md", "caso-aurora.md",
                     "modos-de-trabalho.md", "fluxo.md", "decisoes.md"):
            self.assertIn(page, nomes)

        navigation = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        ordem = [navigation.index(f"modulo-5-especificacao/{p}")
                 for p in ("index.md", "modos-de-trabalho.md", "fluxo.md", "decisoes.md")]
        self.assertEqual(ordem, sorted(ordem))

        opening = (MODULE / "index.md").read_text(encoding="utf-8")
        self.assertIn("Como uma intenção humana atravessa um sistema de agentes", opening)


if __name__ == "__main__":
    unittest.main()
