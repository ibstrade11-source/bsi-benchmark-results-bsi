#!/usr/bin/env python3

import csv
import json
import math
import re
from collections import defaultdict, Counter
from pathlib import Path
from statistics import mean, median, pstdev

ROOT = Path(__file__).resolve().parent.parent
COMPARE = ROOT / "compare"

SCIENTIFIC = ROOT / "benchmark_aggregate_scientific.csv"
AGGREGATE = ROOT / "benchmark_aggregate.csv"
FULL = ROOT / "benchmark_aggregate_full.csv"
ARTICLE = ROOT / "article_level_analysis.csv"
DOMAIN = ROOT / "domain_level_analysis.csv"
DRIFT = ROOT / "drift_repeatability_analysis.csv"
MODEL = ROOT / "model_level_analysis.csv"
INCREMENTAL = ROOT / "incremental_value_analysis.csv"


def clean(x):
    if x is None:
        return ""
    if isinstance(x, bool):
        return str(x).lower()
    return str(x).strip()


def num(x):
    try:
        v = float(x)
        return v if math.isfinite(v) else None
    except Exception:
        return None


def json_load(path):
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def cells_of(result):
    cells = result.get("cells", {})
    if isinstance(cells, dict):
        return cells
    if isinstance(cells, list):
        out = {}
        for c in cells:
            if isinstance(c, dict):
                key = f'{c.get("generator","")}::{c.get("mode","")}'
                out[key] = c
        return out
    return {}


def get_cell(cells, mode):
    for key, cell in cells.items():
        if not isinstance(cell, dict):
            continue
        if clean(cell.get("mode")).lower() == mode:
            return cell
        if key.lower().endswith(f"::{mode}"):
            return cell
    return None


def get_judge(cells):
    for cell in cells.values():
        if isinstance(cell, dict) and isinstance(cell.get("judge_result"), dict):
            return cell["judge_result"]
    return None


def get_analysis_model(cells):
    models = []

    for cell in cells.values():
        if not isinstance(cell, dict):
            continue

        model = cell.get("model_id")
        if model:
            models.append(clean(model))
            continue

        analysis = cell.get("analysis")
        if isinstance(analysis, dict):
            model = analysis.get("source_model")
            if model:
                models.append(clean(model))

    models = [m for m in models if m]
    if not models:
        return ""

    # RAW/BSI should normally use the same analyst model.
    counts = Counter(models)
    return counts.most_common(1)[0][0]


def get_generator(cells):
    vals = []
    for cell in cells.values():
        if isinstance(cell, dict) and cell.get("generator"):
            vals.append(clean(cell["generator"]))
    return Counter(vals).most_common(1)[0][0] if vals else ""


def get_mode(cells):
    modes = []
    for cell in cells.values():
        if isinstance(cell, dict) and cell.get("mode"):
            modes.append(clean(cell["mode"]))
    if len(set(modes)) == 1:
        return modes[0]
    if len(set(modes)) > 1:
        return "raw+bsi"
    return ""


def article_info(data, result):
    article = result.get("article") or {}

    title = (
        article.get("title")
        or article.get("article_title")
        or result.get("article_title")
        or ""
    )

    doi = (
        article.get("doi")
        or result.get("doi")
        or ""
    )

    article_id = (
        result.get("article_id")
        or article.get("id")
        or article.get("article_id")
        or ""
    )

    # Preserve benchmark provenance: historical domain labels are
    # identical to the top-level dataset_name.
    domains = data.get("dataset_name") or ""

    if isinstance(domains, list):
        domains = "; ".join(map(str, domains))

    return clean(title), clean(doi), clean(article_id), clean(domains)


def status_for(path, data, result, cells):
    name = path.name.lower()

    # Explicitly preserve known test/mock nature.
    if (
        "smoke_test" in name
        or "real_article_test" in name
        or "mobile_test" in name
        or "nemotron_test" in name
        or "physics_final_test" in name
        or "physics_mock" in name
        or "mock" in name
    ):
        return "TEST"

    # Archived artifacts.
    if ".archived_" in name or "archived" in name:
        return "ARCHIVED"

    # Explicit benchmark exclusion.
    if clean(data.get("benchmark_status")).lower() == "not_benchmarkable":
        return "UNJUDGED"

    # A valid benchmark result requires an actual judge result.
    judge = get_judge(cells)
    if isinstance(judge, dict):
        return "VALID"

    return "UNJUDGED"


