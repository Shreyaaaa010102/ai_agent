from selenium import webdriver
from selenium_stealth import stealth
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
import json


def search_google_web_automation(query):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=chrome_options)

    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    n_pages = 2
    results = []
    counter = 0
    for page in range(1, n_pages):
        url = (
            "http://www.google.com/search?q="
            + str(query)
            + "&start="
            + str((page - 1) * 10)
        )

        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        search = soup.find_all("div", class_="yuRUbf")
        for h in search:
            counter = counter + 1
            title = h.a.h3.text
            link = h.a.get("href")
            rank = counter
            results.append(
                {
                    "title": h.a.h3.text,
                    "url": link,
                    "domain": urlparse(link).netloc,
                    "rank": rank,
                }
            )
    return results[:3]


