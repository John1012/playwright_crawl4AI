# CLAUDE.MD - Project Context

This file helps Claude Code understand the project structure and conventions.

## Note
Regardless of whether the input in English or Trandition Chinese,Please reply using Trandition Chinese characters


## Project Overview

**Project Name**: Playwright & Crawl4AI 爬蟲教學
**Purpose**: Comprehensive tutorial for modern web scraping using Playwright and Crawl4AI
**Language**: Python 3.8+ (recommended 3.10+)
**Primary Language**: Traditional Chinese (繁體中文)

This is an educational repository containing complete tutorials and practical examples for learning modern web scraping techniques in Python, covering both Playwright (browser automation) and Crawl4AI (AI-powered scraping framework).

## Project Structure

```
playwright_crawl4AI/
├── playwright/          # Playwright tutorial (13 chapters)
│   ├── 第01章_Playwright簡介/
│   ├── 第02章_基礎操作/
│   ├── 第03章_元素定位/
│   ├── 第04章_等待與同步/
│   ├── 第05章_資料擷取/
│   ├── 第06章_進階互動/
│   ├── 第07章_多頁面與框架處理/
│   ├── 第08章_截圖與錄影/
│   ├── 第09章_網路請求與回應/
│   ├── 第10章_登入與Cookie處理/
│   ├── 第11章_反爬蟲對策/
│   ├── 第12章_效能優化/
│   └── 第13章_實戰專案/
│
├── crawl4AI/            # Crawl4AI tutorial
│   ├── 安裝/
│   ├── 初體驗/
│   ├── Crawl4A快速入門/
│   │   └── 手動方式產生css_schema/
│   ├── Crawl4A操控javascript/
│   ├── Crawl4A多頁面爬蟲/
│   ├── asyncio套件教學/
│   ├── 排程/
│   ├── docker/          # Docker configuration
│   ├── .gemini/         # Gemini AI integration
│   └── 實際案例/
│       ├── 1台灣銀行牌告匯率/
│       ├── 2台灣即時股票資訊/
│       ├── 3台灣即時股票資訊_tkinter/
│       └── 4台灣即時股票資訊_tkinter/
│
├── list/                # Additional resources
├── .venv/               # Python virtual environment
├── main.py              # Main entry point
├── pyproject.toml       # Project configuration (uv)
├── uv.lock              # Dependency lock file
└── README.md            # Main documentation

```

## Key Technologies

### Core Libraries
- **Playwright**: Browser automation library (Microsoft)
  - Supports Chromium, Firefox, WebKit
  - Auto-waiting mechanism
  - Network interception
  - Screenshot/video recording

- **Crawl4AI**: AI-powered web scraping framework
  - Built on top of Playwright
  - Async batch processing
  - LLM-powered content extraction
  - CSS Schema for structured data

### Supporting Libraries
- **asyncio**: For asynchronous programming
- **nest-asyncio**: Enables nested event loops (useful in Jupyter notebooks)
- **Tkinter**: GUI applications (in some examples)
- **ipykernel**: Jupyter notebook support

## Learning Path

The recommended learning sequence is:

1. **Start with Playwright** (Chapters 1-13)
   - Understand browser automation fundamentals
   - Learn element location, waiting mechanisms, data extraction
   - Master anti-scraping techniques

2. **Learn asyncio** (if not familiar)
   - Essential for understanding Crawl4AI
   - See: `crawl4AI/asyncio套件教學/`

3. **Progress to Crawl4AI**
   - Build on Playwright knowledge
   - Learn framework-based scraping
   - Explore AI-powered extraction

## Important Conventions

### Language
- **Documentation**: Traditional Chinese (繁體中文)
- **Code comments**: Traditional Chinese preferred
- **Variable names**: English (standard practice)

### File Organization
- Each chapter has its own README.md
- Practical examples include complete working code
- Real-world examples in `實際案例/` folders

### Code Style
- Use async/await for Crawl4AI examples
- Include error handling and retries
- Add comments explaining complex logic
- Keep examples self-contained and runnable

## Development Environment

### Python Version
- Minimum: Python 3.11 (as specified in pyproject.toml)
- Recommended: Python 3.11+
- Current: Using `.python-version` file

### Package Management
- Using **uv** (modern Python package manager)
- Configuration: `pyproject.toml`
- Lock file: `uv.lock`

### Virtual Environment
- Located in `.venv/`
- Activate before running examples

### Installation
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install playwright
playwright install  # Downloads browser binaries (important!)

pip install crawl4ai
pip install nest-asyncio ipykernel

