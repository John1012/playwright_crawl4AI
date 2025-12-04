# Crawl4A快速入門
[官方的Quick Start](https://docs.crawl4ai.com/core/quickstart/)

## 📚 重要參考資料(一定必需了解)
[**Crawl4AI v0.7.7 主要實體介紹**](./crawl4ai_entities.md) - 了解 AsyncWebCrawler、BrowserConfig、CrawlerRunConfig 等核心類別的詳細說明

---

- 使用最小的配置,運行爬蟲
- 產生Markdown的輸出（並了解他如何受到內容過濾器的影響)
- 嘗試一種基於CSS的簡單提取策略
- 了解基於LLM的擷取(包括開源和閉源模型)
- 抓取透過JavaScript載入內容的動態網頁

### 1. 介紹
- 非同步爬蟲,`AsyncWebClawer`
- 可透過`rowserConfig`和`CrawlerRunConfig`設定瀏覽器和運行設定。
- 透過預設 MarkdownGenerator 自動將 HTML 轉換為 Markdown（支援其它過濾器）。
- 多種擷取策略（基於 LLM 或「傳統」CSS/XPath）。

### 2. 第一個爬蟲

下面是一個最小的 Python 腳本，它會建立一個 AsyncWebCrawler，取得一個網頁，並列印其 Markdown 輸出的前 300 個字元：

[**第1個爬蟲.ipynb**](./lesson1_第1個爬蟲.ipynb)

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com")
        print(result.markdown[:300]) #

if __name__ == '__main__':
    #asyncio,run(main())
    await main()
```


### 3.基本配置(簡單介紹)

Crawl4AI 的爬蟲可以透過兩個主要類別進行高度客製化：

1. BrowserConfig：控制瀏覽器的行為（無頭模式或完整使用者介面、使用者代理、JavaScript 開關等）。

2. Crawler RunConfig：控制每個爬蟲如何運作（快取caching、提取extraction、逾時timeout、掛接hooking等）。

[**簡單配置.ipynb**](./lesson2_基本配置.ipynb)

```python
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def main():
    browser_conf= BrowserConfig(headless=True)
    run_conf = CrawlerRunConfig(
        # cache_mode: 設定爬蟲的快取模式
        # CacheMode.BYPASS: 繞過快取,每次都重新抓取網頁內容,不使用任何已儲存的快取資料
        # 其他可用模式:
        #   - CacheMode.ENABLED: 啟用快取,如果快取存在則使用快取資料,避免重複請求
        #   - CacheMode.READ_ONLY: 只讀模式,只從快取讀取,不會更新快取
        #   - CacheMode.WRITE_ONLY: 只寫模式,只更新快取,不從快取讀取
        # 使用 BYPASS 適合:測試階段、需要最新資料、網頁內容經常變動的情況
        cache_mode=CacheMode.BYPASS
    )

    async with AsyncWebCrawler(config=browser_conf) as crawler:
        result = await crawler.arun(
            url='https://example.com',
            config=run_conf
        )
        print(result.markdown)

if __name__ == "__main__":
	#asyncio,run(main())
    await main()
```

### 4. 產生MarkDown輸出
預設情況下，Crawl4AI 會自動從每個爬取的頁面產生 Markdown 檔案。不過，具體輸出結果取決於你指定了 Markdown 產生器還是內容過濾器。

- result.markdown:  
直接將 HTML 轉換為 Markdown。

- result.markdown.fit_markdown:  
套用任何已配置的內容過濾器（例如,PruningContentFilter)。

[**使用內容過濾器.ipynb**](./lesson3_使用內容過濾器.ipynb)

```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig,CacheMode
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

md_generator = DefaultMarkdownGenerator(
    # 建立 PruningContentFilter 內容過濾器,用於過濾低品質或不重要的內容
    # threshold=0.4: 設定過濾閾值為 0.4,內容重要性分數低於此值的內容將被移除
    # threshold_type="fixed": 使用固定閾值模式,所有內容都使用相同的 0.4 標準來判斷是否保留
    # 其他可選的 threshold_type 包括: "dynamic"(動態閾值)、"percentile"(百分位數)
    # 此過濾器會分析 HTML 元素的密度、文字長度、標籤類型等特徵來計算重要性分數
    content_filter = PruningContentFilter(threshold=0.4, threshold_type="fixed")
)

config = CrawlerRunConfig(
    cache_mode = CacheMode.BYPASS,
    markdown_generator = md_generator
)

