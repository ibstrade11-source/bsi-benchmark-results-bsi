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

## Cross-Domain Repeated-Run Samples

The following prior benchmark runs were selected automatically from the canonical `compare/` result set using the same methodological logic as this case study. They are comparative methodological samples, not additional evidence of general framework superiority.

### Physics Briefing Book
- Runs analyzed: **8**
- Delta range: **-2.40 → 2.15**
- Mean delta: **-0.22**
- Winner classification changes: **Yes**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `arxiv_fulltext_final_clean.json` | 9.75 | 7.80 | -1.95 | raw | low |
| `arxiv_fulltext_final_clean_judge2.json` | 8.85 | 6.45 | -2.40 | raw | negative |
| `arxiv_fulltext_from_scratch_20260830.json` | 8.05 | 8.75 | 0.70 | bsi | high |
| `arxiv_fulltext_from_scratch_20260830_rejudge.json` | 8.05 | 8.75 | 0.70 | bsi | high |
| `arxiv_fulltext_from_scratch_20260830_rejudge2.json` | 8.50 | 6.95 | -1.55 | raw | low |
| `arxiv_fulltext_from_scratch_20260830_rejudge3.json` | 7.60 | 7.80 | 0.20 | raw | medium |
| `arxiv_quantum_physics_groq_groq_single.json` | 6.40 | 8.55 | 2.15 | bsi | medium |
| `quantum_single.json` | 7.10 | 7.45 | 0.35 | bsi | medium |

### Philosophy Enters the Optics Laboratory: Bell's Theorem
- Runs analyzed: **11**
- Delta range: **-6.65 → 2.00**
- Mean delta: **-0.13**
- Winner classification changes: **Yes**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `fresh_philosophy_of_mind.json` | 6.20 | 8.20 | 2.00 | bsi | medium |
| `philosophy_openrouter_groq_limit1.json` | 7.20 | 8.60 | 1.40 | bsi | medium |
| `philosophy_openrouter_groq_limit1.json.json` | 7.75 | 7.56 | -0.19 | raw | unknown |
| `philosophy_openrouter_groq_limit1_v4.json` | 8.53 | 8.28 | -0.25 | tie | medium |
| `philosophy_openrouter_groq_limit1_v5.json` | 7.45 | 8.28 | 0.83 | bsi | high |
| `philosophy_rejudge1.json` | 7.50 | 7.50 | 0.00 | raw | medium |
| `philosophy_rejudge2.json` | 7.50 | 8.18 | 0.68 | bsi | medium |
| `philosophy_run1.json` | 7.15 | 5.90 | -1.25 | raw | low |
| `philosophy_run2.json` | 6.65 | 0.00 | -6.65 | raw | negative |
| `philosophy_run3.json` | 7.80 | 8.07 | 0.27 | raw | medium |
| `philosophy_run4.json` | 6.25 | 7.95 | 1.70 | bsi | high |

### A Long History: From Universal Language to Artificial Intelligence
- Runs analyzed: **10**
- Delta range: **-0.56 → 5.45**
- Mean delta: **2.05**
- Winner classification changes: **Yes**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `history_of_technology_long_history_gemini_groq_v1.json` | 4.65 | 8.35 | 3.70 | bsi | high |
| `history_of_technology_long_history_gemini_groq_v2.json` | 6.70 | 8.45 | 1.75 | bsi | high |
| `history_of_technology_long_history_gemini_openrouter_v3.json` | 6.10 | 8.55 | 2.45 | bsi | high |
| `history_of_technology_long_history_gemini_openrouter_v4.json` | 3.30 | 8.75 | 5.45 | bsi | high |
| `history_of_technology_long_history_groq_gemini_v1.json` | 8.53 | 7.97 | -0.56 | raw | low |
| `history_of_technology_long_history_groq_gemini_v2.json` | 7.70 | 7.92 | 0.22 | bsi | medium |
| `history_of_technology_long_history_groq_openrouter_v2.json` | 3.70 | 8.50 | 4.80 | bsi | high |
| `history_of_technology_long_history_openrouter_gemini_v1.json` | 6.67 | 9.03 | 2.36 | bsi | high |
| `history_of_technology_long_history_openrouter_gemini_v2.json` | 8.25 | 7.80 | -0.45 | tie | medium |
| `history_of_technology_long_history_openrouter_groq_v1.json` | 7.15 | 7.95 | 0.80 | bsi | high |

### The Algorithmic Caricature
- Runs analyzed: **4**
- Delta range: **-2.05 → 2.72**
- Mean delta: **0.88**
- Winner classification changes: **Yes**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `arxiv_political_caricature_gemini_groq_single.json` | 6.25 | 8.97 | 2.72 | bsi | high |
| `arxiv_political_caricature_gemini_openrouter_single.json` | 7.10 | 8.65 | 1.55 | bsi | high |
| `arxiv_political_caricature_groq_openrouter_single.json` | 7.65 | 5.60 | -2.05 | raw | low |
| `arxiv_political_caricature_openrouter_groq_single.json` | 7.14 | 8.42 | 1.28 | bsi | high |

