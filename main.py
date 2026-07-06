"""
Data Inspector

Author: Adem Sghaier
Copyright (c) 2026 Adem Sghaier

Licensed under the MIT License.
"""

from pathlib import Path
import sys

# ==================================================
# PROJECT ROOT CONFIGURATION
# ==================================================

PROJECT_ROOT = Path(__file__).resolve().parent

sys.path.insert(0, str(PROJECT_ROOT))

# ==================================================
# IMPORT METRICS LOADER
# ==================================================

from src.utils.metrics_loader import load_metrics

# ==================================================
# DISPLAY HELPERS
# ==================================================

def print_section(title, metrics):
    """
    Pretty-print a metrics section
    """

    print(f"\n{'=' * 50}")
    print(title.upper())
    print(f"{'=' * 50}")

    for metric, value in metrics.items():

        if isinstance(value, (int, float)):

            value = round(value, 2)

            print(f"{metric:<55} : {value}%")

        else:

            print(f"{metric:<55} : {value}")


def print_report(results):
    """
    Print full data quality report
    """

    print("\n")
    print("#" * 60)
    print("DATA QUALITY REPORT")
    print("#" * 60)

    for section, metrics in results.items():

        print_section(
            section,
            metrics
        )

# ==================================================
# MAIN
# ==================================================

def main():

    print("\nLoading data and computing metrics...\n")

    _, metrics = load_metrics()

    results = {
        "Coverage": metrics["coverage"],
        "Noise": metrics["noise"],
        "Integrity": metrics["integrity"],
        "Duplicates": metrics["duplicates"]
    }

    print_report(results)
# ==================================================
# ENTRY POINT
# ==================================================

if __name__ == "__main__":

    main()

