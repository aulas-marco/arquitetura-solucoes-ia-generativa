from pathlib import Path
import re
import unittest

from scripts.validate_content import bloom_sections


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "modulo-1-fundamentos"


class ModuleOneReviewRegressionTest(unittest.TestCase):
    def test_architecture_diagram_has_one_transversal_layer_eight(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")
        diagram = re.search(r"```mermaid\n(.*?)```", text, re.DOTALL)

        self.assertIsNotNone(diagram)
        self.assertEqual(1, diagram.group(1).count('["8.'))
        self.assertIn('["8. Segurança, governança e observabilidade"]', diagram.group(1))

    def test_architecture_diagram_returns_typed_tool_results_to_orchestration(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        self.assertIn('T -. "resultado tipado" .-> O', text)

    def test_exercises_keep_four_recall_and_three_comprehension_answers(self):
        text = (MODULE / "exercicios.md").read_text(encoding="utf-8")
        sections = bloom_sections(text)

        self.assertGreaterEqual(sections["Recordar"].count("<details>"), 4)
        self.assertGreaterEqual(sections["Compreender"].count("<details>"), 3)
        self.assertIn("### 4. Parâmetro de geração", sections["Recordar"])
        self.assertNotIn("Identifique duas abordagens", sections["Recordar"])

    def test_transformer_description_distinguishes_self_attention_and_scalability(self):
        text = (MODULE / "conceitos.md").read_text(encoding="utf-8")

        self.assertIn("autoatenção", text)
        self.assertIn("sem recorrer a redes recorrentes ou convolucionais", text)
        self.assertIn("paralelismo", text)
        self.assertIn("escalabilidade", text)

    def test_lewis_registry_entry_includes_module_one(self):
        text = (ROOT / "docs" / "referencia" / "fontes.yml").read_text(encoding="utf-8")
        entry = re.search(
            r"- id: lewis-et-al-rag-2020\n(.*?)(?=\n- id:|\Z)",
            text,
            re.DOTALL,
        )

        self.assertIsNotNone(entry)
        self.assertRegex(entry.group(1), r"(?m)^  modules: \[[^]]*\b1\b[^]]*\]$")
        bibliography = (ROOT / "docs" / "referencia" / "bibliografia.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("(`lewis-et-al-rag-2020`)", bibliography)


if __name__ == "__main__":
    unittest.main()