async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://news.ycombinator.com", config=config)
    print("raw Markdown length:",len(result.markdown.raw_markdown))
    print("Fit Markdown length:",len(result.markdown.fit_markdown))
```


### 5. 簡單資料擷取（基於CSS）

Crawl4AI 也可以使用 CSS 或 XPath 選擇器來擷取結構化資料 (JSON)。以下是一個基於 CSS 的簡單範例：

> 新功能！ Crawl4AI 現在提供了一個強大的實用程序，可以使用 LLM 自動產生提取模式。只需執行一次，即可獲得可重複使用的模式，實現快速：

**5.1 透過自訂的css_schema擷取網頁內容**

[擷取策略官方文件說明](https://docs.crawl4ai.com/extraction/no-llm-strategies/)

**Schema 定義了以下內容:**

1. 一個基礎選擇器,用於識別頁面上的每個「容器」元素(例如:產品列、部落格文章卡片)。
2. 欄位描述,說明要使用哪些 CSS/XPath 選擇器來擷取每個資料片段(文字、屬性、HTML 區塊等)。
3. 巢狀或清單類型,用於處理重複或階層式結構。

```python
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def main():

    # Schema 基本架構說明:
    # 1. "name": Schema 的名稱,用於識別此擷取規則
    # 2. "baseSelector": 基礎選擇器,定義資料容器的範圍
    #    - 會先找出所有符合此選擇器的元素
    #    - 每個符合的元素會被視為一筆獨立的資料記錄
    #    - 此範例中 HTML 只有一個 div.item,因此只會抓到 1 筆資料
    # 3. "fields": 欄位定義陣列,描述要從每個容器中提取哪些資料
    #    - 每個欄位都是在 baseSelector 範圍內進行相對搜尋
    #    - 支援多種類型: text(文字)、attribute(屬性)、html(HTML內容) 等

    schema = {
        "name": "Example Items",  # Schema 名稱
        "baseSelector": "div.item",  # 容器選擇器: 找出所有 class="item" 的 div (此例只有1個)
        "fields": [  # 欄位定義: 要從每個容器中提取的資料
            {
                "name": "title",       # 欄位名稱: 在結果 JSON 中的 key
                "selector": "h2",      # CSS 選擇器: 在容器內找 h2 元素
                "type": "text"         # 提取類型: 取得元素的文字內容
            },
            {
                "name": "link",           # 欄位名稱: 連結
                "selector": "a",          # CSS 選擇器: 在容器內找 a 元素
                "type": "attribute",      # 提取類型: 取得元素的屬性值
                "attribute": "href"       # 指定要取得的屬性名稱
            }
        ]
    }

    raw_html = "<div class='item'><h2>Item 1</h2><a href='https://example.com/item1'>Link 1</a></div>"

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="raw://" + raw_html,
            config=CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS,
                extraction_strategy=JsonCssExtractionStrategy(schema)
            )
        )
        # The JSON output is stored in 'extracted_content'
        data = json.loads(result.extracted_content)
        print(result.extracted_content)
        print("========================")
        print(data)

if __name__ == "__main__":
    await main()

```

**5.2 透過手動方式產生css_schema**

[**‼️手動方式產生css_schema(內有多個實際案例)**](./手動方式產生css_schema)

**下方程式碼是透過手動schema建立的擷取範例**

```python
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def extract_crypto_prices():
    dummy_html = """
    <html>
      <body>
        <div class='crypto-row'>
          <h2 class='coin-name'>Bitcoin</h2>
          <span class='coin-price'>$28,000</span>
        </div>
        <div class='crypto-row'>
          <h2 class='coin-name'>Ethereum</h2>
          <span class='coin-price'>$1,800</span>
        </div>
      </body>
    </html>
    """
    #1. 定義一個簡單的extraction schema
    schema = {
        "name":"Crypto Prices",
        "baseSelector": "div.crypto-row", #有2筆,所以抓到2筆
        "fields":[
            {
                "name": "coin_name",
                "selector": "h2.coin-name",
                "type":"text"
            },
            {
                "name":"price",
                "selector":"span.coin-price",
                "type":"text"
            }
        ]
    }

    #2. 建立extraction strategy
    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True) #Enables verbose logging for debugging purposes.

    #3. 設定爬蟲配置
    config = CrawlerRunConfig(
        cache_mode = CacheMode.BYPASS,
        extraction_strategy=extraction_strategy
    )

    async with AsyncWebCrawler(verbose=True) as crawler:
        #4. 執行爬蟲和提取任務
        raw_url = f"raw://{dummy_html}"
        result = await crawler.arun(
            url=raw_url,
            config=config
        )

        if not result.success:
            print("Crawl failed:", result.error_message)
            return
        
        # 5. 解析被提取的json資料
        data = json.loads(result.extracted_content)
        print(f"Extracted {len(data)} coin entries")
        print(json.dumps(data[0], indent=2) if data else "No Data found")

