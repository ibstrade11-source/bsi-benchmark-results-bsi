# Comparison: Computational structuralism: Toward a formal theory of meaning in the age of digital intelligence

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-12T19:23:52Z
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

### Generation failures

- **gemini/raw**: Gemini HTTP 404: {
  "error": {
    "code": 404,
    "message": "models/gemini-3.5-flash-free is not found for API version v1beta, or is not supported for generateContent. Call ModelService.ListModels to see the list of available models and their supported methods.",
    "status": "NOT_FOUND"
  }
}

- **gemini/bsi**: Gemini HTTP 404: {
  "error": {
    "code": 404,
    "message": "models/gemini-3.5-flash-free is not found for API version v1beta, or is not supported for generateContent. Call ModelService.ListModels to see the list of available models and their supported methods.",
    "status": "NOT_FOUND"
  }
}


### Judge Evaluation

No judge result.
