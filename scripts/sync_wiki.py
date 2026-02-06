#!/usr/bin/env python3
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

WIKI_URL = "https://github.com/Omni-guides/Tuxborn.wiki.git"
REPO_RAW_BASE = "https://raw.githubusercontent.com/Omni-guides/Tuxborn"
REPO_WEB_BASE = "https://github.com/Omni-guides/Tuxborn"
CACHE_DIR = Path(".cache/wiki")
DOCS_DIR = Path("docs")

PROTECTED_DIRS = {"assets", "checklist"}
PROTECTED_FILES = {"404.md", "broken-links.md"}

ASSET_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico", ".pdf"}

WIKI_LINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]")
MD_LINK_RE = re.compile(r"\]\(([^)]+)\)")
IMAGE_LINK_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def run(cmd, cwd=None):
    result = subprocess.run(cmd, cwd=cwd, check=False, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout.strip()


def ensure_wiki_repo():
    if CACHE_DIR.exists() and (CACHE_DIR / ".git").exists():
        run(["git", "-C", str(CACHE_DIR), "remote", "set-url", "origin", WIKI_URL])
        run(["git", "-C", str(CACHE_DIR), "fetch", "origin", "--prune"])
        if has_ref("origin/master"):
            run(["git", "-C", str(CACHE_DIR), "reset", "--hard", "origin/master"])
        elif has_ref("origin/main"):
            run(["git", "-C", str(CACHE_DIR), "reset", "--hard", "origin/main"])
        else:
            raise RuntimeError("Unable to find origin/master or origin/main in wiki repo.")
    else:
        CACHE_DIR.parent.mkdir(parents=True, exist_ok=True)
        run(["git", "clone", WIKI_URL, str(CACHE_DIR)])


def has_ref(ref_name):
    result = subprocess.run(
        ["git", "-C", str(CACHE_DIR), "rev-parse", "--verify", ref_name],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def normalize_key(value):
    value = value.strip()
    value = value.replace("_", "-")
    value = value.replace(" ", "-")
    value = re.sub(r"-+", "-", value)
    return value.lower()


def build_page_map(md_files):
    page_map = {}
    page_targets = {}
    for src in md_files:
        rel = src.relative_to(CACHE_DIR)
        target_rel = Path("index.md") if rel.name == "Home.md" and rel.parent == Path(".") else rel
        page_targets[rel] = target_rel

        raw = rel.with_suffix("").as_posix()
        base = rel.stem
        candidates = {
            raw,
            raw.replace("-", " "),
            base,
            base.replace("-", " "),
        }
        for candidate in candidates:
            key = normalize_key(candidate)
            page_map.setdefault(key, target_rel.as_posix())
    return page_map, page_targets


def ensure_front_matter(text, edit_uri):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            front = text[: end + 4]
            body = text[end + 4 :].lstrip("\n")
            if re.search(r"^edit_uri:\s*.*$", front, re.MULTILINE):
                front = re.sub(r"^edit_uri:\s*.*$", f"edit_uri: {edit_uri}", front, flags=re.MULTILINE)
            else:
                front = front.replace("\n---", f"\nedit_uri: {edit_uri}\n---")
            return front + "\n\n" + body
    front = f"---\nedit_uri: {edit_uri}\n---\n\n"
    return front + text.lstrip("\n")


def page_url(from_rel, to_rel):
    from_dir = Path(from_rel).parent
    rel = os.path.relpath(to_rel, start=from_dir).replace("\\", "/")
    if rel.endswith("index.md"):
        rel = rel[: -len("index.md")]
        return rel if rel else "./"
    if rel.endswith(".md"):
        rel = rel[: -3] + "/"
    return rel


def rewrite_wiki_links(text, current_rel, page_map):
    def replace(match):
        target = match.group(1).strip()
        label = match.group(2) or target
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        key = normalize_key(target)
        if key not in page_map:
            return match.group(0)
        to_rel = page_map[key]
        url = page_url(current_rel, to_rel) + anchor
        return f"[{label}]({url})"

    return WIKI_LINK_RE.sub(replace, text)




def rewrite_any_links(text, current_rel, page_map):
    def replace(match):
        original = match.group(0)
        target = match.group(1).strip()
        if target.startswith('<') and target.endswith('>'):
            target = target[1:-1]

        parts = target.split(None, 1)
        url = parts[0]
        title = ' ' + parts[1] if len(parts) > 1 else ''

        if url.startswith('#') or url.startswith('mailto:'):
            return original

        cleaned = url
        if cleaned.startswith('http://') or cleaned.startswith('https://'):
            if '/wiki/' in cleaned:
                cleaned = cleaned.split('/wiki/', 1)[1]
            else:
                return original

        if cleaned.endswith('.md'):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip('/')

        key = normalize_key(cleaned)
        if key not in page_map:
            return original
        to_rel = page_map[key]
        new_url = page_url(current_rel, to_rel)
        if '#' in url:
            anchor = url.split('#', 1)[1]
            new_url = new_url + '#' + anchor
        return f"]({new_url}{title})"

    return MD_LINK_RE.sub(replace, text)




def download_asset(url, rel_path):
    try:
        import urllib.request
        dest = DOCS_DIR / 'assets' / 'external' / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(url) as resp:
            dest.write_bytes(resp.read())
        return dest
    except Exception:
        return None


def rewrite_image_links(text, current_rel):
    def replace(match):
        original = match.group(0)
        url = match.group(1).strip()
        if url.startswith('<') and url.endswith('>'):
            url = url[1:-1]
        original_url = url
        if url.startswith(f"{REPO_WEB_BASE}/blob/"):
            url = url.replace(f"{REPO_WEB_BASE}/blob/", f"{REPO_RAW_BASE}/")
        if url.startswith(REPO_RAW_BASE):
            rel = url.replace(f"{REPO_RAW_BASE}/", "")
            dest = download_asset(url, rel)
            if dest:
                rel_url = os.path.relpath(dest, start=(DOCS_DIR / current_rel).parent).replace('\\\\', '/')
                return original.replace(match.group(1), rel_url)
        # Try relative images against the main repo raw URL.
        if not (url.startswith("http://") or url.startswith("https://")):
            rel = url.lstrip("./")
            if any(rel.lower().endswith(ext) for ext in ASSET_EXTS):
                raw_url = f"{REPO_RAW_BASE}/main/{rel}"
                dest = download_asset(raw_url, rel)
                if dest:
                    rel_url = os.path.relpath(dest, start=(DOCS_DIR / current_rel).parent).replace('\\\\', '/')
                    return original.replace(match.group(1), rel_url)
        return original.replace(match.group(1), original_url)

    return IMAGE_LINK_RE.sub(replace, text)


def rewrite_md_links(text, current_rel, page_map):
    def replace(match):
        original = match.group(0)
        target = match.group(1).strip()

        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]

        parts = target.split(None, 1)
        url = parts[0]
        title = " " + parts[1] if len(parts) > 1 else ""

        if url.startswith("#") or url.startswith("mailto:"):
            return original

        cleaned = url
        if cleaned.startswith("https://github.com/Omni-guides/Tuxborn/wiki/"):
            cleaned = cleaned.split("/wiki/", 1)[1]
        elif cleaned.startswith("http://github.com/Omni-guides/Tuxborn/wiki/"):
            cleaned = cleaned.split("/wiki/", 1)[1]
        elif cleaned.startswith("/wiki/"):
            cleaned = cleaned.split("/wiki/", 1)[1]
        else:
            return original

        if "#" in cleaned:
            cleaned, anchor = cleaned.split("#", 1)
            anchor = "#" + anchor
        else:
            anchor = ""

        cleaned = unquote(cleaned).strip("/")
        key = normalize_key(cleaned)
        if key not in page_map:
            return original
        to_rel = page_map[key]
        new_url = page_url(current_rel, to_rel) + anchor
        return f"]({new_url}{title})"

    return MD_LINK_RE.sub(replace, text)


def copy_assets():
    for path in CACHE_DIR.rglob("*"):
        if path.is_dir() or path.name.startswith("."):
            continue
        if path.suffix.lower() in ASSET_EXTS:
            rel = path.relative_to(CACHE_DIR)
            dest = DOCS_DIR / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dest)


