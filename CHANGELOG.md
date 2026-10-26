# Changelog

Todos los cambios relevantes de este proyecto se documentan en este fichero.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto usa [Versionado Semántico](https://semver.org/lang/es/).
La versión de referencia es `metadata.version` en
[`SKILL.md`](skills/accesibilidad-neurodivergente/SKILL.md).

## [Unreleased]

### Cambiado

- Los PR de Dependabot con actualizaciones patch o minor se fusionan solos cuando pasa la CI; las
  major siguen necesitando revisión manual.
- Acciones de GitHub actualizadas: `actions/checkout` v7, `astral-sh/setup-uv` v7 y
  `softprops/action-gh-release` v3.

## [0.1.1] - 2026-10-26

### Añadido

- Tests automáticos: validación de `SKILL.md` contra la especificación Agent Skills y pruebas de
  `audit_render.py` con páginas de ejemplo.
- Integración continua en GitHub Actions (lint, tests, comprobación semanal de enlaces) y
  publicación automática del `.zip` de la skill al crear una etiqueta `vX.Y.Z`.
- Plantillas de issues y pull requests, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`,
  `CODEOWNERS` y Dependabot.

### Corregido

- `audit_render.py` funciona con rutas relativas y rutas de Windows (antes generaba URL `file://`
  inválidas).
- `audit_render.py` muestra el uso en lugar de fallar con `IndexError` cuando falta el argumento, y
  avisa si el archivo no existe.
- `audit_render.py` ya no documenta la opción `--hash-slides`, que no estaba implementada.
- `text.minPx` devuelve `null` cuando no hay texto, en vez de `999`.
- La detección de elementos enfocables sin nombre tiene en cuenta `aria-labelledby`, el `alt` de
  imágenes dentro de enlaces o botones y el `value` de los botones `<input>`; ignora los campos
  ocultos.
- La salida JSON se escribe en UTF-8 también en la consola de Windows.

## [0.1.0] - 2026-10-26

### Añadido

- Primera versión de la skill `accesibilidad-neurodivergente`: auditoría, diseño y reescritura con
  etiquetas de evidencia `[WCAG]`, `[Guía]` y `[Heurística]`.
- Script opcional `scripts/audit_render.py` para auditar HTML renderizado con Playwright.
- Recopilación de fuentes en `references/fuentes.md`.

[Unreleased]: https://github.com/davidop/accesibilidad-neurodivergente/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/davidop/accesibilidad-neurodivergente/compare/3a55294...v0.1.1
[0.1.0]: https://github.com/davidop/accesibilidad-neurodivergente/commit/3a55294
