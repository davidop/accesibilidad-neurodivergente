---
name: accesibilidad-neurodivergente
description: Audita, diseña y reescribe interfaces web, apps, documentos y textos pensando en personas neurodivergentes (TDAH, autismo, dislexia, discalculia, ansiedad, Tourette, dispraxia) y accesibilidad cognitiva. Úsala siempre que el usuario mencione accesibilidad, a11y, WCAG, neurodivergencia, neurodiversidad, accesibilidad cognitiva, lectura fácil, lenguaje claro, dislexia, TDAH o sobrecarga sensorial, o pida revisar un componente, pantalla, formulario, landing, email o documento para que "lo entienda y use todo el mundo", aunque no nombre explícitamente la neurodivergencia.
license: MIT
compatibility: Compatible con agentes que soporten Agent Skills (SKILL.md). El script opcional scripts/audit_render.py requiere Python 3 y Playwright con Chromium; sin ellos, la auditoría se limita al código y contenido.
metadata:
  author: David Oliva Paredes
  version: "0.1.0"
  language: es
---

# Accesibilidad y neurodivergencia

Punto de partida: no todo el mundo procesa, siente y navega igual, y cumplir una checklist de WCAG no garantiza que algo sea usable cognitivamente. WCAG es el suelo, no el techo. Esta skill sirve para ir más allá del suelo sin caer en estereotipos.

## Principios que guían todo lo demás

1. **Diseña para barreras, no para diagnósticos.** Una barrera (texto denso, temporizador, animación, jerga) afecta a perfiles distintos a la vez. Agrupa los hallazgos por barrera y menciona a quién afecta, sin diagnosticar ni suponer quién es el usuario.
2. **Da control en lugar de adivinar.** Las necesidades de personas con el mismo perfil se contradicen (poco estímulo vs. más estructura visual). La solución robusta es respetar preferencias del sistema (`prefers-reduced-motion`, `prefers-color-scheme`, `prefers-contrast`) y ofrecer ajustes visibles, no fijar una única experiencia "neuroinclusiva".
3. **Reducir carga cognitiva beneficia a todos.** Úsalo como argumento de negocio cuando haga falta convencer a un equipo: claridad, predictibilidad y recuperación de errores mejoran conversión y soporte.
4. **Distingue evidencia de heurística.** Cada recomendación de abajo lleva una etiqueta: `[WCAG]` si está en un criterio normativo; `[Guía]` si viene de guías de organizaciones especializadas (p. ej. British Dyslexia Association, GOV.UK); `[Heurística]` si es práctica común de diseño inclusivo sin respaldo normativo claro. Al reportar, conserva la etiqueta para que el equipo sepa cuánto peso darle.

## Modos de trabajo

Elige según lo que pida el usuario; si hay duda, empieza por auditoría.

### A. Auditoría (código, diseño, captura, URL, documento)
1. Identifica qué se está revisando y su contexto de uso (tarea crítica, formulario, pago, lectura larga).
2. Recorre el checklist de abajo por categorías. Si hay código, revisa el HTML/CSS real, no solo lo que "parece". Si es HTML con JavaScript (deck, SPA, contenido generado), el código fuente no basta: renderízalo con `scripts/audit_render.py` (Playwright; mide DOM final, tamaños de texto reales, foco, `aria-live`, reflujo a 390 px y animaciones con movimiento reducido) y completa con lectura del CSS/JS. Si Playwright no está, dilo y limita la auditoría a lo que se ve en el código.
3. Entrega hallazgos priorizados (ver formato). Si algo no se puede verificar sin ejecutarlo o verlo (contraste real, animaciones), dilo en lugar de suponer.

### B. Diseño o implementación
Propón el patrón concreto (CSS, HTML semántico, copy de ejemplo) y explica qué barrera elimina. Prefiere soluciones que respeten preferencias del usuario antes que valores fijos.

