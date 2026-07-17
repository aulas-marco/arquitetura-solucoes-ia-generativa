from pathlib import Path
import re
import unittest

from scripts.validate_content import PAGES, WORD_RE, bloom_sections


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "modulo-5-confianca"


class ModuleFiveContentRegressionTest(unittest.TestCase):
    def test_module_has_standard_pages_navigation_question_and_word_budget(self):
        self.assertEqual(set(PAGES), {path.name for path in MODULE.glob("*.md")})

        navigation = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        positions = [navigation.index(f"modulo-5-confianca/{page}") for page in PAGES]
        self.assertEqual(positions, sorted(positions))

        opening = (MODULE / "index.md").read_text(encoding="utf-8")
        self.assertIn(
            "Como demonstrar que uma solução generativa é suficientemente confiável para seu contexto?",
            opening,
        )

        word_count = sum(
            len(WORD_RE.findall((MODULE / page).read_text(encoding="utf-8")))
            for page in PAGES
        )
        self.assertGreaterEqual(word_count, 6_000)
        self.assertLessEqual(word_count, 9_400)

    def test_concepts_explain_systemic_trust_risk_and_shared_responsibility(self):
        text = (MODULE / "conceitos.md").read_text(encoding="utf-8").casefold()

        for concept in (
            "confiança sistêmica",
            "risco técnico",
            "risco operacional",
            "risco legal",
            "risco reputacional",
            "rastreabilidade",
            "responsabilidade compartilhada",
            "risco residual",
        ):
            self.assertIn(concept, text, concept)

    def test_patterns_cover_threats_guardrail_layers_and_governance(self):
        text = (MODULE / "padroes-e-decisoes.md").read_text(encoding="utf-8").casefold()

        for threat in (
            "injeção direta de prompt",
            "injeção indireta de prompt",
            "vazamento de contexto",
            "vazamento de segredo",
            "uso indevido de ferramenta",
            "conteúdo recuperado não confiável",
            "manipulação de memória",
            "negação de serviço econômica",
            "cadeia de fornecedores",
        ):
            self.assertIn(threat, text, threat)

        for layer in (
            "camada de entrada",
            "camada de contexto",
            "camada de recuperação",
            "camada de ferramenta",
            "camada de saída",
            "camada de aprovação humana",
        ):
            self.assertIn(layer, text, layer)

        for governance in (
            "minimização",
            "retenção",
            "segregação",
            "catálogo",
            "versionamento",
            "auditoria",
            "política de uso",
        ):
            self.assertIn(governance, text, governance)

    def test_evaluation_is_multidimensional_and_covers_pipeline_risks(self):
        text = (MODULE / "estudo-de-caso.md").read_text(encoding="utf-8").casefold()

        for dimension in (
            "factualidade",
            "relevância",
            "fundamentação",
            "segurança",
            "utilidade",
            "latência",
            "custo",
        ):
            self.assertIn(dimension, text, dimension)

        for evaluation_topic in (
            "verificações determinísticas",
            "critérios humanos",
            "avaliação assistida por modelo",
            "conjunto de referência",
            "casos adversariais",
            "avaliação por componente",
            "avaliação ponta a ponta",
            "regressão",
            "viés do avaliador",
        ):
            self.assertIn(evaluation_topic, text, evaluation_topic)

    def test_architectural_example_has_images_diagrams_and_text_equivalents(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")
        folded = text.casefold()

        for image in ("m05-defesas-profundidade.png", "m05-prisma-avaliacao.png"):
            self.assertIn(image, text)
        self.assertGreaterEqual(text.count("```mermaid"), 2)
        self.assertGreaterEqual(text.count("**Equivalente textual"), 2)
        for path in (
            "conteúdo público",
            "conteúdo restrito",
            "dados pessoais",
            "escalonamento obrigatório",
            "modelo de ameaças em camadas",
            "pipeline de avaliação",
        ):
            self.assertIn(path, folded, path)

    def test_threat_model_closes_tool_result_and_human_resolution_paths(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        for edge in (
            'R -->|"trechos autorizados"| O',
            'T -->|"resultado autorizado"| O',
            'O -->|"contexto mínimo com fontes e resultado"| M',
            'V -->|"escalonamento obrigatório"| H',
            'H -->|"resolução humana"| U',
        ):
            self.assertIn(edge, text, edge)

        self.assertNotIn('R --> M', text)
        self.assertNotIn('V --> H', text)

    def test_evaluation_pipeline_samples_execution_and_calibrates_model_judgment(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        for edge in (
            'X --> SAMP["Amostra estratificada de execuções"]',
            'RUB["Critérios humanos versionados"] --> HJ',
            'SAMP --> HJ["Julgamentos humanos com proveniência"]',
            'J --> AM["Resultados assistidos com proveniência"]',
            'AM --> CAL["Calibração e checagem de viés"]',
            'HJ --> CAL',
            'CAL --> G["Agregação por dimensão e fatia"]',
        ):
            self.assertIn(edge, text, edge)

        self.assertNotIn('H["Critérios humanos calibrados"] --> G', text)
        self.assertNotIn('J --> G', text)

    def test_exercises_preserve_bloom_policy_and_required_challenges(self):
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
            "identificação de ameaças",
            "mapeamento de controles",
            "critérios de avaliação",
            "julgamento de risco residual",
            "arquitetura de confiança",
        ):
            self.assertIn(challenge, exercise_text, challenge)

    def test_registered_sources_cover_risk_security_evaluation_and_case(self):
        registry = (ROOT / "docs" / "referencia" / "fontes.yml").read_text(
            encoding="utf-8"
        )

        for source_id in (
            "nist-ai-rmf-1-0-2023",
            "nist-genai-profile-2024",
            "nist-ssdf-genai-2024",
            "owasp-llm-top-10-2025",
            "liang-et-al-helm-2023",
            "es-et-al-ragas-2024",
            "liu-et-al-geval-2023",
            "avila-ahmad-chapter-7-local",
        ):
            entry = re.search(
                rf"- id: {re.escape(source_id)}\n(.*?)(?=\n- id:|\Z)",
                registry,
                re.DOTALL,
            )
            self.assertIsNotNone(entry, source_id)
            self.assertRegex(entry.group(1), r"(?m)^  modules: \[[^]]*\b5\b[^]]*\]$")


if __name__ == "__main__":
    unittest.main()
