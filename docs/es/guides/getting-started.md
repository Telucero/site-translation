# Primeros pasos

Sigue estos pasos para previsualizar el sitio de documentación en tu equipo.

## 1. Crea el entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Sirve el sitio en inglés

```bash
mkdocs serve
```

El sitio estará disponible en `http://127.0.0.1:8000/en/`.

## 3. Compila el sitio multilingüe

```bash
mkdocs build
```

La compilación crea directorios localizados dentro de `site/` para cada idioma configurado.

## 4. Actualiza el contenido

Escribe el contenido en `docs/en/`. El flujo automatizado copiará y traducirá el material al resto de carpetas de idioma.

!!! info "¿Necesitas un nuevo idioma?"
    Actualiza `mkdocs.yml` para registrar el locale y extiende la automatización para generar las traducciones en `docs/<lang>/`.
