from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PLAN_TARGET = "plano-da-disciplina.md"


def third_level_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^### (.+)$", text, re.MULTILINE))
    return {
        match.group(1): text[match.end() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        for index, match in enumerate(matches)
    }


class SharedPageStructureTest(unittest.TestCase):
    def test_required_shared_pages_exist(self):
        required = (
            "comecar/sobre-a-disciplina.md",
            "comecar/como-usar.md",
            "comecar/mapa-de-aprendizagem.md",
            "comecar/taxonomia-de-bloom.md",
            "referencia/glossario.md",
            "referencia/catalogo-de-padroes.md",
            "referencia/atributos-de-qualidade.md",
            "referencia/template-adr.md",
            "sobre/plano-da-disciplina.md",
        )

        self.assertEqual([], [path for path in required if not (DOCS / path).is_file()])

    def test_glossary_has_at_least_sixty_entries_linked_to_first_module(self):
        text = (DOCS / "referencia/glossario.md").read_text(encoding="utf-8")
        entries = third_level_sections(text)

        self.assertGreaterEqual(len(entries), 60)
        for term, body in entries.items():
            with self.subTest(term=term):
                link = re.search(
                    rf"\*Primeiro módulo:\* \[Módulo ([1-6])[^]]*\]"
                    rf"\(\.\./sobre/{PLAN_TARGET}#modulo-([1-6])\)",
                    body,
                )
                self.assertIsNotNone(link)
                self.assertEqual(link.group(1), link.group(2))

    def test_pattern_catalog_has_five_groups_and_at_least_eighteen_complete_patterns(self):
        text = (DOCS / "referencia/catalogo-de-padroes.md").read_text(encoding="utf-8")
        for group in ("Geração", "Conhecimento", "Orquestração", "Confiança", "Operações"):
            self.assertIn(f"## {group}", text)

        patterns = third_level_sections(text)
        self.assertGreaterEqual(len(patterns), 18)
        for name, body in patterns.items():
            with self.subTest(pattern=name):
                for field in (
                    "**Contexto.**",
                    "**Problema.**",
                    "**Solução.**",
                    "**Consequências.**",
                    "**Módulos relacionados.**",
                ):
                    self.assertIn(field, body)

    def test_quality_catalog_has_eleven_six_part_scenarios(self):
        text = (DOCS / "referencia/atributos-de-qualidade.md").read_text(encoding="utf-8")
        expected = {
            "Qualidade",
            "Fundamentação (grounding)",
            "Latência",
            "Custo",
            "Privacidade",
            "Segurança",
            "Confiabilidade",
            "Observabilidade",
            "Explicabilidade",
            "Manutenibilidade",
            "Autonomia",
        }
        headings = list(re.finditer(r"^## (.+)$", text, re.MULTILINE))
        scenarios = {
            heading.group(1): text[
                heading.end() : headings[index + 1].start() if index + 1 < len(headings) else len(text)
            ]
            for index, heading in enumerate(headings)
            if heading.group(1) in expected
        }

        self.assertEqual(expected, set(scenarios))
        for attribute, body in scenarios.items():
            with self.subTest(attribute=attribute):
                for part in ("Fonte", "Estímulo", "Ambiente", "Artefato", "Resposta", "Medida"):
                    self.assertEqual(1, body.count(f"**{part}:**"))


class StableModuleLinkTest(unittest.TestCase):
    def test_curriculum_exposes_six_stable_module_anchors(self):
        text = (DOCS / "sobre/plano-da-disciplina.md").read_text(encoding="utf-8")
        headings = (
            "Fundamentos de sistemas com IA generativa",
            "Desenho conceitual e decisões arquiteturais",
            "Arquitetura de RAG e sistemas de conhecimento",
            "Agentes e integração com sistemas corporativos",
            "Confiança, segurança, avaliação e governança",
            "Operação, LLMOps e plataformas corporativas",
        )
        for module, heading in enumerate(headings, start=1):
            anchor_and_heading = (
                f'<a id="modulo-{module}"></a>\n\n'
                f"## Encontro {module} — {heading}"
            )
            self.assertEqual(1, text.count(anchor_and_heading))

    def test_shared_module_links_use_only_stable_targets(self):
        targets = {
            1: (DOCS / "index.md", "sobre/plano-da-disciplina.md#modulo-"),
            2: (DOCS / "referencia/glossario.md", "../sobre/plano-da-disciplina.md#modulo-"),
            3: (DOCS / "referencia/catalogo-de-padroes.md", "../sobre/plano-da-disciplina.md#modulo-"),
        }
        for _, (path, prefix) in targets.items():
            text = path.read_text(encoding="utf-8")
            self.assertNotIn(f"{PLAN_TARGET}#encontro-", text)
            for module in range(1, 7):
                with self.subTest(path=path.name, module=module):
                    self.assertIn(f"{prefix}{module}", text)

    def test_panorama_terms_first_appear_in_module_one(self):
        text = (DOCS / "referencia/glossario.md").read_text(encoding="utf-8")
        entries = third_level_sections(text)
        terms = (
            "Agente",
            "Autonomia",
            "Avaliação",
            "Ferramenta",
            "Fundamentação (grounding)",
            "Governança",
            "Memória",
            "Observabilidade",
            "RAG",
            "Workflow com LLM",
        )

        for term in terms:
            with self.subTest(term=term):
                self.assertIn(
                    f"[Módulo 1 — Fundamentos](../sobre/{PLAN_TARGET}#modulo-1)",
                    entries[term],
                )


if __name__ == "__main__":
    unittest.main()
