"""
第 01 章 練習題 2：執行第一個程式，訪問你喜歡的網站

這裡用 Playwright 官網當作「喜歡的網站」。
想看瀏覽器實際跑，把 headless 改成 False 即可。

執行：
    uv run python exercise2_visit_site.py
"""

from playwright.sync_api import sync_playwright

# 想訪問的網站，換成你喜歡的就好
MY_FAVORITE_SITE = "https://playwright.dev"


def visit_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(MY_FAVORITE_SITE)
        print(f"網址：{page.url}")
        print(f"標題：{page.title()}")

        browser.close()


if __name__ == "__main__":
    visit_site()
