# Comparison: exoplanet atmosphere characterization

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-14T19:52:50Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: topic
- rejected candidates: 0

## The CoRoT Exoplanet program : status & results

*source:* http://arxiv.org/abs/1105.1887v1
*doi:* 10.1051/epjconf/20111101001

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** raw

RAW presents more comprehensive quantitative coverage and clearer links to broader exoplanet science, giving it a marginal advantage over BSI.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Coverage of Instrumental Status | 25 | 8.0 | 7.0 | 2.00 | 1.75 | RAW gives a detailed mission timeline and hardware issue description; BSI touches on it but less detailed. |
| Depth of Exoplanet Characterisation | 20 | 9.0 | 8.0 | 1.80 | 1.60 | Both analyses cover planet properties, but RAW lists mass‑radius and activity impacts explicitly; BSI is more qualitative. |
| Discussion of Detection Biases | 15 | 8.0 | 9.0 | 1.20 | 1.35 | BSI emphasizes RV selection bias and transit advantage more sharply than RAW. |
| Analysis of Follow‑up Strategy | 15 | 7.0 | 8.0 | 1.05 | 1.20 | BSI outlines the multi‑step follow‑up pipeline, RAW mentions it briefly. |
| Contextualisation of Results in Exoplanet Science | 25 | 9.0 | 7.0 | 2.25 | 1.75 | RAW explicitly links CoRoT to ground‑based transition and population gaps; BSI focuses on methodological points. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 8.30 |
| BSI | 7.65 |

#### Summary

- Winner: **raw**
- Score difference: **-0.65**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