def extract_scores(judge):
    if not isinstance(judge, dict):
        return None, None, None, "", "", "", "", ""

    total = judge.get("total_scores") or {}

    raw = num(total.get("raw"))
    bsi = num(total.get("bsi"))

    delta = None
    if raw is not None and bsi is not None:
        delta = bsi - raw

    winner = clean(judge.get("winner"))

    cap = judge.get("bsi_capability_assessment") or {}

    relevance = clean(cap.get("relevance"))
    realization = clean(cap.get("realization"))
    incremental = clean(cap.get("incremental_value"))

    criteria_source = clean(judge.get("criteria_source"))

    return raw, bsi, delta, winner, relevance, realization, incremental, criteria_source


def full_text_value(data, result):
    vals = [
        result.get("full_text"),
        (result.get("article") or {}).get("full_text"),
        data.get("full_text"),
    ]

    for v in vals:
        if isinstance(v, bool):
            return v
        if isinstance(v, str) and v.strip():
            return True

    return False


def provider_value(data, cells):
    p = data.get("provider") or data.get("provider_name")
    if p:
        return clean(p)

    vals = []
    for cell in cells.values():
        if isinstance(cell, dict) and cell.get("generator"):
            vals.append(clean(cell["generator"]))

    return Counter(vals).most_common(1)[0][0] if vals else ""


def query_value(data):
    rm = data.get("run_metadata") or {}
    return clean(
        data.get("query")
        or rm.get("query")
        or data.get("search_query")
    )


def one_row(path):
    data = json_load(path)

    if not isinstance(data, dict):
        return {
            "file": f"compare/{path.name}",
            "status": "UNJUDGED",
            "article_title": "",
            "doi": "",
            "article_id": "",
            "domain": "",
            "analyst_model": "",
            "generator": "",
            "mode": "",
            "judge_model": "",
            "criteria_source": "",
            "winner": "",
            "raw_score": "",
            "bsi_score": "",
            "delta": "",
            "relevance": "",
            "realization": "",
            "incremental_value": "",
            "full_text": "",
            "provider": "",
            "query": "",
        }

    results = data.get("results") or []

    result = results[0] if results and isinstance(results[0], dict) else {}
    cells = cells_of(result)

    title, doi, article_id, domain = article_info(data, result)

    status = status_for(path, data, result, cells)

    judge = get_judge(cells)
    raw, bsi, delta, winner, relevance, realization, incremental, criteria_source = \
        extract_scores(judge)

    judge_model = ""
    if isinstance(judge, dict):
        judge_model = clean(judge.get("judge_model"))

    return {
        "file": f"compare/{path.name}",
        "status": status,
        "article_title": title,
        "doi": doi,
        "article_id": article_id,
        "domain": domain,
        "analyst_model": get_analysis_model(cells),
        "generator": get_generator(cells),
        "mode": get_mode(cells),
        "judge_model": judge_model,
        "criteria_source": criteria_source,
        "winner": winner,
        "raw_score": "" if raw is None else raw,
        "bsi_score": "" if bsi is None else bsi,
        "delta": "" if delta is None else delta,
        "relevance": relevance,
        "realization": realization,
        "incremental_value": incremental,
        "full_text": full_text_value(data, result),
        "provider": provider_value(data, cells),
        "query": query_value(data),
    }


def write_csv(path, rows, fields):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    tmp.replace(path)


def valid_rows(rows):
    return [
        r for r in rows
        if r["status"] == "VALID"
        and num(r["raw_score"]) is not None
        and num(r["bsi_score"]) is not None
    ]


def group_article(rows):
    groups = defaultdict(list)
    for r in rows:
        key = r["doi"] or r["article_id"] or r["article_title"] or r["file"]
        groups[key].append(r)
    return groups


def group_domain(rows):
    groups = defaultdict(list)
    for r in rows:
        domain = r["domain"] or "UNKNOWN"
        groups[domain].append(r)
    return groups


def stats(rows):
    raw = [num(r["raw_score"]) for r in rows]
    bsi = [num(r["bsi_score"]) for r in rows]
    delta = [num(r["delta"]) for r in rows]

    raw = [x for x in raw if x is not None]
    bsi = [x for x in bsi if x is not None]
    delta = [x for x in delta if x is not None]

    return raw, bsi, delta


