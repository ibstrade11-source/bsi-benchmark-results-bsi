# Comparison: test

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 85f2f01c3cd0011931edf819e040580130965f66 (uncommitted local changes present)
- run timestamp (UTC): 2026-08-03T21:37:06Z
- methodology note: Scores are produced by BSIEvaluator, an offline lexical/keyword-based proxy for the seven BIO v1.0 dimensions (regex and keyword matching, not semantic understanding). They are first-pass triage signals, not a validated measurement of analytical quality, until checked against independent human judgement on a representative sample. Do not cite numeric BSI scores as a certified metric without that validation step.

> BSI prompt source (read it yourself, unedited): https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## test

| generator | mode | D1 | D2 | D3 | D4 | D5 | D6 | D7 | BSI | grounding_ratio | tag_coverage |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mock | raw | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.205 | 1.000 | 0.000 |
| mock | bsi | 1.000 | 1.000 | 0.466 | 0.968 | 1.000 | 0.125 | 1.000 | 0.828 | 1.000 | 1.000 |
| gemini | raw | 0.000 | 1.000 | 0.000 | 0.964 | 0.000 | 0.125 | 0.500 | 0.379 | 1.000 | 0.000 |
| gemini | bsi | 0.149 | 1.000 | 1.000 | 0.998 | 0.000 | 0.625 | 0.000 | 0.612 | 1.000 | 0.000 |
