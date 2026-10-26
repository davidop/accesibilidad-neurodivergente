"""Valida SKILL.md contra la especificación Agent Skills (https://agentskills.io/specification).

Si este test falla, la skill puede no cargarse en Claude Code, Codex o Copilot,
así que se comprueba en CI en lugar de confiar en revisiones manuales.
"""

import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
SKILL_DIRS = sorted(p.parent for p in SKILLS_DIR.glob("*/SKILL.md"))


def read_skill(skill_dir: Path):
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.DOTALL)
    assert match, "SKILL.md debe empezar con un bloque frontmatter YAML delimitado por ---"
    return yaml.safe_load(match.group(1)), match.group(2)


def test_there_is_at_least_one_skill():
    assert SKILL_DIRS, "No se ha encontrado ningún skills/*/SKILL.md"


@pytest.mark.parametrize("skill_dir", SKILL_DIRS, ids=lambda p: p.name)
class TestSkill:
    def test_name(self, skill_dir):
        meta, _ = read_skill(skill_dir)
        name = meta.get("name")
        assert isinstance(name, str) and 1 <= len(name) <= 64
        assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name), "solo minúsculas, dígitos y guiones simples"
        assert name == skill_dir.name, "name debe coincidir con el nombre de la carpeta"

    def test_description(self, skill_dir):
        meta, _ = read_skill(skill_dir)
        description = meta.get("description")
        assert isinstance(description, str) and 1 <= len(description.strip()) <= 1024

    def test_optional_fields(self, skill_dir):
        meta, _ = read_skill(skill_dir)
        allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
        assert set(meta) <= allowed, f"campos no estándar: {set(meta) - allowed}"
        if "compatibility" in meta:
            assert isinstance(meta["compatibility"], str) and len(meta["compatibility"]) <= 500
        if "metadata" in meta:
            assert all(isinstance(k, str) and isinstance(v, str) for k, v in meta["metadata"].items()), (
                "metadata debe ser un mapa de cadenas (pon la versión entre comillas)"
            )

    def test_referenced_files_exist(self, skill_dir):
        _, body = read_skill(skill_dir)
        for ref in set(re.findall(r"`((?:scripts|references|assets)/[^`\s]+)`", body)):
            assert (skill_dir / ref).is_file(), f"SKILL.md menciona {ref}, pero no existe"

    def test_version_is_in_changelog(self, skill_dir):
        meta, _ = read_skill(skill_dir)
        version = meta.get("metadata", {}).get("version")
        if version is None:
            pytest.skip("la skill no declara metadata.version")
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        assert f"## [{version}]" in changelog, f"falta la entrada ## [{version}] en CHANGELOG.md"

    def test_version_matches_pyproject(self, skill_dir):
        tomllib = pytest.importorskip("tomllib")
        meta, _ = read_skill(skill_dir)
        pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        assert pyproject["project"]["version"] == meta["metadata"]["version"]
