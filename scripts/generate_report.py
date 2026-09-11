#!/usr/bin/env python3

from pathlib import Path
import csv
from collections import Counter, defaultdict
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[1]

SCIENTIFIC = ROOT / "benchmark_aggregate_scientific.csv"
AGGREGATE = ROOT / "benchmark_aggregate.csv"
ARTICLE = ROOT / "article_level_analysis.csv"
DOMAIN = ROOT / "domain_level_analysis.csv"
DRIFT = ROOT / "drift_repeatability_analysis.csv"
MODEL = ROOT / "model_level_analysis.csv"

OUT = ROOT / "BENCHMARK_REPORT_8_TABLES.md"


def read_csv(path):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def pct(n, total):
    return f"{100*n/total:.1f}%" if total else "0.0%"


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def fmt(x):
    if x is None:
        return "—"
    return f"{x:.2f}"


def md_escape(x):
    return str(x).replace("|", "\\|").replace("\n", " ")


scientific = read_csv(SCIENTIFIC)
aggregate = read_csv(AGGREGATE)
article = read_csv(ARTICLE)
domain = read_csv(DOMAIN)
drift = read_csv(DRIFT)
model = read_csv(MODEL)

valid = [
    r for r in scientific
    if r.get("status", "").upper() == "VALID"
]

# ============================================================
# TABLE 1 — DATASET / STATUS
# ============================================================

status_counts = Counter(
    (r.get("status") or "").upper() or "UNKNOWN"
    for r in scientific
)

t1 = [
    ("VALID", status_counts["VALID"]),
    ("UNJUDGED", status_counts["UNJUDGED"]),
    ("TEST", status_counts["TEST"]),
    ("ARCHIVED", status_counts["ARCHIVED"]),
]


# ============================================================
# TABLE 2 — RAW vs BSI
# ============================================================

raw_scores = [num(r.get("raw_score")) for r in valid]
bsi_scores = [num(r.get("bsi_score")) for r in valid]
deltas = [num(r.get("delta")) for r in valid]

raw_scores = [x for x in raw_scores if x is not None]
bsi_scores = [x for x in bsi_scores if x is not None]
deltas = [x for x in deltas if x is not None]

winner_counts = Counter(
    (r.get("winner") or "").strip().lower()
    for r in valid
)

t2 = [
    ("RAW mean", fmt(mean(raw_scores))),
    ("BSI mean", fmt(mean(bsi_scores))),
    ("Δ mean (BSI−RAW)", fmt(mean(deltas))),
    ("Δ median", fmt(median(deltas))),
    ("Δ min", fmt(min(deltas))),
    ("Δ max", fmt(max(deltas))),
    ("BSI wins", winner_counts["bsi"]),
    ("RAW wins", winner_counts["raw"]),
    ("Ties", winner_counts["tie"]),
]


# ============================================================
# TABLE 3 — BSI CAPABILITY ASSESSMENT
# ============================================================

def dimension_counts(field):
    values = [
        (r.get(field) or "").strip().lower()
        for r in valid
        if (r.get(field) or "").strip()
    ]
    c = Counter(values)
    return c, len(values)


rel, rel_n = dimension_counts("relevance")
rea, rea_n = dimension_counts("realization")
inc, inc_n = dimension_counts("incremental_value")

t3_rows = [
    ("Relevance", "high", rel["high"], pct(rel["high"], len(valid))),
    ("Relevance", "medium", rel["medium"], pct(rel["medium"], len(valid))),
    ("Relevance", "low", rel["low"], pct(rel["low"], len(valid))),
    ("Realization", "high", rea["high"], pct(rea["high"], len(valid))),
    ("Realization", "medium", rea["medium"], pct(rea["medium"], len(valid))),
    ("Realization", "low", rea["low"], pct(rea["low"], len(valid))),
    ("Incremental value", "high", inc["high"], pct(inc["high"], len(valid))),
    ("Incremental value", "medium", inc["medium"], pct(inc["medium"], len(valid))),
    ("Incremental value", "low", inc["low"], pct(inc["low"], len(valid))),
    ("Incremental value", "none", inc["none"], pct(inc["none"], len(valid))),
    ("Incremental value", "negative", inc["negative"], pct(inc["negative"], len(valid))),
]


# ============================================================
# TABLE 4 — CAPABILITY CROSS-TABULATION
# ============================================================

cross = Counter()

for r in valid:
    rel_v = (r.get("relevance") or "").strip().lower()
    rea_v = (r.get("realization") or "").strip().lower()
    inc_v = (r.get("incremental_value") or "").strip().lower()

    if rel_v and rea_v and inc_v:
        cross[(rel_v, rea_v, inc_v)] += 1

t4_rows = [
    (rel_v, rea_v, inc_v, n)
    for (rel_v, rea_v, inc_v), n in cross.most_common()
]


# ============================================================
# MARKDOWN GENERATION
# ============================================================

lines = []

