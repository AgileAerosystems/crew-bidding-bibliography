#!/usr/bin/env python3
"""
Fail if any DOI/URL in bibliography.bib returns non-200.
"""
import pathlib, bibtexparser, requests, sys, time

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB  = ROOT / "bib" / "bibliography.bib"
db   = bibtexparser.load(open(BIB, encoding="utf8"))

bad = []
for e in db.entries:
    url = e.get("doi") or e.get("url")
    if not url:
        continue
    # turn bare DOI into full URL
    if url.startswith("10."):
        url = "https://doi.org/" + url
    try:
        r = requests.head(url, allow_redirects=True, timeout=10)
        if r.status_code >= 400:
            bad.append((e["ID"], url, r.status_code))
    except Exception as err:
        bad.append((e["ID"], url, str(err)))
    time.sleep(0.5)                      # be polite

if bad:
    for bid, u, code in bad:
        print(f"❌ {bid}  {u}  →  {code}")
    sys.exit(1)
print("✅ All links good.")
