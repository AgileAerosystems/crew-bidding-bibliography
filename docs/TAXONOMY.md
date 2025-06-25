# Evergreen Taxonomy for Crew-Bidding & Scheduling

| Pillar ID | Name                              | Scope (one-line)                                  | Example Tags                           |
|-----------|-----------------------------------|---------------------------------------------------|----------------------------------------|
| **T1**    | Foundations & Regulatory Context | Formulations, FAR/EASA constraints, complexity    | formulation, regulation, constraint-set|
| **T2**    | Algorithmic Advances             | Exact, heuristic, lexicographic, multi-objective  | exact, column-generation, tabu         |
| **T3**    | Systems & Operational Impl.      | Real PBS tools, airline case studies              | preferential-bidding-system, case-study|
| **T4**    | Data & Benchmark Resources       | Public datasets, simulators, synthetic instances  | benchmark, dataset, open-data          |
| **T5**    | Survey & Synthesis               | Literature reviews, taxonomies, meta-analyses     | survey, systematic-review              |
| **T6**    | AI & Data-Driven Methods         | RL, hyper-heuristics, GNN, LLM                    | reinforcement-learning, GNN, LLM        |
| **T7**    | Extensions & Inter-Domain        | Robust/stochastic, equity, fatigue, disruption    | robust, equity, disruption-recovery    |
| **T8**    | Emerging Frontiers               | Quantum, real-time co-pilots, digital twins       | quantum, digital-twin, realtime        |

## Tagging Rules
1. First token **must** be a Pillar ID (`T1`…`T8`).  
2. Tags are lower-case, comma-separated. Re-use existing tags when possible.  
3. Add new tags sparingly—update this file when you do.

### Tag Examples

```bibtex
keywords = {T3, preferential-bidding-system, airline-case-study}
keywords = {T6, reinforcement-learning, hyper-heuristic}
