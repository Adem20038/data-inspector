from config.paths import PROJECT_ROOT
import matplotlib.pyplot as plt
import shutil

from src.dashboards.charts import create_kpi_chart


# ==================================================
# REPORTS / FIGURES PATH
# ==================================================

FIGURES_DIR = (
    PROJECT_ROOT
    / "src"
    / "dashboards"
    / "static"
    / "figures"
)


# ==================================================
# SAFE FILENAME
# ==================================================

def clean_filename(name):

    replacements = {
        "%": "pct",
        " ": "_",
        "/": "_",
        "\\": "_",
        "↔": "_",
        "(": "",
        ")": "",
        ",": "",
        ":": "",
        "<": "lt",
        ">": "gt",
        "=": "eq",
        "-": "_",
        "?": "",
        "*": "",
        "|": "",
        '"': "",
        "'": "",
        "é": "e",
        "è": "e",
        "ê": "e",
        "à": "a",
        "ù": "u"
    }

    filename = name.lower()

    for old, new in replacements.items():
        filename = filename.replace(old, new)

    return filename + ".png"


# ==================================================
# MAIN DASHBOARD GENERATION
# ==================================================

def generate_full_dashboard(metrics):

    # ----------------------------------
    # CLEAN OLD OUTPUT
    # ----------------------------------

    if FIGURES_DIR.exists():
        shutil.rmtree(FIGURES_DIR)

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    # ==================================================
    # CREATE CATEGORY FOLDERS
    # ==================================================

    for folder in ["coverage", "noise", "integrity", "duplicates"]:
        (FIGURES_DIR / folder).mkdir(parents=True, exist_ok=True)

    # ==================================================
    # GENERIC CHART LOOP — one per category
    # ==================================================

    categories = {
        "coverage":   "coverage",
        "noise":      "noise",
        "integrity":  "integrity",
        "duplicates": "duplicates",
    }

    for category, folder in categories.items():

        print(f"Generating {category} charts...")

        for metric, value in metrics[category].items():

            fig = create_kpi_chart(
                metric_key=metric,
                value=value,
            )

            fig.savefig(
                FIGURES_DIR / folder / clean_filename(metric),
                bbox_inches="tight",
            )

            plt.close(fig)

    # ==================================================
    # DONE
    # ==================================================

    print("\nDashboard generated successfully.")
    print(f"Figures saved in:\n{FIGURES_DIR}")