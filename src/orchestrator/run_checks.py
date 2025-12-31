import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from datetime import datetime

from checks.quality_checks import check_nulls, check_row_count
from checks.sla_checks import check_freshness


def main():
    # Load sample dataset
    df = pd.read_csv("data/sample_dataset.csv")

    results = []

    # Quality checks
    null_ok, null_pct = check_nulls(df, "value", max_null_pct=0.05)
    results.append(("null_check:value", null_ok, null_pct))

    row_ok, row_count = check_row_count(df, min_rows=10)
    results.append(("row_count_check", row_ok, row_count))

    # SLA checks (demo: assume dataset updated "now")
    fresh_ok, delay = check_freshness(datetime.utcnow(), max_delay_minutes=30)
    results.append(("freshness_sla", fresh_ok, delay))

    report = pd.DataFrame(results, columns=["check", "pass", "metric"])
    report.to_csv("outputs/sla_report.csv", index=False)
    print("Wrote outputs/sla_report.csv")


if __name__ == "__main__":
    main()

