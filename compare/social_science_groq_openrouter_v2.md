# Comparison: social capital community trust inequality

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: 86fb38868d0d36ae348cb4f9ffd7c49190f311bf
- run timestamp (UTC): 2026-08-25T23:42:53Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Social Capital: Implications for Development Theory, Research, and Policy

*source:* https://openalex.org/W2109745229
*doi:* https://doi.org/10.1093/wbro/15.2.225

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** tie

Both analyses accurately capture the article's core definition, four approaches, synergy argument, bridging claim, and nuance about positive/negative outcomes. BSI is slightly more structured on policy implications; RAW is slightly more explicit on definition evolution and the bridging constituency. Differences are minor and complementary, not decisive.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Accuracy of core concept definition and evolution | 20 | 9.0 | 8.0 | 1.80 | 1.60 | The article's foundation is its definition of social capital and its historical evolution in social science; RAW explicitly captures both the definition and the evolution tracing, while BSI gives the definition but omits the evolution dimension. |
| Coverage and differentiation of the four approaches | 20 | 9.0 | 9.0 | 1.80 | 1.80 | Both analyses correctly identify and name all four approaches (communitarian, networks, institutional, synergy); BSI adds brief descriptive phrases for each, but RAW's coverage is equally complete for a summary task. |
| Treatment of synergy view as empirically supported framework | 15 | 9.0 | 9.0 | 1.35 | 1.35 | The article's central argument is that the synergy view has the greatest empirical support; both analyses convey this claim accurately and with similar emphasis. |
| Identification of development theory, research, and policy implications | 20 | 7.0 | 9.0 | 1.40 | 1.80 | The article's title explicitly promises implications for development theory, research, and policy; BSI provides a structured bullet-point breakdown covering bridging divides, comprehensive policy prescriptions, and positive/negative outcomes, while RAW mentions policy prescriptions and bridging but with less granularity. |
| Recognition of interdisciplinary bridging function | 10 | 9.0 | 9.0 | 0.90 | 0.90 | The article frames bridging disciplinary divides as a key virtue of the social capital concept; both analyses capture this, RAW with explicit reference to scholars, practitioners, and policymakers, BSI with 'bridging orthodox divides' and 'integrated understanding'. |
| Nuanced treatment of positive and negative outcomes | 15 | 8.0 | 9.0 | 1.20 | 1.35 | A hallmark of the synergy view is acknowledging both positive and negative consequences; both analyses note this, but BSI states it more directly as a standalone implication. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 8.45 |
| BSI | 8.80 |

#### Summary

- Winner: **tie**
- Score difference: **+0.35**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
