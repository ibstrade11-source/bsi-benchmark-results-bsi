# bsi-benchmark-results-bsi

## فارسی

مخزن ذخیرهٔ نتایج بنچمارک برای چارچوب **BSI**، جدا از مخزن سورس ابزار (`bsi-benchmark`). این مخزن فقط نتایج ثبت‌شده و گزارش‌های تحلیل تجمیعی آن‌ها را نگه می‌دارد؛ هیچ کد منبع ابزار اینجا قرار ندارد.

هر چارچوبی که با ابزار `bsi-benchmark` سنجیده شود، مخزن نتایج مستقل خودش را دارد؛ این مخزن مخصوص چارچوب BSI است.

### ساختار

```
compare/                              نتایج معتبر compare-cli (هر رکورد: یک جفت .json + .md)
self_compare/                         رکوردهای معتبر self-compare (همان جفت json+md)
scripts/
    rebuild_csvs.py                       تولید ۸ گزارش CSV زیر از روی compare/
    generate_report.py, build_report.sh   تولید گزارش نهایی ۸‌جدولی از روی همان CSVها
BENCHMARK_REPORT_8_TABLES.md          گزارش خوانا و یکجا (۸ جدول)، خروجی generate_report.py
*.csv                                  ۸ فایل گزارش تجمیعی خام
```

نتایج مستقیماً و دستی اینجا اضافه نمی‌شوند؛ همه از مخزن سورس، پس از اعتبارسنجی توسط `validate_and_curate_result.py`، ثبت و push می‌شوند. برای فرمان‌های اجرای بنچمارک و ثبت نتیجه، به README مخزن سورس (`bsi-benchmark`) مراجعه کن.

### گزارش‌های CSV

هر ۸ فایل مستقیماً از پیمایش `compare/*.json` توسط `scripts/rebuild_csvs.py` ساخته می‌شوند؛ به `self_compare/` کاری ندارند.

**بازسازی بعد از ثبت نتایج تازه:**

    cd ~/bsi-benchmark-results-bsi
    python scripts/rebuild_csvs.py

**دسته‌بندی وضعیت (`status`):**

| وضعیت | معیار تشخیص |
|---|---|
| `TEST` | نام فایل حاوی الگوهایی مثل `smoke_test`, `mock`, `nemotron_test`, `mobile_test` است |
| `ARCHIVED` | نام فایل حاوی `archived` است |
| `UNJUDGED` | `benchmark_status` صریحاً `not_benchmarkable` است، یا `judge_result` معتبر ندارد |
| `VALID` | نه TEST نه ARCHIVED، و حداقل یک `judge_result` واقعی دارد |

> این منطق مستقل از اعتبارسنجی `validate_and_curate_result.py` در مخزن سورس است (آنجا `criteria_source == "llm"` هم شرط صریح است، اینجا نه). یک فایل ممکن است در `compare/` باشد ولی اینجا `TEST` یا `ARCHIVED` طبقه‌بندی شود — این عمدی است؛ دو ابزار دو زاویهٔ متفاوت از فیلتر را پیاده می‌کنند.

**فایل‌ها:**

| فایل | سطح هر ردیف | فیلدهای کلیدی |
|---|---|---|
| `benchmark_aggregate_scientific.csv` | هر فایل JSON در `compare/`، بدون فیلتر (VALID + TEST + ARCHIVED + UNJUDGED) | `file, status, article_title, doi, article_id, domain, analyst_model, generator, mode, judge_model, criteria_source, winner, raw_score, bsi_score, delta, relevance, realization, incremental_value, full_text` |
| `benchmark_aggregate_full.csv` | فقط رکوردهای غیر-UNJUDGED | زیرمجموعهٔ ستون‌های بالا + `status` |
| `benchmark_aggregate.csv` | همان زیرمجموعهٔ `full`، بدون ستون `status` | نمای سادهٔ تاریخی |
| `article_level_analysis.csv` | هر مقالهٔ یکتا (DOI/article_id/عنوان) در میان رکوردهای VALID | `runs, raw_mean, bsi_mean, delta_mean, delta_median, delta_sd, delta_min, delta_max, bsi_wins, raw_wins, ties` |
| `domain_level_analysis.csv` | هر حوزه/دامنه | همان آمار بالا + `unique_articles` |
| `model_level_analysis.csv` | هر مدل تحلیل‌گر (`analyst_model`) | همان آمار بالا |
| `drift_repeatability_analysis.csv` | فقط مقالاتی با بیش از یک اجرای VALID | `delta_sd, delta_range, raw_sd, bsi_sd, raw_range, bsi_range, winner_switch` |
| `incremental_value_analysis.csv` | هر ترکیب یکتای (relevance, realization, incremental_value) در میان رکوردهای VALID | `relevance, realization, incremental_value, count, percent_of_valid` |

### گزارش نهایی (`BENCHMARK_REPORT_8_TABLES.md`)

با اجرای زیر، همان ۸ گزارش CSV به یک فایل Markdown خوانا (۸ جدول) تبدیل می‌شود:

    python scripts/generate_report.py

اسکریپت یک بررسی داخلی دارد که اگر هر یک از ۸ جدول ساخته نشود، با خطا متوقف می‌شود — یعنی وجود فایل خروجی خودش تضمینی است که هر ۸ جدول با داده‌های واقعی ساخته شده‌اند.

### فرمان پیشنهادی — بازسازی کامل با یک دستور

