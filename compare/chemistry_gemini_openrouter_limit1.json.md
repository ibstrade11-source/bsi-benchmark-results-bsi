# Comparison: chemistry

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 4611b84b11c40496a9a55179000750ad1c70c7f4
- run timestamp (UTC): 2026-09-13T16:42:55Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Benchmark status

- status: **benchmarkable**

## Retrieval validation

- retrieval status: **accepted**
- query type: topic
- rejected candidates: 0

## CRC Handbook of Chemistry and Physics

*source:* https://openalex.org/W2132905138
*doi:* https://doi.org/10.1201/b17118

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
