.PHONY: venv sync serve build

venv:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

sync:
	. .venv/bin/activate && python scripts/sync_wiki.py
	. .venv/bin/activate && python scripts/sync_checklist.py

serve:
	. .venv/bin/activate && mkdocs serve

build:
	. .venv/bin/activate && mkdocs build --clean
