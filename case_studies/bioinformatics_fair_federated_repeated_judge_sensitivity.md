# Case Study: Bioinformatics / FAIR Federated Data Ecosystems — Repeated Judge Sensitivity

## Purpose

This case study records repeated evaluations of the same bioinformatics / FAIR
federated-data case to study run stability, judge sensitivity, winner changes,
and score-difference variance.

This is a methodological case study, not evidence of general BSI superiority.

## Case Identity

**Topic:** Bioinformatics / FAIR and Federated Data Ecosystems  
**Primary article:** *Towards FAIR and federated data ecosystems for interdisciplinary research*  
**DOI:** 10.1371/journal.pcbi.1013806  
**Generator:** `nvidia/nemotron-3-ultra-550b-a55b:free`  
**Judge:** Groq independent LLM judge

## Observed Evaluations

| Evaluation | Source file | RAW | BSI | Delta (BSI-RAW) | Winner | Criteria source | Retrieval |
|---|---|---:|---:|---:|---|---|---|
| E1 | `compare/bioinformatics_fair_federated_openrouter_groq_limit1.json` | 3.20 | 4.80 | +1.60 | TIE | llm | accepted |
| E2 | `compare/bioinformatics_fair_federated_openrouter_groq_repeat1.json` | 7.35 | 8.85 | +1.50 | BSI | llm | accepted |

## Repeated-Run Observation

The observed BSI-minus-RAW score difference changed from:

**+1.60 → +1.50**

Signed change:

**-0.10 points**

Absolute change:

**0.10 points**

Mean BSI-minus-RAW difference across the two evaluations:

**+1.55 points**

Observed outcomes:

- RAW wins: 0
- BSI wins: 1
- Ties: 1
- Winner changed: Yes (`tie` → `bsi`)

The incremental signal remained positive in both evaluations, while the
winner classification changed from `tie` to `bsi`.
This identifies a useful repeated-run judge-sensitivity case rather than a
stable general winner.

## Analytical Questions

1. What is the variance of the BSI-minus-RAW score difference?
2. How often does the winner change under matched repeated runs?
3. Does winner stability change with full-text availability?
4. Does generator choice affect the result?
5. Does judge configuration affect the result?
6. Are winner changes associated with different independently selected criteria?
7. Are observed differences attributable to the BSI analysis or to judge/run variance?
8. Does the positive incremental signal persist even when winner classification changes?

## Additional Samples

| Evaluation | Source file | Article / DOI | Generator | Judge | RAW | BSI | Delta | Winner | Criteria source | Full text | Retrieval |
|---|---|---|---|---|---:|---:|---:|---|---|---|---|
| E3 |  |  |  |  |  |  |  |  |  |  |  |
| E4 |  |  |  |  |  |  |  |  |  |  |  |
| E5 |  |  |  |  |  |  |  |  |  |  |  |

## Interpretation Boundary

A repeated-run winner must not be interpreted as proof of general BSI
superiority. The purpose of this case is to characterize stability,
sensitivity, and possible sources of variance before aggregate conclusions
are drawn.

In this case, the two matched runs preserve the same article, analyst model,
and judge family. The observed change therefore provides evidence of
run/judge sensitivity, while the persistence of a positive BSI-minus-RAW
difference provides a separate incremental-value signal. These two observations
must not be conflated.

## Evidence Log

New samples must preserve their original benchmark result files and record
their exact source paths here. Benchmark scores must not be manually
overwritten.

Current evidence:

- `compare/bioinformatics_fair_federated_openrouter_groq_limit1.json`
- `compare/bioinformatics_fair_federated_openrouter_groq_repeat1.json`
