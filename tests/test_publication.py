from pathlib import Path
import re
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
WORKFLOW = ROOT / ".github" / "workflows" / "publicar-site.yml"


class PublicationHandoffTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme = README.read_text(encoding="utf-8")
        cls.workflow_text = WORKFLOW.read_text(encoding="utf-8")
        cls.workflow = yaml.load(cls.workflow_text, Loader=yaml.BaseLoader)
        cls.mkdocs = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    def test_readme_covers_local_preview_publication_and_private_material(self):
        expected = [
            "python3 -m venv .venv",
            "pip install -r requirements.txt",
            "mkdocs serve",
            "mkdocs build --strict",
            "Settings → Pages",
            "GitHub Actions",
            "material-professor/",
            "Nenhuma licença",
        ]
        for marker in expected:
            with self.subTest(marker=marker):
                self.assertIn(marker, self.readme)

    def test_every_local_markdown_link_in_readme_exists(self):
        links = re.findall(r"\[[^]]+\]\(([^)]+)\)", self.readme)
        local_links = [
            target.split("#", 1)[0]
            for target in links
            if not target.startswith(("http://", "https://", "mailto:"))
        ]
        missing = [target for target in local_links if not (ROOT / target).exists()]
        self.assertEqual([], missing)

    def test_workflow_has_required_triggers_permissions_and_concurrency(self):
        self.assertEqual(["main"], self.workflow["on"]["push"]["branches"])
        self.assertIn("workflow_dispatch", self.workflow["on"])
        self.assertEqual(
            {"contents": "read", "pages": "write", "id-token": "write"},
            self.workflow["permissions"],
        )
        self.assertEqual("pages", self.workflow["concurrency"]["group"])

    def test_workflow_uses_pinned_pages_actions_and_strict_build(self):
        required = [
            "actions/checkout@v4",
            "actions/setup-python@v5",
            "pip install -r requirements.txt",
            "mkdocs build --strict",
            "actions/configure-pages@v5",
            "actions/upload-pages-artifact@v3",
            "actions/deploy-pages@v4",
        ]
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow_text)
        self.assertEqual("site", self._upload_step()["with"]["path"])

    def test_deployment_uses_github_pages_environment(self):
        deploy = self.workflow["jobs"]["deploy"]
        self.assertEqual("build", deploy["needs"])
        self.assertEqual("github-pages", deploy["environment"]["name"])
        self.assertEqual(
            "${{ steps.deployment.outputs.page_url }}",
            deploy["environment"]["url"],
        )

    def test_configuration_remains_portable(self):
        active_lines = [
            line for line in self.mkdocs.splitlines() if not line.lstrip().startswith("#")
        ]
        self.assertFalse(any(line.startswith("site_url:") for line in active_lines))
        self.assertIn("use_directory_urls: true", active_lines)
        self.assertNotIn("secrets.", self.workflow_text.lower())
        self.assertNotIn("github_token", self.workflow_text.lower())

    def _upload_step(self):
        steps = self.workflow["jobs"]["build"]["steps"]
        return next(
            step
            for step in steps
            if step.get("uses") == "actions/upload-pages-artifact@v3"
        )


if __name__ == "__main__":
    unittest.main()
