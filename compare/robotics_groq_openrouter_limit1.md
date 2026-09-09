# Comparison: robot learning manipulation

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-09T23:38:48Z
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

BSI provides a substantially richer epistemic evaluation: it identifies a Measurement Compliance failure (missing confidence intervals, unspecified success rates), decomposes novelty via CreativeValueAdd, maps mechanistic feedback loops across Manifest/Latent/Meta layers, and quantifies information gain sources. RAW remains a faithful but unevaluated extraction. The incremental analytical value of BSI over RAW is high for this article.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Technical Accuracy & Fidelity | 20 | 8.0 | 7.0 | 1.60 | 1.40 | RAW accurately extracts claims, methods, and results from the paper with high fidelity. BSI captures the main ideas but introduces some framework-driven details (e.g., Bayesian Optimization at Meta layer) not present in the source article. |
| Critical Depth & Evaluation | 20 | 3.0 | 8.0 | 0.60 | 1.60 | RAW is purely extractive with no critical assessment. BSI explicitly identifies limitations (statistical analysis gaps, reproducibility concerns, measurement compliance failure via REIG audit) and evaluates epistemic robustness beyond the paper's self-reporting. |
| Structural Coherence & Organization | 15 | 8.0 | 9.0 | 1.20 | 1.35 | Both are well-organized. RAW uses clean tables and sections. BSI imposes a rigorous multi-layer ontology (Manifest/Latent/Meta), standardized scoring tables, and audit trails that enhance navigability and logical traceability. |
| Methodological Insight | 15 | 5.0 | 8.0 | 0.75 | 1.20 | RAW highlights methodological choices (pose graph, frozen encoder, bootstrapped Q-learning) but does not analyze their interplay. BSI's layering reveals feedback loops, leverage points, memory mechanisms, and how augmentation interacts with the encoder—insights not explicit in RAW. |
| Reproducibility & Transparency Assessment | 10 | 4.0 | 8.0 | 0.40 | 0.80 | RAW notes code unavailability in passing. BSI scores reproducibility (10/20), flags it as a weakness, and includes it in the final recommendations—making the assessment actionable. |
| Generalization & Transfer Evaluation | 10 | 5.0 | 8.0 | 0.50 | 0.80 | RAW reports the zero-shot claim without scrutinizing evidence. BSI's EIG analysis quantifies information gain from augmentation, CreativeValueAdd targets the data-scarcity epistemic gap, and REIG checks Generalization Compliance (PASS) while flagging Measurement Compliance (FAIL). |
| Novelty & Contribution Assessment | 10 | 5.0 | 8.0 | 0.50 | 0.80 | RAW lists contributions descriptively. BSI's CreativeValueAdd explicitly weights Epistemic Gap Targeting (35%), Combinatorial Synthesis (40%), and Generative Capacity (25%), scoring each—providing a principled novelty decomposition. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 5.55 |
| BSI | 7.95 |

#### Summary

- Winner: **bsi**
- Score difference: **+2.40**
- Criteria evaluated: **7**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
