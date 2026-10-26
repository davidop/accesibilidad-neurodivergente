# accesibilidad-neurodivergente

Skill para Claude que audita, diseña y reescribe interfaces, documentos y textos pensando en
accesibilidad cognitiva y en personas neurodivergentes (TDAH, autismo, dislexia, discalculia,
ansiedad, Tourette, dispraxia).

## Qué hace

- **Audita** HTML, decks (.pptx / HTML), documentos Word, correos y textos, y devuelve hallazgos
  priorizados por severidad.
- **Diseña** patrones concretos (CSS, HTML semántico, copy) que respetan las preferencias del usuario.
- **Reescribe** contenido en lenguaje claro sin cambiar el significado.
- Cada recomendación lleva una etiqueta de evidencia: `[WCAG]`, `[Guía]` o `[Heurística]`.

## Qué no hace

- No certifica que algo "es accesible": las herramientas automáticas detectan una minoría de problemas
  y casi ninguno cognitivo.
- No sustituye las pruebas con personas neurodivergentes.
- No diagnostica ni da consejo clínico.
- No sustituye un catálogo técnico de WCAG para código (ARIA, widgets, frameworks).

## Contenido

```
skills/accesibilidad-neurodivergente/
├── SKILL.md                  Instrucciones de la skill (formato Agent Skills)
├── references/fuentes.md     Fuentes y lecturas (lista de referencias, no estudios verificados uno a uno)
└── scripts/audit_render.py   Renderiza un HTML con Playwright y devuelve métricas de accesibilidad en JSON
```

## Compatibilidad

La skill sigue el formato abierto **Agent Skills** (`SKILL.md` con frontmatter `name` y `description`),
sin extensiones específicas de ningún agente. Copia la carpeta `skills/accesibilidad-neurodivergente/`
a la ruta de tu herramienta:

| Herramienta | Proyecto | Usuario |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex CLI | `.agents/skills/` | `~/.agents/skills/` |
| GitHub Copilot (VS Code / Visual Studio) | `.github/skills/` (también lee `.claude/skills/` y `.agents/skills/`) | `~/.copilot/skills/` |
| Claude (web/escritorio) | Súbela como skill desde Ajustes, en .zip | |

> Estado de las pruebas: marca aquí con qué herramientas se ha probado de verdad. Hasta que se pruebe,
> la compatibilidad es la del estándar, no una garantía.

`scripts/audit_render.py` es opcional: necesita Python 3 y Playwright con Chromium. Ejecútalo con
`python3 -I scripts/audit_render.py`.

## Créditos

Creada por **David Oliva Paredes** ([davidop](https://github.com/davidop)).

Inspirada por el trabajo de **Mía Salazar** en accesibilidad y neurodiversidad: las referencias parten de
su recopilación para la charla en Commit Conf, y su ayuda ha sido clave. Mía será colaboradora futura
del proyecto.

Complementa a `a11y.instructions.md` de [github/awesome-copilot](https://github.com/github/awesome-copilot)
para accesibilidad técnica de código.

## Contribuir

Issues y PRs son bienvenidos, sobre todo con casos reales y con evidencia de las recomendaciones.
Si una recomendación no tiene respaldo, marca su etiqueta como `[Heurística]`.

## Licencia

MIT. Ver `LICENSE`.
