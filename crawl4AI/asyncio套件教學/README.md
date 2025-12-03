# Python `asyncio` 完整教學：從入門到實戰

## 🎯 教學目標

1.  **秒懂概念**：用生活化的比喻，讓你真正理解「同步」與「非同步」的差異。
2.  **環境設定**：解決 Jupyter Notebook (`.ipynb`) 無法直接執行 `asyncio.run()` 的痛點。
3.  **實戰應用**：學會 `async/await` 基本語法，並用 `gather` 實現高效率的並行爬蟲。

---

## 1. 觀念篇：為什麼需要 `asyncio`？

### 漫畫圖解：同步 vs 非同步

![sync_async](./images/sync_async.png)

這張圖完美詮釋了兩種模式的差異：

#### **左圖：同步 (Sync)** 🐢
> **「一次只做一件事，做完才換下一個」**

*   **情境**：你是一個服務生，幫客人 A 點完餐後，**你就站在廚房門口乾等**，直到廚房把餐點做好，你端給客人 A，才願意去幫客人 B 點餐。
*   **結果**：客人 B 等到天荒地老，你的時間都浪費在「等待」上。
*   **程式碼**：`time.sleep(5)` (程式完全卡住)。

#### **右圖：非同步 (Async)** ⚡
> **「等待的時間，拿來服務下一位」**

*   **情境**：你幫客人 A 點完餐，把單子丟進廚房。**在廚房做菜的這段空檔，你馬上轉身去幫客人 B 點餐**。
*   **結果**：你一個人就能同時服務多個客人，完全不浪費任何時間。
*   **程式碼**：`await asyncio.sleep(5)` (讓出控制權，去處理其他任務)。

---

## 2. 環境篇：如何在 Jupyter Notebook 執行？

這是新手最常遇到的坑！`asyncio` 需要一個「事件迴圈 (Event Loop)」來運作。

### ❌ 錯誤寫法 (在 .ipynb 中)
在 Jupyter Notebook 中直接執行 `asyncio.run(main())` 通常會報錯：
`RuntimeError: asyncio.run() cannot be called from a running event loop`
因為 Jupyter 本身就已經在一個事件迴圈裡運行了。

### ✅ 正確解法 1：直接 `await` (推薦)
在 Jupyter Notebook (或 IPython) 中，你可以直接在最外層使用 `await`。

```python
# 在 .ipynb 儲存格中直接執行
await main()
```

### ✅ 正確解法 2：使用 `nest_asyncio` (萬用解)
如果你希望程式碼在 `.py` 檔和 `.ipynb` 檔都能通用，或者遇到複雜的迴圈衝突，使用 `nest_asyncio` 是最穩的解法。

**安裝**
```bash
pip install nest_asyncio
```

**使用**
```python
import nest_asyncio
import asyncio

# 這行魔法代碼會允許事件迴圈被嵌套使用
nest_asyncio.apply()

async def main():
    print("Hello Asyncio!")

# 現在 asyncio.run() 在 jupyter 裡也能跑了！
asyncio.run(main())
```

---

## 3. 基礎篇：語法三部曲

### 第一步：定義 (`async def`) 與 執行 (`await`)

*   **`async def`**：定義一個非同步函式（協程 Coroutine）。
*   **`await`**：等待一個非同步任務完成。

```python
import asyncio

# 1. 定義非同步函式
async def say_hello():
    print("開始執行...")
    # 模擬耗時操作 (例如網路請求)，這裡必須用 await
    await asyncio.sleep(1) 
    print("執行結束！")
    return "Success"

# 2. 執行它
# 在 Jupyter 中： await say_hello()
# 在 Python 檔中： asyncio.run(say_hello())
```

### 第二步：循序執行 (Sequential) - 還沒變快？

如果你只是把 `await` 一個接一個寫，那效果跟同步是一樣的（慢）。

```python
import time

async def task(name, seconds):
    print(f"{name} 開始...")
    await asyncio.sleep(seconds)
    print(f"{name} 結束")

async def main_sequential():
    start = time.time()
    
    # 這裡會等 task A 做完，才做 task B
    await task("任務 A", 2)
    await task("任務 B", 2)
    
    print(f"總耗時: {time.time() - start:.2f} 秒")

# 預期結果：約 4 秒 (2 + 2)
# await main_sequential()
```

### 第三步：並行執行 (Concurrent) - 真正的加速！🚀

使用 `asyncio.gather` 同時啟動多個任務。

```python
async def main_concurrent():
    start = time.time()
    
    print("同時啟動所有任務...")
    # 建立任務清單，同時丟給事件迴圈
    # gather 會等待所有任務都完成才繼續
    await asyncio.gather(
        task("任務 A", 2),
        task("任務 B", 2)
    )
    
    print(f"總耗時: {time.time() - start:.2f} 秒")

# 預期結果：約 2 秒 (取決於最慢的那個任務)
# await main_concurrent()
```

---

## 4. 實戰篇：模擬高效率爬蟲

讓我們模擬抓取 3 個網站的資料。

```python
import asyncio
import time
import random

async def fetch_url(url):
    # 模擬網路延遲 (1~3秒隨機)
    delay = random.randint(1, 3)
    print(f"🔍 開始抓取: {url} (預計 {delay} 秒)")
    
    await asyncio.sleep(delay)  # 關鍵：這裡讓出控制權，讓其他任務可以執行
    
    print(f"✅ 完成抓取: {url}")
    return f"[{url} 的網頁內容]"

async def main_crawler():
    urls = [
        "https://www.google.com",
        "https://www.python.org",
        "https://www.github.com"
    ]
    
    start = time.time()
    
    # 1. 建立任務清單 (List of Coroutines)
    tasks = [fetch_url(url) for url in urls]
    
    # 2. 並行執行並取得結果
    results = await asyncio.gather(*tasks)
    
    end = time.time()
    
    print("\n--- 執行結果 ---")
    for result in results:
        print(result)
    print(f"總耗時: {end - start:.2f} 秒 (如果是同步執行大約需要 {sum(range(1,4))} 秒以上)")

# 在 Jupyter 中執行：
# await main_crawler()
```

---

## 5. 重點總結

| 關鍵字 | 說明 | 比喻 |
| :--- | :--- | :--- |
| **`async def`** | 定義非同步函式 | 寫一張「工作清單」，還沒開始做。 |
| **`await`** | 等待任務完成 | 盯著微波爐直到東西熱好 (但 `asyncio` 允許你在這段時間去切菜)。 |
| **`asyncio.gather`** | 並行執行多個任務 | 一次把三個鍋子都開火，同時煮三道菜。 |
| **`nest_asyncio`** | 解決 Jupyter 報錯神器 | 讓你在夢中還能做夢 (允許事件迴圈嵌套)。 |

### 💡 什麼時候該用 `asyncio`？
*   **適合**：I/O 密集型任務 (爬蟲、呼叫 API、讀寫資料庫)。
*   **不適合**：CPU 密集型任務 (影像處理、複雜數學運算) -> 請改用 `multiprocessing`。
