# Lista de comprobación de la integració
n

Utilice esta lista de comprobación siempre que conecte un nuevo repositorio de documentación al proceso de traducción automática.

## 1. Repositorio GitHu
b

- [ ] Flujo de trabajo `translate.yml` presente y pasando en `main`.
- [ ] `TARGET_LANGUAGES` actualizado con las localizaciones que planea generar.
- [ ] `N8N_WEBHOOK_URL_TR` secreto configurado y probado con la bandera dry-run.
- [ ] Las reglas de protección de rama permiten commits desde `GITHUB_TOKEN`.

## 2. Flujo de trabajo n8
n

- [ ] Webhook URL coincide con el secreto almacenado en GitHub.
- [ ] Nodos de validación, filtrado, traducción y formateo habilitados.
- [ ] Canal de alerta configurado para notificar fallos de verificación.
- Glosario y variables de aviso cargadas para cada configuración regional.

## 3. Proyecto MkDoc
s

- [ ] Nuevo contenido en inglés en `docs/en/`.
- [ ] `mkdocs.yml` nav actualizado y entradas `nav_translations` proporcionadas.
- [ ] `mkdocs build` tiene éxito localmente con `mkdocs-material` y `mkdocs-static-i18n`.

## 4. Prueba de hum
o

1. Crea un cambio corto en inglés y abre un PR.
2. Fusionar a `main` y monitorizar el flujo de trabajo **Translate Documentation**.
3. Confirme que los archivos localizados aparecen en `docs/<lang>/`.
4. Ejecute `mkdocs serve` y revise las páginas `/es/` y `/fr/`.

Documente cualquier bloqueo y capture los registros en el libro de ejecución de operaciones compartidas.


## Ejemplo de Pasos de Verificació
n

- [ ] Confirmar que los registros del proceso de traducción contienen el ID del trabajo en `provider_metadata`.
- Compare el Markdown traducido con el glosario para asegurarse de que la terminología y el tono son correctos.
