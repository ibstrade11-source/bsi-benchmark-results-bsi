bsi-benchmark-results-bsi

Registered benchmark results for Behmanesh Structural Index (BSI)

Developed by Mohammadali Behmanesh (محمدعلی بهمنش).

This repository is the public results repository for benchmark experiments conducted with:

BSI — Behmanesh Structural Index / شاخص ساختاری بهمنش

It is intentionally separated from the benchmark source repository.

Purpose

This repository stores registered benchmark evidence and aggregate reports produced from that evidence.

It does not contain the source code of the benchmark tool.

The benchmark infrastructure is maintained separately in:

"BEHMANESH-Mohammadali/bsi-benchmark"

The BSI framework and prompt definitions are maintained separately in:

"BEHMANESH-Mohammadali/behmanesh-index-prompt"

Canonical identity

Author / creator: Mohammadali Behmanesh
فارسی: محمدعلی بهمنش

GitHub: "@BEHMANESH-Mohammadali"

X: "@behmanesham"

Primary framework: Behmanesh Structural Index (BSI)

The canonical GitHub profile connecting the author, framework, benchmark implementation, and benchmark evidence is:

"BEHMANESH-Mohammadali/BEHMANESH-Mohammadali"

Repository structure

compare/
    Registered compare-cli benchmark records
    Each registered record normally contains JSON + Markdown

self_compare/
    Registered self-compare records

scripts/
    rebuild_csvs.py
    generate_report.py
    build_report.sh

BENCHMARK_REPORT_8_TABLES.md
    Human-readable aggregate report

*.csv
    Aggregate benchmark tables

Registration principle

Results are not intended to be manually edited into the aggregate tables.

The normal workflow is:

bsi-benchmark
      ↓
validation / curation
      ↓
registered result
      ↓
compare/
      ↓
CSV reconstruction
      ↓
aggregate reports

The benchmark source repository contains the validation and curation workflow.

Status classification

Registered records may be classified as:

Status| Meaning
"VALID"| Eligible benchmark result with a real judge result
"UNJUDGED"| No valid independent judge result
"TEST"| Test/smoke-test record
"ARCHIVED"| Historical or explicitly archived record

A record being physically present in "compare/" does not by itself imply that it is valid benchmark evidence.

Aggregate CSV reports

The repository maintains eight aggregate reports.

"benchmark_aggregate_scientific.csv"

All scanned compare records, including status information.

"benchmark_aggregate_full.csv"

Non-UNJUDGED records with benchmark metadata and scores.

"benchmark_aggregate.csv"

Historical simplified aggregate view.

"article_level_analysis.csv"

Article-level aggregation across valid runs.

"domain_level_analysis.csv"

Aggregation by research domain.

"model_level_analysis.csv"

Aggregation by analyst model.

"drift_repeatability_analysis.csv"

Analysis of repeated valid runs for the same article.

"incremental_value_analysis.csv"

Distribution of recorded relevance, realization, and incremental-value combinations.

Rebuilding the reports

After registering new results:

cd ~/bsi-benchmark-results-bsi
bash scripts/build_report.sh

This runs the CSV reconstruction and final report generation in sequence.

The final report is:

BENCHMARK_REPORT_8_TABLES.md

Evidence and provenance

The repository preserves benchmark metadata needed to interpret results, including:

- article title
- DOI / article identifier
- domain
- analyst model
- generator
- analysis mode
- judge model
- judging criteria source
- RAW score
- BSI score
- delta
- full-text availability
- benchmark status

The purpose is to keep aggregate numbers connected to their underlying experimental records.

Full-text availability

Input quality matters.

An analysis performed using a full article is not treated as methodologically identical to one performed using only a title or insufficient article content.

Records should therefore preserve whether full text was actually available.

Related repositories

Benchmark infrastructure

"BEHMANESH-Mohammadali/bsi-benchmark"

BSI framework and prompt definitions

"BEHMANESH-Mohammadali/behmanesh-index-prompt"

Canonical GitHub profile

"BEHMANESH-Mohammadali/BEHMANESH-Mohammadali"

Author

Mohammadali Behmanesh / محمدعلی بهمنش

Behmanesh Structural Index (BSI)
شاخص ساختاری بهمنش

License

MIT
