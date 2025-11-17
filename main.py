import streamlit as st
import random

st.set_page_config(page_title="랜덤 숫자 추첨기", layout="wide")

st.title("🎉 랜덤 숫자 추첨기")
st.write("원하는 범위를 설정하고, 제외할 숫자를 선택하고, 중복 없는 여러 개 추첨도 가능합니다!")

# ------------------------------
# 범위 입력
# ------------------------------
st.subheader("1️⃣ 범위 설정")

col1, col2 = st.columns(2)
with col1:
    min_value = st.number_input("🔢 최소 숫자", min_value=0, value=1)
with col2:
    max_value = st.number_input("🔢 최대 숫자", min_value=0, value=50)

if max_value < min_value:
    st.error("❗ 최대값은 최소값보다 크거나 같아야 합니다.")
    st.stop()

# ------------------------------
# 제외할 숫자 입력
# ------------------------------
st.subheader("2️⃣ 제외할 숫자")

exclude_input = st.text_input("🚫 제외할 숫자 입력 (쉼표로 구분)", placeholder="예: 5, 7, 13")

def parse_exclusions(text):
    if not text.strip():
        return []
    try:
        return list(set([int(x.strip()) for x in text.split(",") if x.strip().isdigit()]))
    except:
        return None

exclude_numbers = parse_exclusions(exclude_input)
if exclude_numbers is None:
    st.error("❗ 제외 숫자는 정수만 입력해야 합니다.")
    st.stop()

# ------------------------------
# 중복 없이 추첨할 숫자 개수
# ------------------------------
st.subheader("3️⃣ 추첨 개수")

draw_count = st.number_input("🎯 추첨할 개수 (중복 없음)", min_value=1, value=1)

# ------------------------------
# 실제 추첨 가능한 숫자 계산
# ------------------------------
available_numbers = [n for n in range(min_value, max_value + 1) if n not in exclude_numbers]

st.write("📌 **추첨 가능한 숫자 목록:**")
st.write(available_numbers)

if len(available_numbers) == 0:
    st.error("❗ 가능한 숫자가 없습니다. 범위 또는 제외 설정을 변경하세요.")
    st.stop()

if draw_count > len(available_numbers):
    st.error(f"❗ 추첨 개수({draw_count})가 가능한 숫자 개수({len(available_numbers)})보다 많습니다.")
    st.stop()

# ------------------------------
# 추첨 실행
# ------------------------------
st.subheader("4️⃣ 추첨 시작")

if st.button("🎉 숫자 추첨하기!"):
    result = random.sample(available_numbers, draw_count)
    st.success(f"🎯 추첨 결과: {result}")
