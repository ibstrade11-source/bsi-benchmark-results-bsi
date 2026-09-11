#!/data/data/com.termux/files/usr/bin/bash
set -e

cd "$(dirname "$0")/.."

python scripts/rebuild_csvs.py
python scripts/generate_report.py

printf '%s\n' '===== BUILD REPORT COMPLETE ====='
printf '%s\n' "REPORT: $(pwd)/BENCHMARK_REPORT_8_TABLES.md"
