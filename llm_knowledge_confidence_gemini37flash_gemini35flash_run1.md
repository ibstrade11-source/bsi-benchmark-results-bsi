# Comparison: 10.1038/s42256-024-00976-7

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-10T20:24:22Z
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

BSI delivers substantially greater analytic depth: it uncovers latent mechanisms (encoding-decoding disconnect, feedback loops), quantifies empirical-to-operational gaps (EIG), self-audits its own reasoning (REIG), and evaluates creative combinatorial synthesis. RAW is a competent executive summary but lacks mechanistic explanation, limitation analysis, and structural layering. BSI's incremental value is high for this article because the paper's central contribution — bridging computational probability distributions and human heuristic cognition — demands exactly the multi-layer causal analysis BSI provides.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Conceptual Clarity & Problem Framing | 20 | 8.0 | 9.0 | 1.60 | 1.80 | RAW clearly defines calibration/discrimination gaps concisely. BSI articulates core claim more precisely, distinguishing internal model calibration from human perceptual calibration, and frames the paradigm shift. |
| Empirical Evidence Coverage | 20 | 7.0 | 9.0 | 1.40 | 1.80 | RAW mentions datasets, models, and key findings but briefly. BSI details experimental design (factorial controls, behavioral data, token-likelihood measurement), multi-model evaluation, and methodological rigor. |
| Mechanistic & Structural Depth | 15 | 5.0 | 9.0 | 0.75 | 1.35 | RAW hints at fluency/length heuristics. BSI provides deep latent-layer analysis: fluency heuristic, length-implies-expertise bias, encoding-decoding disconnect, reinforcing/balancing feedback loops, and leverage points. |
| Practical Implications & Mitigation | 15 | 8.0 | 9.0 | 1.20 | 1.35 | RAW covers verbal uncertainty alignment mitigation well. BSI extends to generative capacity for self-calibrating NLG, prompt protocols, UI integration, and high-stakes decision contexts. |
| Limitations & Boundary Conditions | 10 | 3.0 | 9.0 | 0.30 | 0.90 | RAW does not discuss limitations. BSI provides dedicated EIG analysis (token-likelihood vs semantic truth, ecological validity, task complexity) and explicit limitation section. |
| Cross-disciplinary Synthesis | 10 | 6.0 | 9.0 | 0.60 | 0.90 | RAW mentions cognitive science connection in passing. BSI explicitly synthesizes cognitive heuristics (fluency, length bias) with transformer token probabilities and decision theory. |
| Structural Coherence & Organization | 10 | 8.0 | 9.0 | 0.80 | 0.90 | RAW has clean 3-section structure. BSI employs multi-layer architecture (manifest/latent/meta), EIG gap analysis, REIG self-audit, and creative value scoring — a more sophisticated epistemic structure. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 6.65 |
| BSI | 9.00 |

#### Summary

- Winner: **bsi**
- Score difference: **+2.35**
- Criteria evaluated: **7**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
