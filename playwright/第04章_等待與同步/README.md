# 第四章：等待與同步

`網頁載入是非同步`的過程，正確的等待策略是穩定自動化的關鍵。

## 4.1 為什麼需要等待？

### 網頁載入的非同步性質
- JavaScript 動態載入內容
- AJAX 請求延遲
- 圖片和資源載入時間
- 網路速度不穩定

### 常見的時機問題
```python
# 錯誤示範：元素還沒出現就嘗試點擊
page.goto("https://example.com")
page.click("#dynamic-button")  # 可能失敗！
```

---

## 4.2 自動等待機制(Auto-waiting)

### Playwright 的智慧等待

Playwright 的大部分操作都有**內建自動等待**：

```python
# 這些操作會自動等待元素可操作
page.click("button")       # 等待元素可見且可點擊
page.fill("input", "text") # 等待元素可見且可編輯
page.select_option("select", "value")  # 等待元素可選擇
```

自動等待的條件：
- 元素已附加到 DOM
- 元素可見
- 元素穩定（沒有動畫）
- 元素可接收事件
- 元素啟用（非 disabled）

### 預設超時時間設定

```python
# 設定全域超時時間（毫秒）
page.set_default_timeout(60000)  # 60 秒

# 設定導航超時時間
page.set_default_navigation_timeout(30000)  # 30 秒
```

---

## 4.3 明確等待

### `wait_for_selector()` - 等待元素出現

```python
# 等待元素可見
page.wait_for_selector("#submit-button", state="visible")

# 等待元素附加到 DOM
page.wait_for_selector("#submit-button", state="attached")

# 等待元素隱藏
page.wait_for_selector("#loading", state="hidden")

# 設定超時時間
page.wait_for_selector("#submit-button", timeout=5000)
```

**state 選項：**
- `attached` - 元素已附加到 DOM
- `detached` - 元素已從 DOM 移除
- `visible` - 元素可見（預設）
- `hidden` - 元素隱藏

### `wait_for_load_state()` - 等待頁面狀態

```python
# 等待頁面完全載入
page.wait_for_load_state("load")

# 等待 DOM 內容載入
page.wait_for_load_state("domcontentloaded")

# 等待網路閒置（沒有網路請求）
page.wait_for_load_state("networkidle")
```

### `wait_for_timeout()` - 固定時間等待（應避免）

```python
# 不建議：固定等待時間
page.wait_for_timeout(3000)  # 等待 3 秒

# 建議：使用其他等待方法
page.wait_for_selector("#element")
```

---

## 4.4 等待事件

### 等待導航完成

```python
# 方法1：使用 expect_navigation
with page.expect_navigation():
    page.click("a#next-page")

# 方法2：等待特定 URL
with page.expect_navigation(url="**/success"):
    page.click("button#submit")
```

### 等待請求/回應

```python
# 等待特定請求
with page.expect_request("**/api/data") as request_info:
    page.click("button#load-data")
request = request_info.value
print(request.url)

# 等待特定回應
with page.expect_response("**/api/user") as response_info:
    page.click("button#get-user")
response = response_info.value
print(response.status)
```

### 自訂等待條件

```python
# 使用 wait_for_function
page.wait_for_function("document.readyState === 'complete'")

# 等待特定條件
page.wait_for_function("() => document.querySelectorAll('.item').length > 10")

# 傳遞參數
page.wait_for_function("count => document.querySelectorAll('.item').length >= count", 5)
```

---

## 完整範例

本章提供了完整的互動式示範：

### 檔案說明
- `waiting_demo.html` - 互動式示範頁面，包含 6 種等待情境
- `index.py` - 完整的 Python 腳本，展示所有等待策略

### 執行方式

```bash
# 在本章目錄下執行
python index.py
```

### 示範內容

1. **延遲載入元素** - 等待元素在延遲後出現
2. **動態內容載入** - 模擬 AJAX 請求與資料載入
3. **元素狀態變化** - 等待元素從隱藏變為可見
4. **表單提交** - 處理表單提交與回應等待
5. **批次載入** - 等待多個元素逐步載入
6. **API 請求** - 模擬 API 請求與回應處理
7. **頁面載入狀態** - 觀察不同的載入狀態
8. **超時設定** - 自訂超時時間的使用

### 核心程式碼片段

```python
from playwright.sync_api import sync_playwright

# 等待延遲元素
page.click("#trigger-delayed")
page.wait_for_selector("#loading-1", state="visible")
page.wait_for_selector("#loading-1", state="hidden")
page.wait_for_selector("#delayed-result.show", state="visible")

# 等待動態內容
page.click("#load-data")
page.wait_for_function(
    "document.querySelectorAll('#dynamic-content .item').length >= 3"
)

# 等待元素狀態變化
page.click("#toggle-visibility")
page.wait_for_selector("#toggle-element", state="visible")

# 等待頁面載入狀態
page.goto("file://path/to/waiting_demo.html")
page.wait_for_load_state("domcontentloaded")
page.wait_for_load_state("load")
page.wait_for_load_state("networkidle")
```

---

## 最佳實踐

1. **優先使用自動等待** - Playwright 的內建等待已經很強大
2. **避免 wait_for_timeout()** - 使用具體的等待條件
3. **設定合理的超時時間** - 根據網路狀況調整
4. **等待網路閒置** - 處理動態載入內容時很有用
5. **組合使用** - 根據情況選擇合適的等待策略

---

## 練習題

1. 訪問一個動態網站，練習使用 `wait_for_selector()`
2. 嘗試等待頁面的不同載入狀態
3. 練習攔截並等待 API 請求/回應
4. 使用 `wait_for_function()` 自訂等待條件

---

[← 上一章：元素定位](../第03章_元素定位/README.md) | [返回目錄](../README.md) | [下一章：資料擷取 →](../第05章_資料擷取/README.md)
