"""
Enrich crew-bidding references with Crossref metadata.

Input : data/staged/references.json           (from parse_tagged_refs.py)
Output: data/staged/references_enriched.json  (adds doi, title, journal …)

Usage : python scripts/enrich_crossref.py
Env   : CROSSREF_MAILTO   → your@email.com  (recommended by Crossref)
"""
import json, pathlib, requests, time, os, logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
BASE_URL = "https://api.crossref.org/works"
HEADERS  = {"User-Agent": f"AgileAerosystems-CrewBib/1.0 (mailto:{os.getenv('CROSSREF_MAILTO','none@nowhere')})"}

# Throttle: 50 req/min  ≈ 1.2 s between calls
THROTTLE_SEC = 1.3

data_dir  = pathlib.Path("data/staged")
refs_path = data_dir / "references.json"
out_path  = data_dir / "references_enriched.json"

refs = json.loads(refs_path.read_text(encoding="utf8"))
enriched = []

def query_crossref(author, year):
    """Return best match dict or None."""
    params = {
        "query.author": author.split(",")[0],  # first surname is plenty
        "filter": f"from-pub-date:{year}-01-01,until-pub-date:{year}-12-31",
        "rows": 1,
        "select": "DOI,title,container-title,issued,publisher"  # shrink payload
    }
    try:
        r = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=15)
        r.raise_for_status()
        items = r.json()["message"]["items"]
        return items[0] if items else None
    except Exception as exc:
        logging.warning(f"Crossref lookup failed: {exc}")
        return None

for i, ref in enumerate(refs, start=1):
    author, year = ref["author"], ref["year"]
    logging.info(f"[{i:03}/{len(refs)}] {author} ({year}) …")

    meta = query_crossref(author, year)
    if meta:
        ref.update({
            "doi"    : meta.get("DOI"),
            "title"  : meta.get("title"          , [""])[0],
            "journal": meta.get("container-title", [""])[0],
            "publisher": meta.get("publisher", "")
        })
    else:
        logging.info("   ↳ No Crossref hit; keeping minimal record.")
    time.sleep(THROTTLE_SEC)
    enriched.append(ref)

out_path.write_text(json.dumps(enriched, indent=2, ensure_ascii=False), encoding="utf8")
logging.info(f"✅ Enriched {len(enriched)} refs → {out_path}")
