# Playwright & Crawl4AI 爬蟲教學

> 這份講義涵蓋現代網路爬蟲的核心技術，從基礎到實戰應用

## 開始學習

準備好了嗎？建議從這裡開始：

- [開始 Playwright 學習](./playwright/第01章_Playwright簡介/README.md)

等 Playwright 的基礎打好了，再來學 Crawl4AI：

- [開始 Crawl4AI 學習](./crawl4AI/README.md)

## 為什麼要學現代爬蟲？

以前寫爬蟲的時候，大部分網站都是靜態 HTML，用 `requests` + `BeautifulSoup` 就能搞定。但現在情況完全不同了：

### 傳統爬蟲的困境

- ❌ **JavaScript 渲染的內容抓不到**：現在很多網站用 React、Vue 這些框架，資料都是靠 JavaScript 動態載入的

- ❌ **反爬蟲機制越來越強**：User-Agent 檢查、Cookie 追蹤、行為分析...隨便一個擋住你就爬不動了
- ❌ **等待時間很難控制**：頁面載入有快有慢，要用 `time.sleep()` 猜時間，不然就漏資料
- ❌ **處理動態內容很麻煩**：像是下拉選單、無限滾動、彈出視窗...傳統方法很難處理

### 現代爬蟲的優勢

這就是為什麼我們要學 Playwright 和 Crawl4AI：

- ✅ **真的瀏覽器引擎**：不是模擬，而是用真正的 Chromium/Firefox，JavaScript 跑得跟真人瀏覽一樣
- ✅ **自動等待機制**：不用猜時間，程式會等到元素真的出現才繼續
- ✅ **反爬蟲對策內建**：模擬真實使用者行為，降低被擋的機率
- ✅ **AI 輔助提取**：Crawl4AI 可以搭配 LLM 智能解析網頁結構，不用手寫複雜的選擇器

簡單來說，傳統爬蟲像是「照照片」，只能看到拍那瞬間的畫面；現代爬蟲像是「真的在用瀏覽器」，可以看到完整的互動過程。

---

## 這份講義包含什麼？

這份講義分成兩大部分：

1. **Playwright** - 這是基礎，學好它才能理解現代爬蟲的運作原理
2. **Crawl4AI** - 這是進階，把 Playwright 包裝得更方便，還能結合 AI

建議按照順序學習，先打好 Playwright 的基礎，再用 Crawl4AI 會比較順。

---

## 第一部分：Playwright 完整教學

Playwright 是微軟開發的網頁自動化工具。雖然原本是設計給自動化測試用的，但因為它能完整模擬真實瀏覽器行為，所以也是非常強大的爬蟲工具。

### 為什麼要學 Playwright？

如果你之前用過 Selenium，你會發現 Playwright 快很多，而且穩定性更好。它是直接跟瀏覽器通訊，不是透過 WebDriver，所以不會有那種「明明元素就在那裡，卻找不到」的問題。

### Playwright 的雙重用途

- **自動化測試**：這是它的原始設計目的，用來測試網頁應用程式的功能
- **網路爬蟲**：因為能處理 JavaScript 渲染和動態內容，所以也是絕佳的爬蟲工具

### 核心特色

- **真的支援多瀏覽器**：Chromium、Firefox、WebKit 都可以用同一套 API
- **自動等待機制**：這是最棒的功能，不用自己寫 `time.sleep()`，它會自動等到元素出現
- **功能很完整**：截圖、錄影、攔截網路請求、處理 Cookie...該有的都有
- **速度很快**：官方宣稱比 Selenium 快 2-3 倍，實際用起來確實有感

### 課程內容（13 章）

