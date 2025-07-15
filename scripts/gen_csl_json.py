"""
Generate CSL-JSON (Zotero-style) from the same staged references.

Usage: python scripts/gen_csl_json.py
Output: bib/crew-scheduling.json
"""
import json, pathlib, hashlib, datetime

DATA_DIR = pathlib.Path("data/staged")
SRC_FILE = (DATA_DIR / "references_enriched.json"
            if (DATA_DIR / "references_enriched.json").exists()
            else DATA_DIR / "references.json")
OUT_DIR  = pathlib.Path("bib"); OUT_DIR.mkdir(exist_ok=True)
OUT_FILE = OUT_DIR / "crew-scheduling.json"

refs = json.loads(SRC_FILE.read_text(encoding="utf8"))
items = []

for r in refs:
    items.append({
        "id"        : hashlib.md5((r["author"]+r["year"]).encode()).hexdigest()[:8],
        "type"      : "article-journal" if r.get("journal") else "report",
        "title"     : r.get("title", ""),
        "author"    : [{"literal": r["author"]}],
        "issued"    : {"date-parts": [[int(r["year"])]]},
        "container-title": r.get("journal",""),
        "publisher" : r.get("publisher",""),
        "DOI"       : r.get("doi","")
    })

OUT_FILE.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf8")
print(f"✅ Wrote {len(items)} CSL-JSON records → {OUT_FILE}")