def analysis_article(rows):
    out = []

    for key, rs in sorted(group_article(rows).items()):
        raw, bsi, delta = stats(rs)
        if not delta:
            continue

        winners = Counter(clean(r["winner"]).lower() for r in rs)

        domains = sorted(
            set(r["domain"] for r in rs if r["domain"])
        )

        out.append({
            "article_key": key,
            "article_title": rs[0]["article_title"],
            "domains": "; ".join(domains),
            "runs": len(rs),
            "raw_mean": round(mean(raw), 4),
            "bsi_mean": round(mean(bsi), 4),
            "delta_mean": round(mean(delta), 4),
            "delta_median": round(median(delta), 4),
            "delta_sd": round(pstdev(delta), 4) if len(delta) > 1 else 0,
            "delta_min": min(delta),
            "delta_max": max(delta),
            "bsi_wins": winners.get("bsi", 0),
            "raw_wins": winners.get("raw", 0),
            "ties": winners.get("tie", 0),
        })

    return out


def analysis_domain(rows):
    out = []

    for domain, rs in sorted(group_domain(rows).items()):
        raw, bsi, delta = stats(rs)
        if not delta:
            continue

        winners = Counter(clean(r["winner"]).lower() for r in rs)

        articles = {
            r["doi"] or r["article_id"] or r["article_title"] or r["file"]
            for r in rs
        }

        out.append({
            "domain": domain,
            "runs": len(rs),
            "unique_articles": len(articles),
            "raw_mean": round(mean(raw), 4),
            "bsi_mean": round(mean(bsi), 4),
            "delta_mean": round(mean(delta), 4),
            "delta_median": round(median(delta), 4),
            "delta_sd": round(pstdev(delta), 4) if len(delta) > 1 else 0,
            "delta_min": min(delta),
            "delta_max": max(delta),
            "bsi_wins": winners.get("bsi", 0),
            "raw_wins": winners.get("raw", 0),
            "ties": winners.get("tie", 0),
        })

    return out


def analysis_drift(rows):
    out = []

    for key, rs in sorted(group_article(rows).items()):
        if len(rs) < 2:
            continue

        raw, bsi, delta = stats(rs)

        winners = [clean(r["winner"]).lower() for r in rs]

        out.append({
            "article_key": key,
            "article_title": rs[0]["article_title"],
            "runs": len(rs),
            "delta_mean": round(mean(delta), 4),
            "delta_sd": round(pstdev(delta), 4),
            "delta_range": round(max(delta) - min(delta), 4),
            "delta_min": min(delta),
            "delta_max": max(delta),
            "raw_sd": round(pstdev(raw), 4),
            "bsi_sd": round(pstdev(bsi), 4),
            "raw_range": round(max(raw) - min(raw), 4),
            "bsi_range": round(max(bsi) - min(bsi), 4),
            "bsi_wins": winners.count("bsi"),
            "raw_wins": winners.count("raw"),
            "ties": winners.count("tie"),
            "winner_switch": len(set(winners)) > 1,
        })

    return out


def analysis_model(rows):
    out = []
    groups = defaultdict(list)

    for r in rows:
        model = clean(r["analyst_model"])
        if model:
            groups[model].append(r)

    for model, rs in sorted(groups.items()):
        raw, bsi, delta = stats(rs)
        if not delta:
            continue

        winners = Counter(clean(r["winner"]).lower() for r in rs)

        articles = {
            r["doi"] or r["article_id"] or r["article_title"] or r["file"]
            for r in rs
        }

        out.append({
            "analyst_model": model,
            "runs": len(rs),
            "unique_articles": len(articles),
            "raw_mean": round(mean(raw), 4),
            "bsi_mean": round(mean(bsi), 4),
            "delta_mean": round(mean(delta), 4),
            "delta_median": round(median(delta), 4),
            "delta_sd": round(pstdev(delta), 4) if len(delta) > 1 else 0,
            "delta_min": min(delta),
            "delta_max": max(delta),
            "bsi_wins": winners.get("bsi", 0),
            "raw_wins": winners.get("raw", 0),
            "ties": winners.get("tie", 0),
        })

    return out


def analysis_incremental_value(rows):
    """
    Cross-tabulation of (relevance, realization, incremental_value) among
    VALID rows, with counts and percent-of-VALID -- the same underlying
    data as BENCHMARK_REPORT_8_TABLES.md's TABLE 3 / TABLE 4, persisted
    as a standalone CSV instead of only existing inside the rendered
    report.
    """
    out = []
    total = len(rows)

    cross = Counter()
    for r in rows:
        rel = clean(r["relevance"]).lower()
        rea = clean(r["realization"]).lower()
        inc = clean(r["incremental_value"]).lower()
        if rel and rea and inc:
            cross[(rel, rea, inc)] += 1

    for (rel, rea, inc), n in cross.most_common():
        out.append({
            "relevance": rel,
            "realization": rea,
            "incremental_value": inc,
            "count": n,
            "percent_of_valid": round(100 * n / total, 2) if total else 0,
        })

    return out


