# Comparison: social capital community trust inequality

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 024b97bfb660473e5170d398bbc2ddb79f5db5a8
- run timestamp (UTC): 2026-08-13T12:50:13Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Social Capital: Implications for Development Theory, Research, and Policy

*source:* https://openalex.org/W2109745229
*doi:* https://doi.org/10.1093/wbro/15.2.225

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

Both analyses capture the article's substantive content equally well. BSI edges out RAW due to superior clarity and readability (structured headings, bullet points), which modestly improves accessibility for diverse audiences without adding new substantive content. Weighted scoring reflects this modest advantage.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Comprehensiveness of coverage | 25 | 8.0 | 8.0 | 2.00 | 2.00 | A review article's primary value lies in how thoroughly it captures the field's main claims, approaches, and policy implications; thus comprehensiveness carries the highest weight. |
| Conceptual clarity and definitional precision | 20 | 8.0 | 8.0 | 1.60 | 1.60 | Clear definition of social capital is foundational for any synthesis; weight reflects its importance but slightly less than overall coverage. |
| Identification and evaluation of distinct approaches | 20 | 9.0 | 9.0 | 1.80 | 1.80 | The article's central contribution is distinguishing four research approaches; correctly identifying and evaluating them is crucial, warranting a high weight. |
| Synthesis quality and policy relevance (synergy view) | 20 | 8.0 | 8.0 | 1.60 | 1.60 | The article's main analytical advance is the synergy view and its policy implications; synthesis quality directly determines practical usefulness. |
| Clarity and readability of presentation | 15 | 7.0 | 9.0 | 1.05 | 1.35 | Readability affects accessibility for scholars, practitioners, and policymakers; important but secondary to substantive content. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 8.05 |
| BSI | 8.35 |

#### Summary

- Winner: **bsi**
- Score difference: **+0.30**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
