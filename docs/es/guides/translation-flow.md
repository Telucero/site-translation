# Flujo de Traducción

Esta guía resume el proceso de extremo a extremo que mantiene actualizada la documentación localizada del sitio.

## Pasos generales

1. **Detectar cambios** — GitHub Actions se activa al fusionar en la rama `main`.
2. **Notificar a n8n** — El flujo publica metadatos (SHA, archivos modificados, idiomas objetivos) en un webhook de n8n.
3. **Traducir** — n8n recupera el Markdown actualizado, llama al servicio de traducción y devuelve el texto localizado.
4. **Persistir** — GitHub Actions escribe los archivos en `docs/<lang>/`.
5. **Verificar** — MkDocs comprueba que no falten traducciones y publica un artefacto.

## Archivos involucrados

- `.github/workflows/translate.yml` — Flujo de CI que coordina la traducción.
- `scripts/request_translation.py` — Utilidad que empaqueta y envía los datos a n8n.
- `automation/prompts/` — Prompts y plantillas para los servicios de traducción.
- `automation/n8n/` — Instrucciones para construir el flujo correspondiente en n8n.

## Agregar idiomas

1. Amplía el mapa `languages` dentro de `mkdocs.yml`.
2. Actualiza la matriz del GitHub Action para incluir el nuevo locale.
3. Añade glosarios o prompts específicos en `automation/prompts/`.
4. Ajusta el flujo de n8n para distribuir las solicitudes por idioma.

## Monitoreo

- Los registros del GitHub Action contienen la carga enviada a n8n, duración y errores.
- Configura n8n para reenviar fallos a un canal de alertas (correo/Slack).
- Considera guardar las traducciones en almacenamiento externo cuando aumente el volumen.