### C. Reescritura de contenido
Reescribe textos en lenguaje claro: frases cortas, una idea por frase, voz activa, sin metáforas ni ironía, términos definidos la primera vez, siglas desarrolladas, instrucciones en orden y numeradas. Conserva el significado; si el original es ambiguo, señala la ambigüedad en vez de resolverla en silencio.

## Checklist por categorías

### Texto y legibilidad (dislexia, TDAH, discalculia)
- Alinear a la izquierda; evitar texto justificado y párrafos largos centrados. `[Guía]` (WCAG 1.4.8 lo exige en nivel AAA)
- Líneas de ~60–80 caracteres, interlineado ≥1,5, espacio entre párrafos ≥1,5× el interlineado; la interfaz no debe romperse si el usuario sobrescribe el espaciado de texto. `[WCAG 1.4.8 AAA, 1.4.12 AA]`
- Tipografía sans-serif legible, tamaño base ≥16 px, evitar cursiva y mayúsculas sostenidas en bloques de texto; no marcar énfasis solo con subrayado o color. `[Guía]`
- Contraste suficiente (4,5:1 texto normal, `[WCAG 1.4.3]`), pero evaluar si el contraste máximo blanco/negro puro es agresivo: algunas guías de dislexia sugieren fondos suaves (crema) y texto oscuro no puro. `[Guía]` Ofrecer cambio de tema en vez de imponerlo.
- Palabras inusuales, jerga y abreviaturas explicadas o evitadas. `[WCAG 3.1.3, 3.1.4 AAA]` Nivel de lectura adecuado a la audiencia. `[WCAG 3.1.5 AAA]`
- Cifras, fechas, importes y unidades: formato consistente, sin exigir cálculo mental; mostrar totales y ejemplos. `[Heurística]`

### Estructura y atención (TDAH, ansiedad)
- Una acción principal clara por pantalla; títulos descriptivos y jerarquía real (`h1–h6`, landmarks). `[WCAG 1.3.1, 2.4.6]`
- Dividir tareas largas en pasos con indicador de progreso y posibilidad de guardar y retomar. `[Heurística]`
- Sin carruseles que avanzan solos, banners parpadeantes, popups o contenido que se mueve; si existe, debe poder pausarse. `[WCAG 2.2.2]`
- Límites de tiempo evitables o ampliables; no expulsar de la sesión sin aviso. `[WCAG 2.2.1]`
- No pedir memorizar ni transcribir datos entre pasos (reutilizar lo ya introducido; autenticación sin test cognitivo). `[WCAG 3.3.7, 3.3.8 en 2.2]`
- Evitar urgencia artificial (cuentas atrás, "¡solo quedan 2!") en flujos importantes: eleva la ansiedad. `[Heurística]`

### Predecibilidad y lenguaje (autismo, ansiedad)
- Navegación y componentes consistentes entre páginas; nada cambia de contexto sin que el usuario lo provoque. `[WCAG 3.2.x]`
- Lenguaje literal: sin modismos, sarcasmo ni metáforas en instrucciones o errores. `[Guía]`
- Decir qué va a pasar antes de que pase (qué hace un botón, qué pasa tras enviar, cuánto tarda). `[Heurística]`
- Errores: explicar qué falló y cómo corregirlo, sin culpar; permitir deshacer y revisar antes de confirmar. `[WCAG 3.3.1, 3.3.3, 3.3.4]`

### Sensorial (autismo, TDAH, ansiedad)
- Respetar `prefers-reduced-motion`; evitar parallax, animaciones en bucle y transiciones largas. `[WCAG 2.3.3 AAA]`
- Nada de audio o vídeo con autoplay; control de volumen y pausa accesibles. `[WCAG 1.4.2, 2.2.2]`
- Máximo de 3 destellos por segundo. `[WCAG 2.3.1]`
- Paleta moderada: evitar saturaciones altas y combinaciones vibrantes en grandes superficies. `[Heurística]` (la relación color–sobrecarga sensorial tiene evidencia limitada y variable entre personas; ofrece modo de bajo estímulo en vez de afirmar un color "correcto")

