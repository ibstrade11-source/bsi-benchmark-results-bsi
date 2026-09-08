# Comparison: id:1706.03762

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 2455185a98f823c38444459f6056b285c7ca8b4a
- run timestamp (UTC): 2026-08-30T16:43:45Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Attention Is All You Need

*source:* http://arxiv.org/abs/1706.03762v7

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

Both analyses are strong, but BSI’s structured, weighted critique and inclusion of methodological detail give it a measurable advantage over the more narrative RAW evaluation.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Innovation | 25 | 7.0 | 9.0 | 1.75 | 2.25 | RAW highlights novelty but lacks depth; BSI explicitly scores novelty and gives higher mark. |
| Empirical Strength | 20 | 8.0 | 9.0 | 1.60 | 1.80 | Both discuss BLEU gains; BSI provides detailed tables and ablation evidence. |
| Methodological Transparency | 15 | 6.0 | 8.0 | 0.90 | 1.20 | Raw omits many hyper‑parameter details; BSI lists full settings and code release. |
| Logical Coherence | 15 | 7.0 | 8.0 | 1.05 | 1.20 | BSI maps design choices to theory; RAW gives less structured rationale. |
| Impact | 20 | 9.0 | 10.0 | 1.80 | 2.00 | BSI quantifies generative influence (BERT, GPT, etc.); RAW mentions impact but less explicit. |
| Ethical Considerations | 5 | 3.0 | 6.0 | 0.15 | 0.30 | BSI acknowledges limited discussion and rates low; RAW gives no mention. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 7.25 |
| BSI | 8.75 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.50**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