await extract_crypto_prices()
```

**5.3 使用 LLM 自動產生 CSS Schema**

當網頁結構複雜或你不熟悉 CSS 選擇器時，可以讓 LLM（大型語言模型）自動分析 HTML 並產生 Schema。這個方法有**一次性成本**（呼叫 LLM），但產生的 Schema 可以重複使用，無需再次呼叫 LLM。

#### 📋 LLM 產生 Schema 的工作原理

1. **提供 HTML 範例** → LLM 分析結構
2. **LLM 識別模式** → 找出重複元素、類別名稱
3. **自動產生 CSS 選擇器** → 建立 Schema
4. **重複使用 Schema** → 後續擷取無需 LLM

#### ⚖️ 三種 Schema 產生方式比較

| 方式 | 控制程度 | 精確度 | LLM 成本 | 適用場景 |
|------|---------|--------|---------|---------|
| **手動定義** | 高 | 高 | 無 | 生產環境、結構已知 |
| **LLM 自動產生** | 低 | 中 | 一次性 | 快速原型、探索性爬蟲 |
| **LLM 提示詞引導** | 中 | 高 | 每次 | 複雜擷取、非結構化內容 |

---

### 5.3.1 使用本地模型（Ollama）產生 Schema

**優點：**
- ✅ 免費、無需 API 金鑰
- ✅ 資料隱私（在本機執行）
- ✅ 支援多種開源模型

**前置需求：**
```bash
# 安裝 Ollama
# 參考：https://ollama.ai

# 下載模型
ollama pull llama3.2
```

[**透過 llama 和 Gemini 模型實作的 .ipynb**](./lesson4_css_base_使用llm建立schema.ipynb)

**程式碼範例：**

```python
import asyncio
import json
from pprint import pprint
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from crawl4ai import LLMConfig, AsyncWebCrawler, CacheMode, CrawlerRunConfig

async def main():
    # 步驟 1: 準備 HTML 範例（用於讓 LLM 學習結構）
    html = """
    <div class='item'>
        <h2>Item 1</h2>
        <a href='https://example.com/item1'>Link 1</a>
    </div>
    """

    # 步驟 2: 使用 Ollama 本地模型自動產生 Schema（一次性成本）
    # LLM 會分析 HTML 結構並自動產生 CSS 選擇器
    schema = JsonCssExtractionStrategy.generate_schema(
        html,
        llm_config=LLMConfig(
            provider="ollama/llama3.2",  # 使用本地 Ollama 模型
            api_token=None               # 本地模型不需要 API 金鑰
        )
    )

    print("===== Llama3.2 自動產生的 Schema =========")
    pprint(schema)
    print("\n說明：此 Schema 由 LLM 自動分析 HTML 產生")
    print("      後續擷取可重複使用，無需再次呼叫 LLM\n")

    # 步驟 3: 使用產生的 Schema 建立擷取策略
    strategy = JsonCssExtractionStrategy(schema)

    # 步驟 4: 設定爬蟲配置
    # ⚠️ 重要：必須明確指定 extraction_strategy 參數
    # 否則 result.extracted_content 會是 None
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=strategy  # 必須指定
    )

    # 步驟 5: 執行爬蟲擷取資料
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=f"raw://{html}",
            config=config
        )

        print("========== 擷取結果 ==========")
        data = json.loads(result.extracted_content)
        pprint(data)

if __name__ == "__main__":
    await main()  # Jupyter Notebook 環境
    # asyncio.run(main())  # 一般 Python 環境
```

**執行結果範例：**
```python
# LLM 自動產生的 Schema
{
    'name': 'Items',
    'baseSelector': 'div.item',
    'fields': [
        {'name': 'title', 'selector': 'h2', 'type': 'text'},
        {'name': 'link', 'selector': 'a', 'type': 'attribute', 'attribute': 'href'}
    ]
}

