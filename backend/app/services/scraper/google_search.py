import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def search_jobs(query: str):

    url = f"https://www.google.com/search?q={query}"

    response = requests.get(
        url,
        headers=HEADERS
    )

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for g in soup.select("div.yuRUbf"):
        link = g.find("a")

        if link:
            results.append(link["href"])

    return results[:20]