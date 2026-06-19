"""
第 01 章 練習題 4：嘗試使用不同的瀏覽器（Chromium、Firefox、WebKit）

重點：同一套 API，只要換 p.chromium / p.firefox / p.webkit 就能
切換瀏覽器引擎。先用 `uv run playwright install` 下載三種瀏覽器驅動。

執行：
    uv run python exercise4_three_browsers.py
"""

from playwright.sync_api import sync_playwright


def try_all_browsers():
    with sync_playwright() as p:
        # 三種瀏覽器引擎共用同一套 API
        for name, browser_type in [
            ("Chromium", p.chromium),
            ("Firefox", p.firefox),
            ("WebKit", p.webkit),
        ]:
            browser = browser_type.launch(headless=True)
            page = browser.new_page()
            page.goto("https://example.com")
            print(f"{name:8s} -> 標題：{page.title()}")
            browser.close()


if __name__ == "__main__":
    try_all_browsers()
