# Comparison: public policy implementation empirical study

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 6ae2f7dfe0a28c9921608e12a784aab71bb0f86e
- run timestamp (UTC): 2026-09-06T18:48:25Z
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

The BSI evaluation offers deeper methodological detail, layered structural analysis, and higher explanatory power, surpassing the raw summary in all weighted criteria. Consequently, BSI is the superior analytical approach for this article.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Clarity and Precision of Claims | 25 | 6.0 | 9.0 | 1.50 | 2.25 | RAW lists core claims but lacks detailed definitions; BSI explicitly dissects claims with structured sub‑claims. |
| Depth of Evidence and Methodological Rigor | 20 | 5.0 | 8.0 | 1.00 | 1.60 | RAW cites literature synthesis but offers no methodological detail; BSI outlines snowball sampling, systematic review, and layering of evidence. |
| Explanatory and Mechanistic Breadth | 20 | 6.0 | 9.0 | 1.20 | 1.80 | RAW mentions five domains but stops at descriptive level; BSI maps latent mechanisms, feedback loops, and causal structures. |
| Practical Applicability and Usability | 15 | 7.0 | 9.0 | 1.05 | 1.35 | RAW notes CFIR's usage; BSI provides concrete examples of application and potential for formative evaluation. |
| Incremental Knowledge Contribution | 10 | 5.0 | 10.0 | 0.50 | 1.00 | RAW reproduces known framework; BSI assesses novelty, generative capacity, and epistemic value. |
| Structural Coherence Across Layers | 10 | 6.0 | 9.0 | 0.60 | 0.90 | RAW offers a single‑layer overview; BSI demonstrates manifest, latent, and meta layers, showing internal consistency. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 5.85 |
| BSI | 8.90 |

#### Summary

- Winner: **bsi**
- Score difference: **+3.05**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
