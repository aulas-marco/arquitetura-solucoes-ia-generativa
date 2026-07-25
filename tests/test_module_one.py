from pathlib import Path
import re
import unittest

from scripts.validate_content import bloom_sections


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "modulo-1-fundamentos"


class ModuleOneReviewRegressionTest(unittest.TestCase):
    def test_concepts_follow_the_five_architectural_questions(self):
        text = (MODULE / "conceitos.md").read_text(encoding="utf-8")
        movements = (
            "## O que muda no sistema",
            "## De onde emerge o comportamento",
            "## Que informação atravessa o sistema",
            "## Como distribuir responsabilidade",
            "## Como verificar e governar",
        )

        positions = [text.index(heading) for heading in movements]
        self.assertEqual(positions, sorted(positions))
        for term in (
            "modelo",
            "aplicação",
            "sistema sociotécnico",
            "superfície comportamental",
            "conhecimento",
            "contexto",
            "estado",
            "memória",
            "evidência",
            "trace",
            "geração",
            "decisão",
            "autorização",
            "efeito",
            "Teste de software",
            "Avaliação comportamental",
            "Verificação arquitetural",
            "fitness function",
        ):
            self.assertIn(term.casefold(), text.casefold())

    def test_component_image_and_sequence_diagram_have_distinct_jobs(self):
        patterns = (MODULE / "padroes-e-decisoes.md").read_text(encoding="utf-8")
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        self.assertIn("m01-componentes-dependencias.png", patterns)
        self.assertIn("Equivalente textual — componentes", patterns)
        diagrams = re.findall(r"```mermaid\n(.*?)```", text, re.DOTALL)
        sequence = next(
            (diagram for diagram in diagrams if "sequenceDiagram" in diagram),
            None,
        )
        self.assertIsNotNone(sequence)
        for term in (
            "sequenceDiagram",
            "participant U as Usuário",
            "participant A as Aplicação",
            "participant O as Orquestrador",
            "participant R as Recuperação",
            "participant G as Gateway",
            "participant M as Modelo",
            "Validação",
        ):
            self.assertIn(term, sequence)

    def test_architecture_diagram_returns_typed_tool_results_to_orchestration(self):
        text = (MODULE / "padroes-e-decisoes.md").read_text(encoding="utf-8")

        self.assertIn('T -. "resultado tipado" .-> O', text)

    def test_exercises_keep_four_recall_and_three_comprehension_answers(self):
        text = (MODULE / "exercicios.md").read_text(encoding="utf-8")
        sections = bloom_sections(text)

        self.assertGreaterEqual(sections["Recordar"].count("<details>"), 4)
        self.assertGreaterEqual(sections["Compreender"].count("<details>"), 3)
        self.assertIn("### 4. Parâmetro de geração", sections["Recordar"])
        self.assertNotIn("Identifique duas abordagens", sections["Recordar"])

    def test_module_defines_behavioral_surface_and_three_verification_types(self):
        text = (MODULE / "conceitos.md").read_text(encoding="utf-8")

        self.assertIn("O trabalho do arquiteto", text)
        self.assertIn("Um mapa para orientar a leitura", text)
        self.assertLess(
            text.index("O trabalho do arquiteto"),
            text.index("m01-mapa-comportamento-generativo.png"),
        )
        self.assertIn("Superfície comportamental", text)
        for term in (
            "modelo",
            "parâmetros",
            "prompt",
            "contexto",
            "fontes",
            "ferramentas",
            "políticas",
            "estado",
            "memória",
            "implantação",
        ):
            self.assertIn(term, text.casefold())
        for verification in (
            "Teste de software",
            "Avaliação comportamental",
            "Verificação arquitetural",
            "fitness function",
        ):
            self.assertIn(verification, text)

    def test_module_separates_generation_decision_authorization_and_effect(self):
        concepts = (MODULE / "conceitos.md").read_text(encoding="utf-8")
        patterns = (MODULE / "padroes-e-decisoes.md").read_text(encoding="utf-8")
        example = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        self.assertIn("Geração, decisão, autorização e efeito", concepts)
        for responsibility in ("gera", "decide", "autoriza", "executa"):
            self.assertIn(responsibility, concepts.casefold())
        self.assertIn("Trajetória", patterns)
        self.assertIn("Ação", patterns)
        self.assertIn("proposta de chamado", example)

    def test_reference_is_a_responsibility_map_and_bridges_all_later_modules(self):
        opening = (MODULE / "index.md").read_text(encoding="utf-8")
        patterns = (MODULE / "padroes-e-decisoes.md").read_text(encoding="utf-8")
        example = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        self.assertIn("mapa de responsabilidades", patterns.casefold())
        self.assertNotIn("oito camadas", example.casefold())
        self.assertIn("Exemplo arquitetural: atendimento Horizonte", example)
        for module in range(2, 7):
            self.assertRegex(opening, rf"Módulo {module}\b")

    def test_decisions_page_uses_initial_decision_sheet_not_full_adr(self):
        text = (MODULE / "padroes-e-decisoes.md").read_text(encoding="utf-8")

        self.assertIn("Ficha de decisão inicial", text)
        self.assertNotIn("## ADR preliminar", text)

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
