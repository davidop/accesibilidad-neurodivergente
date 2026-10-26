# Política de seguridad

## Versiones con soporte

Solo se mantiene la última versión publicada en
[Releases](https://github.com/davidop/accesibilidad-neurodivergente/releases).

## Qué se considera un problema de seguridad

- Instrucciones en `SKILL.md` o en `references/` que puedan llevar a un agente a ejecutar acciones
  no pedidas, filtrar datos o seguir instrucciones inyectadas desde el contenido auditado.
- Fallos en `scripts/audit_render.py` que permitan ejecutar código en la máquina que lo lanza más
  allá de lo que hace un navegador Chromium al abrir la página indicada.
- Enlaces de `references/fuentes.md` que hayan pasado a apuntar a contenido malicioso.

Ten en cuenta que `audit_render.py` abre en un Chromium sin interfaz la ruta o URL que le pases:
úsalo solo con contenido en el que confíes, igual que lo abrirías en tu navegador.

## Cómo informar

**No abras un issue público.** Usa el
[aviso privado de vulnerabilidades de GitHub](https://github.com/davidop/accesibilidad-neurodivergente/security/advisories/new)
(pestaña *Security* → *Report a vulnerability*).

Incluye qué has encontrado, cómo reproducirlo y qué impacto crees que tiene. Recibirás respuesta en
un plazo razonable y se te reconocerá en las notas de la versión que lo corrija, salvo que prefieras
lo contrario.