lines.append("# Benchmark Report — Standard 8-Table Output")
lines.append("")
lines.append(
    "This report is automatically generated from structured CSV files. "
    "Each report build contains eight standard tables."
)
lines.append("")


# TABLE 1
lines.append("## TABLE 1 - DATA STATUS")
lines.append("")
lines.append("| Status | Count |")
lines.append("|---|---:|")
for status, n in t1:
    lines.append(f"| {status} | {n} |")
lines.append("")


# TABLE 2
lines.append("## TABLE 2 - RAW VS BSI")
lines.append("")
lines.append("| Metric | Value |")
lines.append("|---|---:|")
for label, value in t2:
    lines.append(f"| {label} | {value} |")
lines.append("")


# TABLE 3
lines.append("## TABLE 3 - BSI CAPABILITY AND INCREMENTAL VALUE")
lines.append("")
lines.append("| Dimension | Level | Count | Percent of VALID |")
lines.append("|---|---|---:|---:|")
for dim, level, n, p in t3_rows:
    lines.append(f"| {dim} | {level} | {n} | {p} |")
lines.append("")
lines.append(
    "**Note:** `incremental_value` is the Judge's independent assessment of "
    "the incremental value of BSI analysis relative to RAW and is not identical to Δ."
)
lines.append("")


# TABLE 4
lines.append("## TABLE 4 - RELEVANCE X REALIZATION X INCREMENTAL VALUE")
lines.append("")
lines.append("| Relevance | Realization | Incremental Value | Count |")
lines.append("|---|---|---|---:|")
for rel_v, rea_v, inc_v, n in t4_rows:
    lines.append(f"| {rel_v} | {rea_v} | {inc_v} | {n} |")
lines.append("")


# TABLE 5
lines.append("## TABLE 5 - ARTICLE-LEVEL ANALYSIS")
lines.append("")
lines.append(
    "| Article | Runs | RAW mean | BSI mean | Δ mean | Δ median | "
    "BSI wins | RAW wins | Ties |"
)
lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
for r in article:
    lines.append(
        f"| {md_escape(r.get('article_title',''))} | "
        f"{r.get('runs','')} | "
        f"{r.get('raw_mean','')} | "
        f"{r.get('bsi_mean','')} | "
        f"{r.get('delta_mean','')} | "
        f"{r.get('delta_median','')} | "
        f"{r.get('bsi_wins','')} | "
        f"{r.get('raw_wins','')} | "
        f"{r.get('ties','')} |"
    )
lines.append("")


# TABLE 6
lines.append("## TABLE 6 - DOMAIN-LEVEL ANALYSIS")
lines.append("")
lines.append(
    "| Domain | Runs | Unique articles | RAW mean | BSI mean | "
    "Δ mean | BSI wins | RAW wins | Ties |"
)
lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
for r in domain:
    lines.append(
        f"| {md_escape(r.get('domain',''))} | "
        f"{r.get('runs','')} | "
        f"{r.get('unique_articles','')} | "
        f"{r.get('raw_mean','')} | "
        f"{r.get('bsi_mean','')} | "
        f"{r.get('delta_mean','')} | "
        f"{r.get('bsi_wins','')} | "
        f"{r.get('raw_wins','')} | "
        f"{r.get('ties','')} |"
    )
lines.append("")


# TABLE 7
lines.append("## TABLE 7 - ANALYST-MODEL ANALYSIS")
lines.append("")
lines.append(
    "| Analyst model | Runs | Unique articles | RAW mean | BSI mean | "
    "Δ mean | BSI wins | RAW wins | Ties |"
)
lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
for r in model:
    lines.append(
        f"| {md_escape(r.get('analyst_model',''))} | "
        f"{r.get('runs','')} | "
        f"{r.get('unique_articles','')} | "
        f"{r.get('raw_mean','')} | "
        f"{r.get('bsi_mean','')} | "
        f"{r.get('delta_mean','')} | "
        f"{r.get('bsi_wins','')} | "
        f"{r.get('raw_wins','')} | "
        f"{r.get('ties','')} |"
    )
lines.append("")


# TABLE 8
lines.append("## TABLE 8 - REPEATABILITY AND DRIFT")
lines.append("")
lines.append(
    "| Article | Runs | Δ mean | Δ SD | Δ range | RAW SD | BSI SD | "
    "RAW range | BSI range | BSI wins | RAW wins | Ties | Winner switch |"
)
lines.append(
    "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
)

for r in drift:
    lines.append(
        f"| {md_escape(r.get('article_title',''))} | "
        f"{r.get('runs','')} | "
        f"{r.get('delta_mean','')} | "
        f"{r.get('delta_sd','')} | "
        f"{r.get('delta_range','')} | "
        f"{r.get('raw_sd','')} | "
        f"{r.get('bsi_sd','')} | "
        f"{r.get('raw_range','')} | "
        f"{r.get('bsi_range','')} | "
        f"{r.get('bsi_wins','')} | "
        f"{r.get('raw_wins','')} | "
        f"{r.get('ties','')} | "
        f"{r.get('winner_switch','')} |"
    )

