#!/usr/bin/env python3
"""Auditoría rápida de un HTML renderizado (archivo local o URL) con Playwright.

Uso: python3 -I audit_render.py <ruta-o-url> [--hash-slides N]

Mide lo que no se ve leyendo el código fuente: DOM final tras JavaScript, tamaños
de texto reales, elementos enfocables, regiones aria-live, landmarks, cabeceras
y comportamiento a 390 px de ancho (reflujo / zoom forzado / scroll horizontal).
No sustituye a un lector de pantalla ni a pruebas con personas usuarias.
"""
import json, sys
from playwright.sync_api import sync_playwright

target = sys.argv[1]
url = target if '://' in target else 'file://' + target

JS = """() => {
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
  const sizes = {}; let small = 0, total = 0, min = 999;
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (w.nextNode()) { const n = w.currentNode, p = n.parentElement;
    if (!n.nodeValue.trim() || !p || !vis(p) || ['SCRIPT','STYLE'].includes(p.tagName)) continue;
    const sc = p.offsetWidth ? p.getBoundingClientRect().width / p.offsetWidth : 1;  // detecta transform: scale()
    const fs = parseFloat(getComputedStyle(p).fontSize) * (sc || 1); total++; if (fs < 14) small++; if (fs < min) min = fs; }
  const heads = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(vis)
    .map(h => h.tagName + ': ' + h.innerText.replace(/\\s+/g, ' ').slice(0, 60));
  const imgs = [...document.images];
  const focus = [...document.querySelectorAll('a[href],button,input,select,textarea,[tabindex]:not([tabindex="-1"])')].filter(vis);
  const noName = focus.filter(e => !(e.getAttribute('aria-label') || e.innerText.trim() || e.getAttribute('title') || (e.labels && e.labels.length))).length;
  return {
    lang: document.documentElement.lang || null,
    title: document.title,
    viewportMeta: (document.querySelector('meta[name=viewport]') || {}).content || null,
    landmarks: ['main','nav','header','footer'].reduce((o,k)=>(o[k]=document.querySelectorAll(k+',[role='+k+']').length,o),{}),
    headings: heads.slice(0, 40), h1count: heads.filter(h => h.startsWith('H1')).length,
    images: { total: imgs.length, noAlt: imgs.filter(i => !i.hasAttribute('alt')).length, emptyAlt: imgs.filter(i => i.getAttribute('alt') === '').length },
    focusable: focus.length, focusableWithoutName: noName,
    ariaLive: document.querySelectorAll('[aria-live],[role=status],[role=alert]').length,
    text: { nodes: total, under14px: small, minPx: min },
    horizontalScroll: document.documentElement.scrollWidth > innerWidth + 1,
    bodyOverflowHidden: getComputedStyle(document.body).overflow === 'hidden' || getComputedStyle(document.documentElement).overflow === 'hidden',
    tables: { total: document.querySelectorAll('table').length, th: document.querySelectorAll('th').length, caption: document.querySelectorAll('caption').length },
    autoplayMedia: document.querySelectorAll('video[autoplay],audio[autoplay]').length,
  };
}"""

with sync_playwright() as p:
    b = p.chromium.launch()
    out = {}
    for label, size in (('escritorio_1280x720', (1280, 720)), ('movil_390x844', (390, 844))):
        pg = b.new_page(viewport={'width': size[0], 'height': size[1]})
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto(url); pg.wait_for_timeout(800)
        out[label] = pg.evaluate(JS); out[label]['jsErrors'] = errs[:3]
        pg.close()
    # preferencia de movimiento reducido: ¿cambia algo medible?
    pg = b.new_page(viewport={'width': 1280, 'height': 720}, reduced_motion='reduce')
    pg.goto(url); pg.wait_for_timeout(500)
    out['animaciones_activas_con_reduced_motion'] = pg.evaluate(
        "document.getAnimations().filter(a => a.playState === 'running').length")
    b.close()
print(json.dumps(out, ensure_ascii=False, indent=2))
