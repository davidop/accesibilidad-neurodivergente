#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["playwright"]
# ///
"""Auditoría rápida de un HTML renderizado (archivo local o URL) con Playwright.

Uso: python3 -I audit_render.py <ruta-o-url>
     (en Windows: python -I audit_render.py <ruta-o-url>)

Mide lo que no se ve leyendo el código fuente: DOM final tras JavaScript, tamaños
de texto reales, elementos enfocables, regiones aria-live, landmarks, cabeceras
y comportamiento a 390 px de ancho (reflujo / zoom forzado / scroll horizontal).
No sustituye a un lector de pantalla ni a pruebas con personas usuarias.
"""

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

JS = """() => {
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
  let small = 0, total = 0, min = null;
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (w.nextNode()) { const n = w.currentNode, p = n.parentElement;
    if (!n.nodeValue.trim() || !p || !vis(p) || ['SCRIPT','STYLE'].includes(p.tagName)) continue;
    const sc = p.offsetWidth ? p.getBoundingClientRect().width / p.offsetWidth : 1;  // detecta transform: scale()
    const fs = parseFloat(getComputedStyle(p).fontSize) * (sc || 1); total++;
    if (fs < 14) small++; if (min === null || fs < min) min = fs; }
  const heads = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(vis)
    .map(h => h.tagName + ': ' + h.innerText.replace(/\\s+/g, ' ').slice(0, 60));
  const imgs = [...document.images];
  const focus = [...document.querySelectorAll('a[href],button,input:not([type=hidden]),select,textarea,[tabindex]:not([tabindex="-1"])')].filter(vis);
  // Aproximación al nombre accesible: no implementa el algoritmo completo de accname.
  const named = e => e.getAttribute('aria-label') || e.getAttribute('aria-labelledby') || e.innerText.trim()
    || e.getAttribute('title') || (e.labels && e.labels.length) || e.querySelector('img[alt]:not([alt=""])')
    || (e.tagName === 'INPUT' && ['submit','button','reset'].includes(e.type) && e.value);
  return {
    lang: document.documentElement.lang || null,
    title: document.title,
    viewportMeta: (document.querySelector('meta[name=viewport]') || {}).content || null,
    landmarks: ['main','nav','header','footer'].reduce((o,k)=>(o[k]=document.querySelectorAll(k+',[role='+k+']').length,o),{}),
    headings: heads.slice(0, 40), h1count: heads.filter(h => h.startsWith('H1')).length,
    images: { total: imgs.length, noAlt: imgs.filter(i => !i.hasAttribute('alt')).length, emptyAlt: imgs.filter(i => i.getAttribute('alt') === '').length },
    focusable: focus.length, focusableWithoutName: focus.filter(e => !named(e)).length,
    ariaLive: document.querySelectorAll('[aria-live],[role=status],[role=alert]').length,
    text: { nodes: total, under14px: small, minPx: min },
    horizontalScroll: document.documentElement.scrollWidth > innerWidth + 1,
    bodyOverflowHidden: getComputedStyle(document.body).overflow === 'hidden' || getComputedStyle(document.documentElement).overflow === 'hidden',
    tables: { total: document.querySelectorAll('table').length, th: document.querySelectorAll('th').length, caption: document.querySelectorAll('caption').length },
    autoplayMedia: document.querySelectorAll('video[autoplay],audio[autoplay]').length,
  };
}"""  # noqa: E501

VIEWPORTS = (("escritorio_1280x720", (1280, 720)), ("movil_390x844", (390, 844)))


def to_url(target: str) -> str:
    """Convierte una ruta local en URL file://; deja intactas las URL con esquema.

    Se comprueba la longitud del esquema para no confundir la letra de unidad de
    Windows (C:) con un esquema de URL.
    """
    if len(urlparse(target).scheme) > 1:
        return target
    path = Path(target).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"No existe el archivo: {path}")
    return path.as_uri()


def audit(url: str) -> dict:
    # Import diferido: así --help y los errores de argumentos funcionan sin Playwright.
    from playwright.sync_api import sync_playwright

    out = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for label, (width, height) in VIEWPORTS:
            page = browser.new_page(viewport={"width": width, "height": height})
            errors = []
            page.on("pageerror", lambda e, errors=errors: errors.append(str(e)))
            page.goto(url)
            page.wait_for_timeout(800)
            out[label] = page.evaluate(JS)
            out[label]["jsErrors"] = errors[:3]
            page.close()
        # Preferencia de movimiento reducido: ¿siguen corriendo animaciones?
        page = browser.new_page(viewport={"width": 1280, "height": 720}, reduced_motion="reduce")
        page.goto(url)
        page.wait_for_timeout(500)
        out["animaciones_activas_con_reduced_motion"] = page.evaluate(
            "document.getAnimations().filter(a => a.playState === 'running').length"
        )
        browser.close()
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Renderiza un HTML con Playwright y devuelve métricas de accesibilidad en JSON."
    )
    parser.add_argument("target", help="ruta a un archivo HTML local o URL (http, https, file)")
    args = parser.parse_args(argv)
    try:
        url = to_url(args.target)
    except FileNotFoundError as e:
        parser.error(str(e))
    # La consola de Windows usa cp1252 por defecto y fallaría con emojis o caracteres no latinos.
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(audit(url), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
