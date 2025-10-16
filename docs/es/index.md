# Documentación Multilingüe (Demostración)

Bienvenido al sitio de demostración multilingüe utilizado para prototipar el flujo de traducción del sitio de documentación. El contenido en inglés impulsa el proceso automático de localización que se ejecuta después de fusionar pull requests en la rama principal.

## Qué puedes hacer aquí

- Explora una arquitectura de información similar al sitio de producción.
- Ejecuta `mkdocs serve` para ver el contenido original junto a las compilaciones localizadas.
- Activa el flujo de GitHub Actions para enviar las actualizaciones de las páginas a n8n para su traducción.

!!! tip "Prueba el selector de idioma"
    Usa el selector del pie de página para cambiar entre las versiones de prueba en inglés, español y francés generadas por la automatización.

## Cómo funciona la demo

1. Las actualizaciones se escriben en `docs/en/`.
2. GitHub Actions detecta los cambios fusionados y envía el diff a n8n.
3. n8n traduce el contenido y guarda los archivos en `docs/<lang>/`.
4. MkDocs recompila el sitio estático y produce las variantes `/en/`, `/es/` y `/fr/`.

Consulta la guía de [Flujo de Traducción](guides/translation-flow.md) para conocer los detalles de implementación.
