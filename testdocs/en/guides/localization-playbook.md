# Localization Playbook

This playbook outlines the tactical steps teams should follow after the automated translation workflow has published localized Markdown.

## 1. Verify Pipeline Output

- Open the associated GitHub Action run and confirm the `Request translations via n8n` step succeeded.
- Review the auto-generated commit on `main` to ensure the expected `docs/<lang>/` files were updated.
- Use `mkdocs serve` to spot-check the localized site with the latest translations.

## 2. Perform Glossary QA

Create a lightweight checklist to confirm terminology alignment:

| Item | Action |
| ---- | ------ |
| Product names | Verify product names remain untranslated. |
| Code snippets | Ensure code blocks retain original syntax. |
| Links | Confirm internal links still resolve for each locale. |

Document findings in your team's QA tracker. If translations require edits, push updates to `docs/<lang>/` and rerun `mkdocs build` to validate.

## 3. Escalate Issues to n8n

When translations look incorrect:

1. Capture the failing text and target language.
2. Open the n8n execution log and collect the job ID.
3. Re-run the translation job with refined prompts or glossary entries.

## 4. Prepare Release Notes

After sign-off, update your release checklist with a short summary highlighting:

- New or changed Markdown files.
- Locales affected.
- Any manual interventions required.

Sharing this information keeps downstream stakeholders informed when localized documentation is published.
