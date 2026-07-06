import pandas as pd
import numpy as np


def calculate_noise_metrics(data):
    """
    Calculate noise and data quality metrics
    """

    notes_df = data["Notes_activite"]
    activite_df = data["Activite"]
    evaluation_df = data["Evaluation"]

    # -----------------------------------
    # BASIC COUNTS
    # -----------------------------------

    total_notes = len(notes_df)

    # -----------------------------------
    # VALID / INVALID NOTES
    # -----------------------------------

    valid_notes = notes_df[
        (notes_df["note"].notna()) &
        (notes_df["note"] >= 0) &
        (notes_df["note"] <= 20)
    ]

    invalid_notes = notes_df[
        (notes_df["note"].notna()) &
        (
            (notes_df["note"] < 0) |
            (notes_df["note"] > 20)
        )
    ]

    null_notes = notes_df[
        notes_df["note"].isna()
    ]

    # -----------------------------------
    # % NULL NOTES
    # -----------------------------------

    null_notes_pct = round(
        len(null_notes) / total_notes,
        4
    )

    # -----------------------------------
    # % INVALID NOTES
    # -----------------------------------

    invalid_notes_pct = round(
        len(invalid_notes) / total_notes,
        4
    )

    # -----------------------------------
    # NOTE_COMPORTEMENT NULL
    # -----------------------------------

    total_evaluations = len(evaluation_df)

    null_behavior_pct = round(
        evaluation_df["note_comportement"]
        .isna()
        .mean(),
        4
    )

    # -----------------------------------
    # UNUSABLE ROWS
    # note NULL + invalid activity
    # -----------------------------------

    merged = notes_df.merge(
        activite_df,
        on="id_activité",
        how="left",
        indicator=True
    )

    unusable_rows = merged[
        (merged["note"].isna()) &
        (merged["_merge"] == "left_only")
    ]

    unusable_rows_pct = round(
        len(unusable_rows) / total_notes,
        4
    )

    # -----------------------------------
    # EXTREME VALUES
    # -----------------------------------

    zero_notes_pct = round(
        (notes_df["note"] == 0).mean(),
        4
    )

    perfect_notes_pct = round(
        (notes_df["note"] == 20).mean(),
        4
    )

    # -----------------------------------
    # DISTRIBUTION METRICS
    # -----------------------------------

    valid_note_values = valid_notes["note"]

    mean_note = round(
        valid_note_values.mean(),
        2
    )

    median_note = round(
        valid_note_values.median(),
        2
    )

    std_note = round(
        valid_note_values.std(),
        2
    )

    # -----------------------------------
    # REALISTIC RANGE (8 -> 16)
    # -----------------------------------

    realistic_notes_pct = round(
        (
            (
                (valid_note_values >= 8) &
                (valid_note_values <= 16)
            ).mean()
        ),
        4
    )

    # -----------------------------------
    # OUTLIERS (IQR METHOD)
    # -----------------------------------

    Q1 = valid_note_values.quantile(0.25)
    Q3 = valid_note_values.quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = valid_note_values[
        (valid_note_values < lower_bound) |
        (valid_note_values > upper_bound)
    ]

    outliers_pct = round(
        len(outliers) / len(valid_note_values),
        4
    )

    # -----------------------------------
    # FINAL RESULTS
    # -----------------------------------

    results = {
    "% notes NULL":
        null_notes_pct,

    "% notes invalides":
        invalid_notes_pct,

    "% note_comportement NULL":
        null_behavior_pct,

    "% lignes inutilisables":
        unusable_rows_pct,

    "% notes égales à 0":
        zero_notes_pct,

    "% notes égales à 20":
        perfect_notes_pct,

    "% notes réalistes (8-16)":
        realistic_notes_pct,

    "moyenne générale":
        mean_note,

    "médiane":
        median_note,

    "écart-type":
        std_note,

    "% valeurs aberrantes":
        outliers_pct
}

    return results