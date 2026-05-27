from playwright.sync_api import sync_playwright

from bs4 import BeautifulSoup

from readability import Document

import re


def clean_text(text: str):

    text = re.sub(r"\\s+", " ", text)

    return text.strip()


def parse_job_page(url: str):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.goto(
            url,
            wait_until="networkidle",
            timeout=60000
        )

        html = page.content()

        browser.close()

    readable_html = Document(html).summary()

    soup = BeautifulSoup(
        readable_html,
        "lxml"
    )

    raw_text = clean_text(
        soup.get_text(separator=" ")
    )

    return raw_text