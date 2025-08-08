from bs4 import BeautifulSoup
import pandas as pd
import argparse

from utils.fetch import get_html

BASE_URL = "http://books.toscrape.com"


# Argument Config
parser = argparse.ArgumentParser(description=f"Scrapes book catalogue data from {BASE_URL}")
parser.add_argument("--rating-filter", "-rf", 
                    type=str, 
                    default="1 2 3 4 5", 
                    help="Specify the ratings (1-5) that needs to be scraped. It should be like \"1 3 5\"")
parser.add_argument("--output-file", "-o",
                    type=str,
                    default="catalogue",
                    help="Specify the output file name")
parser.add_argument("--max-pages", "-mp",
                    type=int,
                    default=50,
                    help="Specify the number of pages to be scraped on the website")


def word_to_num(word):
    try:
        return ["One", "Two", "Three", "Four", "Five"].index(word) + 1
    except:
        return 0


def extract_catalog(book):
    title = book.select_one("h3>a")["title"]
    link = f"{BASE_URL}/{book.select_one("h3>a")["href"]}"
    price = book.select_one(".product_price>p").text.strip("Â£")
    avialability = book.select_one(".availability").text.strip()
    rating = word_to_num(book.select_one(".star-rating")["class"][1])

    catalog = {
        "Title": title,
        "Price": price,
        "Availability": avialability,
        "Rating": rating,
        "Product Link": link
    }

    return catalog
    

def extract_catalogs(html, rating_filter):
    soup = BeautifulSoup(html, "html.parser")

    catalogs = []
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        catalog = extract_catalog(book)
        if catalog["Rating"] in rating_filter:
            catalogs.append(catalog)
    
    return catalogs
    

def extract_all_catalogs(rating_filter, max_pages):
    catalogs = []

    page_url = "page-1.html"

    page_no = 1
    while page_url and page_no <= max_pages:
        html = get_html(f"{BASE_URL}/catalogue/{page_url}")
        catalogs.extend(extract_catalogs(html, rating_filter=rating_filter))

        print(f"Scraped {BASE_URL}/catalogue/{page_url}")
        
        next_page = BeautifulSoup(html, "html.parser").select_one(".next>a")
        page_url = next_page["href"] if next_page else None
        page_no += 1

    return catalogs


def save(dataset, filepath):
    df = pd.DataFrame(dataset)    

    df.to_csv(filepath, index=False)
 

if __name__ == "__main__":
    # Get Arguments
    args = parser.parse_args()

    rating_filter = list(map(int, args.rating_filter.split()))
    output_filename = args.output_file
    max_pages = args.max_pages

    catalogs = extract_all_catalogs(max_pages=max_pages, rating_filter=rating_filter)
    save(catalogs, f"data/{output_filename}.csv")

