# Comparison: robot learning manipulation

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-09T15:41:58Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: topic
- rejected candidates: 0

## One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay

*source:* http://arxiv.org/abs/1711.10137v2

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

Across all article‑specific criteria, the BSI analysis consistently scores higher, offering deeper methodological insight, rigorous evaluation, and clearer documentation. The RAW analysis lacks these elements and therefore does not provide a competitive alternative.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Novelty | 25 | 6.0 | 9.0 | 1.50 | 2.25 | BSI highlights a distinct combination of interactive replay, frozen pretrained visual encoding, and stochastic observations that jointly address the data‑efficiency and reality‑gap problems. RAW only describes the idea without emphasizing the novel synthesis. |
| Methodological Rigor | 20 | 6.0 | 9.0 | 1.20 | 1.80 | BSI lists detailed ablation studies, a rigorous Rmin metric, and separate training/validation traversals. RAW lacks explicit ablations and does not report statistical confidence or hyper‑parameter sweeps. |
| Mechanistic Depth | 15 | 5.0 | 8.0 | 0.75 | 1.20 | BSI explains the inner workings of the pose graph world model, the role of frozen features, stochastic observation sampling, and bootstrapped Q exploration. RAW merely states the components without mechanistic linkage. |
| Generalizability | 15 | 5.0 | 6.0 | 0.75 | 0.90 | BSI shows zero‑shot transfer across days but only within a single map and fixed goal. RAW does not discuss transfer or generalisation at all, so the score is lower. |
| Ecological Validity | 10 | 6.0 | 9.0 | 0.60 | 0.90 | BSI reports real‑world deployment on a Pioneer robot with realistic lighting and dynamic obstacles. RAW mentions the robot but lacks detail on deployment conditions. |
| Transparency | 10 | 5.0 | 8.0 | 0.50 | 0.80 | BSI provides figures, algorithm pseudocode, and clear parameter tables. RAW is a narrative summary without concrete implementation details. |
| Incremental Value | 5 | 4.0 | 10.0 | 0.20 | 0.50 | BSI introduces a full pipeline that can be reused by other researchers; RAW does not convey such reusable insight. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 5.50 |
| BSI | 8.35 |

#### Summary

- Winner: **bsi**
- Score difference: **+2.85**
- Criteria evaluated: **7**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
