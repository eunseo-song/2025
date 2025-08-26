import streamlit as st

# 앱 제목과 안내
st.set_page_config(page_title="응급처치 퀴즈 앱", page_icon="🩺", layout="centered")
st.title("🩺 응급처치 퀴즈 앱")
st.write("응급 상황에서 올바른 대응을 선택해 보세요! ✅")
st.write("각 문제 아래 '정답 확인' 버튼을 눌러 결과를 확인하세요.\n")

# 퀴즈 리스트 (문제 5개)
quizzes = [
    {
        "question": "출혈이 심할 때 가장 먼저 해야 할 일은?",
        "options": ["상처를 깨끗이 씻는다", "상처를 압박한다", "즉시 병원으로 간다", "약을 바른다"],
        "answer": "상처를 압박한다"
    },
    {
        "question": "화상을 입었을 때 올바른 초기 대응은?",
        "options": ["뜨거운 물로 씻는다", "차가운 물로 식힌다", "물집을 터뜨린다", "약을 바른다"],
        "answer": "차가운 물로 식힌다"
    },
    {
        "question": "심정지 환자를 발견했을 때 가장 먼저 해야 할 일은?",
        "options": ["심폐소생술 시작", "주변 안전 확인", "병원으로 이동", "음식 제공"],
        "answer": "주변 안전 확인"
    },
    {
        "question": "코피가 날 때 올바른 처치는?",
        "options": ["머리를 뒤로 젖힌다", "머리를 앞으로 숙이고 압박한다", "세게 코를 풀어준다", "즉시 얼음찜질 한다"],
        "answer": "머리를 앞으로 숙이고 압박한다"
    },
    {
        "question": "골절이 의심될 때 가장 먼저 해야 할 일은?",
        "options": ["관절을 움직인다", "부목으로 고정한다", "강하게 마사지한다", "즉시 뼈를 맞춘다"],
        "answer": "부목으로 고정한다"
    }
]

# 점수 초기화
if "score" not in st.session_state:
    st.session_state.score = 0

# 각 문제 표시
for i, quiz in enumerate(quizzes):
    st.subheader(f"문제 {i+1}")
    user_answer = st.radio(quiz["question"], quiz["options"], key=i)
    
    if st.button(f"정답 확인 {i+1}", key=f"btn{i}"):
        if user_answer == quiz["answer"]:
            st.success("✅ 정답입니다!")
            st.session_state.score += 1
        else:
            st.error(f"❌ 틀렸습니다. 정답은 '{quiz['answer']}' 입니다.")

# 화려한 최종 점수 표시
st.markdown("---")
st.markdown(
    f"""
    <div style="
        background-color: #d1f7c4;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 2px 2px 12px #aaa;
    ">
        <h1 style='color: #27ae60; font-size:60px;'>🏆 최종 점수</h1>
        <h2 style='color: #2c3e50; font-size:50px;'>{st.session_state.score} / {len(quizzes)}</h2>
        <p style='font-size:24px;'>응급처치 실력을 확인했습니다!</p>
    </div>
    """,
    unsafe_allow_html=True
)
