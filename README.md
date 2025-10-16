# Documentation Translation Demo

This repository demonstrates how to translate MkDocs-powered documentation (English source) into multiple languages using GitHub Actions, n8n, and an external translation service.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Preview the site at `http://127.0.0.1:8000/en/`. Language variants for Spanish and French are generated with the `mkdocs-static-i18n` plugin.

## Repository Structure

- `mkdocs.yml` — MkDocs configuration with i18n settings.
- `docs/` — English source content (`docs/en/`) and sample translated output (`docs/es/`, `docs/fr/`).
- `scripts/request_translation.py` — Utility script invoked by CI to call n8n and write localized Markdown.
- `.github/workflows/translate.yml` — GitHub Action triggered on merges to `main`, wiring translations and MkDocs builds.
- `automation/` — Prompts, n8n workflow guide, and storage strategy documentation.
- `ARCHITECTURE.md` — Comparison of viable automation patterns.

## Configure GitHub Action

1. Add the secret `N8N_WEBHOOK_URL` pointing to your n8n webhook endpoint.
2. Adjust `TARGET_LANGUAGES` in `.github/workflows/translate.yml` to list the locales you want to produce.
3. Optionally tweak `requirements.txt` or the Python version to match production.

## n8n Workflow

Follow `automation/n8n/README.md` to build the workflow responding to GitHub payloads:

- Webhook trigger.
- Function nodes to fan out jobs per language.
- HTTP Request node to the translation provider.
- Response node returning localized Markdown.

## Adding Languages

1. Update `languages` and `nav_translations` in `mkdocs.yml`.
2. Extend `TARGET_LANGUAGES` in the GitHub Action.
3. Provide glossary entries in `automation/prompts/`.
4. Ensure the n8n workflow fans out to the new locale.

## Storage & Scaling

See `automation/storage.md` for trade-offs between Git-backed, object storage, and database-backed approaches as the number of languages increases.

## Local Verification

- `mkdocs serve` — Live reload preview.
- `mkdocs build` — Static build with translation directories under `site/`.

Commit changes and push to GitHub to exercise the full translation pipeline.
