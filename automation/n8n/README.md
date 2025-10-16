# n8n Workflow Guide

This document describes how to build the companion n8n workflow that translates updated MkDocs pages when the GitHub Action fires a webhook request.

## Prerequisites

- n8n instance (self-hosted or cloud).
- Credentials for your translation provider (e.g., DeepL, OpenAI, Google Translate).
- GitHub personal access token with `repo` scope (required if n8n fetches or commits content directly).

## High-Level Flow

1. **Webhook (Trigger)** — Receives payload from GitHub Action containing changed documents.
2. **Function: Prepare Requests** — Iterates over target languages and documents, creating translation jobs.
3. **Split In Batches** (optional) — Rate limits batches to avoid hitting translation API quotas.
4. **HTTP Request: Translate** — Sends the text, glossary, and prompt to the translation service.
5. **Function: Build Response** — Assembles translated Markdown into the structure expected by the GitHub Action.
6. **Respond to Webhook** — Returns JSON with the translated files.

The workflow responds synchronously so the GitHub Action can immediately write the localized files. If translations take longer, consider switching to an asynchronous design (see `Queued Translation` below).

## Node Configuration

| Step | Node Type | Key Settings |
| ---- | --------- | ------------ |
| 1 | **Webhook** | Method: `POST`; Response: `Last Node`; Path: `/papermoons/translate`; Authentication: HTTP Basic or header token. |
| 2 | **Function** (`Prepare Jobs`) | JavaScript code parses `items[0].json.documents` and `target_languages` to emit one item per language+document. Optionally attaches glossary or prompt metadata from `automation/prompts/`. |
| 3 | **Split In Batches** | Batch size configurable per provider limits; enable `Pause Between Batches` to throttle requests. |
| 4 | **HTTP Request** (`Translate`) | Method: `POST`; URL: provider endpoint; Body contains `text`, `source_language`, `target_language`, and prompt/glossary fields. Use credentials stored in n8n. |
| 5 | **Function** (`Assemble Results`) | Re-groups translated text by locale, constructs file paths such as `docs/es/...` by replacing the `/en/` segment. |
| 6 | **Respond to Webhook** | Returns `{ "translations": [ { "language": "es", "path": "...", "content": "..." }, ... ] }`. |

### Function Node Example — Prepare Jobs

```javascript
const documents = items[0].json.documents;
const targets = items[0].json.target_languages;

const jobs = [];
for (const doc of documents) {
  for (const lang of targets) {
    jobs.push({
      json: {
        source_path: doc.path,
        source_language: items[0].json.default_language,
        target_language: lang,
        content: doc.content,
        checksum: doc.checksum,
        glossary: items[0].json.glossary ?? null,
        prompt: items[0].json.prompt ?? null,
      },
    });
  }
}
return jobs;
```

### HTTP Request Node

- **URL**: Example using OpenAI `https://api.openai.com/v1/responses`.
- **Headers**: `Authorization: Bearer {{$credentials.openAi.apiKey}}`, `Content-Type: application/json`.
- **Body**:
  ```json
  {
    "model": "gpt-4o-mini",
    "input": [
      {"role": "system", "content": $json.prompt},
      {"role": "user", "content": $json.content}
    ],
    "response_format": {"type": "json_schema", "json_schema": {...}}
  }
  ```
- **Response Handling**: Extract translated string (e.g., `{{$json.output_text}}`) and pass along with metadata.

### Assemble Results Node

```javascript
const grouped = {};
for (const item of items) {
  const locale = item.json.target_language;
  if (!grouped[locale]) {
    grouped[locale] = [];
  }
  const translatedPath = item.json.source_path.replace('/en/', `/${locale}/`);
  grouped[locale].push({
    language: locale,
    path: translatedPath,
    content: item.json.translated_content,
  });
}

return [
  {
    json: {
      translations: Object.values(grouped).flat(),
    },
  },
];
```

### Respond to Webhook Node

- Mode: `Last Node` (no additional config if it is the final node).
- Response Code: 200.
- Response Data: `JSON`.
- Response Body: `{{ $json }}` from the Assemble Results node.

## Glossary & Prompt Injection

- Store glossaries or prompts in n8n static data or fetch them from this repository via raw GitHub URLs.
- Attach them to each job so the translation provider maintains terminology consistency.

## Queued Translation (Optional)

When translating dozens of languages or long-form content, replace the synchronous HTTP request with a **RabbitMQ**, **SQS**, or **n8n queue** node. In that case, respond immediately with `{"queued": true}` and let n8n push localized files back to GitHub via API after processing.

## Storage Considerations

- **Git-backed** (default in this repo): The GitHub Action writes localized Markdown under `docs/<lang>/`. Simple to diff and version, but repository size grows with each language. Use if locales ≤10 and file sizes are small.
- **Object Storage** (e.g., S3, GCS): Store translations as JSON/Markdown objects and fetch them at build time. Keeps Git history slim; requires build step to download artifacts.
- **Database**: Useful when storing sentence-level translation memory. Enables reuse across projects and reduces API spend.

Scale by:

- Caching translations keyed by checksum (`documents[*].checksum`).
- Running nightly jobs to refresh stale translations.
- Splitting languages into separate branches or repositories if teams manage translations independently.
