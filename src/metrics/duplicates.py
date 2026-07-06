import pandas as pd


def calculate_duplicate_metrics(data):
    """
    Calculate duplication-related quality metrics
    """

    etudiants_df = data["Etudiants"]
    enseignement_df = data["Enseignement"]
    evaluation_df = data["Evaluation"]
    notes_df = data["Notes_activite"]

    # -----------------------------------
    # TOTAL ROWS
    # -----------------------------------

    total_students = len(etudiants_df)
    total_teaching = len(enseignement_df)
    total_evaluations = len(evaluation_df)
    total_notes = len(notes_df)

    # -----------------------------------
    # 1. PRIMARY KEY DUPLICATES
    # -----------------------------------

    student_pk_dup_pct = round(
        etudiants_df["id_etudiant"].duplicated().mean(),
        4
    )

    teaching_pk_dup_pct = round(
        enseignement_df["id_enseignement"].duplicated().mean(),
        4
    )

    evaluation_pk_dup_pct = round(
        evaluation_df["id_eval"].duplicated().mean(),
        4
    )

    # -----------------------------------
    # 2. BUSINESS DUPLICATES (COMPOSITE KEYS)
    # -----------------------------------

    teaching_business_dup_pct = round(
        enseignement_df.duplicated(
            subset=[
                "id_enseignant",
                "id_matiere",
                "id_classe",
                "id_annee"
            ]
        ).mean(),
        4
    )

    evaluation_business_dup_pct = round(
        evaluation_df.duplicated(
            subset=[
                "id_etudiant",
                "id_matiere",
                "id_trimestre"
            ]
        ).mean(),
        4
    )

    # -----------------------------------
    # 3. STUDENT DUPLICATION LOGIC
    # -----------------------------------

    student_name_user_dup_pct = round(
        etudiants_df.duplicated(
            subset=["nom_etudiant", "id_user"]
        ).mean(),
        4
    )

    student_user_dup_pct = round(
        etudiants_df["id_user"].duplicated().mean(),
        4
    )

    # -----------------------------------
    # FINAL RESULTS
    # -----------------------------------

    results = {
        "% duplication PK étudiants":
            student_pk_dup_pct,

        "% duplication PK enseignement":
            teaching_pk_dup_pct,

        "% duplication PK évaluations":
            evaluation_pk_dup_pct,

        "% duplication métier enseignement":
            teaching_business_dup_pct,

        "% duplication métier évaluations":
            evaluation_business_dup_pct,

        "% duplication étudiant (nom + user)":
            student_name_user_dup_pct,

        "% duplication user étudiant":
            student_user_dup_pct
    }

    return results