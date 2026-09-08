# Comparison: engineering

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 8799f32138a68f7b773b5be43423f6cbd061cb06
- run timestamp (UTC): 2026-08-14T15:11:57Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Morescient GAI for Software Engineering (Extended Version)

*source:* http://arxiv.org/abs/2406.04710v2
*doi:* 10.1145/3709354

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

BSI provides a more comprehensive and detailed analysis, with a stronger theoretical foundation and methodological soundness

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Novelty and Originality | 20 | 8.0 | 9.0 | 1.60 | 1.80 | BSI provides a more detailed and innovative framework |
| Methodological Soundness | 25 | 6.0 | 8.0 | 1.50 | 2.00 | BSI provides more detailed and sound methodologies |
| Practical Applicability | 20 | 7.0 | 8.0 | 1.40 | 1.60 | BSI provides more feasible and applicable ideas |
| Theoretical Foundation | 15 | 5.0 | 8.0 | 0.75 | 1.20 | BSI provides a stronger theoretical foundation |
| Clarity and Coherence | 10 | 8.0 | 9.0 | 0.80 | 0.90 | BSI provides a clear, coherent, and well-structured presentation |
| Evaluation and Validation | 10 | 4.0 | 7.0 | 0.40 | 0.70 | BSI provides more comprehensive evaluation and validation |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 6.45 |
| BSI | 8.20 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.75**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