### Epistemic justification
- Runs analyzed: **3**
- Delta range: **-2.50 → 2.65**
- Mean delta: **0.07**
- Winner classification changes: **Yes**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `philosophy_complex_groq_openrouter.json` | 6.35 | 9.00 | 2.65 | bsi | high |
| `philosophy_complex_groq_openrouter_full_rerun.json.json` | 7.95 | 5.45 | -2.50 | raw | low |
| `philosophy_complex_groq_openrouter_retry.json` | 6.45 | 6.50 | 0.05 | raw | low |

### What large language models know and what people think they know
- Runs analyzed: **3**
- Delta range: **-0.50 → 2.35**
- Mean delta: **1.37**
- Winner classification changes: **Yes**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `llm_knowledge_confidence_gemini37flash_gemini35flash_run1.json` | 6.65 | 9.00 | 2.35 | bsi | high |
| `llm_knowledge_confidence_gemini_gemini37flash_run4.json` | 6.95 | 9.22 | 2.27 | bsi | high |
| `llm_knowledge_confidence_gemini_gemini37flash_run5.json` | 9.00 | 8.50 | -0.50 | raw | medium |

### American Business, Public Policy, Case-Studies, and Political Theory
- Runs analyzed: **10**
- Delta range: **-4.85 → 2.80**
- Mean delta: **-1.53**
- Winner classification changes: **Yes**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `political_science_public_policy_gemini_37_run1.json` | 8.80 | 4.20 | -4.60 | raw | negative |
| `political_science_public_policy_gemini_37_run2.json` | 8.55 | 3.70 | -4.85 | raw | negative |
| `political_science_public_policy_gemini_37_run3.json` | 8.75 | 4.88 | -3.87 | raw | negative |
| `political_science_public_policy_minimax_run3.archived_20260906T001705Z.json` | 7.25 | 4.40 | -2.85 | raw | negative |
| `political_science_public_policy_minimax_run3.archived_20260906T001726Z.json` | 7.00 | 5.45 | -1.55 | raw | low |
| `political_science_public_policy_minimax_run3.json` | 5.20 | 6.60 | 1.40 | bsi | low |
| `political_science_public_policy_nemotron_run1.archived_20260905T221421Z.json` | 7.70 | 7.40 | -0.30 | raw | low |
| `political_science_public_policy_nemotron_run1.json` | 6.75 | 8.60 | 1.85 | bsi | high |
| `political_science_public_policy_nemotron_run2.json` | 5.05 | 7.85 | 2.80 | bsi | high |
| `political_science_public_policy_run1.json` | 8.00 | 4.70 | -3.30 | raw | negative |

### Morescient GAI for Software Engineering
- Runs analyzed: **5**
- Delta range: **1.30 → 2.45**
- Mean delta: **1.65**
- Winner classification changes: **No**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `arxiv_2406_04710_fulltext_openrouter_groq.json` | 6.20 | 7.60 | 1.40 | bsi | high |
| `engineering_fresh_limit1_groq_openrouter.json` | 6.95 | 8.25 | 1.30 | bsi | medium |
| `engineering_groq_openrouter_limit1.json` | 4.45 | 6.90 | 2.45 | bsi | high |
| `engineering_openrouter_groq_limit1.json` | 6.45 | 8.20 | 1.75 | bsi | medium |
| `fulltext_2406_04710v2_openrouter_groq.json` | 6.40 | 7.75 | 1.35 | bsi | medium |

### One-Shot Reinforcement Learning for Robot Navigation
- Runs analyzed: **2**
- Delta range: **2.40 → 2.85**
- Mean delta: **2.62**
- Winner classification changes: **No**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `robotics_groq_openrouter_limit1.json` | 5.55 | 7.95 | 2.40 | bsi | high |
| `robotics_openrouter_groq_limit1.json` | 5.50 | 8.35 | 2.85 | bsi | high |

### The Road to Know-Where
- Runs analyzed: **2**
- Delta range: **1.99 → 2.05**
- Mean delta: **2.02**
- Winner classification changes: **No**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `llm_knowledge_confidence_gemini_gemini37flash_run2.json` | 6.80 | 8.79 | 1.99 | bsi | high |
| `llm_knowledge_confidence_gemini_gemini37flash_run3.json` | 6.55 | 8.60 | 2.05 | bsi | high |

### Evaluating the Economic Feasibility of Labor Replacement Through Robotics and Automation in Qatar
- Runs analyzed: **2**
- Delta range: **1.80 → 1.80**
- Mean delta: **1.80**
- Winner classification changes: **No**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `econ_run8.json` | 6.50 | 8.30 | 1.80 | bsi | high |
| `economics_fulltext_run8.json` | 6.50 | 8.30 | 1.80 | bsi | high |

### Revolutionizing healthcare: the role of artificial intelligence in clinical practice
- Runs analyzed: **2**
- Delta range: **-1.15 → 0.00**
- Mean delta: **-0.58**
- Winner classification changes: **No**

| Run | RAW | BSI | Δ | Winner | Incremental |
|---|---:|---:|---:|---|---|
| `law_openrouter_groq_judge.json` | 6.90 | 6.90 | 0.00 | raw | medium |
| `law_openrouter_groq_judge_2.json` | 7.15 | 6.00 | -1.15 | raw | low |

### Interpretation boundary
The Bioinformatics FAIR runs remain the primary case-specific observation: delta remained positive (+1.60 and +1.50) while winner classification changed from Tie to BSI. The additional samples demonstrate that both sensitivity and stable repeatability occur across domains; they do not establish general BSI superiority.
