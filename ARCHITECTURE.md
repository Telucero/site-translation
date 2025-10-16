# Architecture Options for Automated MkDocs Translations

This repository explores candidate architectures for translating product documentation sites that are authored in English with MkDocs and distributed through GitHub. Each option satisfies the baseline requirement of leveraging GitHub, n8n, and a translation service, while outlining trade-offs, storage implications, and scaling considerations for multiple target languages.

## Option 1 — GitHub Actions as the Orchestrator
- **Trigger**: Push/merge into the tracked branch (e.g., `main`).
- **Workflow**: GitHub Action zips or enumerates updated Markdown files → calls an n8n webhook → n8n relays the content to the translation provider (e.g., DeepL, OpenAI) → translated files are returned through n8n → the Action writes localized Markdown into `docs/<lang>/`.
- **Pros**: All automation lives alongside source; clear CI audit trail; easy secrets management with GitHub.
- **Cons**: GitHub Action runtime must wait for the external translation round-trip; synchronous translation can hit timeout for large sites unless batching is used.
- **When to use**: Moderate volume of pages and limited language set (≤5) where per-merge translation latency is acceptable.

## Option 2 — n8n as the Long-Running Translation Pipeline
- **Trigger**: GitHub Action posts commit metadata to n8n and exits quickly.
- **Workflow**: n8n fetches the changed files from GitHub (via REST API), translates content asynchronously, commits localized output back to a designated branch (using a bot token), and optionally opens a pull request.
- **Pros**: n8n handles retries, batching, and per-language fan-out; no GitHub Action timeout risk; easier to integrate additional enrichment steps.
- **Cons**: Requires n8n to maintain GitHub access tokens and manage branch protections; more complexity outside the repo.
- **When to use**: Larger sites, many target languages, or when translation latency is variable and needs queueing.

## Option 3 — Translation Memory with Pre-Generated Prompts
- **Trigger**: GitHub Action or scheduled job exports updated strings into a translation memory (e.g., JSON/CSV) via n8n.
- **Workflow**: n8n checks translation memory; only missing strings are sent to the translation service; results are stored and re-used; MkDocs consumes compiled locale files (via `mkdocs-static-i18n` or custom macros).
- **Pros**: Minimizes translation cost; supports human-in-the-loop review; scalable for dozens of languages.
- **Cons**: Additional storage backing (database/S3) needed; requires more bookkeeping around keys and contexts.
- **When to use**: Enterprise-level documentation with frequent updates and multiple locales.

## Shared Considerations
- **MkDocs Integration**: Use `mkdocs-static-i18n` (or similar plugin) to organize language directories (`docs/<lang>/...`) while keeping English (`docs/en/`) as the source.
- **Translation Service**: Evaluate cost, latency, and glossary support. Popular choices: DeepL, Google Cloud Translate, OpenAI GPT-4o mini, or Amazon Translate.
- **Secrets Management**: Store API keys and n8n webhook URLs in GitHub Secrets for Actions; n8n should store translation service credentials in its credential vault.
- **Storage Model**: For each language, maintain mirrored Markdown under `docs/<lang>/`. For high scale, consider object storage for translated artifacts and keep Git history lean.
- **Scalability**: Introduce batching and caching in n8n; design the workflow to re-translate only changed files; adopt translation memory to avoid duplicate costs.
- **Human Review**: Optionally add a step where translations open a draft pull request that can be reviewed before merging.

The implementation in this repository aligns with **Option 1** by default while documenting how to extend toward Options 2 and 3 if translation volume or language count grows.