[playwright官方網站](https://playwright.dev/)

我們會從最基礎的開始，一步步帶你熟悉這個工具：

| 章節 | 內容 | 重點 |
|------|------|------|
| [第 1 章](./playwright/第01章_Playwright簡介/) | Playwright 簡介 | 了解它是什麼、怎麼安裝 |
| [第 2 章](./playwright/第02章_基礎操作/) | 基礎操作 | 啟動瀏覽器、開啟網頁、點擊按鈕 |
| [第 3 章](./playwright/第03章_元素定位/) | 元素定位 | CSS 選擇器、XPath、Playwright 內建定位器 |
| [第 4 章](./playwright/第04章_等待與同步/) | 等待與同步 | 這是重點章節，一定要搞懂等待機制 |
| [第 5 章](./playwright/第05章_資料擷取/) | 資料擷取 | 怎麼把網頁上的文字、連結、屬性抓下來 |
| [第 6 章](./playwright/第06章_進階互動/) | 進階互動 | 滑鼠拖曳、鍵盤操作、滾動頁面 |
| [第 7 章](./playwright/第07章_多頁面與框架處理/) | 多頁面處理 | 處理多個分頁、彈出視窗、iframe |
| [第 8 章](./playwright/第08章_截圖與錄影/) | 截圖與錄影 | 頁面截圖、操作過程錄影、存成 PDF |
| [第 9 章](./playwright/第09章_網路請求與回應/) | 網路請求 | 攔截 API 請求、查看回應內容 |
| [第 10 章](./playwright/第10章_登入與Cookie處理/) | 登入處理 | 自動登入網站、管理 Cookie 保持登入狀態 |
| [第 11 章](./playwright/第11章_反爬蟲對策/) | 反爬蟲對策 | 怎麼避免被網站擋掉 |
| [第 12 章](./playwright/第12章_效能優化/) | 效能優化 | 讓爬蟲跑得更快、更省資源 |
| [第 13 章](./playwright/第13章_實戰專案/) | 實戰專案 | 用前面學的知識寫幾個完整的爬蟲 |

### 前置知識

- 基本的 Python 語法（變數、迴圈、函式）
- 知道 HTML 長什麼樣子（不用很精通，看得懂標籤就好）
- 會用命令列（terminal）執行指令

---

## 第二部分：Crawl4AI 教學

學完 Playwright 之後，我們來看看 Crawl4AI。它是一個**專門為爬蟲設計的框架**，建立在 Playwright 之上，把常見的爬蟲任務簡化。

### Crawl4AI 是什麼？

Crawl4AI 不是測試工具，它是純粹的爬蟲框架。它把 Playwright 的強大功能包裝起來，加上爬蟲專用的功能，讓你寫爬蟲更快更方便。

### 為什麼要用 Crawl4AI？

雖然 Playwright 已經很強了，但用它寫爬蟲時，每次都要處理很多重複的邏輯：
- 啟動瀏覽器、管理連線
- 處理等待、錯誤重試
- 資料提取和清洗
- 非同步批次處理

**Crawl4AI 把這些都包好了**，你只要專注在「要抓什麼資料」就好。

更特別的是，它可以搭配 LLM（像是 GPT-4、Claude）來解析網頁結構。這對結構複雜的網站超有用，不用手寫一大串 CSS 選擇器。

### Crawl4AI vs 直接用 Playwright 寫爬蟲

用個實際例子來比較：

**用 Playwright 寫爬蟲**（需要自己處理所有細節）：
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    # 要自己寫等待邏輯
    # 要自己寫資料提取邏輯
    # 要自己處理錯誤重試
    # 要自己管理瀏覽器生命週期
    browser.close()
```

**用 Crawl4AI 寫爬蟲**（框架處理細節，你專注資料）：
```python
from crawl4ai import AsyncWebCrawler

async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url='https://example.com')
    # 框架自動處理等待、重試、資料提取
    print(result.markdown)  # 直接拿到清理好的資料