# Verify installations
playwright --version
python -c "import crawl4ai; print(crawl4ai.__version__)"
```

## Key Differences: Playwright vs Crawl4AI

### Playwright
- **Purpose**: Testing tool + scraping capability
- **Control**: Fine-grained, complete control
- **Learning curve**: Steeper, requires understanding internals
- **Code**: More verbose, manual handling
- **Use when**: Need precise control, testing, simple scraping

### Crawl4AI
- **Purpose**: Pure scraping framework
- **Control**: High-level, focuses on data extraction
- **Learning curve**: Easier, abstracted details
- **Code**: Concise, framework handles details
- **Use when**: Large-scale scraping, complex sites, AI parsing needed

Both are valid for scraping - Playwright gives control, Crawl4AI gives productivity.

## Real-World Examples

### 1. Taiwan Bank Exchange Rates
- **Location**: `crawl4AI/實際案例/1台灣銀行牌告匯率/`
- **Type**: Static web scraping
- **Good for**: Beginners

### 2. Taiwan Stock Information (Real-time)
- **Location**: `crawl4AI/實際案例/2台灣即時股票資訊/`
- **Type**: Dynamic web scraping (JavaScript rendering)
- **Good for**: Intermediate learners

### 3. Stock Info with Tkinter GUI (Version 1)
- **Location**: `crawl4AI/實際案例/3台灣即時股票資訊_tkinter/`
- **Type**: Full application with GUI and auto-refresh
- **Good for**: Complete project reference

### 4. Stock Info with Tkinter GUI (Version 2)
- **Location**: `crawl4AI/實際案例/4台灣即時股票資訊_tkinter/`
- **Type**: Enhanced version with improved UI
- **Good for**: Advanced GUI implementation

## Common Patterns

### Playwright Pattern
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    # Manual waiting, extraction, error handling
    browser.close()
```

### Crawl4AI Pattern
```python
from crawl4ai import AsyncWebCrawler

async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url='https://example.com')
    # Framework handles waiting, retries, extraction
    print(result.markdown)
```

## Session Files

- **Cookies**: `thsrc_cookies.json` - Stores session cookies for authenticated scraping

## When Working with This Project

### For Adding New Examples
1. Follow existing chapter structure
2. Include complete, runnable code
3. Add README.md with explanation
4. Use Traditional Chinese for documentation
5. Test code before committing

### For Modifying Tutorials
1. Maintain consistent formatting
2. Update main README.md if adding chapters
3. Keep examples simple and focused
4. Include error handling
5. Add comments for complex logic

### For Helping Users
1. Recommend Playwright-first learning path
2. Emphasize importance of async understanding for Crawl4AI
3. Point to relevant chapters based on skill level
4. Suggest practical examples for hands-on learning

## External Resources

- [Playwright Official Docs](https://playwright.dev/python/)
- [Crawl4AI GitHub](https://github.com/unclecode/crawl4ai)

## Notes for Claude

### When Assisting with This Project
- Users are learning web scraping, likely Chinese speakers
- Focus on educational value and clear explanations
- Reference specific chapters/examples when relevant
- Respect the learning progression (Playwright → asyncio → Crawl4AI)
- Code examples should be production-ready, not just demos

### Common User Questions
- "Which tool should I use?" → Depends on use case (see comparison above)
- "Why learn Playwright if Crawl4AI is easier?" → Foundation understanding
- "How to avoid getting blocked?" → Chapter 11 (反爬蟲對策)
- "Async is confusing" → Point to asyncio tutorial first

### Project Philosophy
This is an educational resource emphasizing:
1. **Fundamentals first** - Understand how things work (Playwright)
2. **Practical application** - Real-world examples
3. **Progressive learning** - Build on previous knowledge
4. **Modern techniques** - Async, AI-powered scraping

## Advanced Features

### Docker Support
The project includes Docker configuration in `crawl4AI/docker/` for containerized deployment.

### Gemini AI Integration
Found in `crawl4AI/.gemini/` - demonstrates integration with Google's Gemini AI for enhanced content extraction.

### CSS Schema Manual Creation
See `crawl4AI/Crawl4A快速入門/手動方式產生css_schema/` for detailed examples of manually crafting CSS schemas for precise data extraction.

### Multi-page Scraping Techniques
The `Crawl4A多頁面爬蟲/` section covers:
- Loop-based approaches (`lesson1_爬取台灣即時股票資訊_loop方式.py`)
- Different schema strategies (`lesson2_爬取台灣即時股票資訊_不同的schema.py`)
- Batch processing with `arun_many` (`lesson3_爬取台灣即時股票資訊_arun_many.py`)

### Scheduling
The `排程/` directory demonstrates automated scraping with async scheduling for continuous data collection.

## Troubleshooting

### Common Issues
1. **Browser not installed**: Run `playwright install` after installing Playwright
2. **Import errors**: Ensure virtual environment is activated
3. **Async errors in Jupyter**: Use `nest-asyncio` to enable nested event loops
4. **Permission denied**: Check file permissions in project directory
5. **Rate limiting**: Implement delays and respect robots.txt (covered in Chapter 11)

### Dependencies
Current versions (from pyproject.toml):
- crawl4ai >= 0.7.7
- playwright >= 1.55.0
- ipykernel >= 7.1.0
- nest-asyncio >= 1.6.0

## Git Worktree Information
This project uses git worktrees for branch isolation:
- **Worktree location**: `/Users/roberthsu2003/.claude-worktrees/playwright_crawl4AI/romantic-chaum`
- **Main repository**: `/Users/roberthsu2003/Documents/GitHub/playwright_crawl4AI`
- **Current branch**: `romantic-chaum`
- **Main branch**: `main`

When making changes, commits are isolated to the current worktree branch.
