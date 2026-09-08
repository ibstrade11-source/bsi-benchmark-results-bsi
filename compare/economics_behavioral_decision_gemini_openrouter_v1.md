# Comparison: behavioral economics decision making

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-08T14:06:15Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: topic
- rejected candidates: 0

## Behavioral Economics and Marketing in Aid of Decision Making among the Poor

*source:* https://openalex.org/W1971430075
*doi:* https://doi.org/10.1509/jppm.25.1.8

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

BSI analysis substantially outperforms RAW across all criteria, particularly in mechanistic depth (cognitive bandwidth, feedback loops), critical gap identification (three specific epistemic gaps + compliance audit), and interdisciplinary synthesis detail. RAW provides a competent summary but lacks analytical depth, gap analysis, and structural evaluation. BSI's layered architecture and formal audit trail deliver genuine incremental epistemic value for this article type.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Interdisciplinary Synthesis Quality | 25 | 6.0 | 9.0 | 1.50 | 2.25 | RAW mentions the interdisciplinary bridge but only at surface level; BSI provides detailed combinatorial synthesis analysis across psychology, behavioral economics, and marketing communications with explicit integration mechanisms. |
| Policy Actionability Assessment | 20 | 7.0 | 9.0 | 1.40 | 1.80 | RAW identifies nudges and low-cost interventions; BSI goes further with specific leverage points (simplification, defaults, framing), implementation considerations, and sustainability concerns in improvement proposals. |
| Mechanistic Depth | 20 | 5.0 | 9.0 | 1.00 | 1.80 | RAW lists cognitive load/heuristics as labels; BSI's latent layer details cognitive bandwidth taxation, decision fatigue, present bias, and reinforcing feedback loops as operational mechanisms. |
| Critical Gap Identification | 15 | 3.0 | 9.0 | 0.45 | 1.35 | RAW offers no gap analysis; BSI provides structured EIG analysis with three specific epistemic gaps (generalization, causal vs correlation, structural) plus REIG compliance audit. |
| Structural Coherence | 10 | 8.0 | 9.0 | 0.80 | 0.90 | Both are well-structured; BSI's multi-layer architecture with manifest/latent/meta separation and formal audit trail provides superior analytical scaffolding. |
| Evidence Evaluation | 10 | 4.0 | 8.0 | 0.40 | 0.80 | RAW does not assess evidence; BSI explicitly scores empirical grounding (6.5/10), notes absence of new quantitative data, and includes measurement compliance verification. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 5.55 |
| BSI | 8.90 |

#### Summary

- Winner: **bsi**
- Score difference: **+3.35**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
