#!/usr/bin/env python3
"""
Helper utility that packages updated Markdown files, sends them to the n8n
translation workflow, and writes the returned localized content.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List

import requests


def _compute_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def collect_documents(files: List[Path], repo_root: Path, default_language: str) -> List[Dict[str, Any]]:
    documents = []
    for path in files:
        absolute = repo_root / path
        if not absolute.exists():
            raise FileNotFoundError(f"File {absolute} not found.")

        content = absolute.read_text(encoding="utf-8")
        documents.append(
            {
                "path": str(path),
                "language": default_language,
                "checksum": _compute_sha256(content),
                "content": content,
            }
        )
    return documents


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
    return response.json()


def write_translations(translations: List[Dict[str, str]], repo_root: Path) -> None:
    for item in translations:
        target_path = repo_root / item["path"]
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(item["content"], encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Send documentation changes to n8n for translation.")
    parser.add_argument("files", nargs="+", help="List of Markdown files relative to the repository root.")
    parser.add_argument("--webhook-url", required=True, help="n8n webhook URL.")
    parser.add_argument("--languages", nargs="+", required=True, help="Target languages to request (e.g., es fr).")
    parser.add_argument("--default-language", default="en", help="Source language (default: en).")
    parser.add_argument("--branch", default=os.getenv("GITHUB_REF", "local"), help="Source branch.")
    parser.add_argument("--commit", default=os.getenv("GITHUB_SHA", "local"), help="Commit SHA for traceability.")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds.")
    parser.add_argument("--dry-run", action="store_true", help="Print payload without calling the webhook.")

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    files = [Path(f) for f in args.files]

    documents = collect_documents(files, repo_root, args.default_language)
    payload = {
        "branch": args.branch,
        "commit": args.commit,
        "default_language": args.default_language,
        "target_languages": args.languages,
        "documents": documents,
    }

    response = invoke_webhook(args.webhook_url, payload, args.timeout, args.dry_run)
    translations = response.get("translations", [])

    if translations:
        write_translations(translations, repo_root)


if __name__ == "__main__":
    main()
