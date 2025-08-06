# Book Catalogue Scraper

This project scrape book catalogue from https://books.toscrape.com and store them in a CSV file. Each book includes `Title`, `Price`, `Availability`, `Rating`, and `Link to the Catalogue` of the Book.

## Technologies used
- Python
- BeautifulSoup
- Pandas
- Requests

## Ouput
Data is saved in `data/catalog.csv` with the following columns
- Title
- Price
- Availability
- Rating
- Link

## How to Run
```bash
pip install -r requirements.txt
python scraper.py
```