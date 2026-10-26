# accesibilidad-neurodivergente

[![Estado de la CI](https://github.com/davidop/accesibilidad-neurodivergente/actions/workflows/ci.yml/badge.svg)](https://github.com/davidop/accesibilidad-neurodivergente/actions/workflows/ci.yml)
[![Última versión](https://img.shields.io/github/v/release/davidop/accesibilidad-neurodivergente?label=versión)](https://github.com/davidop/accesibilidad-neurodivergente/releases)
[![Licencia MIT](https://img.shields.io/github/license/davidop/accesibilidad-neurodivergente?label=licencia)](LICENSE)

Skill para agentes de IA (Claude, Codex, GitHub Copilot) que audita, diseña y reescribe
interfaces, documentos y textos pensando en accesibilidad cognitiva y en personas neurodivergentes
(TDAH, autismo, dislexia, discalculia, ansiedad, Tourette, dispraxia).

WCAG es el suelo, no el techo: la skill va más allá de la checklist sin caer en estereotipos.

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

## Instalación

La skill sigue el formato abierto [Agent Skills](https://agentskills.io/specification) (`SKILL.md`
con frontmatter `name` y `description`), sin extensiones específicas de ningún agente. Basta con
copiar la carpeta `skills/accesibilidad-neurodivergente/` a la ruta de tu herramienta.

```sh
git clone https://github.com/davidop/accesibilidad-neurodivergente.git
# Ejemplo para Claude Code, a nivel de usuario:
cp -r accesibilidad-neurodivergente/skills/accesibilidad-neurodivergente ~/.claude/skills/
```

En Windows (PowerShell):

```powershell
git clone https://github.com/davidop/accesibilidad-neurodivergente.git
Copy-Item -Recurse accesibilidad-neurodivergente\skills\accesibilidad-neurodivergente "$HOME\.claude\skills\"
```

| Herramienta | Proyecto | Usuario | Estado |
| --- | --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | Pendiente de probar |
| Codex CLI | `.agents/skills/` | `~/.agents/skills/` | Pendiente de probar |
| GitHub Copilot (VS Code / Visual Studio) | `.github/skills/` (también lee `.claude/skills/` y `.agents/skills/`) | `~/.copilot/skills/` | Pendiente de probar |
| Claude (web/escritorio) | Sube el `.zip` de la [última release](https://github.com/davidop/accesibilidad-neurodivergente/releases) desde Ajustes | | Pendiente de probar |

Hasta que se confirme con cada herramienta, la compatibilidad es la del estándar, no una garantía.
Si la pruebas, cuéntalo con un
[informe de compatibilidad](https://github.com/davidop/accesibilidad-neurodivergente/issues/new?template=3-compatibilidad.yml).

## Ejemplos de uso

La skill se activa sola cuando la petición trata de accesibilidad, lenguaje claro o neurodivergencia,
aunque no la nombres:

- "Revisa este formulario de alta: que lo pueda completar alguien con TDAH o dislexia."
- "Audita `presentacion.html` y dime qué falla en móvil y con movimiento reducido."
- "Reescribe este correo a clientes en lenguaje claro sin cambiar lo que dice."
- "Propón el CSS para un modo de bajo estímulo que respete las preferencias del sistema."

Cada hallazgo de una auditoría indica la barrera, a quién afecta, el criterio con su etiqueta de
evidencia, el arreglo concreto y la severidad.

## Contenido

```text
skills/accesibilidad-neurodivergente/
├── SKILL.md                  Instrucciones de la skill (formato Agent Skills)
├── references/fuentes.md     Fuentes y lecturas (lista de referencias, no estudios verificados uno a uno)
└── scripts/audit_render.py   Renderiza un HTML con Playwright y devuelve métricas de accesibilidad en JSON
```

### Script opcional `audit_render.py`

Renderiza una página (archivo local o URL) a 1280×720 y a 390×844, y con movimiento reducido. Mide lo
que no se ve leyendo el código fuente: idioma, landmarks, encabezados, imágenes sin `alt`, elementos
enfocables sin nombre, regiones `aria-live`, tamaños de texto reales (incluido `transform: scale()`),
scroll horizontal, `overflow: hidden`, autoplay y animaciones que ignoran `prefers-reduced-motion`.

Necesita Python 3.9 o superior y Playwright con Chromium:

```sh
# Con uv (no instala nada en tu Python del sistema)
uv run --with playwright playwright install chromium
uv run --with playwright python -I skills/accesibilidad-neurodivergente/scripts/audit_render.py pagina.html

# Con Python y Playwright ya instalados (en Windows, python en lugar de python3)
python3 -I skills/accesibilidad-neurodivergente/scripts/audit_render.py https://example.org
```

Es una ayuda, no un veredicto: no sustituye a un lector de pantalla ni a pruebas con personas usuarias.

## Contribuir

Issues y PRs son bienvenidos, sobre todo con casos reales y con evidencia de las recomendaciones.
Si una recomendación no tiene respaldo, márcala como `[Heurística]`.

Lee [CONTRIBUTING.md](CONTRIBUTING.md) para el entorno de desarrollo, las reglas de contenido y el
proceso de publicación. Los cambios se registran en [CHANGELOG.md](CHANGELOG.md). Para problemas de
seguridad, consulta [SECURITY.md](SECURITY.md).

## Créditos

Creada por **David Oliva Paredes** ([davidop](https://github.com/davidop)).

Inspirada por el trabajo de **Mía Salazar** en accesibilidad y neurodiversidad: las referencias parten de
su recopilación para la charla en Commit Conf, y su ayuda ha sido clave. Mía será colaboradora futura
del proyecto.

Complementa a `a11y.instructions.md` de [github/awesome-copilot](https://github.com/github/awesome-copilot)
para accesibilidad técnica de código.

## Licencia

[MIT](LICENSE).
