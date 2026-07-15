from pathlib import Path
import re
import unittest

from scripts.validate_content import PAGES, WORD_RE, bloom_sections


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "modulo-6-operacao"


class ModuleSixContentRegressionTest(unittest.TestCase):
    def test_module_has_standard_pages_navigation_question_and_word_budget(self):
        self.assertEqual(set(PAGES), {path.name for path in MODULE.glob("*.md")})

        navigation = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        positions = [navigation.index(f"modulo-6-operacao/{page}") for page in PAGES]
        self.assertEqual(positions, sorted(positions))

        opening = (MODULE / "index.md").read_text(encoding="utf-8")
        self.assertIn(
            "Como manter qualidade e controle quando modelos, prompts, dados e ferramentas mudam continuamente?",
            opening,
        )

        word_count = sum(
            len(WORD_RE.findall((MODULE / page).read_text(encoding="utf-8")))
            for page in PAGES
        )
        self.assertGreaterEqual(word_count, 6_000)
        self.assertLessEqual(word_count, 8_000)

    def test_concepts_cover_reproducible_lifecycle_and_observability_layers(self):
        text = (MODULE / "conceitos.md").read_text(encoding="utf-8").casefold()

        for concept in (
            "desenvolvimento",
            "homologação",
            "produção",
            "ativo comportamental",
            "reprodutibilidade",
            "avaliação contínua",
            "entrega controlada",
            "prompt",
            "contexto",
            "recuperação",
            "ferramenta",
            "resposta",
            "produto",
            "modelo",
            "operação",
            "negócio",
            "latência",
            "tokens",
            "erros",
            "custo",
            "logs com preservação de privacidade",
            "slo",
        ):
            self.assertIn(concept, text, concept)

    def test_patterns_cover_delivery_recovery_and_enterprise_platform_tradeoffs(self):
        text = (MODULE / "padroes-e-decisoes.md").read_text(encoding="utf-8").casefold()

        for topic in (
            "portão de regressão",
            "canary",
            "roteamento",
            "fallback",
            "rollback",
            "degradação",
            "resposta a incidente",
            "model gateway",
            "serviço compartilhado de prompts",
            "serviço compartilhado de rag",
            "serviço compartilhado de ferramentas",
            "serviço compartilhado de guardrails",
            "catálogo de modelos",
            "identidade",
            "tenancy",
            "política",
            "portabilidade",
            "estratégia multimodelo",
            "reuso",
            "acoplamento",
            "equipe de plataforma",
            "equipe de produto",
            "cotas",
            "showback",
            "chargeback",
        ):
            self.assertIn(topic, text, topic)

    def test_architectural_example_has_images_diagrams_ownership_and_containment(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")
        folded = text.casefold()

        for image in ("m06-ciclo-llmops.png", "m06-plataforma-corporativa.png"):
            self.assertIn(image, text)
        self.assertGreaterEqual(text.count("```mermaid"), 2)
        self.assertGreaterEqual(text.count("**Equivalente textual"), 2)
        for topic in (
            "arquitetura completa da plataforma",
            "ciclo de entrega e observação",
            "fronteiras de propriedade",
            "contenção de falhas",
            "equipe de plataforma",
            "equipes de produto",
            "segurança e privacidade",
            "operação",
            "dono do processo",
        ):
            self.assertIn(topic, folded, topic)

    def test_platform_diagram_closes_request_retrieval_model_response_and_tool_paths(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        for edge in (
            'P --> ID["Identidade, tenant e quotas"]',
            'GW1 -->|"requisição admitida"| GI["Guardrail de entrada"]',
            'GI --> ORQ["Orquestrador do produto"]',
            'RG -->|"evidências autorizadas"| ORQ',
            'ORQ -->|"prompt + contexto mínimo"| MC["Conector de inferência do gateway"]',
            'M1 -->|"resposta ou intenção estruturada"| GO["Guardrail de saída e validação"]',
            'GO -->|"resposta validada"| P',
            'GO -->|"intenção de ferramenta validada"| TL',
            'TL -->|"após política e aprovação quando exigida"| ERP',
            'TL -->|"resultado autoritativo"| ORQ',
        ):
            self.assertIn(edge, text, edge)

        self.assertNotIn('GW --> GR', text)
        self.assertNotIn('GR --> RG', text)

    def test_gateway_failure_has_replica_failover_equivalent_bypass_and_bounded_degradation(self):
        example = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")
        patterns = (MODULE / "padroes-e-decisoes.md").read_text(
            encoding="utf-8"
        ).casefold()

        for edge in (
            'HE -->|"saudável"| GW1["Gateway — região A"]',
            'HE -->|"health failover"| GW2["Gateway — região B"]',
            'HE -.->|"bypass temporário pré-autorizado"| EC["Edge contingencial com controles equivalentes"]',
            'HE -->|"sem caminho seguro"| DEG["Degradação específica por produto"]',
        ):
            self.assertIn(edge, example, edge)

        for phrase in (
            "domínios de falha",
            "controles equivalentes",
            "prazo curto",
            "raio de impacto",
            "busca oficial",
            "suspende escrita",
        ):
            self.assertIn(phrase, patterns, phrase)

    def test_canary_stop_is_classified_before_incident_response(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        for edge in (
            'K -->|"critério de parada"| CL{"Impacto, guardrail crítico ou severidade?"}',
            'CL -->|"não"| SS["Parada segura + rollback ou degradação"]',
            'SS --> DA["Diagnóstico da hipótese ou qualidade"]',
            'CL -->|"sim"| I["Incidente + evidência minimizada"]',
        ):
            self.assertIn(edge, text, edge)

        self.assertNotIn('RB --> I', text)
        self.assertIn(
            "falha esperada de hipótese ou qualidade não abre automaticamente um incidente",
            text.casefold(),
        )

    def test_llmops_image_alt_separates_routine_rollback_from_true_incident(self):
        text = (MODULE / "exemplo-arquitetural.md").read_text(encoding="utf-8")

        rollback = "rollback seguro rotineiro"
        incident = "incidente real classificado"
        self.assertIn(rollback, text)
        self.assertIn(incident, text)
        self.assertLess(text.index(rollback), text.index(incident))

    def test_retrieval_trace_defaults_to_metadata_and_raw_query_requires_controlled_sample(self):
        text = (MODULE / "conceitos.md").read_text(encoding="utf-8").casefold()

        for phrase in (
            "por padrão, o span de recuperação registra classificação",
            "tamanho",
            "identificador controlado ou hash",
            "metadados de recuperação",
            "consulta derivada em texto bruto",
            "amostra explicitamente autorizada",
            "segregada",
            "retenção limitada",
        ):
            self.assertIn(phrase, text, phrase)

    def test_case_integrates_fragmented_prototypes_and_operational_decisions(self):
        text = (MODULE / "estudo-de-caso.md").read_text(encoding="utf-8").casefold()

        for topic in (
            "copiloto",
            "rag",
            "agente",
            "componentes duplicados",
            "fornecedores incompatíveis",
            "rastreabilidade",
            "custo",
            "adr",
            "risco residual",
            "experimento",
        ):
            self.assertIn(topic, text, topic)

    def test_exercises_preserve_bloom_policy_and_capstone_scope(self):
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
            self.assertIn("**Rubrica", sections[level])

        create = sections["Criar"].casefold()
        for deliverable in (
            "contexto",
            "atributos de qualidade",
            "componentes",
            "fluxos",
            "adrs",
            "guardrails",
            "avaliação",
            "operações",
            "riscos residuais",
            "experimentos",
        ):
            self.assertIn(deliverable, create, deliverable)

    def test_synthesis_closes_course_and_has_production_readiness_checklist(self):
        text = (MODULE / "sintese-e-referencias.md").read_text(encoding="utf-8").casefold()
        self.assertIn("módulo 1", text)
        self.assertIn("módulo 2", text)
        self.assertIn("módulo 3", text)
        self.assertIn("módulo 4", text)
        self.assertIn("módulo 5", text)
        self.assertIn("checklist de prontidão para produção", text)
        self.assertGreaterEqual(text.count("- [ ]"), 12)
        self.assertIn("prática viva", text)

    def test_registered_sources_cover_operations_platform_and_course_case(self):
        registry = (ROOT / "docs" / "referencia" / "fontes.yml").read_text(
            encoding="utf-8"
        )

        for source_id in (
            "sculley-et-al-technical-debt-2015",
            "opentelemetry-semconv-1-43",
            "opentelemetry-genai-semconv",
            "google-sre-slos-2016",
            "dora-delivery-metrics-2026",
            "nist-ai-rmf-1-0-2023",
            "nist-ssdf-genai-2024",
            "avila-ahmad-chapter-7-local",
        ):
            entry = re.search(
                rf"- id: {re.escape(source_id)}\n(.*?)(?=\n- id:|\Z)",
                registry,
                re.DOTALL,
            )
            self.assertIsNotNone(entry, source_id)
            self.assertRegex(entry.group(1), r"(?m)^  modules: \[[^]]*\b6\b[^]]*\]$")


if __name__ == "__main__":
    unittest.main()
