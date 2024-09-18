import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Remote, EdgeOptions
from selenium.webdriver.edge.remote_connection import EdgeRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


AUTH = 'brd-customer-hl_c34d5e71-zone-ai_scrapper:9wmt667skplv'
SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'

def scrape_website(website):
    print("Launching Edge browser")
    sbr_connection = EdgeRemoteConnection(SBR_WEBDRIVER, 'msedge', 'edge')
    options = EdgeOptions()
    with Remote(sbr_connection, options=options) as driver:
        driver.get(website)
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html



def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]






