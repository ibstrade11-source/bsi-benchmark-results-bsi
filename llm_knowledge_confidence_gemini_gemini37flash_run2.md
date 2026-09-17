# Comparison: 2401.13835 What Large Language Models Know and What People Think They Know

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-10T17:10:58Z
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

While RAW provides a crisp, metric-explicit summary of the paper's core claims, BSI delivers an advanced technical evaluation. It thoroughly investigates the recurrent architectural mechanics, visual-linguistic grounding dynamics, systemic limitations (such as detector dependencies and latency), and actionable research extensions.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Technical & Architectural Depth | 25 | 7.5 | 9.2 | 1.88 | 2.30 | RAW accurately captures the primary building blocks (ORIST, LSTM recurrent bridge, multi-task losses). BSI delves deeper into the exact mechanistic interplay, detailing the recurrent compression of the [CLS] token, the state transitions, and the POMDP decision-making formulation. |
| Methodological Contributions & Mechanistic Explanation | 25 | 8.0 | 9.0 | 2.00 | 2.25 | RAW provides a clean, well-structured breakdown of key contributions. BSI elaborates on how the combinatorial synthesis bridges the semantic resolution mismatch between panoptic scenes and linguistic referents. |
| Critical Evaluation of Limitations & Future Directions | 20 | 3.0 | 8.8 | 0.60 | 1.76 | RAW omits critical analysis, potential failure modes, or bottlenecks. BSI identifies key vulnerabilities such as heavy reliance on pretrained Faster R-CNN bounding boxes, latency overhead for physical robotics, and offers concrete forward paths (e.g., open-vocabulary CLIP/SAM, continuous space navigation). |
| Empirical Grounding & Benchmark Reporting | 15 | 9.0 | 7.5 | 1.35 | 1.12 | RAW specifically reports benchmark evaluation metrics (SPL, RGSPL, GP on REVERIE, NDH, R2R). BSI contextualizes empirical validity and datasets accurately but omits specific numerical metric outputs. |
| Systemic & Conceptual Synthesis | 15 | 6.5 | 9.0 | 0.97 | 1.35 | BSI contextualizes the work within embodied AI cognitive transitions (from reactive view matching to object-centric conceptual mapping) and models feedback loops for error correction, whereas RAW remains strictly descriptive. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 6.80 |
| BSI | 8.78 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.98**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
