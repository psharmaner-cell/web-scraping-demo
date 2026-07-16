# Exploratory Data Analysis Report

## 1. Questions to guide the analysis
- Which authors appear most frequently in the scraped sample?
- Which tags are most common across the quotes?
- How much variation exists in quote length and tag count?
- Are there any anomalies or data-quality concerns that should be addressed before deeper analysis?

## 2. Data structure
- Rows: 10
- Columns: text, author, tags, tags_list, tag_count, quote_length
- Missing values: {'text': 0, 'author': 0, 'tags': 0, 'tags_list': 0, 'tag_count': 0, 'quote_length': 0}
- Unique authors: 8

## 3. Summary statistics
- Average tag count per quote: 3.0
- Median tag count per quote: 3.0
- Average quote length: 89.5 characters
- Median quote length: 85.0 characters
- Quote length range: 50 to 131 characters

## 4. Observed patterns and trends
- Albert Einstein appears most often in the sample, contributing 3 of the 10 quotes.
- The tag 'inspirational' appears most frequently, suggesting that motivational language is a recurring theme.
- Most quotes have between 2 and 4 tags, and the distribution is fairly compact.
- Quote lengths are fairly stable, with a moderate spread around the center.

## 5. Hypothesis check and validation
- A simple count-based check suggests Einstein is over-represented relative to the rest of the sample.
- The tag frequency chart shows that a few tags recur more often than others, which supports the idea that the dataset has a recognizable thematic pattern.
- Because the sample is small and comes from one scraped page, these findings are descriptive rather than strong statistical evidence for a broader population.

## 6. Data issues and follow-up recommendations
- The dataset is very small, so conclusions should be treated as exploratory rather than definitive.
- Tags are stored as a single comma-separated string, which makes text analysis less convenient than keeping them in a normalized structure.
- The data comes from a single page, so the sample may be biased and not representative of all quotes on the site.
- Unicode punctuation and accented characters are present, so preserving UTF-8 encoding is important.

## 7. Visual outputs
- Author counts chart: assets/eda/author_counts.png
- Top tags chart: assets/eda/top_tags.png
- Quote length distribution: assets/eda/quote_lengths.png