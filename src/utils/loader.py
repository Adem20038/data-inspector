import pandas as pd
import os

RAW_PATH = "data/raw/"


def load_csv(filename):
    """
    Load a single CSV file from raw data folder
    """
    path = os.path.join(RAW_PATH, filename)
    return pd.read_csv(path)


def load_all():
    """
    Load all datasets (V1 simple version)
    """
    data = {}

    for file in os.listdir(RAW_PATH):
        if file.endswith(".csv"):
            name = file.replace(".csv", "")
            data[name] = load_csv(file)

    return data
