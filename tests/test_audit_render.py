"""Tests de scripts/audit_render.py.

Los tests de render necesitan Playwright con Chromium instalado
(`uv run playwright install chromium`); si Playwright no está, se omiten.
"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills" / "accesibilidad-neurodivergente" / "scripts" / "audit_render.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def load_module():
    spec = importlib.util.spec_from_file_location("audit_render", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_script(*args):
    # -I igual que en la documentación: el script no debe depender del directorio actual.
    return subprocess.run(
        [sys.executable, "-I", str(SCRIPT), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=120,
    )


class TestToUrl:
    def test_keeps_urls_with_scheme(self):
        to_url = load_module().to_url
        assert to_url("https://example.org/a") == "https://example.org/a"
        assert to_url("file:///tmp/a.html") == "file:///tmp/a.html"

    def test_converts_local_path_to_file_uri(self):
        url = load_module().to_url(str(FIXTURES / "correcta.html"))
        assert url.startswith("file://")
        assert url.endswith("/correcta.html")

    def test_resolves_relative_paths(self, monkeypatch):
        monkeypatch.chdir(FIXTURES)
        assert load_module().to_url("correcta.html").endswith("/fixtures/correcta.html")

    def test_missing_file_raises(self):
        with pytest.raises(FileNotFoundError):
            load_module().to_url(str(FIXTURES / "no-existe.html"))


class TestCli:
    def test_without_arguments_shows_usage(self):
        result = run_script()
        assert result.returncode == 2
        assert "usage" in result.stderr.lower()

    def test_missing_file_fails_cleanly(self):
        result = run_script(str(FIXTURES / "no-existe.html"))
        assert result.returncode == 2
        assert "No existe el archivo" in result.stderr
        assert "Traceback" not in result.stderr


@pytest.fixture(scope="module")
def audits():
    pytest.importorskip("playwright")
    results = {}
    for name in ("con_barreras", "correcta"):
        result = run_script(str(FIXTURES / f"{name}.html"))
        assert result.returncode == 0, result.stderr
        results[name] = json.loads(result.stdout)
    return results


class TestRender:
    def test_detects_barriers(self, audits):
        desktop = audits["con_barreras"]["escritorio_1280x720"]
        assert desktop["lang"] is None
        assert desktop["viewportMeta"] is None
        assert desktop["landmarks"]["main"] == 0
        assert desktop["h1count"] == 0
        assert desktop["images"]["noAlt"] == 1
        assert desktop["focusableWithoutName"] == 2
        assert desktop["autoplayMedia"] == 1
        assert desktop["bodyOverflowHidden"] is True
        assert desktop["text"]["minPx"] == 10
        assert desktop["text"]["under14px"] == desktop["text"]["nodes"]
        assert audits["con_barreras"]["animaciones_activas_con_reduced_motion"] >= 1

    def test_accessible_page_has_no_findings(self, audits):
        for viewport in ("escritorio_1280x720", "movil_390x844"):
            data = audits["correcta"][viewport]
            assert data["lang"] == "es"
            assert data["landmarks"] == {"main": 1, "nav": 1, "header": 1, "footer": 1}
            assert data["h1count"] == 1
            assert data["images"]["noAlt"] == 0
            assert data["focusableWithoutName"] == 0
            assert data["autoplayMedia"] == 0
            assert data["horizontalScroll"] is False
            assert data["bodyOverflowHidden"] is False
            assert data["text"]["under14px"] == 0
            assert data["jsErrors"] == []
        assert audits["correcta"]["animaciones_activas_con_reduced_motion"] == 0
