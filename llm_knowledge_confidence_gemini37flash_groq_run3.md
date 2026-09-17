# Comparison: 10.1038/s42256-024-00976-7

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-11T01:35:12Z
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
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

BSI provides a richer, more comprehensive, and more actionable analysis than RAW, thereby achieving a higher overall score and better supporting the article’s evaluation.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Empirical Rigor | 30 | 7.0 | 9.0 | 2.10 | 2.70 | Both analyses report controlled human‑participant experiments on multiple LLMs, but BSI presents detailed statistical controls, diverse datasets, and reproducible design, giving it a clear advantage. |
| Mechanistic Depth | 20 | 6.0 | 8.0 | 1.20 | 1.60 | BSI explicitly traces token‑probability to verbal uncertainty and discusses underlying cognitive heuristics, whereas RAW only mentions the phenomenon without mechanism. |
| Clarity & Coherence | 15 | 8.0 | 9.0 | 1.20 | 1.35 | BSI offers structured layers (manifest, latent, meta) and concise summaries; RAW is concise but less organized, leading to slightly lower clarity. |
| Practical Impact | 20 | 7.0 | 9.0 | 1.40 | 1.80 | BSI proposes a concrete mitigation (verbal alignment) with implementation details; RAW merely reports findings without actionable guidance. |
| Novelty & Insight | 10 | 7.0 | 8.0 | 0.70 | 0.80 | Both introduce calibration/discrimination gaps, but BSI frames them within cognitive science and provides richer theoretical framing. |
| Scope of Evaluation | 5 | 7.0 | 8.0 | 0.35 | 0.40 | BSI tests multiple models (GPT‑3.5, PaLM2, GPT‑4o) and two task types; RAW focuses only on a subset, slightly limiting scope. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 6.95 |
| BSI | 8.65 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.70**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
