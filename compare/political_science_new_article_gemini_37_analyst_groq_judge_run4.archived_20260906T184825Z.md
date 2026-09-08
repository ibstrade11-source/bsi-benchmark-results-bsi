# Comparison: public policy implementation empirical study

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 6ae2f7dfe0a28c9921608e12a784aab71bb0f86e
- run timestamp (UTC): 2026-09-06T18:05:10Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Fostering implementation of health services research findings into practice: a consolidated framework for advancing implementation science

*source:* https://openalex.org/W2020155291
*doi:* https://doi.org/10.1186/1748-5908-4-50

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

The BSI scores outperform the RAW scores across all six criteria, yielding a net advantage of 0.5 points. The BSI analysis provides a richer, layer‑wise evaluation and higher scores, justifying the decision to select the BSI evaluation as the winner.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Clarity & Definition | 20 | 8.0 | 9.5 | 1.60 | 1.90 | Both analyses highlight CFIR’s well‑defined 37 constructs, but the BSI analysis explicitly enumerates them and discusses inter‑construct relationships, giving a marginal clarity advantage. |
| Empirical Support | 15 | 8.0 | 9.0 | 1.20 | 1.35 | The RAW review notes limited direct empirical testing of CFIR, whereas the BSI analysis acknowledges the empirical roots of constituent theories and rates support accordingly. |
| Structural Validity | 20 | 8.5 | 9.5 | 1.70 | 1.90 | BSI explicitly assesses the five‑domain architecture and its internal consistency, while RAW merely states its existence. |
| Generalizability | 15 | 8.0 | 8.5 | 1.20 | 1.27 | Both analyses agree CFIR is broadly applicable, but BSI mentions potential adaptations for non‑clinical settings. |
| Practical Utility | 20 | 8.5 | 9.5 | 1.70 | 1.90 | BSI gives concrete examples of CFIR’s use in formative evaluations and tool development, giving a practical edge. |
| Innovation & Synthesis | 10 | 8.0 | 9.0 | 0.80 | 0.90 | BSI evaluates the novel integration of diverse theories, whereas RAW merely describes the consolidation. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 8.20 |
| BSI | 9.22 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.02**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
