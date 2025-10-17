# Integration Checklist

Use this checklist whenever you connect a new documentation repository to the automated translation pipeline.

## 1. GitHub Repository

- [ ] `translate.yml` workflow present and passing on `main`.
- [ ] `TARGET_LANGUAGES` updated with the locales you plan to generate.
- [ ] `N8N_WEBHOOK_URL_TR` secret configured and tested with the dry-run flag.
- [ ] Branch protection rules allow commits from `GITHUB_TOKEN`.

## 2. n8n Workflow

- [ ] Webhook URL matches the secret stored in GitHub.
- [ ] Validation, filtering, translation, and formatting nodes enabled.
- [ ] Alert channel configured to notify on verification failures.
- [ ] Glossary and prompt variables loaded for each locale.

## 3. MkDocs Project

- [ ] New English content lives under `docs/en/`.
- [ ] `mkdocs.yml` nav updated and `nav_translations` entries provided.
- [ ] `mkdocs build` succeeds locally with `mkdocs-material` and `mkdocs-static-i18n`.

## 4. Smoke Test

1. Create a short English change and open a PR.
2. Merge to `main` and monitor the **Translate Documentation** workflow.
3. Confirm localized files appear in `docs/<lang>/`.
4. Run `mkdocs serve` and review `/es/` and `/fr/` pages.

Document any blockers and capture logs in the shared operations runbook.
