"""
Generate a single BibTeX file from our staged references.

Usage: python scripts/gen_bibtex.py
Output: bib/crew-scheduling.bib
"""

import json, pathlib, textwrap, hashlib, datetime

DATA_DIR   = pathlib.Path("data/staged")
SRC_FILE   = (DATA_DIR / "references_enriched.json"
              if (DATA_DIR / "references_enriched.json").exists()
              else DATA_DIR / "references.json")
OUT_DIR    = pathlib.Path("bib"); OUT_DIR.mkdir(exist_ok=True)
OUT_FILE   = OUT_DIR / "crew-scheduling.bib"

def slugify(s):               # simple ASCII key
    return ''.join(c for c in s if c.isalnum()).lower()

def make_key(author, year, title):
    base = f"{author.split(',')[0]}{year}"
    # ensure uniqueness with 6-digit hash of title
    return slugify(base) + hashlib.md5(title.encode()).hexdigest()[:6]

refs = json.loads(SRC_FILE.read_text(encoding="utf8"))

bib_entries = []
for r in refs:
    key = make_key(r["author"], r["year"], r.get("title", r["author"]))
    entry = textwrap.dedent(f"""\
        @misc{{{key},
          author       = {{{r["author"]}}},
          title        = {{{r.get("title", "")}}},
          year         = {{{r["year"]}}},
          howpublished = {{\\url{{https://doi.org/{r.get("doi","")}}}}},
          note         = {{{r.get("journal","")}}},
        }}""")
    bib_entries.append(entry)

OUT_FILE.write_text("\n\n".join(bib_entries), encoding="utf8")
print(f"✅ Wrote {len(bib_entries)} BibTeX records → {OUT_FILE}")
