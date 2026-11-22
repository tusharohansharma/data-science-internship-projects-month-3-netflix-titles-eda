"""
Data Understanding Module

Loads the raw Netflix Titles dataset and performs initial inspection
to understand its structure, data types, and quality.
"""

from pathlib import Path
import pandas as pd

# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = (PROJECT_ROOT / "data" / "raw" / "netflix_titles.csv")

# Data Loading

def load_dataset(file_path=DATA_PATH):
    # Load the raw Netflix Titles dataset.

    return pd.read_csv(file_path)

# Dataset Inspection

def inspect_dataset(df):
    # Display essentail information about the dataset.

    print("\n===== Dataset Preview =====")
    print(df.head())

    print("\n===== Dataset Dimensions =====")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n===== Dataset Information =====")
    df.info()

    print("\n===== Statistical Summary =====")
    print(df.describe(include="all"))

    print("\n===== Missing Values =====")
    missing_values = df.isnull().sum()

    print(missing_values[missing_values.gt(0)])

    print("\n===== Duplicate Records =====")
    print(f"Duplicate rows: {df.duplicated().sum()}")

# Main Execution

def main():
    # Execute the data understanding workflow.

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Netflix dataset not found at: {DATA_PATH}")

    df = load_dataset()
    inspect_dataset(df)

if __name__ == "__main__":
    main()