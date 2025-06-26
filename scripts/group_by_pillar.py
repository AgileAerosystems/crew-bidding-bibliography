#!/usr/bin/env python3
"""
Generate Markdown files grouped by Pillar.

• docs/_tmp_references.md      – full page (taxonomy table + all pillars)
• docs/_tmp_T1.md … _tmp_T8.md – one page per pillar (no taxonomy table)

The workflow converts these to references.html and T1.html … T8.html.
"""

import re, textwrap, pathlib, sys, bibtexparser

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB  = ROOT / "bib"  / "bibliography.bib"
TAX  = ROOT / "docs" / "TAXONOMY.md"
OUT_ALL  = ROOT / "docs" / "_tmp_references.md"
OUT_PILLAR = ROOT / "docs" / "_tmp_{pid}.md"

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
# Helpers
# ---------------------------------------------------------------------
def load_taxonomy_table():
    lines, collecting = [], False
    for line in TAX.read_text(encoding="utf8").splitlines():
        if line.strip().startswith("|"):
            collecting = True
            lines.append(line)
        elif collecting:
            break
    return "\n".join(lines) + "\n\n"

def write_pillar_md(pid, entries):
    """Write docs/_tmp_T#.md."""
    path = OUT_PILLAR.with_name(f"_tmp_{pid}.md")
    with open(path, "w", encoding="utf8") as out:
        out.write('<link rel="stylesheet" href="style.css">\n\n')
        out.write(f"# {pid} — {PILLAR_NAMES[pid]}\n\n")
        for e in entries:
            bullet = f"- **{e.get('author','?')} ({e.get('year','?')})**. *{e.get('title','?')}*."
            url = e.get("doi") or e.get("url") or ""
            if url:
                bullet += f" [{url}]({url})"
            out.write(textwrap.fill(bullet, width=95) + "\n")
        out.write("\n")

# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():
    db = bibtexparser.load(open(BIB, encoding="utf8"))
    grouped = {k: [] for k in PILLAR_NAMES}
    missing = []

    for e in db.entries:
        m = re.match(r"\s*(T[1-8])\b", e.get("keywords", ""))
        if not m:
            missing.append(e["ID"])
            continue
        grouped[m.group(1)].append(e)

    if missing:
        sys.stderr.write("❌ Missing Pillar tag for: " + ", ".join(missing) + "\n")
        sys.exit(1)

    # Write all-in-one page
    with open(OUT_ALL, "w", encoding="utf8") as out:
        out.write('<link rel="stylesheet" href="style.css">\n\n')
        out.write(load_taxonomy_table())
        for pid in PILLAR_NAMES:
            if not grouped[pid]:
                continue
            out.write(f"## {pid} — {PILLAR_NAMES[pid]}\n\n")
            for e in grouped[pid]:
                url = e.get("doi") or e.get("url") or ""
                bullet = f"- **{e.get('author','?')} ({e.get('year','?')})**. *{e.get('title','?')}*."
                if url:
                    bullet += f" [{url}]({url})"
                out.write(textwrap.fill(bullet, width=95) + "\n")
            out.write("\n")

    # Write per-pillar pages
    for pid in PILLAR_NAMES:
        if grouped[pid]:
            write_pillar_md(pid, grouped[pid])

if __name__ == "__main__":
    main()
