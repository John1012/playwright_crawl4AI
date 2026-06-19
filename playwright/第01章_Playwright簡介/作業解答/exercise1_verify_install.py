"""
第 01 章 練習題 1：安裝 Playwright 並驗證安裝成功

驗證方式：
1. 能成功 import playwright
2. 能啟動 Chromium 並開啟一個頁面
3. 能讀到頁面標題

執行：
    uv run python exercise1_verify_install.py
"""

from importlib.metadata import version

from playwright.sync_api import sync_playwright


def verify_install():
    # 1. 確認套件版本（驗證安裝成功）
    print(f"playwright 版本：{version('playwright')}")

    with sync_playwright() as p:
        # 2. 啟動 Chromium（headless=True 不開視窗，適合驗證/自動化）
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 3. 開啟一個簡單頁面並讀取標題
        page.goto("https://example.com")
        print(f"成功開啟頁面，標題：{page.title()}")

        browser.close()

    print("✅ Playwright 安裝驗證成功")


if __name__ == "__main__":
    verify_install()
