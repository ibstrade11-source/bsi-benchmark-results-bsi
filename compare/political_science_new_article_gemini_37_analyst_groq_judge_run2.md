# Comparison: public policy implementation empirical study

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 6ae2f7dfe0a28c9921608e12a784aab71bb0f86e
- run timestamp (UTC): 2026-09-06T17:35:58Z
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

The BSI analysis provides a richer, multi‑layered evaluation that captures conceptual, methodological, and practical dimensions more comprehensively than the RAW analysis. While both recognize the framework’s importance, BSI’s systematic scoring, latent‑layer insight, and explicit value‑add justify its superiority in this comparison.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Conceptual Integration | 30 | 8.0 | 9.0 | 2.40 | 2.70 | Raw analysis notes fragmentation and need for unified framework; BSI explicitly evaluates integration and scores high. Weight reflects centrality of integration to article. |
| Methodological Transparency | 20 | 6.0 | 8.0 | 1.20 | 1.60 | Raw mentions snowball sampling but not detail; BSI provides detailed sampling rationale and methodological critique. Weight based on importance of clear method. |
| Practical Applicability | 25 | 7.0 | 9.0 | 1.75 | 2.25 | Both note usefulness, but BSI gives higher score for pragmatic tool claim and applicability across settings. Weight reflects relevance to practice. |
| Theoretical Depth | 15 | 7.0 | 8.0 | 1.05 | 1.20 | Both discuss domains and constructs; BSI provides deeper mechanistic discussion and latent layer analysis. Weight reflects importance but less than others. |
| Empirical Support | 10 | 7.0 | 7.0 | 0.70 | 0.70 | Both provide limited empirical evidence in abstract; equal scores. Weight modest because article focuses on framework construction. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 7.10 |
| BSI | 8.45 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.35**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