```

看出差別了嗎？Crawl4AI 讓你用更少的程式碼完成同樣的事。

### 核心特色

- **專為爬蟲設計**：不像 Playwright 是測試工具兼爬蟲，Crawl4AI 從頭到尾就是為爬蟲打造的
- **非同步處理**：可以同時爬多個網頁，速度比傳統的 for 迴圈快很多
- **內建 Playwright**：你不需要另外啟動瀏覽器，它都幫你處理好了
- **AI 驅動提取**：可以請 LLM 幫你分析網頁，找出資料在哪裡
- **Schema 設計**：用 CSS Schema 定義要抓的資料結構，很直觀
- **自動化處理**：等待、重試、錯誤處理都內建好了

### 學習路徑

建議按照這個順序：

1. **初體驗** - 先寫第一個 Crawl4AI 程式，感受一下差別
   - [初體驗](./crawl4AI/初體驗/)

2. **快速入門** - 學會基本配置和內容過濾
   - [快速入門](./crawl4AI/Crawl4A快速入門/)

3. **CSS Schema** - 學習怎麼手動定義要抓的資料（不用 LLM 的方法）
   - [手動方式產生 CSS Schema](./crawl4AI/Crawl4A快速入門/手動方式產生css_schema/)

4. **JavaScript 操控** - 處理需要滾動、點擊按鈕的動態網頁
   - [JavaScript 操控](./crawl4AI/Crawl4A操控javascript/)

5. **多頁面爬蟲** - 一次爬很多網址，學會用 `arun_many()` 加速
   - [多頁面爬蟲](./crawl4AI/Crawl4A多頁面爬蟲/)

6. **排程任務** - 讓爬蟲定時自動執行
   - [排程](./crawl4AI/排程/)

7. **實際案例** - 看幾個真實的專案，像是爬匯率、股票資訊
   - [實際案例](./crawl4AI/實際案例/)

### 重要：先學 Asyncio

Crawl4AI 大量使用非同步編程，所以**一定要先看懂 asyncio**。如果 `async/await` 對你來說很陌生，建議先看這篇：

- [Python Asyncio 非同步編程教學](./crawl4AI/asyncio套件教學/)

別跳過這部分，不然看 Crawl4AI 的程式碼會一頭霧水。

---

## Playwright vs Crawl4AI：什麼時候用哪個？

這是我常被問的問題。首先要知道：**這兩套工具都可以用來寫爬蟲**，差別在於設計目的和使用方式。

### 核心差異對比

| 比較項目 | Playwright | Crawl4AI |
|---------|-----------|----------|
| **原始設計目的** | 自動化測試工具 | 專門的爬蟲框架 |
| **爬蟲功能** | ✅ 完全支援（需自己寫邏輯） | ✅ 完全支援（內建爬蟲功能） |
| **底層技術** | 直接控制瀏覽器 | 基於 Playwright 封裝 |
| **學習曲線** | 需要理解底層原理 | 上手較快，API 更簡潔 |
| **控制精細度** | 非常精細，完全掌控 | 較高層次，專注資料提取 |
| **非同步處理** | 需自己實作 | 內建非同步批次處理 |
| **AI 整合** | 需自己串接 | 內建 LLM 解析功能 |
| **適用場景** | 測試 + 爬蟲 | 純爬蟲應用 |
| **程式碼量** | 較多（需處理細節） | 較少（框架處理細節） |
| **效能優化** | 需自己調整 | 內建優化策略 |

### 使用場景建議

#### 選擇 Playwright 的情況

- 需要很精細的控制（像是測試網站功能）
- 想要完全理解底層的運作原理
- 只是爬幾個簡單的網站
- 需要客製化特殊的瀏覽器行為

#### 選擇 Crawl4AI 的情況

- 要爬很多網頁、處理大量資料
- 網站結構很複雜，想用 AI 幫忙解析
- 想要快速開發，不想處理太多細節
- 需要非同步批次爬取多個網站

### 我的建議

**先學 Playwright 打基礎**，理解瀏覽器自動化的原理。之後再用 Crawl4AI 提升開發效率。

兩者不衝突，Crawl4AI 內部就是用 Playwright，所以你學的 Playwright 知識完全不會浪費。就像學會開手排車之後，開自排車會更得心應手。

### 簡單比喻

- **Playwright** = 瑞士刀（多功能工具，測試和爬蟲都能做，但需要自己組裝）
- **Crawl4AI** = 專業爬蟲工具組（只做爬蟲，但做得更快更方便）

---

## 實際案例

講義裡有幾個完整的專案可以參考：

### [台灣銀行牌告匯率](./crawl4AI/實際案例/1台灣銀行牌告匯率/main.py)
這是靜態網頁的範例，適合剛入門的時候看。

### [台灣即時股票資訊](./crawl4AI/實際案例/2台灣即時股票資訊/main.py)
動態網頁的範例，要處理 JavaScript 渲染的內容。

### [Tkinter GUI 整合](./crawl4AI/實際案例/4台灣即時股票資訊_tkinter/)
不只寫爬蟲，還做成桌面應用程式，加上自動更新功能。這個專案比較完整，可以看到實際應用的樣子。

---

## 開始之前

### 環境需求

- Python 3.8 以上（建議 3.10+）
- 穩定的網路連線（要下載瀏覽器驅動）
- 硬碟空間至少 2GB（瀏覽器檔案不小）

### 安裝步驟

#### 1. 安裝 Playwright

```bash
pip install playwright
playwright install
```

注意：`playwright install` 很重要，它會下載瀏覽器驅動，沒這步程式跑不起來。

#### 2. 安裝 Crawl4AI

```bash
pip install crawl4ai
```

詳細的安裝說明和可能遇到的問題，可以看：
- [Playwright 安裝指南](./playwright/第01章_Playwright簡介/README.md)
- [Crawl4AI 安裝指南](./crawl4AI/安裝/README.md)

---

## 學習建議

### 如果是初學者

1. 從 Playwright 第 1 章開始，不要跳
2. 每章節的範例程式碼都要自己跑過
3. 試著改寫範例，看看會發生什麼事
4. 寫一些自己的小專案（像是爬自己常看的網站）

### 如果已經有基礎

1. 還是建議先快速瀏覽 Playwright 的內容，確認概念都清楚
2. 重點放在 Crawl4AI 的非同步處理和 Schema 設計
3. 研究效能優化的技巧（Playwright 第 12 章）
4. 挑戰更複雜的專案，像是需要登入、處理動態內容的網站

---

## 其他資源

### 官方文件
- [Playwright 官方文件](https://playwright.dev/python/) - API 參考的好地方
- [Crawl4AI GitHub](https://github.com/unclecode/crawl4ai) - 可以看原始碼和 issue

### 遇到問題？

1. 先查各章節的 README，可能有解答
2. 看看實際案例的程式碼，參考別人是怎麼寫的
3. 檢查錯誤訊息，通常會提示問題在哪

---

## 授權資訊

詳見 [LICENSE](./LICENSE) 文件

---


