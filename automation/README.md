# Automation Assets

This folder contains resources that support the end-to-end translation workflow:

- `prompts/` — Prompt templates and per-language configuration snippets for translation services (LLM or MT).
- `n8n/` — Step-by-step setup guide and JSON scaffolding for the companion n8n workflow.
- `storage.md` — Guidance on storing localized artifacts as the number of target languages grows.

These assets complement the GitHub Action defined in `.github/workflows/translate.yml` and the helper script in `scripts/request_translation.py`.
