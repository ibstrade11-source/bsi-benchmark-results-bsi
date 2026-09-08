# Comparison: Fostering implementation of health services research findings into practice: a consolidated framework for advancing implementation science

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 6ae2f7dfe0a28c9921608e12a784aab71bb0f86e
- run timestamp (UTC): 2026-09-07T11:13:02Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Fostering implementation of health services research findings into practice: a consolidated framework for advancing implementation science

*source:* https://openalex.org/W2020155291
*doi:* https://doi.org/10.1186/1748-5908-4-50

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

The BSI analysis scores higher across all substantive criteria, particularly in mechanistic depth and transparency. It also provides a comprehensive latent‑layer evaluation that the RAW summary lacks. Therefore, BSI is the clearer choice for a more thorough, evidence‑grounded understanding of the article. 

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Theoretical Innovation | 25 | 8.5 | 9.0 | 2.12 | 2.25 | Both analyses highlight CFIR as a novel synthesis of prior frameworks; BSI gives higher score for depth of conceptual integration. |
| Methodological Rigor | 20 | 7.5 | 8.5 | 1.50 | 1.70 | RAW notes systematic review and snowball sampling; BSI explicitly rates methodological rigor and notes sampling details. |
| Practical Utility | 15 | 8.0 | 9.5 | 1.20 | 1.43 | Both note applicability, but BSI gives higher due to detailed discussion of pragmatic tools. |
| Causal & Mechanistic Depth | 10 | 6.5 | 8.5 | 0.65 | 0.85 | RAW mentions multi-level context but lacks explicit causal mechanisms; BSI highlights latent mechanisms and feedback loops. |
| Translational Impact | 10 | 8.0 | 8.5 | 0.80 | 0.85 | Both consider real-world implementation; BSI provides richer analysis of implementation pathways. |
| Transparency & Falsifiability | 10 | 7.0 | 8.0 | 0.70 | 0.80 | BIS explicitly rates transparency and discusses limits of causal claims. |
| Overall Coherence | 10 | 8.0 | 9.0 | 0.80 | 0.90 | Both show logical flow; BSI gives higher score for structural coherence and layering. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 7.77 |
| BSI | 8.78 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.01**
- Criteria evaluated: **7**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
