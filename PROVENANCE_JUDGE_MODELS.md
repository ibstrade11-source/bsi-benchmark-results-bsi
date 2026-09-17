# Judge Model Provenance

Historical Judge-model provenance reconstructed from direct evidence.

| Result file | Judge provider | Judge model | Confidence | Evidence |
|---|---|---|---|---|
| `political_science_new_article_gemini_37_analyst_groq_judge_run8` | Groq | `openai/gpt-oss-20b` | DIRECT | Original benchmark command explicitly used `--judge groq --judge-model openai/gpt-oss-20b` |
| `economics_v1_direct_openrouter_judge.json` | OpenRouter | `openai/gpt-4o-mini` | DIRECT | `judge_model` is explicitly recorded inside the result JSON |

## Confidence definitions

- `DIRECT`: exact Judge model is explicitly present in the original command or result JSON.
- `RECONSTRUCTED`: model recovered through an independently corroborated execution-history chain.
- `UNKNOWN`: Judge provider is known, but exact model cannot be established without inference.

Only `DIRECT` entries are recorded in this initial provenance registry.
