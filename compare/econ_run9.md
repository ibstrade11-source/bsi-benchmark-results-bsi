# Comparison: behavioral economics decision making

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 8ee511e177e146befd46c5115b950ba58339cab2
- run timestamp (UTC): 2026-08-29T16:24:39Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Quantum decision making by social agents

*source:* http://arxiv.org/abs/1202.4918v2
*doi:* 10.1142/S0219622014500564

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

Across all article‑specific criteria the BSI analysis consistently receives higher or equal scores, especially in empirical support, predictive power, and practical relevance. The BSI framework introduces a clear quantum‑decoherence mechanism for social attenuation of paradoxes and claims quantitative fits to experimental data, providing a substantive advance beyond the RAW description. Therefore the BSI analysis is the superior evaluation of the article.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Theoretical Novelty | 20 | 7.0 | 8.0 | 1.40 | 1.60 | Both analyses highlight the introduction of a density‑matrix framework for social decision making, but the BSI explicitly frames it as a quantum‑decoherence mechanism, giving it a marginal edge. |
| Empirical Support | 25 | 7.0 | 9.0 | 1.75 | 2.25 | The BSI references the Charness et al. (2010) data and claims quantitative fit; the RAW analysis also notes this but does not detail the fit, so BSI scores higher. |
| Mathematical Rigor | 20 | 8.0 | 9.0 | 1.60 | 1.80 | Both use Hilbert‑space notation; the BSI provides the full density‑matrix derivation and alternation law, slightly superior. |
| Predictive Power | 15 | 7.0 | 8.0 | 1.05 | 1.20 | BSI claims the interference‑alternation law is testable across paradoxes; RAW acknowledges this but does not stress it as a testable prediction. |
| Clarity of Mechanism | 10 | 8.0 | 9.0 | 0.80 | 0.90 | BSI’s discussion of decoherence and attraction factors is more detailed, offering a clearer causal story. |
| Practical Applicability | 10 | 6.0 | 8.0 | 0.60 | 0.80 | BSI suggests potential for designing group consultation protocols, whereas RAW remains largely theoretical. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 7.20 |
| BSI | 8.55 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.35**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
