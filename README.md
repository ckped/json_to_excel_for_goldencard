# json_to_excel_for_goldencard
 Streamlit Web App：將 NotebookLM 產生的數位金卡審核 JSON/TXT 資料自動轉換為 Excel，並提供即時預覽與下載功能。支援檔案上傳及文字貼上兩種模式，內建自動清理與格式檢查，簡化審查文件處理流程。
 # 📄 數位金卡審核 AI 生成結果 TXT→Excel 轉換工具
此工具能將 **NotebookLM 或其他來源產生的 JSON 格式 TXT 檔案**，自動轉換為符合固定欄位的 Excel，並提供即時預覽、下載功能。內建自動清理開頭空白行、移除 NotebookLM 警語等機制，協助加速數位金卡審查流程。

---

## 功能特色
- 支援 **TXT 檔案上傳** 與 **文字貼上** 兩種模式
- 自動清理：
  - 去除開頭/結尾空白行與 BOM 字元
  - 自動補外層 JSON 陣列括號（單筆資料時）
  - 自動移除 NotebookLM 固定警語
- 即時預覽表格後再下載 Excel
- 下載檔名自動生成（含日期時間），例如：數位金卡審核ai生成結果_20250803_142530.xlsx
  
---

## 🛠️ 技術架構
- **前端**：Streamlit
- **資料處理**：Pandas
- **Excel 匯出**：OpenPyXL

---

## 📂 專案結構
streamlit-app/
│
├── text_to_excel1+.py # 主程式 (Streamlit)
├── requirements.txt # 套件需求
└── README.md # 專案說明文件

---

## 🔧 安裝與本地執行
1. 下載專案：
   ```bash
   git clone https://github.com/ckped/json_to_excel_for_goldencard.git
   cd json_to_excel_for_goldencard
2.安裝套件:
   pip install -r requirements.txt
3.啟動streamlit:
   streamlit run text_to_excel1+.py
   

