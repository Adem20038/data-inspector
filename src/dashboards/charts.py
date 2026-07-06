import matplotlib.pyplot as plt
import matplotlib as mpl

# ── Dark theme defaults ───────────────────────────────────────
mpl.rcParams.update({
    "figure.facecolor":  "#1a1a24",
    "axes.facecolor":    "#13131a",
    "axes.edgecolor":    "#2a2a38",
    "axes.labelcolor":   "#888899",
    "axes.titlecolor":   "#ffffff",
    "xtick.color":       "#555566",
    "ytick.color":       "#555566",
    "text.color":        "#ffffff",
    "grid.color":        "#2a2a38",
    "grid.linestyle":    "--",
    "grid.linewidth":    0.5,
    "font.family":       "sans-serif",
    "font.size":         11,
    "axes.titlesize":    12,
    "axes.titleweight":  "normal",
    "axes.titlepad":     12,
    "axes.labelsize":    10,
})

# ── Per-metric chart configuration ───────────────────────────
#
# Keys must match exactly the keys returned by your calculate_*
# functions. Each entry controls:
#   title     – human-readable chart title
#   xlabel    – x-axis label (what the value represents)
#   color     – bar color
#   max_value – x-axis upper bound (100 for %, or a raw number)
#   suffix    – label suffix appended to the value annotation
#
METRIC_CONFIG = {

    # ── Duplicates ────────────────────────────────────────────
    "% duplication PK étudiants": {
        "title":     "Doublons sur la clé primaire — Étudiants",
        "xlabel":    "Part des lignes dupliquées (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% duplication PK enseignement": {
        "title":     "Doublons sur la clé primaire — Enseignement",
        "xlabel":    "Part des lignes dupliquées (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% duplication PK évaluations": {
        "title":     "Doublons sur la clé primaire — Évaluations",
        "xlabel":    "Part des lignes dupliquées (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% duplication métier enseignement": {
        "title":     "Doublons métier — Enseignement (enseignant × matière × classe × année)",
        "xlabel":    "Part des combinaisons dupliquées (%)",
        "color":     "#e08c3c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% duplication métier évaluations": {
        "title":     "Doublons métier — Évaluations (étudiant × matière × trimestre)",
        "xlabel":    "Part des combinaisons dupliquées (%)",
        "color":     "#e08c3c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% duplication étudiant (nom + user)": {
        "title":     "Doublons étudiants — Nom + identifiant utilisateur",
        "xlabel":    "Part des paires dupliquées (%)",
        "color":     "#c05ce0",
        "max_value": 100,
        "suffix":    "%",
    },
    "% duplication user étudiant": {
        "title":     "Doublons — Identifiant utilisateur étudiant",
        "xlabel":    "Part des identifiants dupliqués (%)",
        "color":     "#c05ce0",
        "max_value": 100,
        "suffix":    "%",
    },

    # ── Coverage ──────────────────────────────────────────────
    "% moyen de couverture des étudiants": {
        "title":     "Couverture moyenne des étudiants",
        "xlabel":    "Taux de couverture moyen (% des activités renseignées)",
        "color":     "#3ca8e0",
        "max_value": 100,
        "suffix":    "%",
    },
    "% étudiants avec couverture ≥ 80%": {
        "title":     "Étudiants avec couverture ≥ 80 %",
        "xlabel":    "Part des étudiants (%)",
        "color":     "#4cca6e",
        "max_value": 100,
        "suffix":    "%",
    },
    "% étudiants avec couverture < 50%": {
        "title":     "Étudiants avec couverture < 50 %",
        "xlabel":    "Part des étudiants (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% moyen de densité de couverture par matière": {
        "title":     "Densité de couverture moyenne par matière",
        "xlabel":    "Taux de couverture moyen par matière (%)",
        "color":     "#3ca8e0",
        "max_value": 100,
        "suffix":    "%",
    },
    "% moyen de couverture des matières": {
        "title":     "Couverture moyenne des matières",
        "xlabel":    "Taux de couverture moyen (%)",
        "color":     "#3ca8e0",
        "max_value": 100,
        "suffix":    "%",
    },
    "% moyen de densité de couverture par trimestre": {
        "title":     "Densité de couverture moyenne par trimestre",
        "xlabel":    "Taux de couverture moyen par trimestre (%)",
        "color":     "#3ca8e0",
        "max_value": 100,
        "suffix":    "%",
    },
    "% couverture globale": {
        "title":     "Couverture globale (notes valides / notes attendues)",
        "xlabel":    "Taux de couverture (%)",
        "color":     "#4cca6e",
        "max_value": 100,
        "suffix":    "%",
    },
    "% couverture (étudiant, matière)": {
        "title":     "Couverture des paires (étudiant, matière)",
        "xlabel":    "Part des paires renseignées (%)",
        "color":     "#3ca8e0",
        "max_value": 100,
        "suffix":    "%",
    },
    "% couverture (étudiant, trimestre)": {
        "title":     "Couverture des paires (étudiant, trimestre)",
        "xlabel":    "Part des paires renseignées (%)",
        "color":     "#3ca8e0",
        "max_value": 100,
        "suffix":    "%",
    },

    # ── Noise ────────────────────────────────────────────────
    "% notes NULL": {
        "title":     "Notes manquantes (NULL)",
        "xlabel":    "Part des notes (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% notes invalides": {
        "title":     "Notes invalides (hors plage 0–20)",
        "xlabel":    "Part des notes (%)",
        "color":     "#e08c3c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% note_comportement NULL": {
        "title":     "Notes de comportement manquantes",
        "xlabel":    "Part des évaluations (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% lignes inutilisables": {
        "title":     "Lignes inutilisables (note NULL + activité absente)",
        "xlabel":    "Part des lignes (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% notes égales à 0": {
        "title":     "Notes égales à 0",
        "xlabel":    "Part des notes (%)",
        "color":     "#e08c3c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% notes égales à 20": {
        "title":     "Notes égales à 20 (parfaites)",
        "xlabel":    "Part des notes (%)",
        "color":     "#4cca6e",
        "max_value": 100,
        "suffix":    "%",
    },
    "% notes réalistes (8-16)": {
        "title":     "Notes dans la plage réaliste (8–16)",
        "xlabel":    "Part des notes valides (%)",
        "color":     "#4cca6e",
        "max_value": 100,
        "suffix":    "%",
    },
    "moyenne générale": {
        "title":     "Moyenne générale des notes valides",
        "xlabel":    "Note moyenne (sur 20)",
        "color":     "#3ca8e0",
        "max_value": 20,
        "suffix":    "/20",
    },
    "médiane": {
        "title":     "Médiane des notes valides",
        "xlabel":    "Note médiane (sur 20)",
        "color":     "#3ca8e0",
        "max_value": 20,
        "suffix":    "/20",
    },
    "écart-type": {
        "title":     "Écart-type des notes valides",
        "xlabel":    "Dispersion (points)",
        "color":     "#c05ce0",
        "max_value": 20,
        "suffix":    " pts",
    },
    "% valeurs aberrantes": {
        "title":     "Valeurs aberrantes (méthode IQR)",
        "xlabel":    "Part des notes valides (%)",
        "color":     "#e08c3c",
        "max_value": 100,
        "suffix":    "%",
    },

    # ── Integrity ────────────────────────────────────────────
    "% notes avec activité inexistante": {
        "title":     "Notes référençant une activité inexistante",
        "xlabel":    "Part des notes (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% activités avec enseignant inexistant": {
        "title":     "Activités avec enseignant introuvable",
        "xlabel":    "Part des activités (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% évaluations avec étudiant inexistant": {
        "title":     "Évaluations référençant un étudiant introuvable",
        "xlabel":    "Part des évaluations (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% évaluations avec matière inexistante": {
        "title":     "Évaluations référençant une matière introuvable",
        "xlabel":    "Part des évaluations (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% enseignements avec enseignant inexistant": {
        "title":     "Enseignements avec enseignant introuvable",
        "xlabel":    "Part des enseignements (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% enseignements avec matière inexistante": {
        "title":     "Enseignements avec matière introuvable",
        "xlabel":    "Part des enseignements (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% incohérence activité ↔ enseignant/matière": {
        "title":     "Incohérence activité ↔ enseignant / matière",
        "xlabel":    "Part des activités incohérentes (%)",
        "color":     "#e08c3c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% incohérence classe ↔ niveau": {
        "title":     "Incohérence classe ↔ niveau",
        "xlabel":    "Part des enseignements sans niveau (%)",
        "color":     "#e08c3c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% incohérence trimestre ↔ année": {
        "title":     "Incohérence trimestre ↔ année scolaire",
        "xlabel":    "Part des trimestres incohérents (%)",
        "color":     "#e08c3c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% étudiants sans inscription": {
        "title":     "Étudiants sans inscription",
        "xlabel":    "Part des étudiants (%)",
        "color":     "#e05c5c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% enseignants sans activité": {
        "title":     "Enseignants sans aucune activité enregistrée",
        "xlabel":    "Part des enseignants (%)",
        "color":     "#e08c3c",
        "max_value": 100,
        "suffix":    "%",
    },
    "% matières sans activité": {
        "title":     "Matières sans aucune activité enregistrée",
        "xlabel":    "Part des matières (%)",
        "color":     "#e08c3c",
        "max_value": 100,
        "suffix":    "%",
    },
}


# ── Fallback defaults ─────────────────────────────────────────
_DEFAULT_CONFIG = {
    "title":     None,       # falls back to the metric key itself
    "xlabel":    "Valeur",
    "color":     "royalblue",
    "max_value": 100,
    "suffix":    "",
}


def get_metric_config(metric_key: str) -> dict:
    """Return the chart config for a metric key, with safe defaults."""
    cfg = _DEFAULT_CONFIG.copy()
    cfg.update(METRIC_CONFIG.get(metric_key, {}))
    if cfg["title"] is None:
        cfg["title"] = metric_key
    return cfg


# ── Chart renderer ────────────────────────────────────────────
def create_kpi_chart(metric_key: str, value: float) -> plt.Figure:
    """
    Build a horizontal KPI bar chart for *metric_key*.
    All display properties are looked up from METRIC_CONFIG automatically.
    """
    cfg = get_metric_config(metric_key)

    title     = cfg["title"]
    xlabel    = cfg["xlabel"]
    color     = cfg["color"]
    max_value = cfg["max_value"]
    suffix    = cfg["suffix"]

    # Convert ratio (0–1) to percentage when max_value is 100
    display_value = value * 100 if max_value == 100 else value

    fig, ax = plt.subplots(figsize=(8, 1.6))

    # Background track
    ax.barh([title], [max_value], color="#2a2a38", height=0.45, zorder=0)

    # Value bar
    ax.barh([title], [display_value], color=color, alpha=0.85, height=0.45)

    ax.set_xlim(0, max_value)
    ax.set_xlabel(xlabel, labelpad=8)
    ax.set_title(title)

    # Annotation label
    label_x = display_value + max_value * 0.015
    ax.text(
        label_x, 0,
        f"{display_value:.2f}{suffix}",
        va="center", ha="left",
        fontsize=10, color="#ccccdd",
    )

    ax.set_yticklabels([])
    ax.tick_params(left=False)
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#2a2a38")

    fig.patch.set_facecolor("#1a1a24")
    plt.tight_layout(pad=0.8)

    return fig