def main():
    paths = sorted(COMPARE.glob("*.json"))
    rows = [one_row(p) for p in paths]

    scientific_fields = [
        "file", "status", "article_title", "doi", "article_id",
        "domain", "analyst_model", "generator", "mode",
        "judge_model", "criteria_source", "winner",
        "raw_score", "bsi_score", "delta",
        "relevance", "realization", "incremental_value",
        "full_text",
    ]

    aggregate_fields = [
        "file", "domain", "article_title", "doi",
        "analyst_model", "judge_model", "criteria_source",
        "winner", "raw_score", "bsi_score", "delta",
        "relevance", "realization", "incremental_value",
        "full_text", "provider", "query",
    ]

    full_fields = [
        "status", "file", "domain", "article_title", "doi",
        "analyst_model", "judge_model", "criteria_source",
        "winner", "raw_score", "bsi_score", "delta",
        "relevance", "realization", "incremental_value",
        "provider", "query",
    ]

    write_csv(SCIENTIFIC, rows, scientific_fields)

    # Full benchmark view: benchmarkable records only.
    # UNJUDGED records are excluded; TEST and ARCHIVED remain visible.
    full_rows = [r for r in rows if r["status"] != "UNJUDGED"]

    write_csv(
        FULL,
        [{k: r.get(k, "") for k in full_fields} for r in full_rows],
        full_fields,
    )

    # Historical aggregate view: same benchmarkable subset as FULL.
    write_csv(
        AGGREGATE,
        [{k: r.get(k, "") for k in aggregate_fields} for r in full_rows],
        aggregate_fields,
    )

    valid = valid_rows(rows)

    article_rows = analysis_article(valid)
    domain_rows = analysis_domain(valid)
    drift_rows = analysis_drift(valid)
    model_rows = analysis_model(valid)
    incremental_rows = analysis_incremental_value(valid)

    write_csv(
        ARTICLE,
        article_rows,
        [
            "article_key", "article_title", "domains", "runs",
            "raw_mean", "bsi_mean", "delta_mean", "delta_median",
            "delta_sd", "delta_min", "delta_max",
            "bsi_wins", "raw_wins", "ties",
        ],
    )

    write_csv(
        DOMAIN,
        domain_rows,
        [
            "domain", "runs", "unique_articles",
            "raw_mean", "bsi_mean", "delta_mean",
            "delta_median", "delta_sd", "delta_min", "delta_max",
            "bsi_wins", "raw_wins", "ties",
        ],
    )

    write_csv(
        DRIFT,
        drift_rows,
        [
            "article_key", "article_title", "runs",
            "delta_mean", "delta_sd", "delta_range",
            "delta_min", "delta_max",
            "raw_sd", "bsi_sd", "raw_range", "bsi_range",
            "bsi_wins", "raw_wins", "ties", "winner_switch",
        ],
    )

    write_csv(
        MODEL,
        model_rows,
        [
            "analyst_model", "runs", "unique_articles",
            "raw_mean", "bsi_mean", "delta_mean", "delta_median",
            "delta_sd", "delta_min", "delta_max",
            "bsi_wins", "raw_wins", "ties",
        ],
    )

    write_csv(
        INCREMENTAL,
        incremental_rows,
        [
            "relevance", "realization", "incremental_value",
            "count", "percent_of_valid",
        ],
    )

    status = Counter(r["status"] for r in rows)
    winners = Counter(
        clean(r["winner"]).lower()
        for r in valid
        if clean(r["winner"])
    )

    print("===== CSV REBUILD COMPLETE =====")
    print("JSON files:", len(paths))
    print("VALID:", status.get("VALID", 0))
    print("UNJUDGED:", status.get("UNJUDGED", 0))
    print("TEST:", status.get("TEST", 0))
    print("ARCHIVED:", status.get("ARCHIVED", 0))
    print("VALID scored:", len(valid))
    print()
    print("===== VALID WINNERS =====")
    print("BSI:", winners.get("bsi", 0))
    print("RAW:", winners.get("raw", 0))
    print("TIE:", winners.get("tie", 0))
    print()
    print("===== OUTPUT ROWS =====")
    print("scientific:", len(rows))
    print("full:", len(full_rows))
    print("aggregate:", len(full_rows))
    print("article:", len(article_rows))
    print("domain:", len(domain_rows))
    print("drift:", len(drift_rows))
    print("model:", len(model_rows))
    print("incremental_value:", len(incremental_rows))


if __name__ == "__main__":
    main()
