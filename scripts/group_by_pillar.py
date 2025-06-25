#!/usr/bin/env python3
"""
Read bib/bibliography.bib and emit docs/_tmp_references.md grouped by Pillar ID.
Each entry must have `keywords = {T#, ...}`.
"""

import re, textwrap, bibtexparser, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB = ROOT / "bib" / "bibliography.bib"
OUT = ROOT / "docs" / "_tmp_references.md"

PILLAR_NAMES = {
    "T1": "Foundations & Regulatory Context",
    "T2": "Algorithmic Advances",
    "T3": "Systems & Operational Implementations",
    "T4": "Data & Benchmark Resources",
    "T5": "Survey & Synthesis",
    "T6": "AI & Data-Driven Methods",
    "T7": "Extensions & Inter-Domain Innovations",
    "T8": "Emerging Frontiers",
}

def main():
    with open(BIB, encoding="utf8") as fh:
        db = bibtexparser.load(fh)

    grouped = {k: [] for k in PILLAR_NAMES}
    err = []

    for entry in db.entries:
        kw = entry.get("keywords", "")
        m = re.match(r"\s*(T[1-8])\b", kw)
        if not m:
            err.append(entry.get("ID"))
            continue
        pillar = m.group(1)
        grouped[pillar].append(entry)

    if err:
        sys.stderr.write("⚠️  Missing Pillar tag for: " + ", ".join(err) + "\n")
        sys.exit(1)

    with open(OUT, "w", encoding="utf8") as out:
        out.write("# Crew-Bidding & Scheduling References\n\n")
        for pid, entries in grouped.items():
            if not entries:               # skip empty sections
                continue
            out.write(f"## {pid} — {PILLAR_NAMES[pid]}\n\n")
            for e in sorted(entries, key=lambda x: (x.get("year","9999"), x["ID"])):
                line = f"- **{e.get('author','?')} ({e.get('year','?')})**. " \
                       f"*{e.get('title','?') }*."
                url = e.get("doi") or e.get("url")
                if url:
                    line += f" [{url}]({url})"
                out.write(textwrap.fill(line, width=90) + "\n")
            out.write("\n")

if __name__ == "__main__":
    main()
