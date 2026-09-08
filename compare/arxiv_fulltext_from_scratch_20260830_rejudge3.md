# Comparison: quantum physics

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: b0614be64885037c46eb26d7e0a25e195fef8f61
- run timestamp (UTC): 2026-08-30T23:35:13Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Physics Briefing Book

*source:* http://arxiv.org/abs/1910.11775v2

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** raw

RAW wins on overall analytical completeness, structural fidelity, and decision utility for this document type. BSI contributes a valuable limitation/risk lens and integration perspective that RAW misses, but its own gaps in structural granularity and accessibility prevent it from overtaking RAW as the more useful analysis.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Structural Completeness | 20 | 9.0 | 7.0 | 1.80 | 1.40 | RAW provides a detailed chapter-by-chapter table with domains and focus areas; BSI mentions 11 chapters and 8 domains but lacks granular structural mapping. |
| Process & Governance Transparency | 15 | 9.0 | 8.0 | 1.35 | 1.20 | RAW explicitly outlines the bottom-up flow, PPG/ESG/Council roles, and APPEC boundary; BSI covers the same flow but with less institutional detail. |
| Scientific Priority Articulation | 20 | 8.0 | 8.0 | 1.60 | 1.60 | Both extract HL-LHC, future colliders, precision/intensity frontiers, and dark sector; RAW organizes by time-horizon, BSI synthesizes in executive summary — comparable depth. |
| Cross-Domain Integration Analysis | 15 | 7.0 | 9.0 | 1.05 | 1.35 | RAW notes integration in TOC but does not analyze interplay; BSI explicitly highlights physics–accelerator–instrumentation–computing as a co-designed ecosystem. |
| Strategic Limitation & Risk Assessment | 15 | 4.0 | 8.0 | 0.60 | 1.20 | RAW barely mentions limitations (only theory uncertainties); BSI identifies consensus bias, missing failure scenarios, and unquantified programmatic uncertainties — a clear value add. |
| Decision Utility & Clarity | 15 | 8.0 | 7.0 | 1.20 | 1.05 | RAW's tabular structure and clear sections make it highly usable for quick reference; BSI's executive summary is strong but Persian/English mix and abstract scoring reduce accessibility. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 7.60 |
| BSI | 7.80 |

#### Summary

- Winner: **raw**
- Score difference: **+0.20**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
