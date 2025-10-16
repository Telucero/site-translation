# Translation Workflow

This guide outlines the end-to-end process that keeps localized documentation up to date.

## High-Level Steps

1. **Detect changes** — GitHub Actions triggers on merges to the `main` branch.
2. **Notify n8n** — The workflow posts metadata (commit SHA, changed files, target languages) to an n8n webhook.
3. **Translate** — n8n fetches the changed Markdown, calls the translation service, and returns localized text.
4. **Persist** — GitHub Actions writes localized Markdown into `docs/<lang>/`.
5. **Verify** — MkDocs build checks for missing translations and publishes an artifact.

## Files Involved

- `.github/workflows/translate.yml` — CI workflow orchestrating translation.
- `scripts/request_translation.py` — Helper that packages and sends payloads to n8n.
- `automation/prompts/` — Sample prompts and templates for translation services.
- `automation/n8n/` — Step-by-step instructions for constructing the companion n8n workflow.

## Adding Languages

1. Extend the `languages` map inside `mkdocs.yml`.
2. Update the GitHub Action matrix to include the new locale.
3. Provide translation glossaries or prompts inside `automation/prompts/`.
4. Refresh the n8n workflow to fan out per-locale translation requests.

## Monitoring

- GitHub Action logs include the payload sent to n8n, translation durations, and any errors.
- n8n should forward failures to an alerting channel (email/Slack).
- Consider caching translations in object storage or a database once volume increases.