به‌جای اجرای جداگانهٔ `rebuild_csvs.py` و `generate_report.py`، بعد از هر ثبت نتیجهٔ تازه فقط این را بزن؛ هر دو مرحله را پشت‌سرهم و به‌ترتیب درست اجرا می‌کند:

    cd ~/bsi-benchmark-results-bsi
    bash scripts/build_report.sh

خروجی موفق چیزی شبیه این است:

    ===== BUILD REPORT COMPLETE =====
    REPORT: /path/to/bsi-benchmark-results-bsi/BENCHMARK_REPORT_8_TABLES.md

اگر خطایی در میانهٔ راه رخ دهد (مثلاً یکی از ۸ جدول ساخته نشود)، اسکریپت به‌خاطر `set -e` بلافاصله متوقف می‌شود و پیام «BUILD REPORT COMPLETE» چاپ نمی‌شود — یعنی دیدن این پیام یعنی هم ۸ CSV و هم گزارش نهایی با موفقیت و از روی داده‌های واقعی بازسازی شده‌اند.

---

## English

Results-storage repository for the **BSI** framework, kept separate from the `bsi-benchmark` tool's source repository. This repository holds only registered benchmark results and their aggregate analysis reports — no tool source code lives here.

Every framework benchmarked with the `bsi-benchmark` tool gets its own independent results repository; this one is specific to the BSI framework.

### Structure

```
compare/                              Valid compare-cli results (each record: a .json + .md pair)
self_compare/                         Valid self-compare records (same json+md pairing)
scripts/
    rebuild_csvs.py                       Generates the 8 CSV reports below from compare/
    generate_report.py, build_report.sh   Builds the final 8-table report from those CSVs
BENCHMARK_REPORT_8_TABLES.md          Single readable report (8 tables), output of generate_report.py
*.csv                                  8 raw aggregate report files
```

Results are never added here manually. Everything is registered and pushed from the source repository after validation by `validate_and_curate_result.py`. For benchmark-run and result-registration commands, see the source repo's (`bsi-benchmark`) README.

### CSV reports

All 8 files are built directly from scanning `compare/*.json` via `scripts/rebuild_csvs.py`; `self_compare/` is not included.

**Rebuilding after registering new results:**

    cd ~/bsi-benchmark-results-bsi
    python scripts/rebuild_csvs.py

**Status classification:**

| Status | Determined when |
|---|---|
| `TEST` | Filename matches patterns like `smoke_test`, `mock`, `nemotron_test`, `mobile_test` |
| `ARCHIVED` | Filename contains `archived` |
| `UNJUDGED` | `benchmark_status` is explicitly `not_benchmarkable`, or no valid `judge_result` is present |
| `VALID` | Neither TEST nor ARCHIVED, and contains a real `judge_result` |

> This logic is independent from `validate_and_curate_result.py`'s validation in the source repo (which also explicitly requires `criteria_source == "llm"`). A file can sit in `compare/` yet be classified `TEST` or `ARCHIVED` here — that's intentional; the two tools apply different filtering lenses.

**Files:**

| File | Row granularity | Key fields |
|---|---|---|
| `benchmark_aggregate_scientific.csv` | Every JSON file in `compare/`, unfiltered (VALID + TEST + ARCHIVED + UNJUDGED) | `file, status, article_title, doi, article_id, domain, analyst_model, generator, mode, judge_model, criteria_source, winner, raw_score, bsi_score, delta, relevance, realization, incremental_value, full_text` |
| `benchmark_aggregate_full.csv` | Non-UNJUDGED records only | Subset of the above columns + `status` |
| `benchmark_aggregate.csv` | Same `full` subset, without the `status` column | Simplified historical view |
| `article_level_analysis.csv` | Each unique article (DOI/article_id/title) among VALID records | `runs, raw_mean, bsi_mean, delta_mean, delta_median, delta_sd, delta_min, delta_max, bsi_wins, raw_wins, ties` |
| `domain_level_analysis.csv` | Each domain | Same stats + `unique_articles` |
| `model_level_analysis.csv` | Each analyst model (`analyst_model`) | Same stats |
| `drift_repeatability_analysis.csv` | Only articles with more than one VALID run | `delta_sd, delta_range, raw_sd, bsi_sd, raw_range, bsi_range, winner_switch` |
| `incremental_value_analysis.csv` | Each unique (relevance, realization, incremental_value) combination among VALID records | `relevance, realization, incremental_value, count, percent_of_valid` |

### Final report (`BENCHMARK_REPORT_8_TABLES.md`)

Turns the same 8 CSV reports into one readable Markdown file (8 tables):

    python scripts/generate_report.py

The script runs an internal check and fails loudly if any of the 8 tables can't be built — so the mere existence of the output file guarantees all 8 tables were generated from real data.

### Recommended command — full rebuild in one step

Instead of running `rebuild_csvs.py` and `generate_report.py` separately, after registering new results just run this — it runs both steps in the correct order:

    cd ~/bsi-benchmark-results-bsi
    bash scripts/build_report.sh

A successful run ends with:

    ===== BUILD REPORT COMPLETE =====
    REPORT: /path/to/bsi-benchmark-results-bsi/BENCHMARK_REPORT_8_TABLES.md

If anything fails along the way (e.g. one of the 8 tables can't be built), the script stops immediately (`set -e`) and this completion message is never printed — so seeing it is confirmation that both the 8 CSVs and the final report were successfully rebuilt from real data.
