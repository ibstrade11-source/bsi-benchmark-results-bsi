# Comparison: political science

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 6ae2f7dfe0a28c9921608e12a784aab71bb0f86e
- run timestamp (UTC): 2026-09-07T01:04:00Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Political Science and the Three New Institutionalisms

*source:* https://openalex.org/W1561018600
*doi:* https://doi.org/10.1111/j.1467-9248.1996.tb00343.x

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

The BSI evaluation demonstrates superior coverage across all article‑specific criteria, offering a more comprehensive, systematic, and insightful appraisal than the RAW analysis. Therefore, BSI is the winner.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Conceptual Clarity & Rigor | 30 | 6.0 | 9.0 | 1.80 | 2.70 | The RAW review merely lists the three schools without deep differentiation, whereas the BSI analysis explicitly dissects terminology and delineates precise boundaries of each approach. |
| Logical & Structural Coherence | 25 | 5.0 | 8.0 | 1.25 | 2.00 | RAW presents claims in a loose, non‑linear format; BSI follows a structured, step‑by‑step argument that logically builds from problem definition to synthesis. |
| Theoretical Grounding | 20 | 6.0 | 9.0 | 1.20 | 1.80 | RAW summarizes the schools but offers little engagement with their theoretical roots; BSI links each paradigm to its foundational critiques of behavioralism and situates them within broader academic debates. |
| Explanatory Depth | 15 | 5.0 | 8.0 | 0.75 | 1.20 | RAW lacks mechanistic explanations; BSI explicitly discusses underlying mechanisms (path dependency, transaction costs, cognitive scripts) and their causal roles. |
| Originality & Value Add | 10 | 5.0 | 9.0 | 0.50 | 0.90 | Both texts acknowledge the taxonomy, yet BSI’s assessment highlights the article’s enduring influence and its role in fostering cross‑paradigm integration. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 5.50 |
| BSI | 8.60 |

#### Summary

- Winner: **bsi**
- Score difference: **+3.10**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
