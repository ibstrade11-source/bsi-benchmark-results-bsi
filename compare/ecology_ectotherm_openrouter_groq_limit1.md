# Comparison: Ecology

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-14T19:26:19Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: topic
- rejected candidates: 0

## Predicting the fundamental thermal niche of ectotherms

*source:* https://openalex.org/W4393995029
*doi:* https://doi.org/10.1002/ecy.4289

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

Across all weighted criteria, the BSI analysis achieves higher scores due to its explicit mechanistic detail, broader empirical discussion, and clear novelty. The RAW analysis, while accurate in summarizing the article’s claims, lacks the depth and transparency present in the BSI assessment.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Conceptual Rigor & Theoretical Coherence | 25 | 8.0 | 9.5 | 2.00 | 2.38 | Both analyses articulate a clear mechanistic framework, but the BSI analysis explicitly details the causal chain from thermal physiology to population dynamics and highlights internal consistency, earning a higher score. |
| Empirical Support & Validation | 20 | 6.0 | 7.0 | 1.20 | 1.40 | The RAW analysis reports empirical testing but lacks depth. The BSI analysis acknowledges a single case study yet discusses data quality, uncertainty, and cross‑taxon validation, providing a marginal advantage. |
| Methodological Innovation & Novelty | 20 | 5.0 | 9.0 | 1.00 | 1.80 | BSI presents a fully mechanistic, trait‑based modeling paradigm that moves beyond correlative SDMs, a major innovation not captured in the RAW analysis. |
| Practical Relevance & Policy Utility | 15 | 7.0 | 9.0 | 1.05 | 1.35 | Both analyses note conservation relevance, but the BSI analysis explicitly links predictions to invasion windows and climate‑adaptation strategies, scoring higher. |
| Reproducibility & Falsifiability | 10 | 6.0 | 8.5 | 0.60 | 0.85 | BSI provides detailed equations and mentions data/code availability, whereas RAW offers only a conceptual outline. |
| Epistemic Transparency & Assumption Clarity | 10 | 7.0 | 8.0 | 0.70 | 0.80 | BSI explicitly lists core assumptions (temperature‑dependent density dependence, no evolution, etc.), giving it a slight edge. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 6.55 |
| BSI | 8.58 |

#### Summary

- Winner: **bsi**
- Score difference: **+2.03**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
