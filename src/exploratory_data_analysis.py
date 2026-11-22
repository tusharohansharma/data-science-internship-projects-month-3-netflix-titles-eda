"""
Exploratory Data Analysis Module

Performs exploratory analysis on the feature-engineered Netflix Titles
dataset and generates visualizations for content distribution, yearly
trends, genres, countries and trend prediction.
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_DATA_PATH = (PROJECT_ROOT / "data" / "processed" / "feature_engineered_netflix_titles.csv")
OUTPUT_DIRECTORY = (PROJECT_ROOT / "outputs")

# Data Loading

def load_dataset(file_path=INPUT_DATA_PATH):
    # Load the feature-engineered Netflix Titles dataset.

    if not file_path.exists():
        raise FileNotFoundError(f"Feature-engineered dataset not found at: {file_path}")

    return pd.read_csv(file_path)

# Output Directory

def create_output_directory(output_directory=OUTPUT_DIRECTORY):
    # Create the output directory if it does not exist.

    output_directory.mkdir(parents=True, exist_ok=True)

# Movie vs TV Show Analysis

def plot_content_type_distribution(df, output_directory=OUTPUT_DIRECTORY):
    # Create a pie chart showing the distribution of content types.

    content_counts = df["content_type"].value_counts()

    plt.figure(figsize=(8, 8))

    plt.pie(
        content_counts.values,
        labels=content_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Movie vs TV Show Distribution")
    plt.tight_layout()

    output_path = (output_directory / "movie_vs_tvshow_pie_chart.png")

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

# Content Per Year Analysis

def plot_content_per_year(df, output_directory=OUTPUT_DIRECTORY):
    # Create a line plot showing content released per year.

    yearly_content = (
        df.groupby("release_year")
        .size()
        .reset_index(name="content_count")
    )

    yearly_content = yearly_content.sort_values("release_year")

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=yearly_content,
        x="release_year",
        y="content_count",
        marker="o"
    )

    plt.title("Netflix Content Released Per Year")
    plt.xlabel("Released Year")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=45)

    plt.tight_layout()

    output_path = (output_directory / "content_per_year_lineplot.png")

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

# Top Genres Analysis

def plot_top_genres(df, output_directory=OUTPUT_DIRECTORY):
    # Create a bar plot showing the top 10 genres.

    genre_data = (
        df["listed_in"]
        .dropna()
        .str.split(", ")
        .explode()
    )

    top_genres = (
        genre_data
        .value_counts()
        .head(10)
        .sort_values()
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=top_genres.values,
        y=top_genres.index
    )

    plt.title("Top 10 Netflix Genres")
    plt.xlabel("Number of Titles")
    plt.ylabel("Genre")

    plt.tight_layout()

    output_path = (output_directory / "top_10_genres_barplot.png")

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

# Country Content Analysis

def plot_country_content_heatmap(df, output_directory=OUTPUT_DIRECTORY):
    # Create a heatmap showing content volume across leading countries.

    country_data = df["country"].dropna().str.split(", ").explode()

    top_countries = country_data.value_counts().head(10).index

    country_content = (country_data[country_data.isin(top_countries)]
        .value_counts()
        .reindex(top_countries)
        .fillna(0)
    )

    heatmap_data = country_content.to_frame(name="content_count")
    
    heatmap_data = heatmap_data.sort_values(
        "content_count",
        ascending=False
    )

    plt.figure(figsize=(10, 6))

    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".0f",
        cmap="Blues",
        cbar_kws={"label": "Number of Titles"}
    )

    plt.title("Netflix Content Distribution by Country")
    plt.xlabel("Metric")
    plt.ylabel("Country")

    plt.tight_layout()

    output_path = (output_directory / "country_content_heatmap.png")

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

# Trend Prediction Analysis

def plot_trend_prediction(df, output_directory=OUTPUT_DIRECTORY):
    """
    Generate a simple two-year content trend projection
    based on historical yearly release counts.
    """

    yearly_content = (
        df.groupby("release_year")
        .size()
        .reset_index(name="content_count")
    )

    yearly_content = yearly_content.sort_values("release_year")

    if len(yearly_content) < 2:
        print("Insufficient yearly data for trend prediction")
        return

    x = yearly_content["release_year"]
    y = yearly_content["content_count"]

    trend_coefficients = pd.Series(np.polyfit(x, y, 1))

    trend_function = np.poly1d(trend_coefficients)

    last_year = int(x.max())

    future_years = pd.Series(range(last_year + 1, last_year + 2))

    predicted_counts = trend_function(future_years)

    predicted_counts = pd.Series(predicted_counts).clip(lower=0)

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        x=x,
        y=y,
        marker="o",
        label="Historical Content"
    )

    sns.lineplot(
        x=future_years,
        y=predicted_counts,
        marker="o",
        linestyle="--",
        label="Trend Projection"
    )

    plt.title("Netflix Content Trend Projection")
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")
    plt.legend()

    plt.tight_layout()

    output_path = (output_directory / "trend_prediction_chart.png")

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

# Main EDA Workflow

def perform_eda(df, output_directory=OUTPUT_DIRECTORY):
    # Generate all required exploratory visualizations.

    create_output_directory(output_directory)

    plot_content_type_distribution(df, output_directory)

    plot_content_per_year(df, output_directory)

    plot_top_genres(df, output_directory)

    plot_country_content_heatmap(df, output_directory)

    plot_trend_prediction(df, output_directory)

    print(f"EDA visualizations saved to: {output_directory}")

# Main Execution

def main():
    # Execute the exploratory data analysis workflow.

    df = load_dataset()

    print(f"Dataset shape: {df.shape}")

    perform_eda(df)

if __name__ == "__main__":
    main()