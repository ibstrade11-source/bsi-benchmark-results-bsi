# Comparison: MS25: Materials Science-Focused Benchmark Data Set for Machine Learning Interatomic Potentials

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-13T01:03:18Z
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

**Winner:** raw

RAW analysis is more accurate, faithful to the source article, and practically useful. BSI analysis introduces hallucinated specifics (exact training sizes, error thresholds, mechanistic loops, speedup factors) and generic template outputs that do not reflect the paper's actual content, reducing its reliability and incremental value.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Benchmark Scope Coverage | 20 | 9.0 | 7.0 | 1.80 | 1.40 | RAW accurately captures all 6 systems, 5 models, and dual evaluation (regression + physical observables). BSI covers scope but injects hallucinated specifics (e.g., '1000 images', exact error thresholds). |
| Key Finding Extraction | 20 | 9.0 | 6.0 | 1.80 | 1.20 | RAW correctly identifies equivariant advantage in complex systems, regression-observable discrepancy, transferability limits. BSI states main findings but fabricates mechanistic details (internal stress mechanism, hybrid interaction, error Q/A loops) not in the paper. |
| Limitation & Gap Identification | 15 | 8.0 | 7.0 | 1.20 | 1.05 | RAW notes HEA/Zr-O difficulty, zeolite transferability failure, MgO size-extensivity, documentation gaps. BSI identifies similar gaps but frames them through generic BSI template (EIG gaps) with some fabricated specifics. |
| Practical Actionability | 15 | 8.0 | 6.0 | 1.20 | 0.90 | RAW gives clear, paper-grounded recommendations (equivariant for complex systems, observable-level validation, failure-mode focus). BSI mixes paper recommendations with BSI-specific prescriptions (cost-function weighting, hybrid models) not clearly sourced from the article. |
| Methodological Fidelity | 10 | 8.0 | 5.0 | 0.80 | 0.50 | RAW faithfully represents the paper's experimental design. BSI hallucinates precise numbers (1000 training images, 15 meV/atom threshold, 2x speedup) and mechanisms (phonon fluctuations, automatic weight updates) absent from the source. |
| Analytical Depth | 10 | 7.0 | 6.0 | 0.70 | 0.60 | RAW provides solid summary-level analysis. BSI appears deeper with 3-layer analysis but the latent/meta layers contain fabricated mechanistic content, reducing genuine analytical value. |
| Clarity & Structure | 10 | 9.0 | 6.0 | 0.90 | 0.60 | RAW is well-organized, single-language, easy to follow. BSI mixes Persian/English, uses opaque BSI jargon, and presents fabricated details as factual analysis. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 8.40 |
| BSI | 6.25 |

#### Summary

- Winner: **raw**
- Score difference: **-2.15**
- Criteria evaluated: **7**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
