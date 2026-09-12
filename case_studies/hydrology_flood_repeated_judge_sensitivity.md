# Case Study: Hydrology / Flood Forecasting — Repeated Judge Sensitivity

## Purpose

This case study collects repeated evaluations of the same or closely matched
hydrology / flood-forecasting benchmark case in order to study:

- repeated-run stability
- judge sensitivity
- RAW vs BSI winner flips
- score-difference variance
- criteria-source effects
- retrieval/full-text effects
- generator/judge configuration effects

This is a methodological case study, not evidence of general BSI superiority.

## Case Identity

**Topic:** Hydrology / Flood Forecasting  
**Primary article:** *Climate Change Forecasting Using Deep Learning*  
**DOI:** 10.36713/epra18552

## Observed Evaluations

| Evaluation | Source file | RAW | BSI | Delta (BSI-RAW) | Winner | Criteria source | Retrieval |
|---|---|---:|---:|---:|---|---|---|
| E1 | `compare/hydrology_flood_crossref_openrouter_groq_limit1.archived_20260912T030205Z.md` | 4.45 | 1.75 | -2.70 | RAW | llm | accepted |
| E2 | `compare/hydrology_flood_crossref_openrouter_groq_limit1.md` | 3.40 | 6.35 | +2.95 | BSI | llm | accepted |

## Initial Repeated-Run Observation

For the same case, the observed score difference changed from:

**-2.70 → +2.95**

Absolute change in score difference:

**5.65 points**

Observed outcome:

- RAW wins: 1
- BSI wins: 1
- Ties: 0

This is insufficient to establish a stable winner. It is evidence of
run/judge sensitivity that should be investigated with additional matched
evaluations.

## Analytical Questions

1. How large is the variance of the BSI-minus-RAW score difference?
2. How often does the winner flip?
3. Does winner stability change with full-text availability?
4. Does generator choice affect the result?
5. Does judge configuration affect the result?
6. Are winner flips associated with different independently selected criteria?
7. Are observed differences attributable to BSI analysis or to judge/run variance?

## Additional Samples

| Evaluation | Source file | Article / DOI | Generator | Judge | RAW | BSI | Delta | Winner | Criteria source | Full text | Retrieval |
|---|---|---|---|---|---:|---:|---:|---|---|---|---|
| E3 |  |  |  |  |  |  |  |  |  |  |  |
| E4 |  |  |  |  |  |  |  |  |  |  |  |
| E5 |  |  |  |  |  |  |  |  |  |  |  |

## Interpretation Boundary

A repeated-run winner should not be interpreted as proof of general BSI
superiority. The purpose of this case is to characterize stability,
sensitivity, and possible sources of variance before aggregate conclusions
are drawn.

## Evidence Log

New samples should preserve the original benchmark result files and record
their exact source paths here. Do not manually overwrite benchmark scores.
