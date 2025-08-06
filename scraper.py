from random import betavariate
from bs4 import BeautifulSoup
import pandas as pd

from utils.fetch import get_html

BASE_URL = "http://books.toscrape.com"
NUM_PAGES = 10


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
    

def extract_catalogs(html):
    soup = BeautifulSoup(html, "html.parser")

    catalogs = []
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        catalog = extract_catalog(book)
        catalogs.append(catalog)
    
    return catalogs
    

def extract_all_catalogs(max_pages=500):
    catalogs = []

    page_url = "page-1.html"

    page_no = 1
    while page_url and page_no <= max_pages:
        html = get_html(f"{BASE_URL}/catalogue/{page_url}")
        catalogs.extend(extract_catalogs(html))

        print(f"Scraped {BASE_URL}/catalogue/{page_url}")
        
        next_page = BeautifulSoup(html, "html.parser").select_one(".next>a")
        page_url = next_page["href"] if next_page else None
        page_no += 1

    return catalogs


def save(dataset, filepath):
    df = pd.DataFrame(dataset)    

    df.to_csv(filepath, index=False)
 

if __name__ == "__main__":
    catalogs = extract_all_catalogs(NUM_PAGES)
    save(catalogs, "data/catalogs.csv")

