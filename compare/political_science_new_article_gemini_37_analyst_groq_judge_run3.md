# Comparison: public policy implementation empirical study

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 6ae2f7dfe0a28c9921608e12a784aab71bb0f86e
- run timestamp (UTC): 2026-09-06T17:54:47Z
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

While RAW provides a concise overview, BSI delivers richer methodological detail, deeper theoretical integration, and actionable guidance, yielding a higher overall assessment.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Theoretical Integration Depth | 30 | 7.0 | 9.0 | 2.10 | 2.70 | BSI explicitly rates theoretical integration at 10 and describes synthesis of 10+ theories; RAW mentions integration but with less detail. |
| Methodological Rigor | 20 | 6.0 | 9.0 | 1.20 | 1.80 | BSI scores 9 for rigorous snowball sampling and systematic review; RAW does not discuss sampling or systematic methods. |
| Practical Actionability | 25 | 8.0 | 9.0 | 2.00 | 2.25 | Both note practical use, but BSI gives higher score and discusses actionable guidance for formative evaluations. |
| Clarity of Construct Definitions | 15 | 8.0 | 9.0 | 1.20 | 1.35 | BSI highlights explicit, operational definitions for 39 constructs; RAW mentions definitions but less emphasis. |
| Scope of Empirical Validation | 10 | 7.0 | 8.0 | 0.70 | 0.80 | BSI acknowledges subsequent empirical support; RAW does not detail validation evidence. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 7.20 |
| BSI | 8.90 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.70**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
