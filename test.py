import streamlit as st

# 페이지 설정
st.set_page_config(page_title="응급처치 퀴즈", page_icon="⛑️", layout="centered")

# ===================== CSS =====================
CUSTOM_CSS = """
<style>
    .main > div {max-width: 820px;}
    .quiz-card {
        padding: 20px; border-radius: 18px; border: 1px solid #e6f0ff;
        background: linear-gradient(180deg, #f7fbff 0%, #ffffff 100%);
        box-shadow: 0 8px 24px rgba(30, 64, 175, 0.08);
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

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

total = len(quizzes)

# ===================== 상태 =====================
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.answers = {}  # 사용자가 고른 답

step = st.session_state.step

# ===================== 현재 문제 =====================
if step < total:
    q = quizzes[step]

    # 카드
    st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
    st.subheader(f"문제 {step+1}. {q['question']}")

    # 이전 선택 복원
    prev_answer = st.session_state.answers.get(step, None)
    selected = st.radio("답을 선택하세요:", q["choices"],
                        index=q["choices"].index(prev_answer) if prev_answer in q["choices"] else None,
                        key=f"radio_{step}")

    # 선택 저장
    if selected:
        st.session_state.answers[step] = selected

    # 버튼
    col1, col2 = st.columns(2)
    with col1:
        if st.button("제출하기", type="primary", use_container_width=True):
            if step not in st.session_state.answers:
                st.warning("⚠️ 답을 선택하지 않았습니다. 건너뜀으로 처리됩니다.")
            else:
                if st.session_state.answers[step] == q["answer"]:
                    st.session_state.score += 1
                    st.success("✅ 정답입니다!")
                else:
                    st.error(f"❌ 오답입니다. 정답: {q['answer']}")
                st.info(f"해설: {q['explanation']}")

            st.session_state.step += 1
            st.rerun()

    with col2:
        if st.button("건너뛰기", use_container_width=True):
            st.session_state.step += 1
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ===================== 퀴즈 완료 =====================
else:
    st.success(f"퀴즈 완료! 점수: {st.session_state.score} / {total}")

    # 복습
    st.subheader("📘 복습하기")
    for i, q in enumerate(quizzes):
        user_ans = st.session_state.answers.get(i, "선택 안 함")
        result = "⭕" if user_ans == q["answer"] else "❌"
        st.markdown(f"**문제 {i+1}. {q['question']}**")
        st.write(f"- 내 답: {user_ans} {result}")
        st.write(f"- 정답: {q['answer']}")
        st.caption(f"해설: {q['explanation']}")
        st.divider()

    if st.button("🔄 다시 시작하기", type="primary"):
        st.session_state.clear()
        st.rerun()
