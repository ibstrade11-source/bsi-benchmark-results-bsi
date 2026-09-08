# Comparison: quantum physics

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: b0614be64885037c46eb26d7e0a25e195fef8f61
- run timestamp (UTC): 2026-08-30T19:21:26Z
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

RAW correctly treats the Physics Briefing Book abstract as a procedural document, describes its governance pipeline accurately and completely, flags its limitations honestly, and delivers a clear, usable analysis. BSI misapplies an epistemic-robustness rubric, producing a low score that reflects category error rather than document quality, and presents a partial, less accessible output. RAW is superior on every article-specific criterion.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Correct identification of document type and epistemic status | 25 | 9.0 | 8.0 | 2.25 | 2.00 | RAW explicitly identifies this as a procedural/policy abstract with zero scientific content, calling it a 'governance charter abstract.' BSI also identifies it as procedural/governance but frames the low score as a BSI-framework limitation ('not a deficiency in writing'). RAW's characterization is more direct and reader-useful. |
| Accuracy and completeness in describing the governance process | 20 | 9.0 | 7.0 | 1.80 | 1.40 | RAW clearly outlines the 4-stage pipeline (community input, PPG curation, Briefing Book synthesis, ESG strategy formulation, Council ratification) with specific body names. BSI mentions the stages but in a more compressed, less detailed manner; the Persian text cuts off mid-table. |
| Recognition of the document's purpose, function, and limitations | 20 | 9.0 | 6.0 | 1.80 | 1.20 | RAW explicitly states the document's role as 'translation layer' between scientific proposals and political/funding decisions, notes procedural transparency and legitimacy functions, and clearly flags 'zero scientific content' and 'meta-document' limitations. BSI notes the implicit claim of bottom-up legitimacy but does not articulate the interface/translation function as clearly. |
| Appropriateness of analytical framework for a procedural document | 15 | 8.0 | 5.0 | 1.20 | 0.75 | RAW uses a fit-for-purpose descriptive framework (document type, claims/process, contribution, limitations, conclusion). BSI forces the document into an epistemic-robustness rubric (7 BSI criteria, weighted scores) yielding a 46/100 that mostly reflects category mismatch rather than document quality. RAW's approach is more appropriate for the artifact. |
| Clarity, readability, and utility for a decision-maker or reader | 10 | 9.0 | 6.0 | 0.90 | 0.60 | RAW is concise, well-structured in English, and immediately actionable. BSI is partially in Persian, the table is truncated, and the scoring exercise adds noise without insight for this document type. |
| Avoidance of category errors (treating procedural content as epistemic claim) | 10 | 9.0 | 5.0 | 0.90 | 0.50 | RAW never mistakes the governance description for a knowledge claim. BSI's rubric explicitly penalizes the document for lacking 'epistemic claim, theoretical innovation, conceptual synthesis, generative capacity'—treating absence of epistemic content as a demerit rather than a category fact. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 8.85 |
| BSI | 6.45 |

#### Summary

- Winner: **raw**
- Score difference: **-2.40**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
