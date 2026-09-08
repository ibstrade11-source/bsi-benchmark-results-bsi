# Comparison: public policy implementation empirical study

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 6ae2f7dfe0a28c9921608e12a784aab71bb0f86e
- run timestamp (UTC): 2026-09-06T01:31:39Z
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

While RAW provides a polished, highly accurate summary of CFIR's core claims and domains, BSI delivers deeper analytical and evaluative value. BSI models latent organizational mechanisms and feedback loops, conducts a structured gap analysis (EIG), and provides critical evaluation of methodological limitations (such as snowball sampling and empirical validation needs) that RAW completely omits.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Fidelity & Core Content Representation | 25 | 9.0 | 7.5 | 2.25 | 1.88 | RAW accurately represents the paper's 2009 thesis, 5 domains, and formative evaluation utility without distortion. BSI captures the core constructs (5 domains, 33 constructs) well, but misattributes the publication year to 2023. |
| Mechanistic & Systemic Depth | 25 | 6.8 | 8.8 | 1.70 | 2.20 | RAW focuses on summarizing claims and domains at the manifest descriptive level. BSI adds significant mechanistic depth by modeling latent feedback loops (e.g., leadership-culture reinforcement, resource constraints) and identifying organizational leverage points. |
| Critical Appraisal & Methodological Limitations | 20 | 6.0 | 8.5 | 1.20 | 1.70 | RAW provides purely constructive synthesis with zero critical evaluation. BSI explicitly identifies methodological limitations of the framework's derivation (snowball sampling bias, lack of baseline empirical testing in the conceptual paper, potential reductionism). |
| Taxonomic Clarity & Structural Utility | 15 | 8.5 | 8.0 | 1.27 | 1.20 | RAW cleanly organizes the claims and contributions into actionable thematic buckets. BSI provides structured multi-layer decomposition and gap analysis (EIG), though it includes a noticeable Persian translation error in its criteria table ('جنسیت' instead of 'کیفیت' for Quality). |
| Actionable Generative Guidance | 15 | 7.0 | 8.2 | 1.05 | 1.23 | RAW articulates pragmatic utility for formative evaluation. BSI extends this by proposing concrete forward-looking recommendations (empirical validation studies, software instrumentation, broadened sampling methodologies). |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 7.47 |
| BSI | 8.21 |

#### Summary

- Winner: **bsi**
- Score difference: **+0.74**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
