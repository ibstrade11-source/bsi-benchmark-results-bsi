# Comparison: MS25: Materials Science-Focused Benchmark Data Set for Machine Learning Interatomic Potentials

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-13T00:43:45Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: title
- selected title: MS25: Materials Science-Focused Benchmark Data Set for Machine Learning Interatomic Potentials
- selected candidate rank: 1
- title match score: 1.0
- acceptance threshold: 0.72
- rejected candidates: 0

## MS25: Materials Science-Focused Benchmark Data Set for Machine Learning Interatomic Potentials

*source:* https://openalex.org/W4412789389
*doi:* https://doi.org/10.1021/acs.jcim.5c01262

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

BSI provides a clearer, more detailed, and actionable framework for evaluating MLIPs in complex materials contexts, outperforming the raw analysis in depth and practical applicability.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Comprehensive Coverage of Materials Complexity | 30 | 7.0 | 9.0 | 2.10 | 2.70 | RAW notes diverse domains but BSI explicitly emphasizes disordered alloys and reactive events; BSI scores higher. |
| Observable‑Centric Validation Emphasis | 25 | 7.0 | 10.0 | 1.75 | 2.50 | RAW mentions observable validation; BSI foregrounds it as core claim and methodology, thus higher. |
| Architecture Guidance and Practical Decision Matrix | 20 | 6.0 | 8.0 | 1.20 | 1.60 | RAW gives heuristic; BSI elaborates actionable matrix, thus better. |
| Benchmark Dataset Novelty and Gap Bridging | 15 | 8.0 | 7.0 | 1.20 | 1.05 | RAW highlights novelty; BSI acknowledges but less detailed; RAW slightly higher. |
| Clarity and Structured Presentation | 10 | 7.0 | 6.0 | 0.70 | 0.60 | RAW is concise and well‑organized; BSI is verbose Persian narrative with some repetition. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 6.95 |
| BSI | 8.45 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.50**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
