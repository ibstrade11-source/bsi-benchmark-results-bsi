# Comparison: quantum physics

## Run metadata
- bsi-benchmark version: 0.1.0
- git commit: b0614be64885037c46eb26d7e0a25e195fef8f61
- run timestamp (UTC): 2026-08-30T19:29:03Z
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

**Winner:** bsi

BSI wins on analytical depth. While RAW excels at descriptive completeness and clarity, BSI provides critical evaluation that RAW lacks: it identifies the consensus-driven risk aversion, absence of failure scenarios, and unquantified programmatic uncertainties as structural epistemic limitations. BSI's cross-domain integration insight and explicit strategic milestone framing add interpretive value for decision-makers. The communicative clarity deficit is outweighed by the incremental analytical value for this document type.

#### Criteria Selected by Judge

| Criterion | Weight | Raw (/10) | BSI (/10) | Weighted Raw | Weighted BSI | Explanation |
|---|---:|---:|---:|---:|---:|---|
| Document Classification Accuracy | 15 | 9.0 | 10.0 | 1.35 | 1.50 | RAW correctly identifies it as strategic policy input/consensus review; BSI goes further by explicitly framing it as 'Consensus Strategic Compendium' and articulating the core claim about community consensus guaranteeing progress. |
| Process/Governance Coverage | 15 | 9.0 | 9.0 | 1.35 | 1.35 | Both cover the bottom-up process, 160 inputs, PPG, Granada symposium, ESG→Council flow. RAW slightly more detailed on thematic sessions (B1-B8); BSI captures the governance chain equivalently. |
| Scientific Content Mapping | 20 | 9.0 | 8.0 | 1.80 | 1.60 | RAW provides a comprehensive table mapping all 11 chapters to key focus areas with specific examples (PDFs, αs, CKM unitarity, etc.). BSI lists 9 domains + theory chapter but with less granular detail. |
| Strategic Decision Framework | 15 | 8.0 | 9.0 | 1.20 | 1.35 | RAW details HL-LHC, FCC/CLIC, and other options well. BSI more crisply frames the milestone chain (HL-LHC→FCC-ee→FCC-hh/CLIC) and highlights physics-driven R&D co-design as the decision logic. |
| Cross-Domain Integration | 10 | 7.0 | 9.0 | 0.70 | 0.90 | RAW mentions accelerator R&D and instrumentation as separate chapters. BSI explicitly identifies the 'physics-technology-computing ecosystem' integration as the document's distinguishing feature. |
| Limitations/Caveats Identification | 15 | 5.0 | 9.0 | 0.75 | 1.35 | RAW notes theory uncertainties and APPEC boundary but treats the document descriptively. BSI explicitly flags consensus penalty (risk aversion), missing failure scenarios/Plan-B, and unquantified technical-programmatic uncertainties. |
| Communicative Clarity/Utility | 10 | 9.0 | 7.0 | 0.90 | 0.70 | RAW is professionally structured, accessible, with clear tables and section headers. BSI uses mixed Persian/English, dense weighted tables, and framework jargon that reduces accessibility for general readers. |

#### Final Scores

| Analysis | Score (/10) |
|---|---:|
| Raw | 8.05 |
| BSI | 8.75 |

#### Summary

- Winner: **bsi**
- Score difference: **+0.70**
- Criteria evaluated: **7**

#### Score Formula

Final score = Σ(weight × criterion score / 100)
