# Comparison: What large language models know and what people think they know

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-10T19:09:29Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: topic
- rejected candidates: 0

## The Road to Know-Where: An Object-and-Room Informed Sequential BERT for Indoor Vision-Language Navigation

*source:* http://arxiv.org/abs/2104.04167v2

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

While RAW provides exact quantitative scores across benchmarks that BSI omits in numeric detail, BSI significantly outperforms RAW in critical evaluation, failure mode analysis (cascading detector error, spatial discretization, temporal decay), and concrete engineering recommendations for embodied navigation.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Architectural and Methodological Decomposition | 25 | 8.0 | 9.0 | 2.00 | 2.25 | Both analyses clearly describe the ORIST architecture (Faster R-CNN object bounding boxes, Sequential BERT combining Transformer self-attention with recurrent memory, and room/direction multi-task heads). BSI provides a slightly deeper breakdown of information flow and the role of the [CLS] bottleneck. |
| Benchmark Results & Empirical Precision | 20 | 9.0 | 7.0 | 1.80 | 1.40 | RAW provides exact quantitative performance figures across the standard VLN benchmarks (REVERIE SPL/RGSPL, NDH Goal Progress, R2R SPL). BSI mentions the benchmark names and qualitative success but lacks specific numeric score metrics. |
| Critical Failure Modes and Limitation Analysis | 25 | 5.0 | 9.0 | 1.25 | 2.25 | RAW provides a purely descriptive summary without identifying failure modes. BSI provides strong critical evaluation of offline detector dependency, 4-quadrant spatial discretization limitations, long-horizon temporal drift, and computational footprint. |
| Systemic and Epistemic Contextualization | 15 | 6.0 | 9.0 | 0.90 | 1.35 | BSI examines the shift from reactive scene-matching to symbolic-spatial cognitive mapping within Embodied AI and POMDP dynamics, detailing positive feedback and compounding error dynamics. |
| Actionable Technical Recommendations | 15 | 4.0 | 9.0 | 0.60 | 1.35 | RAW offers no future directions or architectural fixes. BSI suggests concrete technical advancements such as open-vocabulary detector integration (e.g., CLIP) and continuous action space policy networks. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 6.55 |
| BSI | 8.60 |

#### Summary

- Winner: **bsi**
- Score difference: **+2.05**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
