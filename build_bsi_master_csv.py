import csv
import json
import re
from pathlib import Path
from statistics import mean, median

ROOT = Path(".")
COMPARE = ROOT / "compare"
ALL_CSV = ROOT / "BSI_Benchmark_All_Runs.csv"
VALID_CSV = ROOT / "BSI_Benchmark_Valid_Comparisons.csv"
STATS_TXT = ROOT / "BSI_Benchmark_Statistics.txt"


def clean(v):
    if v is None:
        return ""
    if isinstance(v, (dict, list)):
        return json.dumps(v, ensure_ascii=False, separators=(",", ":"))
    return str(v).strip()


def find_total_scores(obj):
    """
    Returns (raw, bsi, path, criteria_source) tuples. criteria_source is
    read from the same dict that holds total_scores (normally the
    judge_result object), so callers can tell a real LLM judgement apart
    from a heuristic_fallback one -- both produce numeric total_scores,
    but only "llm" reflects an actual independent judge run.
    """
    found = []

    def walk(x, path=""):
        if isinstance(x, dict):
            ts = x.get("total_scores")
            if isinstance(ts, dict):
                raw = ts.get("raw", ts.get("RAW"))
                bsi = ts.get("bsi", ts.get("BSI"))
                if raw is not None and bsi is not None:
                    try:
                        criteria_source = str(x.get("criteria_source") or "")
                        found.append((float(raw), float(bsi), path + ".total_scores", criteria_source))
                    except (TypeError, ValueError):
                        pass

            for k, v in x.items():
                walk(v, f"{path}.{k}" if path else k)

        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, f"{path}[{i}]")

    walk(obj)
    return found


def first_value(obj, keys):
    if not isinstance(obj, dict):
        return ""

    for k in keys:
        if k in obj and obj[k] not in (None, ""):
            return obj[k]

    for v in obj.values():
        if isinstance(v, dict):
            r = first_value(v, keys)
            if r not in ("", None):
                return r

    return ""


def infer_from_filename(path):
    name = path.stem
    return name


def infer_generator(name):
    low = name.lower()

    gens = [
        ("gemini37flash", "Gemini 3.7 Flash"),
        ("gemini37", "Gemini 3.7"),
        ("gemini", "Gemini"),
        ("nemotron", "Nemotron"),
        ("openrouter", "OpenRouter"),
        ("groq", "Groq"),
        ("minimax", "MiniMax"),
        ("claude", "Claude"),
    ]

    for token, label in gens:
        if token in low:
            return label
    return ""


def infer_domain(name):
    low = name.lower()

    mapping = [
        ("political_science", "Political Science"),
        ("politics", "Political Science"),
        ("history_of_technology", "History of Technology"),
        ("computational_ecology", "Computational Ecology"),
        ("linguistics", "Linguistics"),
        ("hydrology", "Hydrology"),
        ("agriculture", "Agriculture"),
        ("engineering", "Engineering"),
        ("medicine", "Medicine"),
        ("medical", "Medicine"),
        ("biology", "Biology"),
        ("cognitive", "Cognitive Science"),
        ("psych", "Psychology"),
        ("sociology", "Sociology"),
        ("social_science", "Social Science"),
        ("philosophy", "Philosophy"),
        ("physics", "Physics"),
        ("quantum", "Quantum Physics"),
        ("particle_physics", "Particle Physics"),
        ("chem", "Chemistry"),
        ("economics", "Economics"),
        ("econ_", "Economics"),
        ("law", "Law"),
        ("robotics", "Robotics"),
        ("neuroscience", "Neuroscience"),
        ("llm_knowledge", "LLM / Knowledge"),
        ("self_compare", "Self-Compare"),
        ("arxiv_", "Research / arXiv"),
    ]

    for token, label in mapping:
        if token in low:
            return label
    return "Unknown"


