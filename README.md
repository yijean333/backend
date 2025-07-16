# Backend 

這個後端系統負責管理來自 Discord bot 的資料，並提供給前端網頁使用。

## 功能說明
- 每 5 分鐘由 Discord bot 更新違規資料，寫入 `violations.json`
- 將 JSON 檔內容提供給前端讀取與顯示

## 資料流程簡介
1. Discord bot 抓取最新資料
2. 資料會寫入本地的 `violations.json` 檔案
3. 前端網頁會向後端請求這個 JSON 檔，並將內容顯示在地圖上

## 檔案說明
- `violations.json`：由 Discord bot 自動更新的違規資料
- 主要程式碼：處理 JSON 的儲存與提供給前端的讀取


