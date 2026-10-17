#!/usr/bin/env python3
"""Check the primary-source library: front matter, checksums, indexes, and names.

Exclusion-list tokens are stored as code points so this file does not contain them.
Repository URL prefixes are removed before the scan. The same letters in prose still fail.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TYPES = {
    "statutes",
    "cfr",
    "mpep",
    "ptab",
    "courts",
    "federal-register",
    "notices",
}
REQUIRED = [
    "title",
    "citation",
    "court_or_board",
    "date",
    "docket_or_appeal_number",
    "precedential_status",
    "designation_date",
    "de_designation_date",
    "topic_tags",
    "source_url",
    "retrieved_on",
    "sha256",
    "cited_by_stories",
]
JSONLD_KEYS = [
    "@context",
    "@type",
    "identifier",
    "datePublished",
    "publisher",
    "url",
    "isBasedOn",
]
TEXT_EXT = {".md", ".json", ".csv", ".txt", ".xml", ".yml", ".yaml", ".html"}
URL_PREFIXES = [
    "https://github.com/ssukduang-cpu/pgp-documents",
    "https://raw.githubusercontent.com/ssukduang-cpu/pgp-documents",
    "github.com/ssukduang-cpu/pgp-documents",
]
STORY_URL = "https://postgrantproceeding.com/insights/{slug}"


def _tok(*codes: int) -> str:
    return "".join(chr(code) for code in codes)


BANNED = re.compile(
    "(?i)\\b"
    + _tok(83, 117, 110, 105)
    + "\\b|"
    + _tok(83, 117, 107, 100, 117, 97, 110, 103)
    + "|"
    + _tok(80, 111, 108, 115, 105, 110, 101, 108, 108, 105)
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def strip_repo_urls(text: str) -> str:
    for prefix in URL_PREFIXES:
        text = text.replace(prefix, "")
    return text


def split_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("front matter is not closed")
    meta = yaml.safe_load(text[4:end]) or {}
    body = text[end + 5 :]
    if not isinstance(meta, dict):
        raise ValueError("front matter is not a mapping")
    return meta, body


def jsonld(body: str) -> dict:
    match = re.search(r"```json\n(.*?)\n```", body, re.S)
    if not match:
        raise ValueError("missing JSON-LD block")
    data = json.loads(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("JSON-LD block is not an object")
    return data


def document_paths() -> list[Path]:
    found = []
    docs = ROOT / "docs"
    for path in sorted(docs.glob("*/*/index.md")):
        if path.parts[-3] not in TYPES:
            continue
        found.append(path)
    return found


def check_documents(errors: list[str]) -> dict[str, dict]:
    parsed: dict[str, dict] = {}
    for path in document_paths():
        rel = path.relative_to(ROOT).as_posix()
        try:
            meta, body = split_front_matter(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{rel}: {exc}")
            continue
        for key in REQUIRED:
            if key not in meta:
                errors.append(f"{rel}: missing front matter field {key}")
        if not isinstance(meta.get("topic_tags"), list):
            errors.append(f"{rel}: topic_tags must be a list")
        stories = meta.get("cited_by_stories")
        if not isinstance(stories, list):
            errors.append(f"{rel}: cited_by_stories must be a list")
        else:
            for item in stories:
                if not isinstance(item, dict) or "slug" not in item or "url" not in item:
                    errors.append(f"{rel}: cited_by_stories entries need slug and url")
                    continue
                expected = STORY_URL.format(slug=item["slug"])
                if item["url"] != expected:
                    errors.append(f"{rel}: story URL {item['url']!r} != {expected}")
        status = str(meta.get("confirmation_status") or "")
        original = str(meta.get("original_file") or "")
        digest = str(meta.get("sha256") or "")
        if not digest:
            if status != "Not yet confirmed" or original:
                errors.append(
                    f"{rel}: empty sha256 is allowed only when confirmation_status "
                    "is 'Not yet confirmed' and original_file is empty"
                )
        if original:
            file_path = path.parent / original
            if not file_path.is_file():
                errors.append(f"{rel}: original file {original} is missing")
            elif digest and sha256(file_path) != digest:
                errors.append(f"{rel}: sha256 does not match {original}")
        if meta.get("document_type") == "mpep" and not str(meta.get("mpep_revision") or "").strip():
            errors.append(f"{rel}: MPEP entry needs mpep_revision")
        try:
            linked = jsonld(body)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{rel}: {exc}")
            linked = {}
        for key in JSONLD_KEYS:
            if key not in linked:
                errors.append(f"{rel}: JSON-LD missing {key}")
        publisher = linked.get("publisher")
        if not isinstance(publisher, dict) or not publisher.get("name"):
            errors.append(f"{rel}: JSON-LD publisher needs a name")
        if digest and (linked.get("encoding") or {}).get("sha256") != digest:
            errors.append(f"{rel}: JSON-LD encoding.sha256 does not match front matter")
        parsed[rel] = meta
    return parsed


def same(left, right) -> bool:
    if isinstance(left, str) or left is None:
        return (left or "") == (right or "")
    return left == right


def check_index(errors: list[str], parsed: dict[str, dict]) -> None:
    index_path = ROOT / "index.json"
    try:
        index = json.loads(index_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"index.json: {exc}")
        return
    rows = index.get("documents")
    if not isinstance(rows, list):
        errors.append("index.json: documents must be a list")
        return
    by_path = {row.get("path"): row for row in rows}
    if set(by_path) != set(parsed):
        missing = sorted(set(parsed) - set(by_path))
        extra = sorted(set(by_path) - set(parsed))
        if missing:
            errors.append("index.json missing paths: " + ", ".join(missing[:8]))
        if extra:
            errors.append("index.json extra paths: " + ", ".join(extra[:8]))
    shared = [
        "slug",
        "document_type",
        "title",
        "citation",
        "court_or_board",
        "date",
        "docket_or_appeal_number",
        "paper",
        "related_dockets",
        "precedential_status",
        "designation_scope",
        "designation_date",
        "de_designation_date",
        "topic_tags",
        "source_url",
        "retrieved_on",
        "sha256",
        "original_file",
        "cited_by_stories",
        "mpep_revision",
        "confirmation_status",
        "confirmation_note",
        "story_cite",
        "story_cite_match",
        "legacy_release_file",
        "legacy_release_url",
    ]
    raw_urls = []
    for path, row in by_path.items():
        meta = parsed.get(path)
        if meta is None:
            continue
        for key in shared:
            if not same(meta.get(key), row.get(key)):
                errors.append(f"index.json {path} field {key} does not match front matter")
                break
        raw = row.get("raw_url") or ""
        raw_urls.append(raw)
        if not raw.endswith("/" + path):
            errors.append(f"index.json {path} raw_url does not end with the path")
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if not llms.startswith("# "):
        errors.append("llms.txt must start with an H1")
    if "\n> " not in llms and not llms.splitlines()[2:3] == []:
        if not any(line.startswith("> ") for line in llms.splitlines()):
            errors.append("llms.txt needs a summary blockquote")
    for raw in raw_urls:
        if raw not in llms:
            errors.append(f"llms.txt missing {raw}")
        if f"<loc>{raw}</loc>" not in sitemap:
            errors.append(f"sitemap.xml missing {raw}")
    with (ROOT / "index.csv").open(encoding="utf-8", newline="") as handle:
        csv_rows = list(csv.DictReader(handle))
    if len(csv_rows) != len(rows):
        errors.append(f"index.csv has {len(csv_rows)} rows; index.json has {len(rows)}")
    csv_by_path = {row["path"]: row for row in csv_rows}
    for row in rows:
        csv_row = csv_by_path.get(row["path"])
        if csv_row is None:
            errors.append(f"index.csv missing {row['path']}")
            continue
        if csv_row.get("sha256", "") != (row.get("sha256") or ""):
            errors.append(f"index.csv sha256 mismatch for {row['path']}")
        if csv_row.get("title", "") != row.get("title", ""):
            errors.append(f"index.csv title mismatch for {row['path']}")
        joined = ";".join(row.get("related_dockets") or [])
        if csv_row.get("related_dockets", "") != joined:
            errors.append(f"index.csv related_dockets mismatch for {row['path']}")
        stories = ";".join(
            f"{item['slug']}|{item['url']}" for item in (row.get("cited_by_stories") or [])
        )
        if csv_row.get("cited_by_stories", "") != stories:
            errors.append(f"index.csv cited_by_stories mismatch for {row['path']}")


def check_names(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        suffix = path.suffix.lower()
        rel = path.relative_to(ROOT).as_posix()
        text = ""
        if suffix in TEXT_EXT:
            text = path.read_text(encoding="utf-8", errors="replace")
        elif suffix == ".pdf":
            proc = subprocess.run(
                ["pdftotext", "-q", str(path), "-"],
                capture_output=True,
                check=False,
            )
            if proc.returncode != 0:
                errors.append(f"{rel}: pdftotext failed")
                continue
            text = proc.stdout.decode("utf-8", "replace")
        else:
            continue
        if BANNED.search(strip_repo_urls(text)):
            errors.append(f"{rel}: exclusion-list name in content")


def main() -> int:
    errors: list[str] = []
    parsed = check_documents(errors)
    check_index(errors, parsed)
    check_names(errors)
    if errors:
        print(f"{len(errors)} validation error(s):")
        for item in errors[:80]:
            print(f"- {item}")
        if len(errors) > 80:
            print(f"... {len(errors) - 80} more")
        return 1
    print(f"ok: {len(parsed)} documents")
    return 0


if __name__ == "__main__":
    sys.exit(main())
