import json
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
        level = len(heading) - len(heading.lstrip("#"))
        match = re.search(
            rf"^{re.escape(heading)}[ \t]*\r?$\n(?P<body>.*?)(?=^#{{1,{level}}}[ \t]|\Z)",
            text,
            flags=re.MULTILINE | re.DOTALL,
        )
        if match is None:
            return None
        return match.group("body").strip()

    def test_section_stops_at_a_heading_of_the_same_or_higher_level(self):
        text = """### Essencial, sem cartão
conteúdo essencial
### Institucional
conteúdo institucional
## Atividade guiada
conteúdo da atividade
"""

        self.assertEqual("conteúdo essencial", self.section(text, "### Essencial, sem cartão"))
        self.assertEqual("conteúdo institucional", self.section(text, "### Institucional"))

    def test_module_one_workshop_is_an_exploratory_ollama_lab(self):
        text = (DOCS / "modulo-1-fundamentos" / OFFICE).read_text(encoding="utf-8")
        self.assertIn("## Ferramenta", text)
        self.assertIn("**Ollama**", text)
        self.assertNotIn("Essencial, sem cartão", text)
        for command in ("ollama --version", "ollama pull llama3.2:3b", "ollama run llama3.2:3b", "ollama rm llama3.2:3b"):
            self.assertIn(command, text)
        for label in ("Essencial em aula", "Exploração em dupla", "Extensão"):
            self.assertIn(label, text)
        for experiment in ("Experimento A", "Experimento B", "Experimento C", "Experimento D"):
            self.assertIn(experiment, text)
        for prompt in ("Objetivo", "Pré-requisito", "Execute", "Observe", "Compare", "Questões exploratórias"):
            self.assertGreaterEqual(text.count(prompt), 4)
        for term in ("modelo", "inferência", "prompt", "corpus", "contexto", "fundamentação", "alucinação"):
            self.assertRegex(text.casefold(), rf"\[{term}[^]]*\]\([^)]*\)")

    def test_module_one_temperature_experiment_uses_the_local_ollama_api(self):
        text = (DOCS / "modulo-1-fundamentos" / OFFICE).read_text(encoding="utf-8")
        experiment = self.section(text, "## Experimento D — compare temperaturas pela API local")

        self.assertIsNotNone(experiment)
        self.assertIn("http://localhost:11434/api/generate", experiment)
        self.assertEqual(2, experiment.count("curl"))
        self.assertIn('"temperature": 0.1', experiment)
        self.assertIn('"temperature": 0.9', experiment)
        payloads = [
            json.loads(payload)
            for payload in re.findall(r"-d '(\{.*?\})'", experiment, flags=re.DOTALL)
        ]
        self.assertEqual(2, len(payloads))
        lower_temperature, higher_temperature = payloads
        self.assertEqual(0.1, lower_temperature.pop("options").pop("temperature"))
        self.assertEqual(0.9, higher_temperature.pop("options").pop("temperature"))
        self.assertEqual(lower_temperature, higher_temperature)
        self.assertIn("diversidade", experiment.casefold())
        self.assertIn("fundamentação", experiment.casefold())
        self.assertIn("correção", experiment.casefold())
        self.assertRegex(experiment, r"(?i)temperatura.*n.o.*prova.*factualidade")
        self.assertIn("Questões exploratórias", experiment)

    def test_every_workshop_is_a_local_executable_lab(self):
        forbidden = re.compile(
            r"cart[ãa]o|crédito|cobrança|sem cart[ãa]o|rota comercial|rota institucional",
            re.IGNORECASE,
        )
        required = (
            "## Ferramenta",
            "## Pré-requisitos",
            "## Instalação",
            "## Preparação do laboratório",
            "## Execução",
            "## Resultado esperado",
            "## Interpretação",
            "## Limpeza e contingência",
            "## Evidência a entregar",
        )
        for slug in MODULES:
            text = (DOCS / slug / OFFICE).read_text(encoding="utf-8")
            with self.subTest(module=slug):
                for marker in required:
                    self.assertIn(marker, text)
                self.assertRegex(text, r"(?m)^```bash$")
                self.assertIsNone(forbidden.search(text), "linguagem de acesso antiga")
                bloom_lines = re.findall(
                    r"^.*objetivo\s+Bloom.*$", text, flags=re.MULTILINE | re.IGNORECASE
                )
                self.assertEqual(1, len(bloom_lines), "a oficina deve declarar um único objetivo Bloom")

    def test_module_two_uses_litellm_proxy_and_a_versioned_manifest(self):
        text = (DOCS / "modulo-2-desenho-conceitual" / OFFICE).read_text(encoding="utf-8")
        for term in (
            "LiteLLM Proxy",
            "Ollama",
            "litellm_config.yaml",
            "boreal-local",
            "localhost:4000",
            "curl",
            "troca controlada",
        ):
            self.assertIn(term, text)

    def test_module_three_provides_files_ingestion_retrieval_and_abstention(self):
        text = (DOCS / "modulo-3-rag" / OFFICE).read_text(encoding="utf-8")
        for term in (
            "LangChain",
            "Chroma",
            "politica-reembolso.txt",
            "rag_local.py",
            "chroma-boreal",
            "POL-17:v3",
            "revisão humana",
        ):
            self.assertIn(term, text)

    def test_modules_two_to_six_offer_selectable_exploratory_experiments(self):
        for slug in (slug for slug in MODULES if slug != "modulo-1-fundamentos"):
            text = (DOCS / slug / OFFICE).read_text(encoding="utf-8")
            with self.subTest(module=slug):
                self.assertIn("## Roteiro sugerido para aula", text)
                for label in ("Essencial em aula", "Exploração em dupla", "Extensão"):
                    self.assertIn(label, text)
                for experiment in ("Experimento A", "Experimento B", "Experimento C"):
                    self.assertIn(experiment, text)
                self.assertGreaterEqual(text.count("Questões exploratórias"), 3)

    def test_shared_guide_and_group_project_prioritize_local_evidence(self):
        guide = (DOCS / "referencia" / "guia-de-ferramentas.md").read_text(encoding="utf-8").casefold()
        project = (DOCS / "sobre" / "projeto-final.md").read_text(encoding="utf-8").casefold()

        for term in ("local", "open source", "framework", "gateway", "ollama"):
            self.assertIn(term, guide)
        for term in ("grupo", "evidências", "ferramenta", "reproduzível"):
            self.assertIn(term, project)

    def test_concepts_and_workshops_name_tools_and_reproducible_steps(self):
        expected_tools = {
            "modulo-1-fundamentos": ("Ollama", "LM Studio"),
            "modulo-2-desenho-conceitual": ("LiteLLM", "OpenAI SDK"),
            "modulo-3-rag": ("LangChain", "Chroma"),
            "modulo-4-agentes": ("n8n", "LangGraph"),
            "modulo-5-confianca": ("Langfuse", "Phoenix"),
            "modulo-6-operacao": ("LiteLLM Proxy", "OpenTelemetry"),
        }
        for slug, tools in expected_tools.items():
            concepts = (DOCS / slug / "conceitos.md").read_text(encoding="utf-8")
            workshop = (DOCS / slug / OFFICE).read_text(encoding="utf-8")

            self.assertIn("## Ferramentas no mercado", concepts)
            for tool in tools:
                self.assertIn(tool, concepts)
            if slug != "modulo-1-fundamentos":
                for heading in (
                    "## Receita principal",
                    "## Pré-requisitos",
                    "## Resultado esperado",
                    "## Limpeza e contingência",
                ):
                    self.assertIn(heading, workshop)
            self.assertRegex(workshop, r"(?m)^\s*```(?:bash|yaml|json)$")
