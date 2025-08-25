# ===================== 상태 초기화 =====================
if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0
    st.session_state.score = 0
    st.session_state.revealed = False
    st.session_state.selected = None
    st.session_state.shuffled_choices = {}   # 문제별 보기 순서 저장용 딕셔너리

# 현재 문제
step = st.session_state.quiz_step
q = quizzes[step]

# ===================== 보기 순서 섞기 =====================
if step not in st.session_state.shuffled_choices:
    choices = q["choices"][:]
    if randomize:
        random.shuffle(choices)
    st.session_state.shuffled_choices[step] = choices

choices = st.session_state.shuffled_choices[step]

# ===================== 답 선택 =====================
st.session_state.selected = st.radio(
    "답을 선택하세요:",
    choices,
    index=None,
    key=f"radio_{step}"
)
