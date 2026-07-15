from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProjectTest(unittest.TestCase):
    def test_required_project_files_exist(self):
        required = [
            "mkdocs.yml",
            "requirements.txt",
            ".gitignore",
            "docs/index.md",
            "docs/assets/stylesheets/extra.css",
            "scripts/validate_content.py",
        ]
        self.assertEqual([], [name for name in required if not (ROOT / name).exists()])

    def test_validator_help_runs(self):
        result = subprocess.run(
            ["python3", "scripts/validate_content.py", "--help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)


if __name__ == "__main__":
    unittest.main()
