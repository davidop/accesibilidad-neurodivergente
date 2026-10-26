# Cómo contribuir

Gracias por querer mejorar la skill. Las contribuciones más valiosas son recomendaciones respaldadas
por evidencia y casos reales en los que la skill acierta o falla.

## Antes de empezar

- Para cambios pequeños (erratas, enlaces rotos), abre directamente un pull request.
- Para recomendaciones nuevas o cambios de criterio, abre antes un issue con la plantilla
  **Proponer o corregir una recomendación**, para comentar la evidencia antes de redactar.
- Si has probado la skill en una herramienta, usa la plantilla **Informe de compatibilidad**. Con
  esos informes se completa la tabla del README.

## Reglas de contenido

1. **Cada recomendación lleva etiqueta de evidencia.** `[WCAG x.x.x]` si está en un criterio
   normativo, `[Guía]` si viene de una organización especializada y `[Heurística]` si no tiene
   respaldo claro. Ante la duda, `[Heurística]`: es mejor quedarse corto que exagerar.
2. **Barreras, no diagnósticos.** Describe qué dificulta algo y a quién puede afectar, sin presentar
   rasgos como si definieran a todas las personas de un perfil.
3. **Abre la fuente antes de citarla.** `references/fuentes.md` es una lista de lecturas, no un
   conjunto de estudios verificados.
4. **Nada de datos personales reales** en ejemplos, capturas, fixtures ni issues. Usa datos ficticios.
5. **Mantén `SKILL.md` breve.** La especificación Agent Skills recomienda menos de 500 líneas; el
   material de consulta largo va en `references/`.

## Entorno de desarrollo

Necesitas [uv](https://docs.astral.sh/uv/). La skill en sí no necesita instalar nada: esto solo
sirve para los tests y el lint.

```sh
uv sync                                 # crea el entorno con las dependencias de desarrollo
uv run playwright install chromium      # navegador para los tests de audit_render.py
uv run pytest                           # tests
uv run ruff check . && uv run ruff format --check .   # lint y formato
```

Los tests comprueban, entre otras cosas, que el frontmatter de `SKILL.md` cumple la
[especificación Agent Skills](https://agentskills.io/specification) y que cada fichero que menciona
existe.

## Commits y pull requests

- Trabaja en una rama (`feat/...`, `fix/...`, `docs/...`), nunca directamente en `main`.
- Usa [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/):
  `tipo(ámbito): descripción`, con tipos `feat`, `fix`, `docs`, `refactor`, `test` o `chore`.
  Por ejemplo: `feat(checklist): añadir criterio sobre temporizadores en formularios`.
- Añade una entrada en `CHANGELOG.md`, en la sección `[Unreleased]`.
- Rellena la plantilla del pull request. La CI tiene que pasar.

Los PR de Dependabot con cambios patch o minor se fusionan solos cuando pasa la CI
(`dependabot-auto-merge.yml`). Los major quedan abiertos con un comentario para revisarlos a mano.
Si uno se queda parado porque `main` ha avanzado, comenta `@dependabot rebase` en el PR.

## Publicar una versión (mantenedores)

1. Mueve las entradas de `[Unreleased]` a una sección `## [X.Y.Z] - AAAA-MM-DD` en `CHANGELOG.md` y
   actualiza los enlaces del final.
2. Actualiza `metadata.version` en `SKILL.md` y `version` en `pyproject.toml`.
3. Haz merge en `main`, crea la etiqueta y súbela:

   ```sh
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

El workflow `release.yml` comprueba que la etiqueta coincide con la versión y publica la release
con el `.zip` de la skill y las notas del CHANGELOG.

## Código de conducta

Este proyecto sigue el [Código de conducta](CODE_OF_CONDUCT.md). Al participar, te comprometes a
respetarlo.