def is_external(url):
    return url.startswith(("http://", "https://", "mailto:"))


def normalize_link_target(url):
    if url.startswith("<") and url.endswith(">"):
        url = url[1:-1]
    url = url.split("#", 1)[0]
    url = url.split("?", 1)[0]
    return url.strip()


def resolve_target_path(current_file, url):
    url = normalize_link_target(url)
    if not url or url.startswith("#") or is_external(url):
        return None
    if url.startswith("/"):
        target = (DOCS_DIR / url.lstrip("/")).resolve()
    else:
        target = (Path(current_file).parent / url).resolve()

    if url.endswith("/"):
        index_target = target / "index.md"
        md_target = target.with_suffix(".md")
        if md_target.exists():
            return md_target
        return index_target

    if target.suffix:
        return target

    return target.with_suffix(".md")


def create_stub_pages():
    missing = {}
    for path in DOCS_DIR.rglob("*.md"):
        content = path.read_text(encoding="utf-8")
        for match in MD_LINK_RE.finditer(content):
            url = match.group(1).strip()
            target = resolve_target_path(path, url)
            if target is None:
                continue
            if not target.exists():
                missing.setdefault(target, url)

    for target, url in missing.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        slug = target.stem.replace("-", " ")
        wiki_slug = target.stem
        edit_uri = f"https://github.com/Omni-guides/Tuxborn/wiki/{wiki_slug}"
        body = [
            "---",
            f"edit_uri: {edit_uri}",
            "---",
            "",
            f"# {slug}",
            "",
            "This page is linked in the wiki but does not exist yet.",
            "",
            f"Create it here: [{edit_uri}]({edit_uri})",
            "",
        ]
        target.write_text("\n".join(body), encoding="utf-8")


