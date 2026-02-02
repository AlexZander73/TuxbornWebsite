# Tuxborn Wiki Site (MkDocs + Material)

This repository builds a modern documentation site from the **GitHub Wiki** for Tuxborn. The wiki remains the source of truth — maintainers keep editing Markdown in the wiki, and the site rebuilds automatically.

## How it works
- `scripts/sync_wiki.py` clones (or updates) the wiki repo and copies Markdown into `docs/`.
- It rewrites common GitHub wiki links (including `[[Wiki Links]]` and `/wiki/Page-Name`) to MkDocs-friendly relative links.
- It generates `docs/.pages` for consistent sidebar ordering and creates `docs/index.md` from `Home.md`.
- `scripts/check_links.py` validates internal links.
- `scripts/sync_checklist.py` pulls the public checklist spreadsheet and renders it as searchable, filterable tables in `docs/checklist/`.
- GitHub Actions builds and deploys to GitHub Pages on every push, manual dispatch, and a weekly schedule.

## Local development
1) Create a virtual environment and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Sync wiki content:

```bash
python scripts/sync_wiki.py
```

3) Sync checklist data:

```bash
python scripts/sync_checklist.py
```

The checklist sync requires the Google Sheet to be shared as **Anyone with the link can view**.

4) Serve locally:

```bash
mkdocs serve
```

Open the dev server URL printed by MkDocs.

## Maintainer workflow
- **Edit content:** continue editing in the GitHub Wiki.
- **Sync (optional locally):** `python scripts/sync_wiki.py` and `python scripts/sync_checklist.py`.
- **Deploy:** push to `main` (or use the GitHub Actions workflow dispatch). A weekly scheduled build also keeps the site in sync even if no code changes happen here.

## GitHub Pages setup
1) Go to **Settings → Pages**.
2) Under **Build and deployment**, set **Source** to **GitHub Actions**.
3) Ensure the default branch is `main`.

## License note
This site republishes content from the Tuxborn GitHub Wiki. Ensure you respect the original repository and wiki license terms. See `LICENSE-NOTE.md` for guidance.
