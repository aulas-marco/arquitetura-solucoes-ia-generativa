from pathlib import Path
import re
import unittest

from scripts.validate_content import PAGES, bloom_sections


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "modulo-2-desenho-conceitual"

# O Módulo 2 pratica os exercícios logo após o exemplo arquitetural e antes
# da oficina de ferramentas e do estudo de caso de transferência, ao contrário
# da ordem padrão (estudo de caso, oficina, exercícios) usada nos demais módulos.
MODULE_TWO_PAGE_ORDER = (
    "index.md", "conceitos.md", "padroes-e-decisoes.md",
    "exemplo-arquitetural.md", "exercicios.md",
    "oficina-de-ferramentas.md", "estudo-de-caso.md", "sintese-e-referencias.md",
)


class ModuleTwoContentRegressionTest(unittest.TestCase):
    def test_module_has_standard_pages_and_pedagogical_navigation_order(self):
        self.assertEqual(
            set(PAGES) | {"caso-lume.md", "caso-aurora.md"},
            {path.name for path in MODULE.glob("*.md")},
        )

        navigation = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        positions = [
            navigation.index(f"modulo-2-desenho-conceitual/{page}")
            for page in MODULE_TWO_PAGE_ORDER
        ]
        self.assertEqual(positions, sorted(positions))

        opening = (MODULE / "index.md").read_text(encoding="utf-8")
        self.assertIn(
            "Como evitar construir a solução de IA certa para o problema errado?",
            opening,
        )

    def test_architectural_example_keeps_images_diagrams_adrs_and_failure_modes(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        self.assertIn("m02-oportunidade-arquitetura.png", text)
        self.assertIn("| Alternativa | Direcionador atendido |", text)
        self.assertGreaterEqual(text.count("```mermaid"), 2)
        self.assertGreaterEqual(text.count("**Equivalente textual"), 2)
        self.assertIn("### ADR-001", text)
        self.assertIn("### ADR-002", text)
        for failure in (
            "dados sensíveis",
            "indisponibilidade do modelo",
            "resposta sem suporte",
        ):
            self.assertIn(failure, text.casefold())

    def test_architecture_description_taxonomy_is_explicit_and_not_conflated(self):
        concepts = (MODULE / "conceitos.md").read_text(encoding="utf-8")
        decisions = (MODULE / "padroes-e-decisoes.md").read_text(encoding="utf-8")

        for term in (
            "Ponto de vista",
            "Visão",
            "Modelo arquitetural",
            "Cenário de qualidade",
            "ADR",
        ):
            self.assertIn(term, concepts)
        self.assertIn("É memória de decisão, não modelo do sistema.", concepts)
        self.assertIn("| Entrada da análise | Cenário de qualidade |", decisions)
        self.assertIn("| Registro | ADR |", decisions)

    def test_module_covers_five_views_and_correspondence_rules(self):
        concepts = (MODULE / "conceitos.md").read_text(encoding="utf-8")
        example = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        for view in (
            "Contexto",
            "Responsabilidades",
            "Interação",
            "Informação",
            "Implantação",
        ):
            self.assertIn(view, concepts)
            self.assertIn(view, example)
        self.assertIn("Correspondências entre visões", concepts)
        self.assertIn("Correspondências verificadas", example)

    def test_tactics_are_linked_to_quality_tradeoffs_and_evidence(self):
        concepts = (MODULE / "conceitos.md").read_text(encoding="utf-8")
        decisions = (MODULE / "padroes-e-decisoes.md").read_text(encoding="utf-8")
        example = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        for term in (
            "Tática",
            "Mecanismo",
            "Padrão",
            "Estilo arquitetural",
            "Ponto de sensibilidade",
            "Ponto de trade-off",
            "Risco arquitetural",
        ):
            self.assertIn(term, concepts)
        self.assertIn("árvore de utilidade reduzida", decisions.casefold())
        self.assertIn("Árvore de utilidade reduzida", example)
        self.assertIn("Registro de risco e incerteza", example)

    def test_case_compares_all_four_conceptual_directions(self):
        text = (MODULE / "estudo-de-caso.md").read_text(encoding="utf-8").casefold()

        for direction in (
            "automação convencional",
            "copiloto com contexto",
            "rag",
            "agente com ferramentas",
        ):
            self.assertIn(direction, text)
        self.assertIn("revisão humana obrigatória", text)
        self.assertIn("sistemas legados", text)

    def test_exercises_preserve_bloom_counts_and_hybrid_answer_policy(self):
        text = (MODULE / "exercicios.md").read_text(encoding="utf-8")
        sections = bloom_sections(text)
        expected_counts = {
            "Recordar": 4,
            "Compreender": 3,
            "Aplicar": 1,
            "Analisar": 2,
            "Avaliar": 1,
            "Criar": 1,
        }

        for level, expected in expected_counts.items():
            questions = re.findall(r"(?m)^### \d+\.", sections[level])
            self.assertEqual(expected, len(questions), level)

        self.assertEqual(4, sections["Recordar"].count("<details>"))
        self.assertEqual(3, sections["Compreender"].count("<details>"))
        for level in ("Aplicar", "Analisar", "Avaliar", "Criar"):
            self.assertNotIn("<details>", sections[level])
            self.assertIn("**Critérios de avaliação", sections[level])

    def test_registered_sources_cover_module_two_book_chapters_and_rag(self):
        registry = (ROOT / "docs" / "referencia" / "fontes.yml").read_text(
            encoding="utf-8"
        )

        for source_id in (
            "avila-ahmad-chapter-2-local",
            "avila-ahmad-chapter-3-local",
            "avila-ahmad-chapter-4-local",
            "lewis-et-al-rag-2020",
        ):
            entry = re.search(
                rf"- id: {re.escape(source_id)}\n(.*?)(?=\n- id:|\Z)",
                registry,
                re.DOTALL,
            )
            self.assertIsNotNone(entry, source_id)
            self.assertRegex(entry.group(1), r"(?m)^  modules: \[[^]]*\b2\b[^]]*\]$")


if __name__ == "__main__":
    unittest.main()
