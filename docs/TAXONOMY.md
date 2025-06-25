# Evergreen Taxonomy for Crew-Bidding & Scheduling Research

| Pillar&nbsp;ID | Name                                   | Why it Exists / Scope (one-liner)                                                   | Typical Questions Answered                               |
|---------------|----------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------|
| **T1**        | Foundations & Regulatory Context       | Mathematical formulations, FAR/CAA rules, constraint typologies                     | “What are the baseline legal or optimisation constraints?” |
| **T2**        | Algorithmic Advances                   | Exact, heuristic, metaheuristic, lexicographic, multi-objective, decomposition      | “Which algorithms solved it best at the time?”           |
| **T3**        | Systems & Operational Implementations  | Real-world PBS deployments, integrated pairing-rostering engines, vendor white papers | “How did an airline or vendor make it work in production?” |
| **T4**        | Data & Benchmark Resources             | Public datasets, synthetic generators, simulation frameworks                        | “Where can I get test instances or evaluate my solver?”  |
| **T5**        | Survey & Synthesis                     | Literature reviews, taxonomies, meta-analyses                                       | “What’s the state-of-the-art as of 20XX?”                |
| **T6**        | AI & Data-Driven Methods               | Reinforcement learning, hyper-heuristics, predictive delay models, generative scheduling | “How is ML/AI augmenting or replacing classic optimisation?” |
| **T7**        | Extensions & Inter-Domain Innovations  | Robust/stochastic, equity/fatigue, fairness, disruption recovery, sustainability    | “How does the core model adapt to special goals or shocks?” |
| **T8**        | Emerging Frontiers                     | Concept papers, patents, preprints &lt; 3 yrs old (LLM co-pilots, quantum, digital twins) | “What might matter in five years?”                      |

---

## Level-2 Starter Tags  (`keywords` field)

| Pillar | Suggested Tags (comma-separated) |
|--------|----------------------------------|
| **T1** | formulation, regulation, constraint-set, duality, complexity |
| **T2** | exact, column-generation, benders, branch-price-and-cut, heuristic, metaheuristic, tabu, lexicographic, multiobjective |
| **T3** | preferential-bidding-system, integrated-crew-management, vendor-whitepaper, airline-case-study, decision-support-tool |
| **T4** | benchmark, dataset, simulator, open-data, instance-generator |
| **T5** | survey, systematic-review, taxonomy, bibliometric |
| **T6** | reinforcement-learning, hyper-heuristic, predictive-model, graph-neural-network, LLM, constraint-learning |
| **T7** | robust, stochastic, equity, fatigue, fairness, disruption-recovery, sustainability |
| **T8** | quantum, digital-twin, human-in-the-loop, edge-optimisation, realtime |

### Tagging Rules

1. **First token** in every `keywords` field must be a Pillar ID (`T1`…`T8`).  
2. Tags are lowercase, comma-separated. Re-use existing tags when possible.  
3. If you invent a new tag, add it to the table above in your PR.

### Tag Examples

```bibtex
keywords = {T3, preferential-bidding-system, airline-case-study}
keywords = {T6, reinforcement-learning, hyper-heuristic}

### Example Entry

```bibtex
@techreport{Tumpson2005OptimizedPBS,
  author   = {Tumpson, Daniel},
  title    = {Optimized Preferential Bidding Systems: Models and Implementations},
  year     = {2005},
  keywords = {T3, preferential-bidding-system, vendor-whitepaper}
}