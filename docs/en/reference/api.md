# API Overview

The platform exposes a REST API that powers dynamic content such as release notes, multilingual search, and personalized onboarding. The following sections illustrate placeholder endpoints for testing the translation pipeline.

## Authentication

- `POST /api/v1/token` — exchange client credentials for a bearer token.
- `GET /api/v1/token/refresh` — renew an expiring token.

## Localization Endpoints

- `GET /api/v1/pages/{slug}` — retrieve localized Markdown for the specified slug.
- `POST /api/v1/pages` — create or replace localized Markdown.
- `GET /api/v1/languages` — list active locales for the site.
- `POST /api/v1/translation-jobs` — submit batches of Markdown fragments for asynchronous translation.
- `GET /api/v1/translation-jobs/{id}` — check the status of an asynchronous translation job, including errors reported by downstream workflows.

### Translation Job Payload

```json
{
  "source_language": "en",
  "target_languages": ["es", "fr"],
  "documents": [
    {"path": "docs/en/index.md", "content": "..."},
    {"path": "docs/en/reference/api.md", "content": "..."}
  ],
  "webhook_url": "https://automation.example.com/hooks/translation-complete"
}
```

!!! note "Asynchronous translations"
    The API queues each translation request and posts results to the provided webhook. Use the `GET /api/v1/translation-jobs/{id}` endpoint to poll status if a webhook is not available.

## Error Codes

!!! info "Audit reference"
    Responses include an `x-correlation-id` header that maps to n8n execution logs.
    Each API request emits a correlation ID (header `x-request-id`) which you can use to trace translation jobs across GitHub Actions and n8n logs.

| Code | Meaning | Suggested Action |
| ---- | ------- | ---------------- |
| 400 | Validation error | Inspect the request payload for missing fields. |
| 401 | Unauthorized | Ensure the access token is provided and valid. |
| 404 | Not found | Confirm the slug exists for the requested locale. |
| 503 | Service unavailable | Retry with exponential backoff. |
| 524 | Translation timeout | Split the batch into smaller chunks and resubmit. |
| 529 | Translation verification failed | Review the verification errors attached to the job payload and resubmit after fixes. |

!!! warning "Preview API only"
    These endpoints are sample data used to stress test translation configurations and do not represent the production contract.
