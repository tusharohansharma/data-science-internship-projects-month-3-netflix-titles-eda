"""
Data Cleaning Module

Cleans the Netflix Titles dataset by handling missing values,
removing duplicate records, and standardizing data-related data.
"""

from pathlib import Path
import pandas as pd

# Projects Paths

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = (PROJECT_ROOT / "data" / "raw" / "netflix_titles.csv")
PROCESSED_DATA_PATH = (PROJECT_ROOT / "data" / "processed" / "cleaned_netflix_titles.csv")

# Data Loading

def load_dataset(file_path=RAW_DATA_PATH):
    # Load the raw Netflix Titles dataset.

    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at: {file_path}")

    return pd.read_csv(file_path)

# Data Cleaning

def clean_dataset(df):
    # Clean the dataset and return the cleaned DataFrame.

    cleaned_df = df.copy()

    # Remove duplicate records.
    cleaned_df = cleaned_df.drop_duplicates()

    # Standardize text fields and handle missing values.
    text_columns = ["director", "cast", "country", "rating", "duration"]

    for column in text_columns:
        if column in cleaned_df.columns:
            cleaned_df[column] = cleaned_df[column].fillna("Unknown")

    # Convert date_added to datetime.
    if "date_added" in cleaned_df.columns:
        cleaned_df["date_added"] = pd.to_datetime(cleaned_df["date_added"], errors="coerce")

    # Remove leading and trailing whitespace from text columns.
    for column in cleaned_df.select_dtypes(include="object").columns:
        cleaned_df[column] = cleaned_df[column].str.strip()

    return cleaned_df

# Saved Cleaned Dataset

def save_cleaned_dataset(df, output_path=PROCESSED_DATA_PATH):
    # Save the cleaned dataset to the processed data directory.

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved to: {output_path}")

# Main Execution

def main():
    # Execute the data cleaning workflow.

    df = load_dataset()

    print(f"Original dataset shape: {df.shape}")

    cleaned_df = clean_dataset(df)

    print(f"Cleaned dataset shape: {cleaned_df.shape}")
    print("Remaining missing values:", cleaned_df.isnull().sum())
    print("Remaining duplicate rows:", cleaned_df.duplicated().sum())

    save_cleaned_dataset(cleaned_df)

if __name__ == "__main__":
    main()