def generate_all_pages(pages, current_rel):
    lines = ["# All Pages", "", "Browse every page pulled from the Tuxborn GitHub Wiki.", ""]
    for page in pages:
        if page == "index.md":
            continue
        title = Path(page).stem.replace("-", " ")
        link = "../" + page_url("index.md", page)
        lines.append(f"- [{title}]({link})")
    return "\n".join(lines) + "\n"


def write_pages_file(nav_list):
    content = ["nav:"]
    for entry in nav_list:
        entry_path = entry.rstrip("/")
        if not (DOCS_DIR / entry_path).exists():
            continue
        content.append(f"  - {entry}")
    (DOCS_DIR / ".pages").write_text("\n".join(content) + "\n", encoding="utf-8")




def fetch_readme(page_map):
    import urllib.request
    urls = [
        f"{REPO_RAW_BASE}/HEAD/README.md",
        f"{REPO_RAW_BASE}/main/README.md",
        f"{REPO_RAW_BASE}/master/README.md",
    ]
    content = None
    for url in urls:
        try:
            with urllib.request.urlopen(url) as resp:
                content = resp.read().decode("utf-8", errors="replace")
                break
        except Exception:
            continue
    if content is None:
        return

    readme_path = DOCS_DIR / "project-readme.md"
    content = ensure_front_matter(content, f"{REPO_WEB_BASE}/blob/HEAD/README.md")
    content = rewrite_any_links(content, "project-readme.md", page_map)
    content = rewrite_image_links(content, "project-readme.md")
    readme_path.write_text(content, encoding="utf-8")




def ensure_404():
    path = DOCS_DIR / "404.md"
    if path.exists():
        return
    path.write_text(
        "---\ntitle: Page not found\n---\n\n# 404 — Page not found\n\nIt looks like this page moved or doesn’t exist.\n\n- Try the search bar in the header\n- Browse the sidebar\n- Or head back to the home page\n\nIf you think this is a broken link in the wiki, please update it there.\n",
        encoding="utf-8",
    )



