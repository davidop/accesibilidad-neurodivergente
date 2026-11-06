"""Comprobaciones documentales de la declaración de accesibilidad."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def test_accessibility_statement_exists_and_is_discoverable():
    statement = (ROOT / "ACCESSIBILITY.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "ACCESSIBILITY.md" in readme
    assert "ACCESSIBILITY.md" in contributing
    for section in (
        "## Compromiso y alcance",
        "## Comprobaciones y entornos",
        "## Limitaciones y alternativas",
        "## Cómo comunicar una barrera",
        "## Qué ocurre después",
        "## Mantenimiento",
    ):
        assert section in statement


def test_accessibility_issue_is_text_based_and_respects_privacy():
    path = ROOT / ".github/ISSUE_TEMPLATE/4-accesibilidad.yml"
    template = yaml.safe_load(path.read_text(encoding="utf-8"))
    fields = template["body"]
    assert any(field.get("type") == "textarea" for field in fields)
    assert all(field.get("type") != "upload" for field in fields)
    assert "neurotipo" in fields[0]["attributes"]["value"]
    assert "issues/new?template=4-accesibilidad.yml" in (ROOT / "ACCESSIBILITY.md").read_text(encoding="utf-8")


def test_skill_documents_accessibility_statement_workflow():
    skill = (ROOT / "skills/accesibilidad-neurodivergente/SKILL.md").read_text(encoding="utf-8")
    guide = ROOT / "skills/accesibilidad-neurodivergente/references/declaracion-accesibilidad.md"
    assert "### D. Declaración de accesibilidad" in skill
    assert guide.is_file()
    assert "WCAG 2.2 AA" in guide.read_text(encoding="utf-8")
