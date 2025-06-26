#!/usr/bin/env python3
"""
Generate docs/_tmp_references.md grouped by Pillar ID.

• Reads docs/TAXONOMY.md, extracts the first Markdown table (until the
  first '---' separator), and inserts it under the title.
• Adds <link rel="stylesheet" href="style.css"> so GitHub Pages uses
  the external CSS you placed in style.css.
• Fails if any BibTeX entry lacks a Pillar tag (T1–T8).
"""

import re, textwrap, pathlib, sys, bibtexparser

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB  = ROOT / "bib"  / "bibliography.bib"
TAX  = ROOT / "docs" / "TAXONOMY.md"
OUT  = ROOT / "docs" / "_tmp_references.md"

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

# ---------------------------------------------------------------------
# Helper: return the first Markdown table in TAXONOMY.md
# ---------------------------------------------------------------------
def load_taxonomy_table() -> str:
    lines, collecting = [], False
    for line in TAX.read_text(encoding="utf8").splitlines():
        if line.strip().startswith("|"):
            collecting = True
            lines.append(line)
        elif collecting:
            break                       # stop at first non-table line
    return "\n".join(lines) + "\n\n"

# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():
    db = bibtexparser.load(open(BIB, encoding="utf8"))

    grouped, missing = {k: [] for k in PILLAR_NAMES}, []
    for entry in db.entries:
        m = re.match(r"\s*(T[1-8])\b", entry.get("keywords", ""))
        if not m:
            missing.append(entry["ID"])
            continue
        grouped[m.group(1)].append(entry)

    if missing:
        sys.stderr.write("❌ Missing Pillar tag for: " + ", ".join(missing) + "\n")
        sys.exit(1)

    with open(OUT, "w", encoding="utf8") as out:
        # H1 comes from pandoc --metadata title.  Add stylesheet link.
        out.write('<link rel="stylesheet" href="style.css">\n\n')
        out.write(load_taxonomy_table())

        # Write each Pillar section
        for pid in PILLAR_NAMES:
            entries = grouped[pid]
            if not entries:
                continue
            out.write(f"## {pid} — {PILLAR_NAMES[pid]}\n\n")
            for e in sorted(entries, key=lambda x: (x.get("year","9999"), x["ID"])):
                url = e.get("doi") or e.get("url") or ""
                bullet = f"- **{e.get('author','?')} ({e.get('year','?')})**. *{e.get('title','?')}*."
                if url:
                    bullet += f" [{url}]({url})"
                out.write(textwrap.fill(bullet, width=95) + "\n")
            out.write("\n")

if __name__ == "__main__":
    main()
