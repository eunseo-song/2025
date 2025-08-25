# ===================== 상태 초기화 =====================
if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0
    st.session_state.score = 0
    st.session_state.revealed = False
    st.session_state.selected = {}
    st.session_state.shuffled_choices = {}

step = st.session_state.quiz_step
q = quizzes[step]

# ===================== 보기 순서 (한 번만 섞기) =====================
if step not in st.session_state.shuffled_choices:
    choices = q["choices"][:]
    if randomize:
        random.shuffle(choices)
    st.session_state.shuffled_choices[step] = choices

choices = st.session_state.shuffled_choices[step]

# ===================== 답 선택 =====================
selected = st.radio(
    "답을 선택하세요:",
    choices,
    index=None if step not in st.session_state.selected else choices.index(st.session_state.selected[step]),
    key=f"radio_{step}"
)

if selected:
    st.session_state.selected[step] = selected  # 선택값 저장
