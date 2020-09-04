import os
import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


DRIVER_PATH = os.environ["CHROMEDRIVER_LOCATION"]


def access_site(symbol):
    """Return the Chrome driver open to the TMX quote for the given symbol."""
    chrome_options = Options()  
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(DRIVER_PATH, chrome_options=chrome_options)
    url = "https://money.tmx.com/en/quote/{symbol}".format(symbol=symbol)
    driver.get(url)
    return driver

def refresh_site(driver):
    """Return the Chrome driver after refreshing the page with the TMX quote for the given symbol."""
    driver.refresh()
    return driver

def parse_data(driver):
    """Return a float of the current price given the driver open to the TMX page of the specific symbol."""
    # The driver needs time to load the page before it can be parsed.
    time.sleep(5)
    content_obj = driver.find_element(by="id", value="root")
    content_text = content_obj.text
    price_string = content_text.split("PRICE")[1].split("CHANGE")[0].strip()
    try:
        price_float = float(price_string.replace("$", "").replace(",", ""))
        return price_float
    except ValueError as e:
        raise e
