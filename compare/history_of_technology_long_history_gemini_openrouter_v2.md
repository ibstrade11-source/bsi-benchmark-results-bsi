# Comparison: A Long History: From Universal Language to Artificial Intelligence

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 89a941006de1ccab30f7a16e09f86841cd5991eb
- run timestamp (UTC): 2026-09-07T15:34:36Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **not_benchmarkable**
- No analysis/judge score from this run is benchmark evidence.

## Retrieval validation

- retrieval status: **invalid**
- query type: title
- title match score: 0.2944
- acceptance threshold: 0.72
- rejection reason: title_query_mismatch
- rejected candidates: 5

### Rejected retrieval candidates

| Rank | Match score | Status | Title |
|---:|---:|---|---|
| 5 | 0.2944 | invalid_retrieval | Ethical principles for artificial intelligence in education |
| 2 | 0.2867 | invalid_retrieval | Explainability for artificial intelligence in healthcare: a multidisciplinary perspective |
| 3 | 0.2867 | invalid_retrieval | Foundation models for generalist medical artificial intelligence |
| 4 | 0.275 | invalid_retrieval | Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence |
| 1 | 0.2604 | invalid_retrieval | Artificial Intelligence (AI): Multidisciplinary perspectives on emerging challenges, opportunities, and agenda for research, practice and policy |
