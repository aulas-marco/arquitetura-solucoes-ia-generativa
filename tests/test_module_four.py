from pathlib import Path
import re
import unittest

from scripts.validate_content import PAGES, bloom_sections, teaching_text, thematic_pages


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "modulo-4-agentes"


class ModuleFourContentRegressionTest(unittest.TestCase):
    def test_module_has_standard_pages_navigation_and_guiding_question(self):
        nomes = {path.name for path in MODULE.glob("*.md")}
        self.assertTrue(set(PAGES) | {"caso-lume.md", "caso-aurora.md"} <= nomes)
        tematicas = thematic_pages(MODULE)
        self.assertGreaterEqual(len(tematicas), 5)

        navigation = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        ordem = [navigation.index(f"modulo-4-agentes/{page}") for page in ("index.md", "exemplo-arquitetural.md", "estudo-de-caso.md",
                     "oficina-de-ferramentas.md", "exercicios.md", "sintese-e-referencias.md")]
        self.assertEqual(ordem, sorted(ordem))
        for page in tematicas:
            self.assertIn(f"modulo-4-agentes/{page}", navigation)

        opening = (MODULE / "index.md").read_text(encoding="utf-8")
        self.assertIn(
            "Quando permitir que o modelo escolha e execute ações?",
            opening,
        )

    def test_concepts_distinguish_interaction_and_control_models(self):
        text = teaching_text(MODULE).casefold()

        for concept in (
            "chatbot",
            "copiloto",
            "workflow determinístico",
            "agente",
            "saída estruturada",
            "planejamento",
            "estado",
            "memória de trabalho",
            "memória persistente",
            "contexto",
            "políticas",
            "agente único",
            "múltiplos agentes",
        ):
            self.assertIn(concept, text, concept)

    def test_patterns_cover_enterprise_integration_and_control_mechanisms(self):
        text = teaching_text(MODULE).casefold()

        for topic in (
            "contrato de ferramenta",
            "api",
            "mensageria",
            "eventos",
            "adaptador",
            "identidade do usuário",
            "autorização delegada",
            "idempotência",
            "timeout",
            "retry",
            "circuit breaker",
            "compensação",
            "auditoria",
            "aprovação humana",
            "workflow determinístico",
            "orçamento de etapas",
            "orçamento de tempo",
            "orçamento de custo",
        ):
            self.assertIn(topic, text, topic)

    def test_architectural_example_has_images_diagrams_and_required_paths(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")
        folded = text.casefold()

        for image in ("m04-agente-ferramentas.png", "m04-fronteiras-autonomia.png"):
            self.assertIn(image, text)
        self.assertGreaterEqual(text.count("```mermaid"), 2)
        self.assertIn("sequenceDiagram", text)
        self.assertGreaterEqual(text.count("**Equivalente textual"), 2)
        for path in (
            "caminho feliz",
            "ação rejeitada",
            "prevenção de chamada repetida",
            "compensação",
        ):
            self.assertIn(path, folded, path)

    def test_sequence_messages_do_not_use_mermaid_statement_separator(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")
        sequence = re.search(r"```mermaid\nsequenceDiagram\n(.*?)```", text, re.DOTALL)

        self.assertIsNotNone(sequence)
        self.assertNotIn(
            ";",
            sequence.group(1),
            "Ponto e vírgula encerra a instrução no parser de sequenceDiagram",
        )

    def test_agent_image_accessibility_and_manifest_close_result_return_path(self):
        example = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")
        manifest = (
            ROOT / "docs" / "assets" / "images" / "prompts.md"
        ).read_text(encoding="utf-8")

        for phrase in (
            "resultados tipados retornam por auditoria e estado ao orquestrador",
            "antes de chegar ao canal",
        ):
            self.assertIn(phrase, example, phrase)

        for phrase in (
            "external systems -> adapters -> audit/state inside control plane -> orchestrator -> authenticated channel",
            "no direct adapter-to-channel shortcut",
            "no result path outside the control plane",
        ):
            self.assertIn(phrase, manifest, phrase)

    def test_component_diagram_returns_typed_adapter_results_to_orchestration(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        self.assertIn('ACRM -- "observação tipada" --> ORQ', text)
        self.assertIn('APED -- "resultado tipado" --> ORQ', text)

    def test_write_timeout_reconciles_authoritatively_before_result_reuse(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        required_sequence = (
            "Marcar K-845-1 como outcome_unknown",
            "Reconciliar K-845-1 no destino",
            "Consultar operação por K-845-1",
            "Confirmar R9 como resultado autoritativo",
            "Persistir completed e resultado R9",
        )
        positions = [text.index(step) for step in required_sequence]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("reconciliation: query destination by idempotency key", text)
        self.assertIn(
            "timeout de escrita persiste `outcome_unknown`",
            text,
        )

    def test_effectful_calls_reenter_deterministic_boundary_after_wait(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        for semantic in (
            "Avaliar identidade, política, parâmetros, pedido v17 e risco",
            "Revalidar identidade, política, aprovação e pedido v17",
            "Persistir intenção confirmar + K-845-2",
            "Executor: confirmar troca, expected=v17, K-845-2",
            "Persistir intenção registrar + K-845-3",
            "Executor: registrar resolução, pedido v18, K-845-3",
            "Persistir compensação C-K-845-1 e estado compensation_pending",
            "Executor: liberar R9, expected=reserva-v1, C-K-845-1",
        ):
            self.assertIn(semantic, text, semantic)

        for bypass in (
            "O->>D: Confirmar troca",
            "O->>R: Registrar resolução",
            "O->>D: Liberar R9",
        ):
            self.assertNotIn(bypass, text, bypass)

    def test_case_discloses_active_reservation_before_exchange_completion(self):
        text = (MODULE / "estudo-de-caso.md").read_text(encoding="utf-8")

        self.assertIn("a troca ainda não está concluída", text)
        self.assertIn("a reserva temporária já pode estar ativa", text)

    def test_exercises_preserve_bloom_policy_and_required_challenges(self):
        text = (MODULE / "exercicios.md").read_text(encoding="utf-8")
        sections = bloom_sections(text)
        expected_counts = {
            "Recordar": 5,
            "Compreender": 4,
            "Aplicar": 2,
            "Analisar": 3,
            "Avaliar": 1,
            "Criar": 1,
        }

        for level, expected in expected_counts.items():
            questions = re.findall(r"(?m)^### \d+\.", sections[level])
            self.assertEqual(expected, len(questions), level)

        self.assertEqual(5, sections["Recordar"].count("<details>"))
        self.assertEqual(4, sections["Compreender"].count("<details>"))
        for level in ("Aplicar", "Analisar", "Avaliar", "Criar"):
            self.assertNotIn("<details>", sections[level])
            self.assertIn("**Critérios de avaliação", sections[level])

        exercise_text = text.casefold()
        for challenge in (
            "seleção de ferramentas",
            "classificação de autonomia",
            "diagnóstico de trace",
            "crítica arquitetural",
            "arquitetura de agente controlado",
            "componentes do arnês",
            "melhoria de robustez no uso de llms",
            "parada por julgamento e parada por critério",
        ):
            self.assertIn(challenge, exercise_text, challenge)

    def test_registered_sources_cover_agents_tools_protocol_and_book_case(self):
        registry = (ROOT / "docs" / "referencia" / "fontes.yml").read_text(
            encoding="utf-8"
        )

        for source_id in (
            "yao-et-al-react-2023",
            "schick-et-al-toolformer-2023",
            "mcp-specification-2025-11-25",
            "opentelemetry-genai-semconv",
            "avila-ahmad-chapter-7-local",
        ):
            entry = re.search(
                rf"- id: {re.escape(source_id)}\n(.*?)(?=\n- id:|\Z)",
                registry,
                re.DOTALL,
            )
            self.assertIsNotNone(entry, source_id)
            self.assertRegex(entry.group(1), r"(?m)^  modules: \[[^]]*\b4\b[^]]*\]$")


if __name__ == "__main__":
    unittest.main()
