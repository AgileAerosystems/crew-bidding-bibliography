#!/usr/bin/env python3
"""
Generate docs/_tmp_references.md grouped by Pillar ID
(+ CSS + taxonomy table). Each BibTeX entry must start its `keywords`
with a Pillar tag {T1-T8}.  Pandoc later converts the MD to HTML.
"""

import re, textwrap, bibtexparser, pathlib, sys, hashlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB  = ROOT / "bib"  / "bibliography.bib"
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

CSS = """
<style>
/* widen GitHub-Pages default column */
.markdown-body { max-width: 95vw; margin: 2rem auto; font-family: sans-serif; }

/* table layout */
table              { width: 100%; table-layout: fixed; border-collapse: collapse; }
th, td             { padding: 0.45rem 0.6rem; border: 1px solid #ccc; }
th:nth-child(1),
td:nth-child(1)    { text-align:center; width:12%;  }
th:nth-child(2),
td:nth-child(2)    {                      width:18%; }
th:nth-child(3),
td:nth-child(3)    {                      width:25%; }
th:nth-child(4),
td:nth-child(4)    {                      width:45%; }

@media (max-width: 600px){
  table { display:block; overflow-x:auto; }
}
</style>
"""

TAXONOMY_TABLE = """
| Pillar&nbsp;ID | Name                                   | Why it Exists / Scope (one-liner)                                            | Typical Questions Answered |
|---------------|----------------------------------------|-------------------------------------------------------------------------------|----------------------------|
| **T1** | Foundations & Regulatory Context       | Mathematical formulations, FAR/CAA rules, constraint typologies              | What are the baseline legal or optimisation constraints? |
| **T2** | Algorithmic Advances                   | Exact, heuristic, metaheuristic, lexicographic, multi-objective, decomposition| Which algorithms solved it best at the time? |
| **T3** | Systems & Operational Implementations  | Real-world PBS deployments, integrated pairing-rostering engines, white papers| How did an airline or vendor make it work in production? |
| **T4** | Data & Benchmark Resources             | Public datasets, synthetic generators, simulation frameworks                 | Where can I get test instances or evaluate my solver? |
| **T5** | Survey & Synthesis                     | Literature reviews, taxonomies, meta-analyses                                | What’s the state-of-the-art as of 20XX? |
| **T6** | AI & Data-Driven Methods               | RL, hyper-heuristics, predictive delay models, generative scheduling         | How is ML/AI augmenting or replacing classic optimisation? |
| **T7** | Extensions & Inter-Domain Innovations  | Robust/stochastic, equity/fatigue, fairness, disruption recovery, sustainability | How does the core model adapt to special goals or shocks? |
| **T8** | Emerging Frontiers                     | LLM co-pilots, quantum, digital twins (preprints < 3 yrs)                     | What might matter in five years? |
"""

def main():
    with open(BIB, encoding="utf8") as fh:
        db = bibtexparser.load(fh)

    grouped, missing = {k: [] for k in PILLAR_NAMES}, []
    for entry in db.entries:
        m = re.match(r"\s*(T[1-8])\b", entry.get("keywords", ""))
        if not m:
            missing.append(entry["ID"]); continue
        grouped[m.group(1)].append(entry)

    if missing:
        sys.stderr.write("⚠️  Missing Pillar tag for: " + ", ".join(missing) + "\n")
        sys.exit(1)

    with open(OUT, "w", encoding="utf8") as out:
        # H1 title is handled by pandoc’s --metadata title; no duplicate here
        out.write(CSS + "\n")
        out.write(TAXONOMY_TABLE + "\n\n")

        for pid, entries in grouped.items():
            if not entries: continue
            out.write(f"## {pid} — {PILLAR_NAMES[pid]}\n\n")
            for e in sorted(entries, key=lambda x: (x.get("year","9999"), x["ID"])):
                line = f"- **{e.get('author','?')} ({e.get('year','?')})**. *{e.get('title','?')}*."
                url  = e.get("doi") or e.get("url")
                if url: line += f" [{url}]({url})"
                out.write(textwrap.fill(line, width=90) + "\n")
            out.write("\n")

if __name__ == "__main__":
    main()

