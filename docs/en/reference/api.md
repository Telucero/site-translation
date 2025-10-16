# API Overview

The platform exposes a REST API that powers dynamic content such as release notes, multilingual search, and personalized onboarding. The following sections illustrate placeholder endpoints for testing the translation pipeline.

## Authentication

- `POST /api/v1/token` — exchange client credentials for a bearer token.
- `GET /api/v1/token/refresh` — renew an expiring token.

## Localization Endpoints

- `GET /api/v1/pages/{slug}` — retrieve localized Markdown for the specified slug.
- `POST /api/v1/pages` — create or replace localized Markdown.
- `GET /api/v1/languages` — list active locales for the site.

## Error Codes

| Code | Meaning | Suggested Action |
| ---- | ------- | ---------------- |
| 400 | Validation error | Inspect the request payload for missing fields. |
| 401 | Unauthorized | Ensure the access token is provided and valid. |
| 404 | Not found | Confirm the slug exists for the requested locale. |
| 503 | Service unavailable | Retry with exponential backoff. |

!!! warning "Preview API only"
    These endpoints are sample data used to stress test translation configurations and do not represent the production contract.
