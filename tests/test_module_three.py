from pathlib import Path
import re
import unittest

from scripts.validate_content import PAGES, bloom_sections


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "modulo-3-rag"


class ModuleThreeContentRegressionTest(unittest.TestCase):
    def test_module_has_standard_pages_navigation_and_guiding_question(self):
        self.assertEqual(set(PAGES), {path.name for path in MODULE.glob("*.md")})

        navigation = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        positions = [navigation.index(f"modulo-3-rag/{page}") for page in PAGES]
        self.assertEqual(positions, sorted(positions))

        opening = (MODULE / "index.md").read_text(encoding="utf-8")
        self.assertIn(
            "Como conectar um modelo a conhecimento verificável e atualizável?",
            opening,
        )

    def test_patterns_cover_retrieval_authorization_provenance_and_rag_variants(self):
        text = (MODULE / "padroes-e-decisoes.md").read_text(encoding="utf-8").casefold()

        for topic in (
            "busca vetorial",
            "busca lexical",
            "recuperação híbrida",
            "reranking",
            "transformação da consulta",
            "autorização",
            "proveniência",
            "evidência insuficiente",
            "rag básico",
            "rag hierárquico",
            "rag adaptativo",
            "rag corretivo",
            "rag multisource",
            "dados estruturados",
        ):
            self.assertIn(topic, text, topic)

    def test_architectural_example_has_both_images_three_diagrams_and_text_equivalents(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        for image in ("m03-dois-fluxos-rag.png", "m03-pergunta-evidencia.png"):
            self.assertIn(image, text)
        self.assertGreaterEqual(text.count("```mermaid"), 3)
        self.assertIn("sequenceDiagram", text)
        self.assertGreaterEqual(text.count("**Equivalente textual"), 3)
        self.assertIn("fronteira de autorização", text.casefold())

    def test_case_requires_permissions_citations_fast_updates_and_abstention(self):
        text = (MODULE / "estudo-de-caso.md").read_text(encoding="utf-8").casefold()

        for requirement in (
            "permissões por usuário",
            "citações",
            "atualização",
            "abstenção",
            "políticas",
            "contratos",
        ):
            self.assertIn(requirement, text, requirement)

    def test_exercises_preserve_bloom_counts_hybrid_answers_and_required_challenges(self):
        text = (MODULE / "exercicios.md").read_text(encoding="utf-8")
        sections = bloom_sections(text)
        expected_counts = {
            "Recordar": 4,
            "Compreender": 3,
            "Aplicar": 2,
            "Analisar": 1,
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

        exercise_text = text.casefold()
        for challenge in (
            "recall@5",
            "estratégias de chunking",
            "falha de permissão",
            "arquitetura rag completa",
        ):
            self.assertIn(challenge, exercise_text, challenge)

    def test_registered_sources_cover_rag_retrieval_evaluation_and_pipeline_chapters(self):
        registry = (ROOT / "docs" / "referencia" / "fontes.yml").read_text(
            encoding="utf-8"
        )

        for source_id in (
            "lewis-et-al-rag-2020",
            "karpukhin-et-al-dpr-2020",
            "reimers-gurevych-sbert-2019",
            "es-et-al-ragas-2024",
            "avila-ahmad-chapter-5-local",
            "avila-ahmad-chapter-7-local",
        ):
            entry = re.search(
                rf"- id: {re.escape(source_id)}\n(.*?)(?=\n- id:|\Z)",
                registry,
                re.DOTALL,
            )
            self.assertIsNotNone(entry, source_id)
            self.assertRegex(entry.group(1), r"(?m)^  modules: \[[^]]*\b3\b[^]]*\]$")


if __name__ == "__main__":
    unittest.main()
