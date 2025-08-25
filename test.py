import streamlit as st

# 페이지 설정
st.set_page_config(page_title="응급처치 퀴즈", page_icon="⛑️", layout="centered")

st.title("⛑️ 응급처치 퀴즈")
st.write("모든 문제를 풀고 마지막에 결과를 확인하세요!")

# ===================== 퀴즈 데이터 =====================
quizzes = [
    {"question": "심폐소생술(CPR)에서 성인 가슴 압박 깊이는?",
     "choices": ["약 2cm", "약 5cm", "약 8cm"],
     "answer": "약 5cm",
     "explanation": "성인은 약 5cm(2인치) 깊이, 분당 100~120회 속도로 강하고 빠르게 압박합니다."},
    {"question": "심한 출혈이 있을 때 가장 먼저 할 일은?",
     "choices": ["지혈을 위해 직접 압박", "환자를 즉시 이동", "물을 마시게 함"],
     "answer": "지혈을 위해 직접 압박",
     "explanation": "가장 먼저 직접 압박으로 지혈합니다. 필요 시 지압점·지혈대는 지침에 따라 사용합니다."},
    {"question": "화상 응급처치로 올바른 것은?",
     "choices": ["얼음을 대기", "흐르는 차가운 물에 10~20분 식히기", "수포를 터뜨리기"],
     "answer": "흐르는 차가운 물에 10~20분 식히기",
     "explanation": "화상 부위는 즉시 미지근~차가운 물로 10~20분 냉각, 얼음·연고·치약은 피합니다."},
]

# ===================== 상태 =====================
if "submitted" not in st.session_state:
    st.session_state.submitted = False
    st.session_state.answers = {}

# ===================== 문제 출력 =====================
st.header("문제 풀기")

for idx, q in enumerate(quizzes):
    st.subheader(f"문제 {idx+1}. {q['question']}")
    choice = st.radio(
        "답을 고르세요:",
        q["choices"],
        key=f"q_{idx}",
        index=None
    )
    if choice:
        st.session_state.answers[idx] = choice
    st.markdown("---")

# ===================== 결과 버튼 =====================
if not st.session_state.submitted:
    if st.button("결과 확인", type="primary"):
        st.session_state.submitted = True
        st.rerun()

# ===================== 결과 화면 =====================
if st.session_state.submitted:
    st.header("📊 결과")
    score = 0

    for idx, q in enumerate(quizzes):
        user_ans = st.session_state.answers.get(idx, "선택 안 함")
        correct = (user_ans == q["answer"])
        if correct:
            score += 1
            st.success(f"문제 {idx+1}: 정답 ✅ ({user_ans})")
        else:
            st.error(f"문제 {idx+1}: 오답 ❌ (내 답: {user_ans})")
            st.info(f"정답: {q['answer']}")

        st.caption(f"💡 해설: {q['explanation']}")
        st.markdown("---")

    st.subheader(f"최종 점수: {score} / {len(quizzes)}")

    if st.button("🔄 다시 풀기"):
        st.session_state.clear()
        st.rerun()
