import streamlit as st
import pandas as pd
import json
import io
from datetime import datetime

# === 固定欄位名稱 (寫死) ===
EXCEL_COLUMNS = [
    '英文名字＋英文姓氏',
    '中文姓名',
    '性別',
    '國籍',
    '學歷＋學校＋科系',
    '申請資格條件',
    '出生日期',
    '護照號碼',
    '子領域',
    '現職公司',
    '現職職稱',
    '現職是否為主管',
    '其他工作經歷',
    '教育背景(學校)',
    '教育背景(系所)',
    '工作經歷',
    '產業實績專長',
    '求學期間',
    '畢業年份',
    '總工作年資',
    '審查意見或備注',
    '勞動部檢核結果',
    '是否為轉自其他領域',
    '第1次申請',
    '年齡',
    '月薪'
]



# === 清理輸入文字的函式 ===
def clean_json_text(raw_text):
    cleaned = raw_text.strip().replace("\ufeff", "")  # 去除空白與 BOM
    warning = "NotebookLM 提供的資訊未必正確，請查證回覆內容。"
    if warning in cleaned:
        cleaned = cleaned.split(warning)[0].strip()
    # 自動補外層中括號
    if not cleaned.startswith("["):
        if cleaned.startswith("{") and cleaned.endswith("}"):
            cleaned = "[" + cleaned + "]"
    return cleaned

# === JSON 轉 Excel 函式 ===
def json_to_excel(json_text):
    try:
        data = json.loads(json_text)
        if isinstance(data, dict):  # 若為單筆資料包裝成列表
            data = [data]
        df = pd.DataFrame(data)
        # 自動補上缺失欄位，或過濾多餘欄位
        for col in EXCEL_COLUMNS:
            if col not in df.columns:
                df[col] = ""
        df = df[EXCEL_COLUMNS]
        output = io.BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        return df, output, None
    except Exception as e:
        return None, None, str(e)

# === Streamlit UI ===
st.set_page_config(page_title="TXT(JSON) 轉 Excel 工具", page_icon="📄", layout="centered")

st.title("📄 TXT(JSON) 轉 Excel 工具")
st.caption("此工具會自動清理空行與符號，並驗證 JSON 格式，支援上傳或貼上文字。")

tab1, tab2 = st.tabs(["📂 上傳 TXT 檔案", "📝 貼上文字內容"])

# --- 功能1：自訂中文上傳區 ---
with tab1:
    
    uploaded_file = st.file_uploader("選擇檔案", type=["txt"], label_visibility="collapsed")

    if uploaded_file:
        raw_text = uploaded_file.read().decode("utf-8", errors="ignore")
        cleaned_text = clean_json_text(raw_text)
        df, excel_file, error = json_to_excel(cleaned_text)
        if error:
            st.error(f"❌ 解析失敗：{error}")
        else:
            st.success("✅ 轉換成功！請先預覽資料後再下載：")
            st.dataframe(df, use_container_width=True)  # 預覽表格
            st.download_button(
                label="📥 下載 Excel 檔案",
                data=excel_file,
                file_name='數位金卡審核ai生成結果'+datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="download_file_tab1"
            )

# --- 功能2：貼上文字內容 ---
with tab2:
    text_input = st.text_area("請貼上 JSON 格式的 TXT 文字內容", height=300, placeholder="請將 JSON 文字貼在這裡...")
    if st.button("轉換為 Excel"):
        cleaned_text = clean_json_text(text_input)
        df, excel_file, error = json_to_excel(cleaned_text)
        if error:
            st.error(f"❌ 解析失敗：{error}")
        else:
            st.success("✅ 轉換成功！請先預覽資料後再下載：")
            st.dataframe(df, use_container_width=True)
            st.download_button(
                label="📥 下載 Excel 檔案",
                data=excel_file,
                file_name='數位金卡審核ai生成結果'+datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="download_file_tab2"
                
            )
