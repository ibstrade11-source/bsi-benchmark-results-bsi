# Comparison: engineering

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 8799f32138a68f7b773b5be43423f6cbd061cb06
- run timestamp (UTC): 2026-08-14T15:25:12Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Morescient GAI for Software Engineering (Extended Version)

*source:* http://arxiv.org/abs/2406.04710v2
*doi:* 10.1145/3709354

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

The BSI analysis offers a more comprehensive, structured, and critical examination of the article, addressing latent mechanisms, evidence considerations, and methodological detail that the RAW analysis lacks. Consequently, BSI demonstrates superior analytical quality for this article.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Claim Clarity and Precision | 20 | 9.0 | 6.0 | 1.80 | 1.20 | The article’s main claims are explicitly enumerated in the RAW analysis, providing clear, concise statements. The BSI analysis presents a claim but does so in a more generalized, less precise manner. |
| Evidence Mapping | 15 | 2.0 | 5.0 | 0.30 | 0.75 | RAW offers no mapping of evidence to claims, whereas BSI references the need for observation platforms and open‑science principles, indicating some evidence consideration. |
| Methodological Insight | 15 | 5.0 | 7.0 | 0.75 | 1.05 | RAW outlines a high‑level roadmap but lacks detail; BSI provides a more detailed discussion of principles and a roadmap, though still high‑level. |
| Depth of Analysis (Mechanistic/Latent) | 20 | 2.0 | 8.0 | 0.40 | 1.60 | BSI explicitly discusses latent mechanisms, feedback loops, and causal compliance, whereas RAW does not address underlying mechanisms. |
| Structural Coherence and Organization | 10 | 4.0 | 9.0 | 0.40 | 0.90 | BSI employs tables, layered analysis, and structured sections, enhancing readability; RAW is a single paragraph. |
| Critical Evaluation / Gap Identification | 10 | 2.0 | 7.0 | 0.20 | 0.70 | BSI identifies missing details and suggests improvements; RAW makes no critical assessment. |
| Domain‑Specific Terminology and Contextualization | 10 | 6.0 | 7.0 | 0.60 | 0.70 | Both analyses mention GAI and software engineering, but BSI incorporates additional domain concepts such as semantics, syntax, and open‑science principles. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 4.45 |
| BSI | 6.90 |

#### Summary

- Winner: **bsi**
- Score difference: **+2.45**
- Criteria evaluated: **7**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
