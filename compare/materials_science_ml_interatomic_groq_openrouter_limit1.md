# Comparison: MS25: Materials Science-Focused Benchmark Data Set for Machine Learning Interatomic Potentials

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-13T00:58:34Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: title
- selected title: MS25: Materials Science-Focused Benchmark Data Set for Machine Learning Interatomic Potentials
- selected candidate rank: 1
- title match score: 1.0
- acceptance threshold: 0.72
- rejected candidates: 0

## MS25: Materials Science-Focused Benchmark Data Set for Machine Learning Interatomic Potentials

*source:* https://openalex.org/W4412789389
*doi:* https://doi.org/10.1021/acs.jcim.5c01262

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** bsi

BSI provides a substantially deeper epistemic evaluation: it quantifies robustness across seven criteria, decomposes claims into manifest/latent/meta layers, identifies concrete epistemic gaps (EIG), and validates compliance (REIG). RAW is a clear, practitioner-oriented summary but lacks any epistemic robustness assessment, gap analysis, or structural decomposition. The incremental value of BSI is high for meta-scientific evaluation, though RAW remains more accessible for immediate practical decisions.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Benchmark Dataset Quality & Diversity Assessment | 20 | 8.0 | 9.0 | 1.60 | 1.80 | RAW covers the 6 systems and 5 architectures clearly; BSI's Manifest layer adds explicit note on limited HEA/Zr-O sample size (1000 images) as a dataset weakness. |
| Model Comparison Rigor (Equivariant vs Non-Equivariant) | 15 | 7.0 | 8.0 | 1.05 | 1.20 | RAW states the 1.5–2× equivariant advantage; BSI's Latent layer explains the mechanistic feedback loop (error → equivariance optimization) and leverage points for architecture design. |
| Physical Observable Evaluation (Error–Observable Disconnect) | 20 | 8.0 | 7.0 | 1.60 | 1.40 | RAW highlights the disconnect as a main claim with concrete examples (lattice constants, reaction barriers); BSI acknowledges it in Accuracy/Validity but rates the analysis of error→observable impact as insufficient. |
| Transferability & Generalization Analysis | 15 | 7.0 | 8.0 | 1.05 | 1.20 | RAW notes CHA→MFI failure and MgO size-extensivity; BSI's Latent layer frames transferability as a feedback loop with Domain Adaptation leverage point and notes the analysis is limited to two frameworks. |
| Epistemic Robustness Assessment | 10 | 4.0 | 9.0 | 0.40 | 0.90 | RAW provides no epistemic framework; BSI delivers a full 7-criterion epistemic evaluation, EIG gap analysis, REIG compliance check, and multi-layer decomposition. |
| Practical Guidance Utility for Practitioners | 10 | 8.0 | 7.0 | 0.80 | 0.70 | RAW gives concise actionable guidelines (prioritize equivariance, consider MD integration, cost vs RMSE); BSI's recommendations are more academic (expand data, hybrid models, domain adaptation). |
| Gap Identification & Future Research Directions | 10 | 6.0 | 9.0 | 0.60 | 0.90 | RAW implies gaps in the takeaway; BSI explicitly lists three weaknesses, four improvement proposals, CreativeValueAdd scoring, and EIG-driven research agenda. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 7.10 |
| BSI | 8.10 |

#### Summary

- Winner: **bsi**
- Score difference: **+1.00**
- Criteria evaluated: **7**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
