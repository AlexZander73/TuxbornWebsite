#!/usr/bin/env python3
import re
import sys
from pathlib import Path

DOCS_DIR = Path("docs")
LINK_RE = re.compile(r"\]\(([^)]+)\)")


def is_external(url):
    return url.startswith(("http://", "https://", "mailto:"))


def normalize_target(url):
    if url.startswith("<") and url.endswith(">"):
        url = url[1:-1]
    url = url.split("#", 1)[0]
    url = url.split("?", 1)[0]
    return url


def resolve_target(current_file, url):
    url = normalize_target(url)
    if not url or url.startswith("#"):
        return None
    if is_external(url):
        return None
    if url.startswith("/"):
        target = (DOCS_DIR / url.lstrip("/")).resolve()
    else:
        target = (current_file.parent / url).resolve()

    if url.endswith("/"):
        index_file = target / "index.md"
        if index_file.exists():
            return index_file
        md_file = target.with_suffix(".md")
        return md_file if md_file.exists() else None

    if target.suffix:
        return target if target.exists() else None

    md_target = target.with_suffix(".md")
    if md_target.exists():
        return md_target

    index_target = target / "index.md"
    if index_target.exists():
        return index_target

    return None


def check_file(path):
    content = path.read_text(encoding="utf-8")
    broken = []
    for match in LINK_RE.finditer(content):
        url = match.group(1).strip()
        target = resolve_target(path, url)
        if target is None and not is_external(url) and not url.startswith("#"):
            broken.append(url)
    return broken


def main():
    if not DOCS_DIR.exists():
        print("docs/ not found. Run scripts/sync_wiki.py first.")
        return 1

    failures = {}
    for path in DOCS_DIR.rglob("*.md"):
        broken = check_file(path)
        if broken:
            failures[path] = broken

    if failures:
        print("Broken internal links detected:")
        for path, links in sorted(failures.items()):
            for link in links:
                print(f"- {path}: {link}")
        return 1

    print("Link check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
