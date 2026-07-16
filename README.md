# Web Scraping Demo

This project demonstrates a simple Python web scraper and a GitHub Pages-friendly static website.

## Files
- scrape_example.py: Python scraper script
- quotes.csv: generated dataset
- index.html: landing page for the static website
- styles.css: styling for the website
- script.js: small JavaScript enhancement
- assets/data/sample-quotes.json: static example dataset used by the website
- eda_quotes.py: exploratory data analysis script
- eda_report.md: summary report from the EDA

## How to run locally
1. Install dependencies:
   pip install requests beautifulsoup4 pandas matplotlib seaborn
2. Run the scraper:
   python scrape_example.py
3. Run the EDA script:
   python eda_quotes.py
4. Open index.html in a browser to view the website.

## GitHub Pages
This site is compatible with GitHub Pages because it uses static HTML, CSS, and JavaScript only.

### Publish steps
1. Commit all changes to GitHub.
2. In GitHub, open the repository settings.
3. Under Pages, choose the main branch and the root folder.
4. Your site will be available at:
   https://psharmaner-cell.github.io/web-scraping-demo/
