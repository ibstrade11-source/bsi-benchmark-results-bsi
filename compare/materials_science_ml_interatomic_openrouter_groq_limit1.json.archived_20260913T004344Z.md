# Comparison: MS25: Materials Science-Focused Benchmark Data Set for Machine Learning Interatomic Potentials

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-13T00:36:36Z
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

### Generation failures

- **openrouter/bsi**: OpenRouter response did not contain a non-empty 'choices' array. keys=['id', 'error']; error={'message': 'Upstream error from Nvidia: Service temporarily overloaded', 'code': 502, 'metadata': {'error_type': 'provider_unavailable'}}; body_prefix='\n         \n\n         \n\n         \n{"id":"gen-1789260019-oRT1sZ4wmLYBpvWPgHwd","error":{"message":"Upstream error from Nvidia: Service temporarily overloaded","code":502,"metadata":{"error_type":"provider_unavailable"}}}'

### Judge Evaluation

No judge result.
