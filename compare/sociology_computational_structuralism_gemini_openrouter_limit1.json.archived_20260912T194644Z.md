# Comparison: Computational structuralism: Toward a formal theory of meaning in the age of digital intelligence

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-12T19:17:35Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: title
- selected title: Computational structuralism: Toward a formal theory of meaning in the age of digital intelligence
- selected candidate rank: 1
- title match score: 1.0
- acceptance threshold: 0.72
- rejected candidates: 3

### Rejected retrieval candidates

| Rank | Match score | Status | Title |
|---:|---:|---|---|
| 3 | 0.2125 | rejected_lower_match | Application and theory gaps during the rise of Artificial Intelligence in Education |
| 2 | 0.1082 | rejected_lower_match | A Survey on Explainable Artificial Intelligence (XAI): Toward Medical XAI |
| 4 | 0.1007 | rejected_lower_match | Explainable Artificial Intelligence (XAI): What we know and what is left to attain Trustworthy Artificial Intelligence |

## Computational structuralism: Toward a formal theory of meaning in the age of digital intelligence

*source:* https://openalex.org/W7152568811
*doi:* https://doi.org/10.1007/s11186-026-09685-z

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

BSI outperforms RAW on every article-specific criterion, especially mechanistic explanation depth (+5), critical gap engagement (+7), and formal rigor assessment (+5). RAW provides only a surface summary; BSI delivers a multi-layered epistemic evaluation with self-audit, gap analysis, and generative assessment appropriate for a theoretical synthesis claim.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Theoretical Synthesis Quality | 20 | 6.0 | 9.0 | 1.20 | 1.80 | RAW mentions the three components (structuralism, DL, info theory) but does not analyze their integration. BSI explicitly maps Saussurean relations to vector spaces, details the three-way synthesis, and evaluates its coherence (Conceptual Coherence 8.8). |
| Mechanistic Explanation Depth | 20 | 4.0 | 9.0 | 0.80 | 1.80 | RAW states meaning arises from 'compressing redundancies into latent structural representations' without mechanism. BSI's latent layer details compression optimization in continuous latent spaces, co-occurrence/substitution as geometric realization of Saussurean relations, and two feedback loops (Pattern Reinforcement, Self-Referential Semantics). |
| Critical Engagement with Gaps | 15 | 2.0 | 9.0 | 0.30 | 1.35 | RAW identifies no fundamental problems. BSI's EIG analysis explicitly addresses the Symbol Grounding Problem (internal relations vs. intentionality/first-person experience) and the quantitative-to-qualitative formalization gap, scoring Critical Resilience 8.8. |
| Formal/Mathematical Rigor Assessment | 15 | 3.0 | 8.0 | 0.45 | 1.20 | RAW notes 'formal vocabulary' claim uncritically. BSI's Methodological Precision (7.5) and Meta layer note formalization tools 'remain at theoretical proposal stage,' and EIG flags the quantitative-to-qualitative gap. |
| Generative Research Potential | 10 | 4.0 | 8.0 | 0.40 | 0.80 | RAW vaguely mentions 'formal vocabulary for studying systems.' BSI's CVA Generative Capacity (78) and recommendations specify formal principles for latent transformations and post-structuralist integration for hallucination modeling. |
| Structural Coherence of Analysis | 10 | 7.0 | 9.0 | 0.70 | 0.90 | RAW is clear but thin. BSI maintains consistency across manifest/latent/meta layers, seven criteria table, CVA table, EIG, REIG, and recommendations—all mutually reinforcing. |
| Epistemic Honesty/Humility | 10 | 8.0 | 9.0 | 0.80 | 0.90 | RAW is factual and restrained. BSI's REIG audit explicitly passes Causal/Generalization/Measurement/Framing compliance, frames LLM success as 'proof of concept' not definitive proof, and avoids false certainty. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 4.65 |
| BSI | 8.75 |

#### Summary

- Winner: **bsi**
- Score difference: **+4.10**
- Criteria evaluated: **7**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
