# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Language

Always reply in Traditional Chinese (繁體中文), regardless of whether the user writes in English or Chinese. Documentation and code comments in this repo are Traditional Chinese; variable/function names stay English.

## What this repo is

An **educational repository** — a hands-on tutorial for modern Python web scraping. It is not a deployable app; it's a collection of self-contained lessons and worked examples. Two tracks:

- **`playwright/`** — Playwright (browser automation), 13 chapters from intro to full projects.
- **`crawl4AI/`** — Crawl4AI (AI-powered scraping framework built on Playwright), plus an asyncio primer and real-world cases.

Intended learning order: Playwright basics → asyncio → Crawl4AI.

## Setup & running

```bash
uv sync                 # install deps (preferred)
uv run playwright install   # download browser binaries — required before any scraping
```

Run an example:
```bash
uv run python crawl4AI/Crawl4A多頁面爬蟲/lesson1_爬取台灣即時股票資訊_loop方式.py
```

Notebooks (`.ipynb`) need `ipykernel`; if you hit "event loop already running" inside a notebook, that's what `nest-asyncio` is for.

- Python: **3.11** (`.python-version`, `pyproject.toml requires-python >=3.11`).
- Package manager: **uv** (`pyproject.toml` + `uv.lock`).
- Key deps: `crawl4ai>=0.7.7`, `playwright>=1.55.0`, `nest-asyncio`, `ipykernel`.

## Layout

```
playwright/                  # 第01章 … 第13章 + 專案一/二/三
crawl4AI/
  asyncio套件教學/           # read before Crawl4AI
  初體驗/  Crawl4A快速入門/  Crawl4A操控javascript/
  Crawl4A多頁面爬蟲/  排程/  docker/  .gemini/
  實際案例/                  # 1 匯率 · 2 股票 · 3/4 股票 + Tkinter GUI
thsrc_cookies.json           # saved Taiwan HSR session cookies (used by 專案三 高鐵時刻表)
```

Each chapter/lesson folder is independent and carries its own `README.md`. Many lessons ship a local `*_demo.html` so they run offline against a static page.

## Conventions when adding/editing

- Keep each example **self-contained and runnable**, with its own `README.md` explaining it.
- Documentation and comments in Traditional Chinese; include error handling/retries where a real site is involved.
- Crawl4AI examples use `async/await`; prefer `arun_many()` for batch/multi-page scraping (see `Crawl4A多頁面爬蟲/lesson3`).
- Match the existing folder naming pattern (`第NN章_主題/` or `lessonN_描述`).
- Update the top-level `README.md` chapter tables if you add a chapter or case.

## Practical examples (real Taiwan sites)

- `crawl4AI/實際案例/1台灣銀行牌告匯率/` — static page, CSS Schema. Beginner.
- `crawl4AI/實際案例/2台灣即時股票資訊/` — JS-rendered dynamic content. Intermediate.
- `crawl4AI/實際案例/3…_tkinter/` & `4…_tkinter/` — full Tkinter GUI apps, AI-assisted, each with a `prd.md`. Advanced.
- `playwright/專案三_台灣高鐵時刻表查詢/main.py` — uses `thsrc_cookies.json`.

## Notes

- `thsrc_cookies.json` holds real session cookies; don't commit fresh credentials and treat it as throwaway/regenerable.
- No CI, tests, or build step — verify changes by running the specific lesson.
