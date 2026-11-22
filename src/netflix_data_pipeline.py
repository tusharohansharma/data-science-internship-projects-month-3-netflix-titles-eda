"""
Netflix Data Pipeline

Orchestrates the complete Netflix Titles data preparation
and exploratory data analysis workflow.
"""

from data_understanding import inspect_dataset
from data_cleaning import load_dataset, clean_dataset, save_cleaned_dataset
from feature_engineering import create_features, save_dataset
from exploratory_data_analysis import perform_eda

# Pipeline Execution

def run_pipeline():
    # Execute the complete Netflix data analysis pipeline.

    print("=" * 70)
    print("Netflix Titles Data Analysis Pipeline")
    print("=" * 70)

    # Step 1: Load the raw dataset.
    print("\n[1/5] Loading raw dataset...")

    df = load_dataset()

    print(f"Raw dataset shape: {df.shape}")

    # Step 2: Understand the dataset.
    print("\n[2/5] Performing data understanding...")

    inspect_dataset(df)

    # Step 3: Clean the dataset.
    print("\n[3/5] Cleaning dataset...")

    cleaned_df = clean_dataset(df)

    print(f"Cleaned dataset shape: {cleaned_df.shape}")

    save_cleaned_dataset(cleaned_df)

    # Step 4: Feature engineering.
    print("\n[4/5] Performing feature engineering...")

    feature_engineered_df = create_features(cleaned_df)

    print(f"Feature-engineered dataset shape: {feature_engineered_df.shape}")

    save_dataset(feature_engineered_df)

    # Step 5: Exploratory data analysis.
    print("\n[5/5] Performing exploratory data analysis...")

    perform_eda(feature_engineered_df)

    print("\n" + "=" * 70)
    print("Netflix data pipeline completed successfully.")
    print("=" * 70)

# Main Execution

def main():
    # Run the Netflix data pipeline.

    run_pipeline()

if __name__ == "__main__":
    main()