# 擷取結果
[
    {
        'title': 'Item 1',
        'link': 'https://example.com/item1'
    }
]
```

---

### 5.3.2 使用雲端 LLM（Gemini/OpenAI/Claude）產生 Schema

**優點：**
- ✅ 更強大的推理能力
- ✅ 更準確的 Schema 產生
- ✅ 支援複雜 HTML 結構

**缺點：**
- ❌ 需要 API 金鑰和付費
- ❌ 資料需上傳至雲端

#### 使用 Google Gemini

```python
import asyncio
import json
from pprint import pprint
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from crawl4ai import LLMConfig, AsyncWebCrawler, CacheMode, CrawlerRunConfig

async def main():
    # 準備 HTML 範例
    html = """
    <html>
        <body>
            <div class='product'>
                <h2>Gaming Laptop</h2>
                <span class='price'>$999.99</span>
            </div>
        </body>
    </html>
    """

    # 使用 Gemini 模型產生 Schema
    schema = JsonCssExtractionStrategy.generate_schema(
        html,
        llm_config=LLMConfig(
            provider="gemini/gemini-2.0-flash-exp",     # Gemini 模型
            api_token="YOUR_GEMINI_API_KEY"  # 替換為你的 API 金鑰
        )
    )

    print("====== Gemini 自動產生的 Schema ======")
    pprint(schema)

    # 使用產生的 Schema 進行擷取
    strategy = JsonCssExtractionStrategy(schema, verbose=True)

    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=strategy
    )

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=f"raw://{html}",
            config=config
        )

        print("\n======= 擷取結果 ===========")
        data = json.loads(result.extracted_content)
        pprint(data)

if __name__ == "__main__":
    await main()
```

#### 使用 OpenAI GPT

```python
# 只需更改 LLM 配置
schema = JsonCssExtractionStrategy.generate_schema(
    html,
    llm_config=LLMConfig(
        provider="openai/gpt-4o-mini",      # OpenAI 模型
        api_token="YOUR_OPENAI_API_KEY"  # OpenAI API 金鑰
    )
)
```

#### 使用 Anthropic Claude

```python
# 只需更改 LLM 配置
schema = JsonCssExtractionStrategy.generate_schema(
    html,
    llm_config=LLMConfig(
        provider="anthropic/claude-3-5-sonnet-20241022",  # Claude 模型
        api_token="YOUR_ANTHROPIC_API_KEY"     # Anthropic API 金鑰
    )
)
```

---

### 5.3.3 手動 Schema vs LLM 產生的比較

```python
# 方法 A: LLM 自動產生（快速但不可控）
schema_auto = JsonCssExtractionStrategy.generate_schema(
    html,
    llm_config=LLMConfig(provider="ollama/llama3.2", api_token=None)
)

# 方法 B: 手動定義（精確可控）
schema_manual = {
    'name': 'Product Details',
    'baseSelector': '.product',
    'fields': [
        {'name': 'title', 'selector': 'h2', 'type': 'text'},
        {'name': 'price', 'selector': '.price', 'type': 'text'}
    ]
}

# 兩者都可以用於建立擷取策略
strategy_auto = JsonCssExtractionStrategy(schema_auto)
strategy_manual = JsonCssExtractionStrategy(schema_manual)
```

---

### 5.3.4 完整實作範例

[**查看完整範例：manual_control_example.py**](./manual_control_example.py)

這個範例展示了三種控制 Schema 的方法：
1. LLM 自動產生（快速原型）
2. 手動定義 Schema（生產環境）
3. 使用自訂提示詞引導 LLM（複雜擷取）

---

### 🎯 使用建議

| 場景 | 推薦方式 | 原因 |
|------|---------|------|
| 🚀 快速原型開發 | LLM 自動產生 | 快速、自動化 |
| 🏭 生產環境 | 手動定義 Schema | 精確、快速、無 LLM 成本 |
| 🔬 複雜網頁探索 | LLM 自動產生 | 節省手動分析時間 |
| 📊 大規模爬蟲 | 手動定義 Schema | 避免重複 LLM 成本 |
| 🧩 非結構化內容 | LLMExtractionStrategy | 需要 AI 理解語義 |

---

### ⚠️ 重要注意事項

1. **Schema 可重複使用**
   產生一次後，儲存 Schema 並重複使用，避免每次都呼叫 LLM

2. **必須指定 extraction_strategy**
   ```python
   config = CrawlerRunConfig(
       extraction_strategy=strategy  # 必須明確指定
   )
   ```
   否則 `result.extracted_content` 會是 `None`

3. **本地 vs 雲端 LLM**
   - 開發/測試 → 使用 Ollama（免費）
   - 複雜任務 → 使用雲端 LLM（更準確）

4. **HTML 範例品質**
   提供完整且具代表性的 HTML 範例，LLM 才能產生準確的 Schema