def extract(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return [{
            "file": str(path),
            "status": "unreadable",
            "error": repr(e),
        }]

    name = path.name
    low = name.lower()

    archived = ".archived_" in low or ".archived" in low
    self_compare = "self_compare" in str(path).lower()

    article = data.get("article", {}) if isinstance(data, dict) else {}
    if not isinstance(article, dict):
        article = {}

    article_title = (
        article.get("title")
        or data.get("title")
        or data.get("article_title")
        or first_value(data, ["title"])
        or ""
    )

    doi = (
        article.get("doi")
        or data.get("doi")
        or first_value(data, ["doi"])
        or ""
    )

    work_id = (
        article.get("work_id")
        or article.get("id")
        or data.get("work_id")
        or data.get("article_id")
        or ""
    )

    analyst = (
        data.get("analyst")
        or data.get("generator")
        or data.get("generator_name")
        or first_value(data, ["analyst", "generator"])
        or infer_generator(name)
    )

    judge = (
        data.get("judge")
        or data.get("judge_model")
        or data.get("judge_name")
        or first_value(data, ["judge", "judge_model", "judge_name"])
        or ""
    )

    candidates = find_total_scores(data)
    # Prefer an actual judge_result path when several score pairs exist.
    candidates.sort(key=lambda x: ("judge_result" not in x[2], len(x[2])))

    base = {
        "file": str(path),
        "run_name": path.stem,
        "domain": infer_domain(name),
        "article_title": clean(article_title),
        "doi": clean(doi),
        "work_id": clean(work_id),
        "analyst": clean(analyst),
        "judge": clean(judge),
        "archived": "yes" if archived else "no",
        "self_compare": "yes" if self_compare else "no",
        "score_source": "",
        "criteria_source": "",
        "raw": "",
        "bsi": "",
        "delta_bsi_minus_raw": "",
        "winner": "",
        "evidence_status": "",
        "status": clean(data.get("status", "")) if isinstance(data, dict) else "",
        "error": clean(data.get("error", "")) if isinstance(data, dict) else "",
    }

    if not candidates:
        base["evidence_status"] = "NO_VALID_TOTAL_SCORES"
        return [base]

    raw, bsi, score_path, criteria_source = candidates[0]
    base["score_source"] = score_path
    base["criteria_source"] = criteria_source
    base["raw"] = raw
    base["bsi"] = bsi
    base["delta_bsi_minus_raw"] = round(bsi - raw, 3)

    if bsi > raw:
        base["winner"] = "BSI"
    elif raw > bsi:
        base["winner"] = "RAW"
    else:
        base["winner"] = "TIE"

    # Evidence validity: numeric RAW/BSI scores, not archived/self-compare,
    # AND a real LLM judge (criteria_source == "llm") -- a heuristic
    # fallback also produces numeric total_scores but is not an
    # independent judgement, so it must never count as a valid comparison.
    if archived:
        base["evidence_status"] = "ARCHIVED"
    elif self_compare:
        base["evidence_status"] = "SELF_COMPARE"
    elif "judge_result" in score_path and criteria_source == "llm":
        base["evidence_status"] = "VALID_JUDGE_COMPARISON"
    elif "judge_result" in score_path and criteria_source and criteria_source != "llm":
        base["evidence_status"] = "HEURISTIC_JUDGE"
    else:
        base["evidence_status"] = "SCORE_FOUND_NONSTANDARD_PATH"

    return [base]


rows = []

files = sorted(
    p for p in COMPARE.glob("*.json")
    if ".checkpoint.json" not in p.name
)

for path in files:
    rows.extend(extract(path))

fields = [
    "file",
    "run_name",
    "domain",
    "article_title",
    "doi",
    "work_id",
    "analyst",
    "judge",
    "archived",
    "self_compare",
    "score_source",
    "criteria_source",
    "raw",
    "bsi",
    "delta_bsi_minus_raw",
    "winner",
    "evidence_status",
    "status",
    "error",
]

with ALL_CSV.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

valid = [
    r for r in rows
    if r["evidence_status"] == "VALID_JUDGE_COMPARISON"
]

with VALID_CSV.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(valid)

raw_scores = [float(r["raw"]) for r in valid]
bsi_scores = [float(r["bsi"]) for r in valid]
deltas = [float(r["delta_bsi_minus_raw"]) for r in valid]

bsi_wins = sum(r["winner"] == "BSI" for r in valid)
raw_wins = sum(r["winner"] == "RAW" for r in valid)
ties = sum(r["winner"] == "TIE" for r in valid)
domains = {}
for r in valid:
    domains.setdefault(r["domain"], []).append(r)

lines = []
lines.append("=" * 78)
lines.append("BSI BENCHMARK — COMPLETE MASTER STATISTICS")
lines.append("=" * 78)
lines.append("")
lines.append(f"JSON files scanned              : {len(files)}")
lines.append(f"CSV rows generated              : {len(rows)}")
lines.append(f"Valid judge comparisons         : {len(valid)}")
lines.append(
    f"Non-valid / other rows          : "
    f"{len(rows) - len(valid)}"
)
lines.append("")
lines.append("SCORE STATISTICS")
lines.append("-" * 78)

if valid:
    lines += [
        f"RAW mean                        : {mean(raw_scores):.3f}",
        f"BSI mean                        : {mean(bsi_scores):.3f}",
        f"Mean Δ (BSI − RAW)              : {mean(deltas):+.3f}",
        f"Median Δ                        : {median(deltas):+.3f}",
        f"RAW minimum                     : {min(raw_scores):.3f}",
        f"RAW maximum                     : {max(raw_scores):.3f}",
        f"BSI minimum                     : {min(bsi_scores):.3f}",
        f"BSI maximum                     : {max(bsi_scores):.3f}",
        "",
        "WIN / TIE STATISTICS",
        "-" * 78,
        f"BSI wins                        : {bsi_wins}",
        f"RAW wins                        : {raw_wins}",
        f"Ties                            : {ties}",
        f"BSI win rate                    : {100*bsi_wins/len(valid):.1f}%",
        f"RAW win rate                    : {100*raw_wins/len(valid):.1f}%",
        f"Tie rate                        : {100*ties/len(valid):.1f}%",
        "",
        "DOMAIN BREAKDOWN",
        "-" * 78,
    ]

    for domain in sorted(domains):
        rs = domains[domain]
        ds = [float(x["delta_bsi_minus_raw"]) for x in rs]
        bw = sum(x["winner"] == "BSI" for x in rs)
        rw = sum(x["winner"] == "RAW" for x in rs)
        tt = sum(x["winner"] == "TIE" for x in rs)
        lines.append(
            f"{domain:<28} N={len(rs):>3} "
            f"RAW={mean(float(x['raw']) for x in rs):.2f} "
            f"BSI={mean(float(x['bsi']) for x in rs):.2f} "
            f"Δ={mean(ds):+.2f} "
            f"W(B/R/T)={bw}/{rw}/{tt}"
        )
else:
    lines.append("No VALID_JUDGE_COMPARISON rows were detected.")

lines += [
    "",
    "EVIDENCE STATUS COUNTS",
    "-" * 78,
]

status_counts = {}
for r in rows:
    status_counts[r["evidence_status"]] = status_counts.get(
        r["evidence_status"], 0
    ) + 1

for k, v in sorted(status_counts.items()):
    lines.append(f"{k:<40} {v}")

STATS_TXT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("\n".join(lines))
print("")
print("CREATED:")
print(f"  {ALL_CSV}")
print(f"  {VALID_CSV}")
print(f"  {STATS_TXT}")
