# Crew-Bidding & Scheduling Bibliography

[![CI](https://github.com/AgileAerosystems/crew-bidding-bibliography/actions/workflows/render.yml/badge.svg)](https://github.com/AgileAerosystems/crew-bidding-bibliography/actions/workflows/render.yml)

---

## 📚 Quick Pillar Directory (Evergreen Taxonomy)

| Pillar                                | Name                                   | View rendered                                      | Why it Exists / Scope                                             | Typical Questions Answered                               |
|---------------------------------------|----------------------------------------|----------------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------|
| [T1](T1-Foundations-and-Regulatory-Context.html)  | Foundations & Regulatory Context       | [Live](https://agileaerosystems.github.io/crew-bidding-bibliography/T1-Foundations-and-Regulatory-Context.html)  | Mathematical formulations, FAR/CAA rules, constraint typologies    | What are the baseline legal or optimisation constraints? |
| [T2](https://agileaerosystems.github.io/crew-bidding-bibliography/T2-Algorithmic-Advances.html)    | Algorithmic Advances                   | [Live](https://agileaerosystems.github.io/crew-bidding-bibliography/T2-Algorithmic-Advances.html)    | Exact, heuristic, metaheuristic, lexicographic, multi-objective, decomposition | Which algorithms solved it best at the time?            |
| [T3](T3-Systems-and-Operational-Implementations.html) | Systems & Operational Implementations  | [Live](https://agileaerosystems.github.io/crew-bidding-bibliography/T3-Systems-and-Operational-Implementations.html) | Real-world PBS deployments, integrated pairing-rostering engines, white papers | How did an airline or vendor make it work in production? |
| [T4](T4-Data-and-Benchmark-Resources.html)   | Data & Benchmark Resources             | [Live](https://agileaerosystems.github.io/crew-bidding-bibliography/T4-Data-and-Benchmark-Resources.html)   | Public datasets, synthetic generators, simulation frameworks      | Where can I get test instances or evaluate my solver?   |
| [T5](T5-Survey-and-Synthesis.html)    | Survey & Synthesis                     | [Live](https://agileaerosystems.github.io/crew-bidding-bibliography/T5-Survey-and-Synthesis.html)    | Literature reviews, taxonomies, meta-analyses                     | What’s the state-of-the-art as of 20XX?                 |
| [T6](T6-AI-and-Data-Driven-Methods.html)  | AI & Data-Driven Methods               | [Live](https://agileaerosystems.github.io/crew-bidding-bibliography/T6-AI-and-Data-Driven-Methods.html)  | RL, hyper-heuristics, predictive delay models, generative scheduling | How is ML/AI augmenting or replacing classic optimisation? |
| [T7](T7-Extensions-and-Inter-Domain-Innovations.html) | Extensions & Inter-Domain Innovations  | [Live](https://agileaerosystems.github.io/crew-bidding-bibliography/T7-Extensions-and-Inter-Domain-Innovations.html) | Robust/stochastic, equity/fatigue, fairness, disruption recovery, sustainability | How does the core model adapt to special goals or shocks? |
| [T8](T8-Emerging-Frontiers.html)      | Emerging Frontiers                     | [Live](https://agileaerosystems.github.io/crew-bidding-bibliography/T8-Emerging-Frontiers.html)      | LLM co-pilots, quantum, digital twins (preprints < 3 yrs)          | What might matter in five years?                         |




🌐 **Live references page:** <https://agileaerosystems.github.io/crew-bidding-bibliography/references.html>

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
