#!/usr/bin/env python3
"""
Sort bib/bibliography.bib by entry key (ID) and overwrite the file
only if the order changed. Exits 0 on success, 1 on parse error.
"""

import bibtexparser, pathlib, sys, hashlib

root = pathlib.Path(__file__).resolve().parents[1]
bib_file = root / "bib" / "bibliography.bib"

try:
    with open(bib_file, encoding="utf8") as fh:
        db = bibtexparser.load(fh)
except Exception as e:
    sys.stderr.write(f"parse error: {e}\n")
    sys.exit(1)

# Serialize current state for change-detection
orig_hash = hashlib.sha1(open(bib_file, "rb").read()).hexdigest()

# Sort entries by ID
db.entries = sorted(db.entries, key=lambda e: e["ID"].lower())

# Write back
with open(bib_file, "w", encoding="utf8") as fh:
    bibtexparser.dump(db, fh)

new_hash = hashlib.sha1(open(bib_file, "rb").read()).hexdigest()

# Return 0 even if modified; caller decides to git-add
if orig_hash != new_hash:
    print("🔄 bibliography.bib re-sorted by BibTeX key")
sys.exit(0)
