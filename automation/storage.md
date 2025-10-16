# Storage Strategy for Localized Content

Choosing the right storage approach depends on content volume, number of locales, and review workflows.

## Git Repository (default)

- **Pros**: Full history, simple pull request review, integrates with MkDocs builds.
- **Cons**: Repository grows linearly with each added locale.
- **Use when**: ≤10 locales, Markdown pages under 1 MB each, and teams prefer Git-based review.

## Artifact/Object Storage

- **Pros**: Offloads binary size from Git, enables CDN-style distribution, straightforward to expire or roll back.
- **Cons**: Requires authenticated fetch during `mkdocs build`; review process shifts away from pull requests.
- **Use when**: Localized output is produced by external vendors or is large (binary assets, PDFs).

## Database / Translation Memory

- **Pros**: Deduplicates repeated strings, supports human-in-the-loop editing, integrates with TMS tools.
- **Cons**: Adds infrastructure overhead; needs synchronization with MkDocs content at build time.
- **Use when**: Many locales (≥10) with frequent updates and desire for translation re-use.

## Hybrid Strategy

1. Keep curated Markdown in Git for key locales (en + top 3).
2. Store long-tail languages in object storage and fetch during CI builds.
3. Maintain translation memory to seed either path and minimize API calls.

The implemented demo uses the Git-backed model. Transition paths to hybrid/object storage are documented in `automation/n8n/README.md`.
