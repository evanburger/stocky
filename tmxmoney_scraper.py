import csv
import io

import requests
from bs4 import BeautifulSoup


def scrape_tmxmoney(symbol):
    url = "https://web.tmxmoney.com/quote.php?qm_symbol={symbol}".format(symbol=symbol)
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    outer_span_tag = soup.find("span", class_="price")
    span_tag_text = outer_span_tag.find("span").text
    
    try:
        data_float = float(span_tag_text.replace(",", "_"))
        return data_float
    except ValueError as e:
        raise e
