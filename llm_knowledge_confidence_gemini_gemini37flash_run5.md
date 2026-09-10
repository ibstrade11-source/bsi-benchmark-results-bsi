# Comparison: 10.1038/s42256-024-00976-7

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-10T19:27:55Z
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

**Winner:** raw

While BSI offers valuable structural layering and critical meta-evaluation regarding human cognitive heuristics, RAW delivers a superior, highly granular, and complete technical breakdown of the paper's methodology, specific datasets, model comparisons, and experimental 3x3 manipulations.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Conceptual Precision & Core Metric Definitions | 25 | 9.5 | 9.0 | 2.38 | 2.25 | RAW explicitly defines Model Confidence, Human Confidence, Calibration Gap, and Discrimination Gap with exact mathematical and cognitive delineations. BSI accurately captures these concepts in its executive summary and deep layering, though in slightly more condensed terms. |
| Methodological & Experimental Granularity | 25 | 9.5 | 7.5 | 2.38 | 1.88 | RAW provides exhaustive experimental specifics, detailing the exact models (GPT-3.5, PaLM2, GPT-4o), datasets (MMLU, Trivia QA), and the 3x3 manipulation matrix (uncertainty levels x explanation length). BSI provides a solid overview and mentions MMLU, but omits specific dataset breakdowns and experimental design nuances. |
| Empirical Findings & Mechanistic Insights | 25 | 9.5 | 8.5 | 2.38 | 2.12 | RAW clearly articulates the three core empirical findings: baseline overestimation, the length bias heuristic, and gap reduction via verbal calibration prompts. BSI covers the core findings well and highlights the psychological mechanism of verbosity heuristics. |
| Critical Epistemic Evaluation & Structural Layering | 25 | 7.5 | 9.0 | 1.88 | 2.25 | BSI excels in structural synthesis, categorizing the findings across manifest, latent (psychological feedback loop), and meta layers, while providing an audit and identifying contextual limitations (e.g., cross-cultural perception, high-stakes domain extensions). RAW focuses on factual summarization. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 9.02 |
| BSI | 8.50 |

#### Summary

- Winner: **raw**
- Score difference: **-0.52**
- Criteria evaluated: **4**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
