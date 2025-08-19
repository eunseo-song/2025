import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 궁합 추천기 💖", page_icon="✨", layout="centered")

# MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 궁합 데이터 (샘플)
compatibility = {
    "INTJ": ["💘 ENFP", "🌈 ENTP"],
    "INTP": ["💞 ENTJ", "✨ ESTJ"],
    "ENTJ": ["🌟 INTP", "💖 INFJ"],
    "ENTP": ["🔥 INFJ", "💘 INTJ"],
    "INFJ": ["🌷 ENFP", "🌈 ENTP"],
    "INFP": ["💎 ENFJ", "💫 ENTJ"],
    "ENFJ": ["🌼 INFP", "🌟 ISFP"],
    "ENFP": ["💖 INFJ", "💘 INTJ"],
    "ISTJ": ["🌸 ESFP", "💛 ESTP"],
    "ISFJ": ["🌻 ESFP", "💚 ESTP"],
    "ESTJ": ["🌟 INTP", "💞 ISFP"],
    "ESFJ": ["💖 ISFP", "🌷 INFP"],
    "ISTP": ["🔥 ESFJ", "💎 ENFJ"],
    "ISFP": ["💘 ESFJ", "💫 ENFJ"],
    "ESTP": ["🌈 ISFJ", "✨ INFJ"],
    "ESFP": ["💎 ISTJ", "💖 INTJ"]
}

# 헤더
st.markdown(
    """
    <h1 style='text-align: center; color: #FF69B4;'>
        ✨ MBTI 궁합 추천기 💕
    </h1>
    <p style='text-align: center; font-size: 18px;'>
        당신의 MBTI를 선택하면 🌈 잘 맞는 MBTI를 추천해드려요!  
        <br> 소울메이트를 찾아보세요 💘
    </p>
    """,
    unsafe_allow_html=True
)

# 선택 박스
user_mbti = st.selectbox("👇 나의 MBTI를 골라주세요!", mbti_types, index=None)

# 추천 결과 출력
if user_mbti:
    st.markdown("---")
    st.subheader(f"💖 {user_mbti} 와(과) 잘 맞는 MBTI는...")
    matches = compatibility.get(user_mbti, [])
    if matches:
        st.success(" ✨ ".join(matches))
        st.balloons()  # 풍선 효과 🎈
    else:
        st.warning("😢 아직 데이터가 없어요. 곧 추가될 예정이에요!")
