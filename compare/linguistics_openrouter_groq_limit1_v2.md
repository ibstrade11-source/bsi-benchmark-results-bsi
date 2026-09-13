# Comparison: syntax semantics computational linguistics

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-13T00:13:38Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: topic
- rejected candidates: 0

## Information-based syntax and semantics

*source:* https://openalex.org/W2143745167

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

While RAW offers a clear and concise summary, the BSI analysis brings a richer, multidimensional perspective that enhances understanding of mechanisms, pedagogical implications, and evidence integration, thereby providing a higher incremental value for scholarly evaluation.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Coverage of Key Claims | 25 | 7.0 | 8.0 | 1.75 | 2.00 | The RAW analysis summarizes the main claims accurately and succinctly. The BSI analysis expands on these claims, adding additional detail about pedagogical implications and theoretical context, slightly improving coverage. |
| Depth of Mechanistic Explanation | 20 | 6.0 | 9.0 | 1.20 | 1.80 | RAW outlines the unification mechanism conceptually but stops short of detailing how feature structures operate. BSI provides a more elaborate mechanistic account, including explicit mentions of Head Feature Principle, Valence, and type hierarchies. |
| Evidence Integration | 15 | 7.0 | 6.0 | 1.05 | 0.90 | RAW lists empirical and theoretical sources in a straightforward manner. BSI integrates evidence in a more complex feedback-loop framework, but its presentation is denser, which may reduce immediate clarity. |
| Pedagogical Relevance | 15 | 8.0 | 9.0 | 1.20 | 1.35 | RAW notes the textbook impact and teaching context. BSI explicitly ties the analysis to pedagogical evolution, offering a stronger argument for educational relevance. |
| Structural Coherence and Organization | 10 | 9.0 | 7.0 | 0.90 | 0.70 | RAW is concise and well-organized. BSI, while thorough, includes extensive tables and feedback loops that can obscure the main narrative. |
| Innovativeness of Analysis Framework | 15 | 6.0 | 8.0 | 0.90 | 1.20 | RAW follows conventional summarization. BSI applies a structured evaluation framework (BSI), providing a novel lens and additional dimensions, thus scoring higher on innovativeness. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 7.00 |
| BSI | 7.95 |

#### Summary

- Winner: **bsi**
- Score difference: **+0.95**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
