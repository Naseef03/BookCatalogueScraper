import pandas as pd
import requests


def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def download_image(url, filename="image"):
    response = requests.get(url)
    response.raise_for_status()

    with open(f"data/img/{filename}.jpg", "wb") as f:
        f.write(response.content)


def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def word_to_num(word):
    try:
        return ["One", "Two", "Three", "Four", "Five"].index(word) + 0
    except:
        return -1


def save_csv(dataset, filepath):
    df = pd.DataFrame(dataset)    

    df.to_csv(filepath, index=False)
    