# CLAUDE.md

提供給 Claude Code 在本儲存庫工作時的指引。

## 語言

無論使用者用英文或中文提問，一律以**繁體中文**回覆。本儲存庫的文件與程式碼註解皆為繁體中文；變數與函式名稱維持英文。

## 這個儲存庫是什麼

這是一個**教學用儲存庫** —— 現代 Python 網路爬蟲的實作教材。它不是可部署的應用程式，而是一系列各自獨立的課程與範例。內容分為兩條學習路線：

- **`playwright/`** —— Playwright（瀏覽器自動化），共 13 章，從入門到完整專案。
- **`crawl4AI/`** —— Crawl4AI（建立在 Playwright 之上、由 AI 輔助的爬蟲框架），另含 asyncio 入門與實際案例。

建議學習順序：Playwright 基礎 → asyncio → Crawl4AI。

## 安裝與執行

```bash
uv sync                      # 安裝相依套件（建議方式）
uv run playwright install    # 下載瀏覽器驅動 —— 任何爬蟲執行前都必須先做
```

執行範例：
```bash
uv run python crawl4AI/Crawl4A多頁面爬蟲/lesson1_爬取台灣即時股票資訊_loop方式.py
```

Notebook（`.ipynb`）需要 `ipykernel`；若在 notebook 中遇到「event loop already running」錯誤，那正是 `nest-asyncio` 要解決的問題。

- Python：**3.11**（見 `.python-version`、`pyproject.toml` 的 `requires-python >=3.11`）。
- 套件管理：**uv**（`pyproject.toml` + `uv.lock`）。
- 主要相依：`crawl4ai>=0.7.7`、`playwright>=1.55.0`、`nest-asyncio`、`ipykernel`。

## 目錄結構

```
playwright/                  # 第01章 … 第13章 + 專案一/二/三
crawl4AI/
  asyncio套件教學/           # 學 Crawl4AI 前必讀
  初體驗/  Crawl4A快速入門/  Crawl4A操控javascript/
  Crawl4A多頁面爬蟲/  排程/  docker/  .gemini/
  實際案例/                  # 1 匯率 · 2 股票 · 3/4 股票 + Tkinter GUI
thsrc_cookies.json           # 台灣高鐵的 session cookies（專案三 高鐵時刻表使用）
```

每個章節 / 課程資料夾都各自獨立，並附有自己的 `README.md`。許多課程附帶本地的 `*_demo.html`，可離線對著靜態頁面執行。

## 新增 / 修改時的慣例

- 每個範例都要**自成一體且可直接執行**，並附上說明用的 `README.md`。
- 文件與註解使用繁體中文；只要牽涉到真實網站，就加入錯誤處理 / 重試機制。
- Crawl4AI 範例使用 `async/await`；批次 / 多頁面爬取請優先使用 `arun_many()`（參見 `Crawl4A多頁面爬蟲/lesson3`）。
- 沿用既有的資料夾命名規則（`第NN章_主題/` 或 `lessonN_描述`）。
- 若新增章節或案例，記得同步更新最上層 `README.md` 的章節表格。

## 實際案例（真實的台灣網站）

- `crawl4AI/實際案例/1台灣銀行牌告匯率/` —— 靜態頁面、CSS Schema。初級。
- `crawl4AI/實際案例/2台灣即時股票資訊/` —— JavaScript 渲染的動態內容。中級。
- `crawl4AI/實際案例/3…_tkinter/` 與 `4…_tkinter/` —— 完整的 Tkinter GUI 應用，AI 輔助開發，各自附有 `prd.md`。高級。
- `playwright/專案三_台灣高鐵時刻表查詢/main.py` —— 使用 `thsrc_cookies.json`。

## 注意事項

- `thsrc_cookies.json` 內含真實的 session cookies；請勿提交新的憑證，並把它視為可重新產生的拋棄式檔案。
- 沒有 CI、測試或建置流程 —— 變更請以執行對應課程的方式來驗證。
