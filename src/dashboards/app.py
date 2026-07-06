"""
Data Inspector

Author: Adem Sghaier
Copyright (c) 2026 Adem Sghaier

Licensed under the MIT License.
"""

from flask import Flask, render_template
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.utils.metrics_loader import load_metrics

data, metrics = load_metrics()

coverage_metrics = metrics["coverage"]
noise_metrics = metrics["noise"]
integrity_metrics = metrics["integrity"]
duplicates_metrics = metrics["duplicates"]

# ==================================================
# FLASK APP
# ==================================================

app = Flask(__name__)

# ==================================================
# HELPER : LOAD IMAGES
# ==================================================

def load_images(directory):

    figures_dir = os.path.join(
        app.static_folder,
        "figures",
        directory
    )

    images = sorted([
        f"figures/{directory}/{img}"
        for img in os.listdir(figures_dir)
        if img.endswith(".png")
    ])

    return images


# ==================================================
# HOME PAGE
# ==================================================

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


# ==================================================
# COVERAGE PAGE
# ==================================================

@app.route("/coverage")
def coverage():

    return render_template(
        "coverage.html",

        images=load_images("coverage"),

        avg_coverage=
            coverage_metrics[
                "% couverture globale"
            ],

        high_coverage=
            coverage_metrics[
                "% étudiants avec couverture ≥ 80%"
            ],

        low_coverage=
            coverage_metrics[
                "% étudiants avec couverture < 50%"
            ]
    )


# ==================================================
# NOISE PAGE
# ==================================================

@app.route("/noise")
def noise():

    return render_template(
        "noise.html",

        images=load_images("noise"),

        null_notes=
            noise_metrics[
                "% notes NULL"
            ],

        invalid_notes=
            noise_metrics[
                "% notes invalides"
            ],

        outliers=
            noise_metrics[
                "% valeurs aberrantes"
            ]
    )


# ==================================================
# INTEGRITY PAGE
# ==================================================

@app.route("/integrity")
def integrity():

    return render_template(
        "integrity.html",

        images=load_images("integrity"),

        broken_refs=
            integrity_metrics[
                "% notes avec activité inexistante"
            ],

        business_issues=
            integrity_metrics[
                "% incohérence activité ↔ enseignant/matière"
            ],

        class_level_inconsistency=
            integrity_metrics[
                "% incohérence classe ↔ niveau"
            ]
    )


# ==================================================
# DUPLICATES PAGE
# ==================================================

@app.route("/duplicates")
def duplicates():

    return render_template(
        "duplicates.html",

        images=load_images("duplicates"),

        pk_duplicates=
            duplicates_metrics[
                "% duplication PK étudiants"
            ],

        business_duplicates=
            duplicates_metrics[
                "% duplication métier enseignement"
            ],

        user_duplicates=
            duplicates_metrics[
                "% duplication user étudiant"
            ]
    )


# ==================================================
# RUN APP
# ==================================================

if __name__ == "__main__":

    app.run(debug=True)