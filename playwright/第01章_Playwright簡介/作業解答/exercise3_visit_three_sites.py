"""
第 01 章 練習題 3：修改程式，讓瀏覽器訪問 3 個不同的網站

重點：開一次瀏覽器，用迴圈依序訪問多個網站，
分別讀出每個網站的標題。

執行：
    uv run python exercise3_visit_three_sites.py
"""

from playwright.sync_api import sync_playwright

SITES = [
    "https://example.com",
    "https://playwright.dev",
    "https://www.wikipedia.org",
]


def visit_three_sites():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for index, url in enumerate(SITES, start=1):
            page.goto(url)
            print(f"{index}. {url} -> {page.title()}")

        browser.close()


if __name__ == "__main__":
    visit_three_sites()
