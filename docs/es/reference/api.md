# Descripción de la API

La plataforma ofrece una API REST que alimenta contenido dinámico como notas de lanzamiento, búsqueda multilingüe y experiencias personalizadas. Las secciones siguientes representan endpoints de ejemplo para probar el flujo de traducción.

## Autenticación

- `POST /api/v1/token` — intercambia credenciales de cliente por un token bearer.
- `GET /api/v1/token/refresh` — renueva un token próximo a expirar.

## Endpoints de localización

- `GET /api/v1/pages/{slug}` — obtiene el Markdown localizado para el slug indicado.
- `POST /api/v1/pages` — crea o reemplaza Markdown localizado.
- `GET /api/v1/languages` — lista los locales activos del sitio.

## Códigos de error

| Código | Significado | Acción sugerida |
| ------ | ----------- | --------------- |
| 400 | Error de validación | Revisa el payload por campos faltantes. |
| 401 | No autorizado | Comprueba que el token de acceso sea válido. |
| 404 | No encontrado | Confirma que el slug exista para el locale solicitado. |
| 503 | Servicio no disponible | Reintenta con retroceso exponencial. |

!!! warning "API de demostración"
    Estos endpoints son datos ficticios usados para validar configuraciones de traducción y no representan el contrato en producción.
