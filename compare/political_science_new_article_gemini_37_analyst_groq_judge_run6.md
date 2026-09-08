# Comparison: public policy implementation empirical study

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 6ae2f7dfe0a28c9921608e12a784aab71bb0f86e
- run timestamp (UTC): 2026-09-07T01:00:42Z
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

The BSI analysis demonstrates superior depth, methodological clarity, and practical guidance, justifying selection of the BSI analysis as the winner.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Comprehensiveness | 25 | 8.0 | 9.0 | 2.00 | 2.25 | Both analyses cover the CFIR’s five domains and 37 constructs, but the BSI analysis provides a more detailed breakdown of construct numbers and domain functions, offering a fuller mapping. |
| Methodological Clarity | 20 | 8.0 | 8.5 | 1.60 | 1.70 | The RAW summary mentions systematic synthesis but lacks detail on sampling and coding. BSI cites snowball sampling and explicit criteria, improving transparency. |
| Practical Applicability | 20 | 8.5 | 9.5 | 1.70 | 1.90 | RAW highlights general use of CFIR for diagnosis; BSI explicitly links CFIR to operational tools, stakeholder engagement, and feedback loops, giving practitioners clearer guidance. |
| Theoretical Integration | 15 | 7.5 | 9.0 | 1.12 | 1.35 | RAW lists domain structures but does not deeply discuss underlying mechanisms or causal loops; BSI delves into latent mechanisms, feedback loops, and critical realism, providing deeper theory. |
| Innovation | 20 | 8.0 | 9.0 | 1.60 | 1.80 | Both present CFIR, but BSI adds novel discussion of generative capacity, combinatorial synthesis, and epistemic gap targeting, which RAW omits. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 8.02 |
| BSI | 9.00 |

#### Summary

- Winner: **bsi**
- Score difference: **+0.98**
- Criteria evaluated: **5**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