### Motricidad y entrada (dispraxia, Tourette, TDAH)
- Objetivos táctiles/clic ≥24×24 px como mínimo normativo (mejor 44 px) y con separación. `[WCAG 2.5.8 en 2.2]`
- Alternativas al arrastrar, a gestos complejos y a la precisión; todo operable por teclado con foco visible. `[WCAG 2.1.1, 2.4.7, 2.5.7 en 2.2]`
- Evitar acciones irreversibles con un solo clic; confirmar o permitir deshacer. `[WCAG 3.3.4]`

## Aplicación por formato

La skill vale para cualquier soporte. Los principios no cambian, pero cada formato falla en sitios distintos y se arregla con herramientas distintas. Primero abre el archivo de verdad (no lo juzgues por una captura si puedes leer su estructura), luego aplica el checklist de arriba más estos puntos específicos. Si vas a modificar un archivo, trabaja sobre una copia y conserva el original.

**Web / HTML / componentes**: esta skill no pretende sustituir un catálogo técnico de WCAG para código (ARIA, widgets, frameworks). Para eso complementa con una instrucción o agente especializado, como `a11y.instructions.md` de github/awesome-copilot (WCAG 2.2 AA, anti-patrones con código). Aquí céntrate en lo cognitivo y sensorial y en los básicos: `lang` en `<html>`, un único `h1` y jerarquía sin saltos, landmarks (`main`, `nav`), `alt` útil (vacío si es decorativa), `<label>` asociadas, foco visible, `prefers-reduced-motion` y `prefers-contrast`, `autocomplete` en formularios `[WCAG 1.3.5]`. Revisa el DOM real, no solo la plantilla.

**Decks y presentaciones en HTML** (lienzo fijo escalado con JS, tipo 1280×720): fallan de forma recurrente en cinco sitios. (1) *Reflujo*: un lienzo escalado se encoge en móvil (a 390 px el texto de 14 px queda en ~4 px) y `overflow:hidden` impide el scroll `[WCAG 1.4.4, 1.4.10 AA]`; ofrece una vista lineal sin escalar por debajo de ~900 px. (2) *Cambio de slide no anunciado*: usa `aria-live="polite"` en el contador y mueve el foco al título de la slide activa `[WCAG 4.1.3, 2.4.3]`; añade `<main>` y marca cada slide como región etiquetada ("3 de 12"). (3) *Teclado secuestrado*: si Espacio/flechas cambian de slide, no interceptes la tecla cuando el foco esté en un botón, enlace o campo. (4) *Texto pequeño y denso*: cuerpo ≥18 px sobre el lienzo, mínimo ≥16 px; más de ~150–200 palabras por slide pide dividirla. (5) *Contraste en degradados y chips*: comprueba el extremo más claro de un texto con degradado y los textos de 12–13 px (los colores de acento suelen quedarse en 4,0–4,4:1). Avisos críticos ("uso interno", "no enviar") en minúsculas con negrita o icono, no en mayúsculas sostenidas. Si respeta `prefers-reduced-motion` tanto en CSS como en la librería de animación (GSAP, etc.), anótalo como acierto.

**Word (.docx) y Google Docs**: usa estilos reales de Título/Encabezado 1–3 en lugar de negrita y tamaño manuales (es lo que permite navegar, el índice y los lectores de pantalla); listas con el estilo de lista, no con guiones tecleados; texto alternativo en imágenes; tablas simples con fila de encabezado y sin celdas combinadas; enlaces con texto descriptivo (no "clic aquí"); idioma del documento bien definido; evitar cuadros de texto y objetos flotantes para contenido principal. Cuerpo ≥12 pt, alineado a la izquierda. En Word, el Comprobador de accesibilidad detecta lo estructural; en Google Docs no confíes en que exista un equivalente y revisa a mano.

