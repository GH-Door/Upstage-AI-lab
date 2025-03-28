import streamlit as st
import json
from datetime import datetime
import os

DATA_FILE = "todo.json"

# 파일이 없으면 기본 구조 생성
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({}, f)

# 할 일 저장 함수
def save_task(date, task):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    if date in data:
        data[date].append(task)
    else:
        data[date] = [task]

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 오늘 할 일 불러오기
def get_today_tasks():
    today = datetime.now().strftime("%Y-%m-%d")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return today, data.get(today, [])

# Streamlit 앱 UI
st.title("📅 오늘의 할 일 알리미")

st.subheader("✅ 할 일 추가")
col1, col2 = st.columns(2)
with col1:
    date_input = st.date_input("날짜 선택", datetime.now())
    date_str = date_input.strftime("%Y-%m-%d")
with col2:
    task_input = st.text_input("할 일 내용 입력")

if st.button("💾 저장하기") and task_input:
    save_task(date_str, task_input)
    st.success(f"'{date_str}' 할 일이 저장되었습니다!")

st.divider()

st.subheader("📌 오늘의 할 일")
today, today_tasks = get_today_tasks()

if today_tasks:
    for task in today_tasks:
        st.write(f"🔹 {task}")
else:
    st.info("오늘 할 일이 없습니다!")