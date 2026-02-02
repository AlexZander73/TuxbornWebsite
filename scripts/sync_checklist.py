#!/usr/bin/env python3
import csv
import json
import re
import sys
import ssl
import urllib.request
import urllib.error
from pathlib import Path

SHEET_URL = "https://docs.google.com/spreadsheets/d/1MJkkLPh240zZ_PnnJucv_NtCE0qFY5uB636VNKBIxOw/edit?usp=sharing"
PUBLISHED_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTfX8hFip2tBkJztpRJEGmi3pMB9TjRKVA_nll9qPkTYVqEzr1MINJ5c-18s5nA2vVw1RGfurXo-yZQ/pub?output=csv"
PUBLISHED_HTML_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTfX8hFip2tBkJztpRJEGmi3pMB9TjRKVA_nll9qPkTYVqEzr1MINJ5c-18s5nA2vVw1RGfurXo-yZQ/pubhtml"
DOCS_DIR = Path("docs")
OUTPUT_DIR = DOCS_DIR / "checklist"
ASSETS_DIR = DOCS_DIR / "assets"

SHEET_ID_RE = re.compile(r"/d/([a-zA-Z0-9-_]+)")
PUBLISHED_ID_RE = re.compile(r"/d/e/([a-zA-Z0-9-_]+)")
SHEET_META_PATTERNS = [
    re.compile(r"\"sheetId\":(\d+),\"title\":\"([^\"]+)\""),
    re.compile(r"\"title\":\"([^\"]+)\",\"sheetId\":(\d+)\"?"),
]


def fetch_url(url):
    try:
        with urllib.request.urlopen(url) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        if exc.code in (401, 403):
            raise RuntimeError(
                "Checklist sheet is not publicly accessible. Set sharing to 'Anyone with the link' and retry."
            ) from exc
        raise
    except urllib.error.URLError as exc:
        if isinstance(exc.reason, ssl.SSLError):
            context = ssl._create_unverified_context()
            try:
                with urllib.request.urlopen(url, context=context) as resp:
                    return resp.read().decode("utf-8", errors="replace")
            except urllib.error.HTTPError as inner:
                if inner.code in (401, 403):
                    raise RuntimeError(
                        "Checklist sheet is not publicly accessible. Set sharing to 'Anyone with the link' and retry."
                    ) from inner
                raise
        raise


def get_sheet_id():
    match = SHEET_ID_RE.search(SHEET_URL)
    if not match:
        raise RuntimeError("Unable to parse sheet id from URL.")
    return match.group(1)

def get_published_id():
    match = PUBLISHED_ID_RE.search(PUBLISHED_CSV_URL or "")
    return match.group(1) if match else None

def parse_tabs_from_pubhtml(html):
    tabs = []
    seen = set()
    patterns = [
        r'href=\"#gid=(\d+)\"[^>]*>\s*([^<]+)\s*<',
        r'name: \"([^\"]+)\", pageUrl: \"[^\"]+gid=(\d+)[^\"]*\"',
    ]
    for pattern in patterns:
        for match in re.findall(pattern, html):
            if len(match) != 2:
                continue
            if pattern.startswith('href='):
                gid, title = match
            else:
                title, gid = match
            if gid in seen:
                continue
            seen.add(gid)
            tabs.append({"gid": gid, "title": title.strip()})
    return tabs


def get_sheet_tabs(sheet_id):
    urls = [
        f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit",
        f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit?usp=sharing",
        f"https://docs.google.com/spreadsheets/d/{sheet_id}/pubhtml",
    ]
    tabs = []
    seen = set()
    for url in urls:
        try:
            html = fetch_url(url)
        except RuntimeError:
            html = ""
        for pattern in SHEET_META_PATTERNS:
            for match in pattern.findall(html):
                if len(match) != 2:
                    continue
                if pattern.pattern.startswith('\"sheetId\"'):
                    sheet_id_value, title = match
                else:
                    title, sheet_id_value = match
                if sheet_id_value in seen:
                    continue
                seen.add(sheet_id_value)
                tabs.append({"gid": sheet_id_value, "title": title})
    if not tabs:
        published_id = get_published_id()
        if published_id:
            try:
                html = fetch_url(PUBLISHED_HTML_URL or f"https://docs.google.com/spreadsheets/d/e/{published_id}/pubhtml")
                tabs = parse_tabs_from_pubhtml(html)
            except RuntimeError:
                tabs = []
    if not tabs:
        tabs = [{"gid": None, "title": "Checklist"}]
    return tabs


def fetch_csv(sheet_id, gid):
    if gid is None and PUBLISHED_CSV_URL:
        content = fetch_url(PUBLISHED_CSV_URL)
    elif gid is not None and PUBLISHED_CSV_URL:
        published_id = get_published_id()
        if published_id:
            url = f"https://docs.google.com/spreadsheets/d/e/{published_id}/pub?output=csv&gid={gid}"
            content = fetch_url(url)
        else:
            url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
            content = fetch_url(url)
    else:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
        content = fetch_url(url)
    reader = csv.reader(content.splitlines())
    rows = [row for row in reader]
    return rows


def normalize_heading(value):
    return re.sub(r"\s+", " ", value.strip())


def slugify(value):
    value = value.strip().replace(" ", "-")
    value = re.sub(r"-+", "-", value)
    value = re.sub(r"[^A-Za-z0-9-]", "", value)
    return value or "sheet"


