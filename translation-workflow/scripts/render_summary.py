#!/usr/bin/env python3
"""Render translation summary markdown from JSON report."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


def _format_missing(data: dict[str, list[str]]) -> list[str]:
    lines: list[str] = []
    lines.append("#### Translation coverage")
    if not data:
        lines.append("- No files required translation.")
        return lines
    for lang, paths in sorted(data.items()):
        if not paths:
            lines.append(f"- `{lang}`: ✅ up to date")
        else:
            lines.append(f"- `{lang}`: ❌ missing {len(paths)} file(s)")
            for path in paths[:5]:
                lines.append(f"  - `{path}`")
            if len(paths) > 5:
                lines.append("  - ...")
    return lines


def _format_locale_added(data: dict[str, int]) -> list[str]:
    lines: list[str] = []
    lines.append("#### Locale key additions")
    if not data:
        lines.append("- No new locale keys were added.")
        return lines
    for locale, count in sorted(data.items()):
        lines.append(f"- `{locale}`: {count} new key(s)")
    return lines


def _format_unused(keys: list[str]) -> list[str]:
    lines: list[str] = []
    lines.append("#### Locale keys unused in templates")
    if not keys:
        lines.append("- No unused locale keys detected.")
        return lines
    for key in keys[:10]:
        lines.append(f"- `{key}`")
    if len(keys) > 10:
        lines.append("- ...")
    return lines


def _group_validation_issues(validation: dict[str, Any]) -> dict[str, dict[str, list[dict[str, Any]]]]:
    grouped: dict[str, dict[str, list[dict[str, Any]]]] = {}
    issues: List[dict[str, Any]] = list(validation.get("issues") or [])

    if issues:
        for issue in issues:
            lang = issue.get("language") or issue.get("target_language") or "unknown"
            path = issue.get("target_path") or issue.get("source_path") or "unknown"
            grouped.setdefault(lang, {}).setdefault(path, []).append(issue)

    if grouped:
        return grouped

    issues_by_language: Dict[str, Any] = validation.get("issues_by_language") or {}
    for lang, payload in issues_by_language.items():
        files = payload.get("files", {})
        for path, file_issues in files.items():
            for issue in file_issues:
                entry = dict(issue)
                entry.setdefault("language", lang)
                entry.setdefault("target_path", path)
                grouped.setdefault(lang, {}).setdefault(path, []).append(entry)
    return grouped


def _format_validation(validation: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    lines.append("#### Validation status")
    status = validation.get("status", "unknown")
    issue_count = validation.get("issue_count", len(validation.get("issues", [])))
    grouped = _group_validation_issues(validation)

    if status == "passed":
        lines.append("- ✅ Structural validation passed.")
        return lines
    if status not in {"failed", "warning"}:
        lines.append("- ⚠️ Validation status unknown.")
        return lines

    if issue_count:
        lines.append(f"- ❌ {issue_count} issue(s) detected across translations.")
    else:
        lines.append("- ❌ Validation reported issues but no details were captured.")

    if not grouped:
        lines.append("  - No structured issue breakdown available. See translation-workflow/translations/validation_report.json.")
        return lines

    lines.append("- Detailed discrepancies:")
    for lang in sorted(grouped.keys()):
        files = grouped[lang]
        total_for_lang = sum(len(items) for items in files.values())
        lines.append(f"  - Locale `{lang}` ({total_for_lang} issue(s))")
        for path, file_issues in sorted(files.items()):
            lines.append(f"    - `{path}`")
            for issue in sorted(file_issues, key=lambda item: item.get("line") or 0):
                line_num = issue.get("line")
                line_hint = f"L{line_num}" if line_num else "line n/a"
                issue_type = issue.get("issue_type") or "validation_issue"
                message = issue.get("message") or "See validation report for details."
                lines.append(f"      - {line_hint}: [{issue_type}] {message}")
    lines.append("  - Full details: translation-workflow/translations/validation_report.json")
    return lines


def build_markdown(summary_path: Path) -> str:
    data = json.loads(summary_path.read_text(encoding="utf-8"))
    blocks: list[str] = ["### Translation Summary"]
    blocks.extend(_format_missing(data.get("missing_per_language", {})))
    blocks.append("")
    blocks.extend(_format_locale_added(data.get("locale_added_per_locale", {})))
    blocks.append("")
    blocks.extend(_format_unused(data.get("locale_unused_keys", [])))
    blocks.append("")
    validation_block = data.get("validation") or {
        "status": data.get("validation_status", "unknown"),
    }
    if not validation_block.get("issues"):
        validation_block["issues"] = data.get("validation_issues", [])
    blocks.extend(_format_validation(validation_block))
    return "\n".join(blocks).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", type=Path, required=True, help="Path to summary_report.json")
    parser.add_argument("--output", type=Path, required=True, help="Markdown output path")
    args = parser.parse_args()

    if not args.summary.exists():
        raise FileNotFoundError(args.summary)

    markdown = build_markdown(args.summary)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown, encoding="utf-8")
    print(markdown)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
