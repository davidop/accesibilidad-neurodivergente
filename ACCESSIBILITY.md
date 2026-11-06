# Accesibilidad del proyecto

Última revisión: 7 de noviembre de 2026.

## Compromiso y alcance

`accesibilidad-neurodivergente` es una skill en español para agentes de IA, con
recomendaciones de accesibilidad cognitiva y neurodivergencia. Queremos que sus instrucciones,
referencias, documentación y herramientas de apoyo sean comprensibles y utilizables por el mayor
número de personas posible, incluidas personas que utilizan tecnologías asistivas.

Esta declaración cubre el contenido del repositorio: documentación Markdown, instrucciones de
la skill, ejemplos y el script opcional de auditoría. **No evalúa ni certifica las interfaces,
documentos ni servicios de terceros** que puedan analizarse utilizando la skill.

## Prioridades de accesibilidad

- Instrucciones directas, encabezados descriptivos, enlaces con significado y estructura simple.
- Criterios de revisión basados en barreras, sin atribuir comportamientos a diagnósticos.
- Opciones y alternativas prácticas en vez de imponer una experiencia única.
- Mensajes de error explicativos y salida estructurada en el script de auditoría.
- Posibilidad de enviar comentarios y describir barreras por texto, sin revelar condiciones médicas.

Nuestra referencia técnica para experiencias web es WCAG 2.2 AA, **como objetivo de diseño**.
No afirmamos que este repositorio ni la skill hayan superado una auditoría completa de
conformidad WCAG.

## Comprobaciones y entornos

El repositorio incluye pruebas automáticas para el formato Agent Skills y para el script de
auditoría con páginas HTML de ejemplo, además de revisión de estilo de código y enlaces en CI.
Estas comprobaciones **no verifican** la accesibilidad de toda la documentación ni equivalen
a pruebas de uso con personas neurodivergentes.

No hay evidencia documentada de pruebas completas del repositorio usando lectores de pantalla,
solo teclado, ampliación de pantalla o combinaciones concretas de sistema operativo y
tecnología asistiva. Por tanto, no se declara soporte verificado de esas combinaciones.
El uso en Claude Code, Codex CLI y GitHub Copilot depende de cada herramienta y sus versiones;
la compatibilidad indicada en el README está pendiente de validación práctica.

## Limitaciones y alternativas

- La auditoría automática de HTML no detecta todas las barreras cognitivas ni sustituye
  una evaluación con tecnologías asistivas o personas usuarias. Consulta
  [las limitaciones del script](README.md#script-opcional-audit_renderpy).
- Para ejecutar el script es necesario instalar Python, Playwright y Chromium; la
  [skill puede utilizarse sin ese script](README.md#instalación) para revisar
  contenido y código, indicando qué comprobaciones no se han efectuado.
- La estructura y legibilidad real de las interfaces y documentos creados por un agente
  dependen de sus resultados y requieren verificación independiente.

No existe un inventario exhaustivo de barreras confirmadas del repositorio.
La ausencia de incidencias abiertas no significa ausencia de barreras.

## Cómo comunicar una barrera

[Abre un informe de barrera de accesibilidad](https://github.com/davidop/accesibilidad-neurodivergente/issues/new?template=4-accesibilidad.yml).

Puedes contar en texto qué intentabas hacer, dónde ocurrió el problema y qué pasó.
La información sobre navegador, sistema operativo o tecnología asistiva puede ayudar, pero
es opcional. **No necesitas explicar tu discapacidad o neurotipo ni adjuntar capturas,
grabaciones o informes médicos.** No publiques datos personales o material confidencial.

Si la incidencia requiere comunicar una vulnerabilidad o información sensible,
utiliza la [vía privada de seguridad](SECURITY.md) cuando resulte apropiada.
Esa vía está destinada a seguridad, no garantiza un canal privado general para
todos los problemas de accesibilidad.

## Qué ocurre después

El mantenedor revisará el reporte, pedirá únicamente la información adicional necesaria
y, cuando corresponda, confirmará su impacto y prioridad, propondrá una alternativa y
actualizará el estado en el issue. Podrás comentar si la solución elimina la barrera.
No se establece un plazo de respuesta o resolución garantizado.

Para propuestas de mejoras o cambios en las guías, consulta [CONTRIBUTING.md](CONTRIBUTING.md).
Las personas y agentes de IA que contribuyan deben describir qué pruebas han realizado
y cuáles permanecen pendientes.

## Mantenimiento

Responsable: [David Oliva Paredes (@davidop)](https://github.com/davidop).
Esta declaración se revisará al introducir cambios importantes o cuando se comunique
una barrera que haga necesario actualizarla.
