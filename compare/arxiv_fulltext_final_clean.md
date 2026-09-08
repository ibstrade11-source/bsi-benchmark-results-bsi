# Comparison: quantum physics

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: b0614be64885037c46eb26d7e0a25e195fef8f61
- run timestamp (UTC): 2026-08-30T19:05:47Z
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

RAW analysis is superior across all criteria: it correctly categorizes the document, accurately describes the governance pipeline, identifies the Briefing Book's strategic function as a translation layer, acknowledges limitations without forcing an inappropriate epistemic score, and presents findings in clear, structured English. BSI's analysis suffers from language barrier, text corruption, and a fundamental category error—applying an epistemic robustness framework to a procedural document that makes no knowledge claims. The BSI score of 46/100 is misleading and adds no interpretive value beyond RAW's clearer qualitative assessment.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Document Type Identification | 20 | 10.0 | 9.0 | 2.00 | 1.80 | RAW explicitly identifies this as a 'governance charter abstract' and 'procedural policy document' with zero scientific content. BSI identifies it as procedural/governance but the Persian text has encoding corruption in reasoning fields. |
| Process Description Accuracy | 20 | 10.0 | 8.0 | 2.00 | 1.60 | RAW cleanly describes the four-stage bottom-up pipeline (community input, PPG curation, Briefing Book synthesis, ESG strategy formulation, Council ratification). BSI references the stages but reasoning text is corrupted. |
| Purpose/Function Analysis | 15 | 9.0 | 7.0 | 1.35 | 1.05 | RAW identifies the Briefing Book as the critical 'translation layer' between scientific proposals and political/funding decisions. BSI mentions this function but less clearly due to language barrier and corruption. |
| Limitations Recognition | 15 | 10.0 | 9.0 | 1.50 | 1.35 | Both correctly note zero scientific content and meta-document nature. RAW states it more directly; BSI notes 'lack of epistemic claims' and 'no generative capacity' but in corrupted text. |
| Strategic Significance | 10 | 9.0 | 6.0 | 0.90 | 0.60 | RAW articulates why the governance model matters: procedural transparency, community ownership, legitimacy for funding decisions, model for large-scale prioritization. BSI touches on legitimacy but less comprehensively. |
| Analytical Clarity/Structure | 10 | 10.0 | 5.0 | 1.00 | 0.50 | RAW uses clear English sections (Document Type, Main Claims, Contribution, Limitations, Conclusion). BSI uses a structured table but reasoning fields contain garbled characters ('那些那些那些'), making evaluation difficult. |
| Freedom from Hallucination | 10 | 10.0 | 9.0 | 1.00 | 0.90 | Neither analysis invents physics content. RAW stays strictly within the abstract. BSI stays within scope but the corruption introduces noise. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 9.75 |
| BSI | 7.80 |

#### Summary

- Winner: **raw**
- Score difference: **-1.95**
- Criteria evaluated: **7**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
