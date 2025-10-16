# Getting Started

Follow these steps to preview the documentation site locally.

## 1. Create the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Serve the site in English

```bash
mkdocs serve
```

The site becomes available at `http://127.0.0.1:8000/en/`.

## 3. Build the multilingual site

```bash
mkdocs build
```

The build outputs localized directories under `site/` for every configured language.

## 4. Update Content

Author content inside `docs/en/`. The automation pipeline will copy and translate it into the other language folders.

!!! info "Need to add a new language?"
    Update `mkdocs.yml` to register the locale, then extend the automation to provide translations under `docs/<lang>/`.