def build_table(rows):
    if not rows:
        return [], []
    headers = [normalize_heading(h) for h in rows[0]]
    data_rows = [row + [""] * (len(headers) - len(row)) for row in rows[1:]]
    return headers, data_rows




def normalize_key(value):
    value = value.strip().lower()
    value = value.replace("_", "-").replace(" ", "-")
    value = re.sub(r"-+", "-", value)
    return value


def pick_label(headers, row):
    priorities = ["quest", "mod", "item", "name", "title"]
    for key in priorities:
        for idx, header in enumerate(headers):
            if key in header.lower() and idx < len(row) and row[idx].strip():
                return row[idx].strip()
    for idx, cell in enumerate(row):
        if cell.strip():
            return cell.strip()
    return "(unnamed)"


def find_status(headers, row):
    for idx, header in enumerate(headers):
        if "status" in header.lower() or "state" in header.lower() or "done" in header.lower():
            if idx < len(row) and row[idx].strip():
                return row[idx].strip()
    return ""


def update_related_sections(mapping):
    marker_start = "<!-- checklist-related:start -->"
    marker_end = "<!-- checklist-related:end -->"

    for path in DOCS_DIR.rglob("*.md"):
        if "checklist" in path.parts or "assets" in path.parts:
            continue
        if path.name.startswith("."):
            continue
        content = path.read_text(encoding="utf-8")
        page_keys = {normalize_key(path.stem)}
        for line in content.splitlines():
            if line.startswith("# "):
                page_keys.add(normalize_key(line[2:]))
                break

        related = []
        for key in page_keys:
            related.extend(mapping.get(key, []))
        if related:
            lines = [
                marker_start,
                "",
                "## Related checklist items",
                "",
                "These items are tracked in the master checklist.",
                "",
                "- [Open the checklist dashboard](../checklist/)",
            ]
            for entry in related:
                tab = entry["tab"]
                label = entry["label"]
                status = entry.get("status", "")
                status_text = f" — **Status:** {status}" if status else ""
                lines.append(f"- **{tab}**: {label}{status_text}")
            lines.extend(["", marker_end])
            block = "\n".join(lines)
            if marker_start in content and marker_end in content:
                content = re.sub(r"<!-- checklist-related:start -->[\s\S]*?<!-- checklist-related:end -->", block, content)
            else:
                content = content.rstrip() + "\n\n" + block + "\n"
        else:
            if marker_start in content and marker_end in content:
                content = re.sub(r"<!-- checklist-related:start -->[\s\S]*?<!-- checklist-related:end -->\n?", "", content)
        path.write_text(content, encoding="utf-8")



def write_table_page(title, headers, rows, path, include_tab_column=False):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    data = {
        "title": title,
        "headers": headers,
        "rows": rows,
        "include_tab_column": include_tab_column,
    }

    json_blob = json.dumps(data, ensure_ascii=False)
    content = f"""---\ntitle: {title}\n---\n\n# {title}\n\n<div class=\"checklist-controls\">\n  <input type=\"search\" class=\"checklist-search\" placeholder=\"Search...\" aria-label=\"Search checklist\" />\n  <div class=\"checklist-filters\"></div>\n</div>\n\n<div class=\"checklist-table\" data-checklist='{json_blob}'></div>\n"""
    path.write_text(content, encoding="utf-8")


def main():
    sheet_id = get_sheet_id()
    tabs = get_sheet_tabs(sheet_id)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pages = []
    master_rows = []
    master_headers = None
    mapping = {}

    for tab in tabs:
        rows = fetch_csv(sheet_id, tab["gid"])
        headers, data_rows = build_table(rows)
        if not headers:
            continue

        tab_title = tab["title"]
        filename = f"{slugify(tab_title)}.md"
        page_path = OUTPUT_DIR / filename
        write_table_page(tab_title, headers, data_rows, page_path)
        pages.append((tab_title, filename))

        mapping_columns = [
            idx for idx, header in enumerate(headers)
            if any(token in header.lower() for token in ("wiki", "page", "article"))
        ]

        for row in data_rows:
            label = pick_label(headers, row)
            status = find_status(headers, row)
            for idx in mapping_columns:
                if idx >= len(row):
                    continue
                raw_value = row[idx].strip()
                if not raw_value:
                    continue
                for token in re.split(r"[;,]", raw_value):
                    token = token.strip()
                    if not token:
                        continue
                    key = normalize_key(token)
                    mapping.setdefault(key, []).append({
                        "tab": tab_title,
                        "label": label,
                        "status": status,
                    })

        if master_headers is None:
            master_headers = ["Tab"] + headers
        if headers != master_headers[1:]:
            max_len = max(len(headers), len(master_headers) - 1)
            while len(master_headers) - 1 < max_len:
                master_headers.append(f"Column {len(master_headers)}")

        for row in data_rows:
            padded = row + [""] * (len(master_headers) - 1 - len(row))
            master_rows.append([tab_title] + padded)

    if master_headers:
        write_table_page("Checklist Dashboard", master_headers, master_rows, OUTPUT_DIR / "index.md", include_tab_column=True)

    if mapping:
        update_related_sections(mapping)

    pages.sort(key=lambda item: item[0].lower())
    lines = ["title: Checklist", "nav:", "  - index.md"]
    for title, filename in pages:
        if filename == "index.md":
            continue
        lines.append(f"  - {filename}")
    (OUTPUT_DIR / ".pages").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Synced {len(pages)} checklist tabs into {OUTPUT_DIR}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"sync_checklist.py failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
