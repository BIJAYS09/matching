import re

import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from readability import Document


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
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

    # -----------------------------
    # Extract clean readable content
    # -----------------------------

    readable_html = Document(html).summary()

    soup = BeautifulSoup(
        readable_html,
        "lxml"
    )

    # -----------------------------
    # Extract title
    # -----------------------------

    title = None

    h1 = soup.find("h1")

    if h1:
        title = clean_text(h1.get_text())

    # -----------------------------
    # Extract company
    # -----------------------------

    company = None

    page_text = soup.get_text(" ")

    company_match = re.search(
        r"Company:\s*(.+?)\s",
        page_text
    )

    if company_match:
        company = clean_text(
            company_match.group(1)
        )

    # -----------------------------
    # Extract location
    # -----------------------------

    location = None

    location_match = re.search(
        r"Location:\s*(.+?)\s",
        page_text
    )

    if location_match:
        location = clean_text(
            location_match.group(1)
        )

    # -----------------------------
    # Extract full raw text
    # -----------------------------

    raw_text = clean_text(
        soup.get_text(separator=" ")
    )

    # -----------------------------
    # Fallbacks
    # -----------------------------

    if not company:
        company = "Unknown"

    if not location:
        location = "Unknown"

    return {
        "title": title,
        "company": company,
        "location": location,
        "url": url,
        "raw_text": raw_text
    }