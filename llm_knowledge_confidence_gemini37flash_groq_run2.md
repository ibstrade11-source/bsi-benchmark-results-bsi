# Comparison: 10.1038/s42256-024-00976-7

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-10T20:27:44Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: topic
- rejected candidates: 0

## What large language models know and what people think they know

*source:* https://openalex.org/W4406679533
*doi:* https://doi.org/10.1038/s42256-024-00976-7

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | heuristic_fallback |
| Score scale | 0-10 |
| Weight sum | 100 |

#### Judge Reasoning

**Winner:** bsi

No LLM judge was available or its response could not be parsed -- this result is from a fixed keyword-presence heuristic, not an independent LLM judgement. Treat it as a placeholder, not a real evaluation.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| structural_layers | 30 | 0.0 | 10.0 | 0.00 | 3.00 | Presence of analytical layers |
| epistemic_separation | 20 | 10.0 | 0.0 | 2.00 | 0.00 | Fact / inference / speculation separation |
| uncertainty_awareness | 20 | 10.0 | 10.0 | 2.00 | 2.00 | Recognition of uncertainty |
| evidence_grounding | 15 | 6.0 | 8.0 | 0.90 | 1.20 | Grounding in evidence |
| analysis_depth | 15 | 10.0 | 10.0 | 1.50 | 1.50 | Analytical coverage |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 6.40 |
| BSI | 7.70 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.30**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