**PowerPoint (.pptx) y Google Slides**: cada diapositiva con título único y propio de su layout (no un cuadro de texto suelto); una idea por diapositiva; texto ≥24 pt en cuerpo y ≥18 pt como mínimo; orden de lectura coherente con el orden visual; texto alternativo en imágenes y gráficos, y los datos clave también en texto, no solo en la figura; contraste suficiente; sin animaciones ni transiciones llamativas, sin avance automático ni vídeo con autoplay. Las notas del orador sirven como versión en lenguaje claro de lo proyectado. Si un gráfico transmite significado por color, añade etiqueta o patrón.

**PDF exportado**: solo es accesible si se exporta etiquetado (tagged PDF) desde un documento ya bien estructurado; un PDF generado desde una imagen no lo es. Si el origen está mal, arregla el origen.

**Correos y mensajes**: asunto descriptivo, la petición principal en las primeras líneas, listas cortas, fechas y acciones explícitas, sin depender de imágenes para el contenido.

**Cómo ejecutar el trabajo según la herramienta disponible**:
- Archivo adjunto .docx/.pptx: léelo con las skills de `docx`/`pptx` o con python-docx/python-pptx para inspeccionar estilos, títulos, alt text y orden de lectura. Entrega un informe y, si el usuario lo pide, una copia corregida en el mismo formato.
- Google Docs/Slides en Drive: léelo con el conector disponible. Si no hay conector que pueda escribir, entrega el informe con los cambios concretos para aplicar a mano o el contenido reescrito, y dilo en una línea.
- URL: léela con una herramienta de navegación o fetch; ten en cuenta que el HTML recibido puede diferir del renderizado (JavaScript).
- Contenido pegado en el chat: audita el texto y la estructura visible; indica qué no puedes evaluar sin el archivo original (estilos, alt text, orden de lectura).

## Formato de entrega en auditorías

Para cada hallazgo, en este orden:
- **Barrera**: qué dificulta y en qué punto concreto (archivo/línea o elemento).
- **A quién afecta**: perfiles, sin diagnosticar.
- **Criterio**: referencia y etiqueta `[WCAG x.x.x nivel]`, `[Guía]` o `[Heurística]`.
- **Arreglo**: cambio concreto (código o texto), no consejo genérico.
- **Severidad**: bloquea la tarea / la dificulta / mejora.

Ordena por severidad, no por categoría. Termina con lo que no pudiste comprobar y cómo comprobarlo (lector de pantalla, zoom 200 %, modo reducir movimiento, prueba con personas usuarias).

## Qué evitar

- No presentar una lista de rasgos como si definiera a todas las personas de un perfil.
- No decir que algo "es accesible" solo por pasar un validador automático: las herramientas automáticas detectan una minoría de los problemas, y casi ninguno cognitivo.
- No sustituir pruebas con personas neurodivergentes por la checklist; recomiéndalas cuando el producto sea crítico.
- No dar consejo clínico. Si surge salud mental o diagnóstico, limita la respuesta al diseño y deriva lo demás a profesionales.

## Referencias

`scripts/audit_render.py` renderiza un HTML (ruta local o URL) y devuelve métricas de accesibilidad en JSON. Ejecútalo con `python3 -I scripts/audit_render.py <ruta-o-url>` (`python -I` en Windows) o, si hay uv, con `uv run --with playwright python -I scripts/audit_render.py <ruta-o-url>`. Es una ayuda, no un veredicto: las herramientas automáticas no detectan casi nada cognitivo.

Para profundizar o citar fuentes (guías de diseño, WCAG, dislexia, artículos académicos), lee `references/fuentes.md`. Está basada en la recopilación de Mía Salazar para su charla en Commit Conf. Antes de citar un enlace como evidencia, ábrelo: es una lista de referencias, no un conjunto de estudios verificados uno a uno.
