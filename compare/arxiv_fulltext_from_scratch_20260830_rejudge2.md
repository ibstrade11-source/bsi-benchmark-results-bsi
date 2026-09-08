# Comparison: quantum physics

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: b0614be64885037c46eb26d7e0a25e195fef8f61
- run timestamp (UTC): 2026-08-30T23:31:38Z
- methodology: Scores/judgements come from an independent LLM judge (see comparison/judge.py) instructed not to reuse BSI's own D1-D7/EIG vocabulary and to choose its own evaluation criteria. If no judge model is available or its response cannot be parsed, the run falls back to a simple keyword-presence heuristic -- the stored record's own 'criteria_source' field ('llm' vs 'heuristic_fallback') always says honestly which one produced a given result. Neither path is a validated measurement of analytical quality until checked against independent human judgement on a representative sample.

> BSI prompt source: https://github.com/ibstrade11-source/behmanesh-index-prompt/blob/main/MASTER_PROMPT_BSI_v3.4.2.md

## Physics Briefing Book

*source:* http://arxiv.org/abs/1910.11775v2

### Judge Evaluation

#### Judge Information

| Field | Value |
|---|---|
| Criteria source | llm |
| Score scale | 0-10 |
| Weight sum | 100.0 |

#### Judge Reasoning

**Winner:** raw

RAW delivers a more complete, technically detailed, and strategically informative analysis of the Physics Briefing Book. It excels on all six article-specific criteria, particularly completeness, process understanding, strategic insight, and technical depth. BSI's evaluation adds a meta-scoring layer but sacrifices substantive content coverage and physics-specific insight. The BSI incremental value is low because its framework is mismatched to a consensus-policy document and its output is less useful for understanding the actual Briefing Book.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Completeness of Coverage | 20 | 9.0 | 7.0 | 1.80 | 1.40 | RAW systematically covers all 11 chapters in a structured table with key focus areas; BSI mentions chapter count but lacks domain-specific detail. |
| Process Understanding | 20 | 9.0 | 8.0 | 1.80 | 1.60 | RAW explicitly maps the governance flow (Inputs→PPG→Symposium→Briefing Book→ESG→Council) and notes APPEC boundary; BSI describes the process but less clearly structured. |
| Strategic Insight | 25 | 8.0 | 7.0 | 2.00 | 1.75 | RAW identifies the central strategic decision (FCC vs CLIC), HL-LHC anchor, theory uncertainty bottleneck, and precision/intensity frontiers as discovery tools; BSI notes the HL-LHC→FCC-ee→FCC-hh/CLIC sequence but with less physics rationale. |
| Technical Depth | 15 | 8.0 | 6.0 | 1.20 | 0.90 | RAW includes specific quantitative targets (1% Higgs couplings, O(10^-4-10^-5) EWPO, 100s TeV flavour reach, theory uncertainty dominance); BSI stays at higher abstraction. |
| Governance/Decision-Making Clarity | 10 | 9.0 | 7.0 | 0.90 | 0.70 | RAW presents a clear 'Output Flow' chain and notes the 160 submissions, 8 parallel sessions, and APPEC boundary; BSI mentions these elements but less coherently. |
| Forward-Looking Assessment | 10 | 8.0 | 6.0 | 0.80 | 0.60 | RAW details near/mid/long-term milestones (HL-LHC Run 2 results, FCC CDR, CLIC Implementation Plan, muon collider R&D, plasma wakefield); BSI references milestones only in passing. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 8.50 |
| BSI | 6.95 |

#### Summary

- Winner: **raw**
- Score difference: **-1.55**
- Criteria evaluated: **6**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
