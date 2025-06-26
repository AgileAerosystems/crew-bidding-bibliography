# Crew-Bidding & Scheduling Bibliography

[![CI](https://github.com/AgileAerosystems/crew-bidding-bibliography/actions/workflows/render.yml/badge.svg)](https://github.com/AgileAerosystems/crew-bidding-bibliography/actions/workflows/render.yml)

---

## 📚 Quick Pillar Directory (Evergreen Taxonomy)

| Pillar&nbsp;ID | Name                                   | Why it Exists / Scope (one-liner)                                            | Typical Questions Answered |
|---------------|----------------------------------------|-------------------------------------------------------------------------------|----------------------------|
| **T1** | Foundations & Regulatory Context       | Mathematical formulations, FAR/CAA rules, constraint typologies              | What are the baseline legal or optimisation constraints? |
| **T2** | Algorithmic Advances                   | Exact, heuristic, metaheuristic, lexicographic, multi-objective, decomposition| Which algorithms solved it best at the time? |
| **T3** | Systems & Operational Implementations  | Real-world PBS deployments, integrated pairing-rostering engines, white papers| How did an airline or vendor make it work in production? |
| **T4** | Data & Benchmark Resources             | Public datasets, synthetic generators, simulation frameworks                 | Where can I get test instances or evaluate my solver? |
| **T5** | Survey & Synthesis                     | Literature reviews, taxonomies, meta-analyses                                | What’s the state-of-the-art as of 20XX? |
| **T6** | AI & Data-Driven Methods               | RL, hyper-heuristics, predictive delay models, generative scheduling         | How is ML/AI augmenting or replacing classic optimisation? |
| **T7** | Extensions & Inter-Domain Innovations  | Robust/stochastic, equity/fatigue, fairness, disruption recovery, sustainability | How does the core model adapt to special goals or shocks? |
| **T8** | Emerging Frontiers                     | LLM co-pilots, quantum, digital twins (preprints &lt; 3 yrs)                  | What might matter in five years? |


🌐 **Live references page:** <https://agileaerosystems.github.io/crew-bidding-bibliography/references.html>

| [T2](T2-Algorithmic-Advances.html) | [Algorithmic Advances](T2-Algorithmic-Advances.html) |
|      |                             |
| [T7](T7-Extensions-and-Inter-Domain-Innovations.html) | [Extensions-and-Inter-Domain-Innovations](T7-Extensions-and-Inter-Domain-Innovations.html) |

**Status:** link-only mode, community-maintained  

Community BibTeX library for airline crew-bidding and crew-scheduling research.

---

## Quick-Start Tagging Guide

Each entry’s `keywords` field **must start** with a Pillar ID (`T1`–`T8`) and then comma-separated tags:

```bibtex
keywords = {T2, exact, lexicographic}
```
* **Full evergreen taxonomy → [docs/TAXONOMY.md](docs/TAXONOMY.md)**
* **Contribution rules   → [contributing.md](contributing.md)**
