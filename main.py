import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 궁합 추천기 💖", page_icon="🌟", layout="wide")

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

# CSS 꾸미기
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffafbd, #ffc3a0);
        color: white;
        font-family: "Comic Sans MS", cursive, sans-serif;
    }
    .title {
        text-align: center;
        font-size: 60px;
        color: #ff4d94;
        text-shadow: 3px 3px 5px #fff, 0 0 30px #ff0080;
        animation: glow 1.5s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #ff80bf, 0 0 20px #ff33cc, 0 0 30px #ff1a8c; }
        to { text-shadow: 0 0 20px #ff66cc, 0 0 30px #ff3399, 0 0 40px #ff0066; }
    }
    .subtitle {
        text-align: center;
        font-size: 22px;
        color: #fff8dc;
        margin-bottom: 30px;
    }
    .result-box {
        background: rgba(255,255,255,0.2);
        border-radius: 20px;
        padding: 20px;
        margin-top: 20px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        box-shadow: 0px 0px 20px #ff99cc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목
st.markdown("<div class='title'>✨ MBTI 궁합 추천기 💕</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>🌈 당신의 MBTI를 선택하면 소울메이트를 알려드려요! 💖</div>", unsafe_allow_html=True)

# 선택 박스
user_mbti = st.selectbox("👇 나의 MBTI를 선택해주세요!", mbti_types, index=None)

# 결과 출력
if user_mbti:
    matches = compatibility.get(user_mbti, [])
    if matches:
        st.balloons()  # 풍선 이펙트 🎈
        st.snow()      # 눈 내리는 효과 ❄️
        st.markdown(f"<div class='result-box'>💘 {user_mbti}와 찰떡궁합 MBTI는 👉 {' ✨ '.join(matches)} 💘</div>", unsafe_allow_html=True)
    else:
        st.error("😢 아직 데이터가 없어요. 곧 업데이트될 예정이에요!")
