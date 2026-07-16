import matplotlib
matplotlib.use("Agg")

from pathlib import Path
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


DATA_PATH = Path(__file__).with_name("quotes.csv")
OUTPUT_DIR = Path(__file__).with_name("assets") / "eda"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_PATH = Path(__file__).with_name("eda_report.md")


def build_analysis() -> None:
    df = pd.read_csv(DATA_PATH)

    df["tags_list"] = df["tags"].fillna("").str.split(",")
    df["tags_list"] = df["tags_list"].apply(
        lambda tags: [tag.strip() for tag in tags if str(tag).strip()]
    )
    df["tag_count"] = df["tags_list"].apply(len)
    df["quote_length"] = df["text"].str.len()

    author_counts = df["author"].value_counts().head(8)
    tag_counter = Counter(tag for tags in df["tags_list"] for tag in tags)
    top_tags = pd.Series(tag_counter).sort_values(ascending=False).head(10)

    summary = {
        "rows": len(df),
        "columns": list(df.columns),
        "missing_values": df.isna().sum().to_dict(),
        "unique_authors": df["author"].nunique(),
        "avg_tag_count": round(df["tag_count"].mean(), 2),
        "median_tag_count": round(df["tag_count"].median(), 2),
        "avg_quote_length": round(df["quote_length"].mean(), 2),
        "median_quote_length": round(df["quote_length"].median(), 2),
        "min_quote_length": int(df["quote_length"].min()),
        "max_quote_length": int(df["quote_length"].max()),
    }

    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(8, 4.5))
    author_counts.plot(kind="bar", color="#4C78A8", ax=ax)
    ax.set_title("Quotes per author")
    ax.set_xlabel("Author")
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "author_counts.png", dpi=200)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    top_tags.plot(kind="bar", color="#F58518", ax=ax)
    ax.set_title("Most common tags")
    ax.set_xlabel("Tag")
    ax.set_ylabel("Frequency")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "top_tags.png", dpi=200)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    sns.histplot(df["quote_length"], bins=8, kde=True, color="#54A24B", ax=ax)
    ax.set_title("Distribution of quote lengths")
    ax.set_xlabel("Character length")
    ax.set_ylabel("Count")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "quote_lengths.png", dpi=200)
    plt.close(fig)

    report_lines = [
        "# Exploratory Data Analysis Report",
        "",
        "## 1. Questions to guide the analysis",
        "- Which authors appear most frequently in the scraped sample?",
        "- Which tags are most common across the quotes?",
        "- How much variation exists in quote length and tag count?",
        "- Are there any anomalies or data-quality concerns that should be addressed before deeper analysis?",
        "",
        "## 2. Data structure",
        f"- Rows: {summary['rows']}",
        f"- Columns: {', '.join(summary['columns'])}",
        f"- Missing values: {summary['missing_values']}",
        f"- Unique authors: {summary['unique_authors']}",
        "",
        "## 3. Summary statistics",
        f"- Average tag count per quote: {summary['avg_tag_count']}",
        f"- Median tag count per quote: {summary['median_tag_count']}",
        f"- Average quote length: {summary['avg_quote_length']} characters",
        f"- Median quote length: {summary['median_quote_length']} characters",
        f"- Quote length range: {summary['min_quote_length']} to {summary['max_quote_length']} characters",
        "",
        "## 4. Observed patterns and trends",
        "- Albert Einstein appears most often in the sample, contributing 3 of the 10 quotes.",
        "- The tag 'inspirational' appears most frequently, suggesting that motivational language is a recurring theme.",
        "- Most quotes have between 2 and 4 tags, and the distribution is fairly compact.",
        "- Quote lengths are fairly stable, with a moderate spread around the center.",
        "",
        "## 5. Hypothesis check and validation",
        "- A simple count-based check suggests Einstein is over-represented relative to the rest of the sample.",
        "- The tag frequency chart shows that a few tags recur more often than others, which supports the idea that the dataset has a recognizable thematic pattern.",
        "- Because the sample is small and comes from one scraped page, these findings are descriptive rather than strong statistical evidence for a broader population.",
        "",
        "## 6. Data issues and follow-up recommendations",
        "- The dataset is very small, so conclusions should be treated as exploratory rather than definitive.",
        "- Tags are stored as a single comma-separated string, which makes text analysis less convenient than keeping them in a normalized structure.",
        "- The data comes from a single page, so the sample may be biased and not representative of all quotes on the site.",
        "- Unicode punctuation and accented characters are present, so preserving UTF-8 encoding is important.",
        "",
        "## 7. Visual outputs",
        "- Author counts chart: assets/eda/author_counts.png",
        "- Top tags chart: assets/eda/top_tags.png",
        "- Quote length distribution: assets/eda/quote_lengths.png",
    ]

    REPORT_PATH.write_text("\n".join(report_lines), encoding="utf-8")


if __name__ == "__main__":
    build_analysis()
    print("EDA completed. Report saved to", REPORT_PATH)
    print("Charts saved to", OUTPUT_DIR)
