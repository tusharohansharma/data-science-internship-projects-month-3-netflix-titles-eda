"""
Feature Engineering Module

Creates analytical features from the
cleaned Netflix Titles dataset.
"""

from pathlib import Path
import pandas as pd

# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_DATA_PATH = (PROJECT_ROOT / "data" / "processed" / "cleaned_netflix_titles.csv")
OUTPUT_DATA_PATH = (PROJECT_ROOT / "data" / "processed" / "feature_engineered_netflix_titles.csv")

# Data Loading

def load_dataset(file_path = INPUT_DATA_PATH):
    # Load the cleaned Netflix Titles dataset.

    if not file_path.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found at: {file_path}"
        )

    return pd.read_csv(file_path)

# Feature Creation

def create_features(df):
    # Create analytical features for Netflix content analysis.

    feature_df = df.copy()

    # Convert date_added to datetime if required.
    if "date_added" in feature_df.columns:
        feature_df["date_added"] = pd.to_datetime(feature_df["date_added"], errors="coerce")

    # Create the release decade feature.
    if "release_year" in feature_df.columns:
        feature_df["release_decade"] = ((feature_df["release_year"] // 10) * 10)

    # Create a binary indicator for movie content.
    if "type" in feature_df.columns:
        feature_df["is_movie"] = (feature_df["type"].str.lower().eq("movie").astype(int))

    # Create a standardized content type feature.
    if "type" in feature_df.columns:
        feature_df["content_type"] = (feature_df["type"].str.strip().str.title())

    # Extract the year in which content was added to Netflix.
    if "date_added" in feature_df.columns:
        feature_df["added_year"] = (feature_df["date_added"].dt.year)

        return feature_df

    # Save Feature-Engineered Dataset

def save_dataset(df, output_path=OUTPUT_DATA_PATH):
    # Save the feature-engineered dataset.

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"Feature-engineered dataset saved to: {output_path}")

# Main Execution

def main():
    # Execute the feature engineering workflow.

    df = load_dataset()

    print(f"Input dataset shape: {df.shape}")

    feature_engineered_df = create_features(df)

    print(f"Feature_engineered dataset shape: {feature_engineered_df.shape}")

    print("\nCreated Features:")

    new_features = [
        "release_decade",
        "is_movie",
        "content_type",
        "added_year"
    ]

    for feature in new_features:
        if feature in feature_engineered_df.columns:
            print(f"- {feature}")

    save_dataset(feature_engineered_df)

if __name__ == "__main__":
    main()