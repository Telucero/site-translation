#!/usr/bin/env python3
"""
Helper utility that packages updated Markdown files, sends them to the n8n
translation workflow, and writes the returned localized content.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

import requests


def _compute_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _load_file_paths(
    positional: Sequence[str],
    file_list: str | None,
    repo_root: Path,
) -> List[Path]:
    paths: List[Path] = []

    if file_list:
        list_path = Path(file_list)
        if not list_path.is_absolute():
            list_path = repo_root / list_path
        if not list_path.exists():
            raise FileNotFoundError(f"File list {list_path} not found.")
        for line in list_path.read_text(encoding="utf-8").splitlines():
            entry = line.strip()
            if entry:
                paths.append(Path(entry))

    for value in positional:
        value = value.strip()
        if value:
            paths.append(Path(value))

    seen = set()
    unique: List[Path] = []
    for path in paths:
        if path not in seen:
            seen.add(path)
            unique.append(path)

    if not unique:
        raise ValueError("No Markdown files were provided to request translation.")

    return unique


def collect_documents(
    files: Sequence[Path],
    repo_root: Path,
    default_language: str,
) -> Tuple[List[Dict[str, Any]], int]:
    documents: List[Dict[str, Any]] = []
    total_bytes = 0

    for path in files:
        absolute = repo_root / path
        if not absolute.exists():
            raise FileNotFoundError(f"File {absolute} not found.")

        content = absolute.read_text(encoding="utf-8")
        byte_length = len(content.encode("utf-8"))
        total_bytes += byte_length

        documents.append(
            {
                "path": str(path),
                "language": default_language,
                "checksum": _compute_sha256(content),
                "content": content,
                "bytes": byte_length,
            }
        )

    return documents, total_bytes


def _build_manifest(documents: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    manifest: List[Dict[str, Any]] = []
    for entry in documents:
        manifest.append(
            {
                "path": entry["path"],
                "language": entry["language"],
                "checksum": entry["checksum"],
                "bytes": entry.get("bytes"),
            }
        )
    return manifest


def _build_archive(documents: Sequence[Dict[str, Any]]) -> str:
    payload = json.dumps(documents, ensure_ascii=False).encode("utf-8")
    compressed = gzip.compress(payload)
    return base64.b64encode(compressed).decode("ascii")


def _prepare_payload(
    documents: List[Dict[str, Any]],
    total_bytes: int,
    args: argparse.Namespace,
) -> Dict[str, Any]:
    manifest = _build_manifest(documents)
    payload_docs: List[Dict[str, Any]] = documents
    archive_b64: str | None = None

    if args.archive_threshold_bytes and total_bytes >= args.archive_threshold_bytes:
        archive_b64 = _build_archive(documents)
        payload_docs = _build_manifest(documents)

    payload: Dict[str, Any] = {
        "branch": args.branch,
        "commit": args.commit,
        "default_language": args.default_language,
        "target_languages": args.languages,
        "documents": payload_docs,
        "documents_manifest": manifest,
        "document_total_bytes": total_bytes,
    }

    if archive_b64:
        payload.update(
            {
                "documents_archive": archive_b64,
                "documents_archive_encoding": "base64",
                "documents_archive_format": "gzip-json",
            }
        )

    return payload


def invoke_webhook(
    webhook_url: str,
    payload: Dict[str, Any],
    timeout: int,
    dry_run: bool,
) -> Dict[str, Any]:
    if dry_run:
        print(json.dumps(payload, indent=2))
        return {"translations": []}

    response = requests.post(webhook_url, json=payload, timeout=timeout)
    response.raise_for_status()
    body = response.content.strip()
    if not body:
        return {"translations": []}
    try:
        return response.json()
    except ValueError as exc:
        preview = response.text.strip()
        if len(preview) > 200:
            preview = preview[:200] + "..."
        raise RuntimeError(
            f"Webhook returned non-JSON response (status {response.status_code}): "
            f"{preview or '<empty response>'}"
        ) from exc


def _normalize_entry(
    entry: Dict[str, Any],
    default_language: str,
) -> Dict[str, str]:
    language_raw = (
        entry.get("language")
        or entry.get("target_language")
        or entry.get("locale")
    )
    language = language_raw.lower() if isinstance(language_raw, str) else None
    path = entry.get("path") or entry.get("target_path")
    content = (
        entry.get("translated_markdown")
        or entry.get("content")
        or entry.get("markdown")
        or entry.get("text")
    )
    source_path = entry.get("source_path") or entry.get("original_path")

    if not path and source_path and language:
        path = source_path.replace(
            f"docs/{default_language}/", f"docs/{language}/"
        )

    missing = []
    if not path:
        missing.append("path/target_path (or source_path+language)")
    if not content:
        missing.append("content/translated_markdown")

    if missing:
        raise KeyError(
            "Translation entry missing required fields: "
            + ", ".join(missing)
        )

    return {"path": path, "content": content}


def write_translations(
    translations: List[Dict[str, Any]],
    repo_root: Path,
    default_language: str,
) -> int:
    if not translations:
        print("No translations returned; nothing to write.")
        return 0

    written = 0

    for index, item in enumerate(translations):
        if not isinstance(item, dict):
            raise TypeError(f"Translation entry at index {index} is not a dict: {item!r}")

        if item.get("verification_errors"):
            warnings = "; ".join(item["verification_errors"])
            print(
                "WARNING: Translation entry reported verification issues for "
                f"{item.get('source_path', '<unknown>')} "
                f"({item.get('target_language', '?')}): {warnings}",
                file=sys.stderr,
            )

        normalized = _normalize_entry(item, default_language)

        target_path = repo_root / normalized["path"]
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(normalized["content"], encoding="utf-8")
        written += 1
        print(f"Wrote translation: {normalized['path']}")

    return written


def main() -> None:
    parser = argparse.ArgumentParser(description="Send documentation changes to n8n for translation.")
    parser.add_argument(
        "files",
        nargs="*",
        help="Optional list of Markdown files relative to the repository root.",
    )
    parser.add_argument("--file-list", help="Path to a file containing newline-delimited Markdown paths.")
    parser.add_argument("--webhook-url", required=True, help="n8n webhook URL.")
    parser.add_argument("--languages", nargs="+", required=True, help="Target languages to request (e.g., es fr).")
    parser.add_argument("--default-language", default="en", help="Source language (default: en).")
    parser.add_argument("--branch", default=os.getenv("GITHUB_REF", "local"), help="Source branch.")
    parser.add_argument("--commit", default=os.getenv("GITHUB_SHA", "local"), help="Commit SHA for traceability.")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds.")
    parser.add_argument(
        "--archive-threshold-bytes",
        type=int,
        default=2_000_000,
        help="Compress the documents payload when the combined size meets or exceeds this value.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print payload without calling the webhook.")

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    files = _load_file_paths(args.files, args.file_list, repo_root)

    documents, total_bytes = collect_documents(files, repo_root, args.default_language)
    payload = _prepare_payload(documents, total_bytes, args)

    response = invoke_webhook(args.webhook_url, payload, args.timeout, args.dry_run)

    if isinstance(response, list):
        translations = response
    elif isinstance(response, dict):
        translations = response.get("translations", [])
    else:
        raise TypeError(
            f"Unexpected response type from n8n webhook: {type(response).__name__}. "
            "Expected dict with 'translations' key or list of translation items."
        )

    written = write_translations(translations, repo_root, args.default_language)
    print(f"Total translations written: {written}")


if __name__ == "__main__":
    main()