lines.append("")
lines.append("---")
lines.append("")
lines.append(
    f"Count VALID: **{len(valid)}** | "
    f"Article count: **{len(article)}** | "
    f"Domain count: **{len(domain)}** | "
    f"Model count: **{len(model)}** | "
    f"Articles with repeated runs for drift analysis: **{len(drift)}"
)
lines.append("")

report_text = "\n".join(lines)

EXPECTED_TABLES = [
    "## TABLE 1 - DATA STATUS",
    "## TABLE 2 - RAW VS BSI",
    "## TABLE 3 - BSI CAPABILITY AND INCREMENTAL VALUE",
    "## TABLE 4 - RELEVANCE X REALIZATION X INCREMENTAL VALUE",
    "## TABLE 5 - ARTICLE-LEVEL ANALYSIS",
    "## TABLE 6 - DOMAIN-LEVEL ANALYSIS",
    "## TABLE 7 - ANALYST-MODEL ANALYSIS",
    "## TABLE 8 - REPEATABILITY AND DRIFT",
]

missing = [h for h in EXPECTED_TABLES if h not in report_text]
actual_count = report_text.count("## TABLE ")

if missing or actual_count != 8:
    raise RuntimeError(
        f"REPORT QA FAILED: expected 8 tables, found {actual_count}; "
        f"missing={missing}"
    )

OUT.write_text(report_text, encoding="utf-8")


import re
# Print the 8 report tables as compact terminal views.
import re

print()
print("=" * 72)
print("BENCHMARK REPORT - 8 TABLES")
print("=" * 72)

table_pattern = re.compile(
    r"^##\s+TABLE\s+([1-8])\b.*$",
    re.MULTILINE,
)

table_matches = list(table_pattern.finditer(report_text))

EXPECTED_TABLES = [
    "## TABLE 1 - DATA STATUS",
    "## TABLE 2 - RAW VS BSI",
    "## TABLE 3 - BSI CAPABILITY AND INCREMENTAL VALUE",
    "## TABLE 4 - RELEVANCE X REALIZATION X INCREMENTAL VALUE",
    "## TABLE 5 - ARTICLE-LEVEL ANALYSIS",
    "## TABLE 6 - DOMAIN-LEVEL ANALYSIS",
    "## TABLE 7 - ANALYST-MODEL ANALYSIS",
    "## TABLE 8 - REPEATABILITY AND DRIFT",
]

missing = [h for h in EXPECTED_TABLES if h not in report_text]

if len(table_matches) != 8 or missing:
    raise RuntimeError(
        f"REPORT QA FAILED: expected 8 tables, "
        f"found {len(table_matches)}, missing={missing}"
    )


def parse_markdown_table(block):
    rows = []

    for line in block.splitlines():
        line = line.strip()

        if not (line.startswith("|") and line.endswith("|")):
            continue

        cells = [x.strip() for x in line[1:-1].split("|")]

        if cells and all(set(x) <= set("-: ") for x in cells):
            continue

        rows.append(cells)

    return rows


def clean_text(value):
    return " ".join(str(value).replace("\n", " ").split())


def compact(value, width):
    value = clean_text(value)

    if len(value) <= width:
        return value

    if width <= 3:
        return value[:width]

    return value[:width - 3] + "..."


def render_table(title, block, widths):
    rows = parse_markdown_table(block)

    if not rows:
        return

    n = len(widths)
    normalized = []

    for row in rows:
        row = row[:n] + [""] * max(0, n - len(row))
        normalized.append([
            compact(row[i], widths[i])
            for i in range(n)
        ])

    def line():
        return "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def row_text(row):
        return "| " + " | ".join(
            row[i].ljust(widths[i])
            for i in range(n)
        ) + " |"

    print()
    print(title)
    print(line())
    print(row_text(normalized[0]))
    print(line())

    for row in normalized[1:]:
        print(row_text(row))

    print(line())


# Deliberately narrow terminal widths.
# The Markdown report itself remains unchanged.
TABLE_WIDTHS = {
    1: [16, 7],
    2: [20, 10],
    3: [18, 10, 7, 12],
    4: [9, 11, 12, 6],
    5: [24, 5, 8, 8, 8, 9, 8, 8],
    6: [24, 5, 7, 8, 8, 8, 8, 8],
    7: [24, 5, 7, 8, 8, 8, 8, 8],
    8: [24, 5, 8, 8, 8, 8, 8, 9, 9, 8, 8, 6, 9],
}


for i, match in enumerate(table_matches):
    start = match.end()
    end = (
        table_matches[i + 1].start()
        if i + 1 < len(table_matches)
        else len(report_text)
    )

    block = report_text[start:end]
    title = match.group(0).strip()

    render_table(
        title,
        block,
        TABLE_WIDTHS[i + 1],
    )

print()
print("=" * 72)
print("REPORT QA: PASS")
print("8 canonical tables detected.")
print("=" * 72)
print("8 canonical tables detected.")
print("=" * 110)
