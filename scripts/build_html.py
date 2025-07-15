"""
Build static HTML pages for crew-bidding bibliography.
Usage: python scripts/build_html.py
"""

import json, pathlib, re, datetime
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader, select_autoescape

# ---------- paths ----------
ROOT       = pathlib.Path(".")
DATA_DIR   = ROOT / "data" / "staged"
SRC_FILE   = (DATA_DIR / "references_enriched.json"
              if (DATA_DIR / "references_enriched.json").exists()
              else DATA_DIR / "references.json")
DOCS_DIR   = ROOT / "docs"; DOCS_DIR.mkdir(exist_ok=True)

# ---------- load refs ----------
refs = json.loads(SRC_FILE.read_text(encoding="utf8"))
# extract first T-tag (T1–T8). Default to "Unsorted".
pillar_re = re.compile(r"\bT\d\b", re.IGNORECASE)

grouped = defaultdict(list)
for r in refs:
    tags = r.get("keywords", [])
    pillar = next((t.upper() for t in tags if pillar_re.fullmatch(t)), "UNSORTED")
    grouped[pillar].append(r)

# sort refs within each pillar
for lst in grouped.values():
    lst.sort(key=lambda x: (x["author"].lower(), x["year"]))

# ---------- Jinja2 env ----------
env = Environment(
    loader=FileSystemLoader(searchpath=str(ROOT / "scripts" / "templates")),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template("bibliography.html.j2")
today    = datetime.date.today().isoformat()

# ---------- write pillar pages ----------
pillar_pages = []
for pillar, items in sorted(grouped.items()):
    html = template.render(
        title=f"Pillar {pillar} References",
        pillar=pillar,
        refs=items,
        generated=today,
        index=False
    )
    out_file = DOCS_DIR / f"{pillar}.html"
    out_file.write_text(html, encoding="utf8")
    pillar_pages.append((pillar, f"{pillar}.html"))

# ---------- write index page ----------
index_html = template.render(
    title="Crew-Bidding Bibliography",
    pillar_pages=pillar_pages,
    generated=today,
    index=True
)
(DOCS_DIR / "index.html").write_text(index_html, encoding="utf8")

print(f"✅ Built {len(pillar_pages)+1} HTML files → {DOCS_DIR}")
