import pandas as pd


def calculate_coverage_metrics(data):
    """
    Calculate coverage metrics for the dataset
    """

    notes_df = data["Notes_activite"]
    activite_df = data["Activite"]
    etudiants_df = data["Etudiants"]

    # -----------------------------------
    # VALID NOTES ONLY
    # -----------------------------------

    valid_notes = notes_df[
        (notes_df["note"].notna()) &
        (notes_df["note"] >= 0) &
        (notes_df["note"] <= 20)
    ]

    # merge to access subject + trimester
    merged = valid_notes.merge(
        activite_df,
        on="id_activité",
        how="left"
    )
    total_students = etudiants_df["id_etudiant"].nunique()
    # -----------------------------------
    # 1. STUDENT COVERAGE ANALYSIS
    # -----------------------------------

    # total expected activities per student
    expected_notes_per_student = activite_df["id_activité"].nunique()

    # number of valid notes for each student
    student_valid_counts = (
        valid_notes
        .groupby("id_etudiant")
        .size()
        .reset_index(name="valid_notes_count")
    )

    # coverage ratio
    student_valid_counts["coverage_ratio"] = (
        student_valid_counts["valid_notes_count"] /
        expected_notes_per_student
    )

    # average coverage
    avg_student_coverage_pct = round(
        student_valid_counts["coverage_ratio"].mean(),
        4
    )

    # students with >=80% coverage
    students_above_80_pct = round(
        (
            student_valid_counts[
                student_valid_counts["coverage_ratio"] >= 0.8
            ].shape[0]
            /
            total_students
        ),
        4
    )

    # students with <50% coverage
    students_below_50_pct = round(
        (
            student_valid_counts[
                student_valid_counts["coverage_ratio"] < 0.5
            ].shape[0]
            /
            total_students
        ),
        4
    )
    # -----------------------------------
    # 2. SUBJECT COVERAGE DENSITY
    # -----------------------------------

    # expected activities per subject
    expected_per_subject = (
        activite_df
        .groupby("id_matière")["id_activité"]
        .nunique()
        .to_dict()
    )

    # valid notes count per student + subject
    student_subject_counts = (
        merged
        .groupby(["id_etudiant", "id_matière"])
        .size()
        .reset_index(name="valid_notes_count")
    )

    # expected notes for that subject
    student_subject_counts["expected_notes"] = (
        student_subject_counts["id_matière"]
        .map(expected_per_subject)
    )

    # coverage ratio per subject
    student_subject_counts["subject_coverage_ratio"] = (
        student_subject_counts["valid_notes_count"] /
        student_subject_counts["expected_notes"]
    )

    # average coverage per student
    student_subject_coverage = (
        student_subject_counts
        .groupby("id_etudiant")["subject_coverage_ratio"]
        .mean()
    )

    # final global average
    avg_subject_coverage_pct = round(
        student_subject_coverage.mean(),
        4
    )

    # -----------------------------------
    # 3. TRIMESTER COVERAGE DENSITY
    # -----------------------------------

    # expected activities per trimester
    expected_per_trimester = (
        activite_df
        .groupby("id_trimestre")["id_activité"]
        .nunique()
        .to_dict()
    )

    # valid notes count per student + trimester
    student_trimester_counts = (
        merged
        .groupby(["id_etudiant", "id_trimestre"])
        .size()
        .reset_index(name="valid_notes_count")
    )

    # expected notes for that trimester
    student_trimester_counts["expected_notes"] = (
        student_trimester_counts["id_trimestre"]
        .map(expected_per_trimester)
    )

    # coverage ratio per trimester
    student_trimester_counts["trimester_coverage_ratio"] = (
        student_trimester_counts["valid_notes_count"] /
        student_trimester_counts["expected_notes"]
    )

    # average trimester coverage per student
    student_trimester_coverage = (
        student_trimester_counts
        .groupby("id_etudiant")["trimester_coverage_ratio"]
        .mean()
    )

    # final global average
    avg_trimester_coverage_pct = round(
        student_trimester_coverage.mean(),
        4
    )

    # -----------------------------------
    # 4. Global coverage (actual/expected)
    # -----------------------------------

    expected_notes = (
        total_students *
        activite_df["id_activité"].nunique()
    )

    actual_valid_notes = len(valid_notes)

    global_coverage_pct = round(
        actual_valid_notes / expected_notes,
        4
    )

    # -----------------------------------
    # 5. Coverage (student, subject)
    # -----------------------------------
    total_subjects = activite_df["id_matière"].nunique()
    expected_student_subject_pairs = (
        total_students *
        total_subjects
    )

    actual_student_subject_pairs = (
        merged[["id_etudiant", "id_matière"]]
        .drop_duplicates()
        .shape[0]
    )

    student_subject_coverage_pct = round(
        actual_student_subject_pairs /
        expected_student_subject_pairs,
        4
    )

    # -----------------------------------
    # 6. Coverage (student, trimester)
    # -----------------------------------
    total_trimesters = activite_df["id_trimestre"].nunique()
    expected_student_trimester_pairs = (
        total_students *
        total_trimesters
    )

    actual_student_trimester_pairs = (
        merged[["id_etudiant", "id_trimestre"]]
        .drop_duplicates()
        .shape[0]
    )

    student_trimester_coverage_pct = round(
        actual_student_trimester_pairs /
        expected_student_trimester_pairs,
        4
    )

    # -----------------------------------
    # FINAL RESULTS
    # -----------------------------------

    results = {
    "% moyen de couverture des étudiants":
        avg_student_coverage_pct,

    "% étudiants avec couverture ≥ 80%":
        students_above_80_pct,

    "% étudiants avec couverture < 50%":
        students_below_50_pct,

    "% moyen de densité de couverture par matière":
        avg_subject_coverage_pct,

    "% moyen de couverture des matières":
        avg_subject_coverage_pct,

    "% moyen de densité de couverture par trimestre":
        avg_trimester_coverage_pct,

    "% couverture globale":
        global_coverage_pct,

    "% couverture (étudiant, matière)":
        student_subject_coverage_pct,

    "% couverture (étudiant, trimestre)":
        student_trimester_coverage_pct
}

    return results