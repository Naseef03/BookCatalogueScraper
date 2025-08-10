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

## Usage 
```bash
pip install -r requirements.txt
python scraper.py [OPTIONS]
```

#### Options:
| Argument | Description | Example |
|---|---|---|
| `-o` `--output-file` | Output CSV filename (default: `catalogue`) | `-o books` |
| `-mp` `--max-pages` | Max number of pages to scrape | `-mp 10` |
| `-rf` `--rating-filter` | Ratings that should be included | `-rf "1 4 5"` |
| `-i` `--image` | Download images of book | `-i` | 