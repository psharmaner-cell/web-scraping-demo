import requests
from bs4 import BeautifulSoup
import csv
from pathlib import Path

URL = "https://quotes.toscrape.com/"


def fetch_page(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def parse_quotes(html: str):
    soup = BeautifulSoup(html, "html.parser")
    quotes = []
    for item in soup.select('.quote'):
        text = item.select_one('.text').get_text(strip=True)
        author = item.select_one('.author').get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in item.select('.tag')]
        quotes.append({"text": text, "author": author, "tags": ", ".join(tags)})
    return quotes


def save_csv(data, path: str):
    fieldnames = ["text", "author", "tags"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    html = fetch_page(URL)
    quotes = parse_quotes(html)
    output_path = Path(__file__).with_name("quotes.csv")
    save_csv(quotes, str(output_path))
    print(f"Saved {len(quotes)} quotes to {output_path}")
