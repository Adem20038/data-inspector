from src.utils.loader import load_all

from src.metrics.coverage import calculate_coverage_metrics
from src.metrics.noise import calculate_noise_metrics
from src.metrics.integrity import calculate_integrity_metrics
from src.metrics.duplicates import calculate_duplicate_metrics


def load_metrics():

    print("Loading data...")

    data = load_all()

    print("Computing metrics...")

    metrics = {

        "coverage":
            calculate_coverage_metrics(data),

        "noise":
            calculate_noise_metrics(data),

        "integrity":
            calculate_integrity_metrics(data),

        "duplicates":
            calculate_duplicate_metrics(data)
    }

    return data, metrics