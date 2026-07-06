import pandas as pd


def calculate_integrity_metrics(data):
    """
    Integrity checks: referential + business + system consistency
    """

    notes_df = data["Notes_activite"]
    activite_df = data["Activite"]
    etudiants_df = data["Etudiants"]
    enseignants_df = data["Enseignant"]
    enseignement_df = data["Enseignement"]
    evaluation_df = data["Evaluation"]
    matiere_df = data["Matiere"]
    classe_df = data["Classe"]
    annee_df = data["Annee_scolaire"]
    trimestres_df = data["Trimestre"]

    # ===================================
    # 1. REFERENTIAL INTEGRITY
    # ===================================

    notes_missing_activity = notes_df[
        ~notes_df["id_activité"].isin(activite_df["id_activité"])
    ]

    activity_missing_teacher = activite_df[
        ~activite_df["id_enseignant"].isin(enseignants_df["id_enseignant"])
    ]

    evaluation_missing_student = evaluation_df[
        ~evaluation_df["id_etudiant"].isin(etudiants_df["id_etudiant"])
    ]

    evaluation_missing_subject = evaluation_df[
        ~evaluation_df["id_matiere"].isin(matiere_df["id_matiere"])
    ]

    teaching_missing_teacher = enseignement_df[
        ~enseignement_df["id_enseignant"].isin(enseignants_df["id_enseignant"])
    ]

    teaching_missing_subject = enseignement_df[
        ~enseignement_df["id_matiere"].isin(matiere_df["id_matiere"])
    ]

    trimester_missing = activite_df[
        ~activite_df["id_trimestre"].isin(trimestres_df["id_trimestre"])
    ]

    # ===================================
    # 2. BUSINESS LOGIC INTEGRITY
    # ===================================

    # Activité ↔ Enseignement mismatch
    activity_teacher_mismatch = activite_df.merge(
        enseignement_df,
        left_on=["id_enseignant", "id_matière"],
        right_on=["id_enseignant", "id_matiere"],
        how="left",
        indicator=True
    )

    activity_teacher_mismatch_pct = round(
        len(activity_teacher_mismatch[
            activity_teacher_mismatch["_merge"] == "left_only"
        ]) / len(activite_df),
        4
    )

    # Classe ↔ niveau incohérence
    class_level_issue = enseignement_df.merge(
        classe_df,
        on="id_classe",
        how="left"
    )

    class_level_missing = class_level_issue["id_niveau"].isna().mean()

    # Trimestre ↔ année incohérence (correct logic)
    trimester_year_issue = trimestres_df[
        ~trimestres_df["id_annee"].isin(annee_df["id_annee"])
    ]

    trimester_year_issue_pct = round(
        len(trimester_year_issue) / len(trimestres_df),
        4
    )

    # ===================================
    # 3. SYSTEM CONSISTENCY
    # ===================================

    students_without_inscription = etudiants_df[
        ~etudiants_df["id_etudiant"].isin(
            data["Inscription"]["id_etudiant"]
        )
    ]

    teachers_without_activity = enseignants_df[
        ~enseignants_df["id_enseignant"].isin(
            activite_df["id_enseignant"]
        )
    ]

    subjects_without_activity = matiere_df[
        ~matiere_df["id_matiere"].isin(
            activite_df["id_matière"]
        )
    ]

    # ===================================
    # SAFETY DENOMINATORS
    # ===================================

    def safe_div(num, den):
        return round(num / den, 4) if den > 0 else 0

    # ===================================
    # FINAL RESULTS
    # ===================================

    results = {
        "% notes avec activité inexistante":
            safe_div(len(notes_missing_activity), len(notes_df)),

        "% activités avec enseignant inexistant":
            safe_div(len(activity_missing_teacher), len(activite_df)),

        "% évaluations avec étudiant inexistant":
            safe_div(len(evaluation_missing_student), len(evaluation_df)),

        "% évaluations avec matière inexistante":
            safe_div(len(evaluation_missing_subject), len(evaluation_df)),

        "% enseignements avec enseignant inexistant":
            safe_div(len(teaching_missing_teacher), len(enseignement_df)),

        "% enseignements avec matière inexistante":
            safe_div(len(teaching_missing_subject), len(enseignement_df)),

        "% incohérence activité ↔ enseignant/matière":
            activity_teacher_mismatch_pct,

        "% incohérence classe ↔ niveau":
            round(class_level_missing, 4),

        "% incohérence trimestre ↔ année":
            trimester_year_issue_pct,

        "% étudiants sans inscription":
            safe_div(len(students_without_inscription), len(etudiants_df)),

        "% enseignants sans activité":
            safe_div(len(teachers_without_activity), len(enseignants_df)),

        "% matières sans activité":
            safe_div(len(subjects_without_activity), len(matiere_df))
    }

    return results