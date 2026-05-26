import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def parse_job_page(url: str):

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    text = soup.get_text(separator=" ")

    return text