def sync():
    ensure_wiki_repo()

    if DOCS_DIR.exists():
        for item in DOCS_DIR.iterdir():
            if item.name.startswith("."):
                continue
            if item.name in PROTECTED_DIRS or item.name in PROTECTED_FILES:
                continue
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    else:
        DOCS_DIR.mkdir(parents=True, exist_ok=True)

    md_files = [p for p in CACHE_DIR.rglob("*.md") if p.is_file() and not p.name.startswith(".")]
    page_map, page_targets = build_page_map(md_files)

    for src in md_files:
        rel = src.relative_to(CACHE_DIR)
        target_rel = page_targets[rel]
        dest = DOCS_DIR / target_rel
        dest.parent.mkdir(parents=True, exist_ok=True)

        text = src.read_text(encoding="utf-8")
        text = rewrite_wiki_links(text, target_rel.as_posix(), page_map)
        text = rewrite_md_links(text, target_rel.as_posix(), page_map)
        text = rewrite_any_links(text, target_rel.as_posix(), page_map)
        text = rewrite_image_links(text, target_rel.as_posix())

        page_slug = rel.with_suffix("").as_posix().replace(" ", "-")
        if rel.name == "Home.md" and rel.parent == Path("."):
            edit_uri = "https://github.com/Omni-guides/Tuxborn/wiki/Home"
        else:
            edit_uri = f"https://github.com/Omni-guides/Tuxborn/wiki/{page_slug}"

        text = ensure_front_matter(text, edit_uri)
        dest.write_text(text, encoding="utf-8")

    copy_assets()
    fetch_readme(page_map)
    ensure_404()
    create_stub_pages()

    has_home = any(
        rel.name == "Home.md" and rel.parent == Path(".")
        for rel in page_targets.keys()
    )

    if not has_home:
        index_path = DOCS_DIR / "index.md"
        page_list = sorted({p.as_posix() for p in page_targets.values()})
        index_body = [
            "# Tuxborn Wiki",
            "",
            "The wiki does not have a Home page. This index is generated automatically.",
            "",
            "## Pages",
            "",
        ]
        for page in page_list:
            title = Path(page).stem.replace("-", " ")
            link = page_url("index.md", page)
            index_body.append(f"- [{title}]({link})")
        index_text = "\n".join(index_body) + "\n"
        index_text = ensure_front_matter(index_text, "https://github.com/Omni-guides/Tuxborn/wiki/Home")
        index_path.write_text(index_text, encoding="utf-8")

    hub_key = normalize_key("Main topics covered")
    hub_page = page_map.get(hub_key)

    nav_entries = []
    if (DOCS_DIR / "index.md").exists():
        nav_entries.append("index.md")

    checklist_index = DOCS_DIR / "checklist" / "index.md"
    if not checklist_index.exists():
        checklist_index.parent.mkdir(parents=True, exist_ok=True)
        checklist_index.write_text(
            "---\ntitle: Checklist\n---\n\n# Checklist\n\nThe checklist dashboard will appear here after the checklist sync runs.\n",
            encoding="utf-8",
        )
    if checklist_index.exists():
        nav_entries.append("checklist")

    if hub_page:
        nav_entries.append(hub_page)
    else:
        all_pages_path = DOCS_DIR / "all-pages.md"
        page_list = sorted({p.as_posix() for p in page_targets.values()})
        all_pages_text = generate_all_pages(page_list, "all-pages.md")
        all_pages_text = ensure_front_matter(all_pages_text, "https://github.com/Omni-guides/Tuxborn/wiki/Home")
        all_pages_path.write_text(all_pages_text, encoding="utf-8")
        nav_entries.append("all-pages.md")

    page_list = sorted({p.as_posix() for p in page_targets.values()})
    for page in page_list:
        if page in nav_entries:
            continue
        nav_entries.append(page)

    # Safety: ensure the checklist placeholder exists if referenced in nav.
    if "checklist" in nav_entries and not checklist_index.exists():
        checklist_index.parent.mkdir(parents=True, exist_ok=True)
        checklist_index.write_text(
            "---\ntitle: Checklist\n---\n\n# Checklist\n\nThe checklist dashboard will appear here after the checklist sync runs.\n",
            encoding="utf-8",
        )
    write_pages_file(nav_entries)

    print(f"Synced {len(md_files)} pages into {DOCS_DIR}")


if __name__ == "__main__":
    try:
        sync()
    except Exception as exc:
        print(f"sync_wiki.py failed: {exc}", file=sys.stderr)
        sys.exit(1)
