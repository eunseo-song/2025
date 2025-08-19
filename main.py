import streamlit as st

# MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 궁합 데이터 (예시: 실제 심리학적 궁합과 다를 수 있음)
compatibility = {
    "INTJ": ["ENFP", "ENTP"],
    "INTP": ["ENTJ", "ESTJ"],
    "ENTJ": ["INTP", "INFJ"],
    "ENTP": ["INFJ", "INTJ"],
    "INFJ": ["ENFP", "ENTP"],
    "INFP": ["ENFJ", "ENTJ"],
    "ENFJ": ["INFP", "ISFP"],
    "ENFP": ["INFJ", "INTJ"],
    "ISTJ": ["ESFP", "ESTP"],
    "ISFJ": ["ESFP", "ESTP"],
    "ESTJ": ["INTP", "ISFP"],
    "ESFJ": ["ISFP", "INFP"],
    "ISTP": ["ESFJ", "ENFJ"],
    "ISFP": ["ESFJ", "ENFJ"],
    "ESTP": ["ISFJ", "INFJ"],
    "ESFP": ["ISTJ", "INTJ"]
}

# Streamlit 앱 시작
st.title("✨ MBTI 궁합 추천기 ✨")
st.write("당신의 MBTI를 선택하면 잘 맞는 MBTI를 추천해드려요!")

# 사용자 MBTI 선택
user_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

if user_mbti:
    st.subheader(f"✅ {user_mbti}와 잘 맞는 MBTI는...")
    matches = compatibility.get(user_mbti, [])
    if matches:
        st.success(", ".join(matches))
    else:
        st.warning("아직 데이터가 없어요 😢")
