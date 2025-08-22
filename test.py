import streamlit as st
import random

st.set_page_config(page_title="응급처치 퀴즈", page_icon="⛑️", layout="centered")

# ===================== 스타일 =====================
CUSTOM_CSS = """
<style>
    .main > div {max-width: 820px;}
    .quiz-card {
        padding: 20px; border-radius: 18px; border: 1px solid #e6f0ff;
        background: linear-gradient(180deg, #f7fbff 0%, #ffffff 100%);
        box-shadow: 0 8px 24px rgba(30, 64, 175, 0.08);
    }
    .badge {display:inline-block;padding:6px 10px;border-radius:999px;background:#eef2ff;color:#3730a3;font-weight:600;font-size:12px;border:1px solid #c7d2fe}
    .snowflake {
        color: #9dd9ff;
        font-size: 24px;
        position: fixed;
        top: -10px;
        animation-name: fall;
        animation-duration: 10s;
        animation-iteration-count: infinite;
    }
    @keyframes fall {
        0% {transform: translateY(0); opacity: 1;}
        100% {transform: translateY(100vh); opacity: 0;}
    }
    .firework {
        position: fixed;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: radial-gradient(circle, #ff0, #f00, transparent);
        animation: explode 1.5s ease-out forwards;
    }
    @keyframes explode {
        0% {transform: scale(0.2); opacity: 1;}
        80% {transform: scale(2); opacity: 1;}
        100% {transform: scale(3); opacity: 0;}
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# 눈송이 효과
snowflakes = "".join([
    f"<div class='snowflake' style='left:{random.randint(0,100)}%; animation-delay:{random.random()*5}s;'>❄️</div>"
    for _ in range(15)
])
st.markdown(snowflakes, unsafe_allow_html=True)

# 불꽃놀이 효과 (정답률 100%일 때)
def fireworks():
    fire_html = "".join([
        f"<div class='firework' style='top:{random.randint(10,80)}%; left:{random.randint(10,90)}%; animation-delay:{random.random()}s;'></div>"
        for _ in range(20)
    ])
    st.markdown(fire_html, unsafe_allow_html=True)
    # 축하 사운드 삽입
    st.audio('https://www.soundjay.com/human/applause-01.mp3', format='audio/mp3', start_time=0)

# ===================== 타이틀 =====================
st.title("⛑️ 응급처치 퀴즈 앱")
st.markdown("""
간단한 퀴즈를 풀면서 **응급처치 지식**을 확인해보세요! 발표 모드에서는 청중과 함께 정답을 토론한 뒤 제출하세요.
""")

# ===================== 사이드바 =====================
st.sidebar.header("🎤 발표 모드")
present_mode = st.sidebar.toggle("발표 모드 활성화", value=True)
randomize = st.sidebar.toggle("보기 순서 섞기", value=True)
show_tips = st.sidebar.checkbox("해설 요약 띄우기", value=True)

st.sidebar.divider()
st.sidebar.caption("*의료 상황에 따라 실제 행동은 기관 가이드라인과 전문가 지시에 따르세요.*")

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
    {"question": "기도 막힘(성인)에서 기침이 가능하면?",
     "choices": ["즉시 등압박 5회", "하임리히법 시행", "기침 유도하며 관찰"],
     "answer": "기침 유도하며 관찰",
     "explanation": "효과적인 기침이 가능하면 스스로 배출하도록 격려하고 관찰합니다. 기침 불가·청색증 시 등압박/복부밀치기."},
    {"question": "의식 없는 사람을 발견했다. 첫 순서는?",
     "choices": ["기도열기", "의식·호흡 확인 및 119 신고/자동심장충격기 요청", "회복자세"],
     "answer": "의식·호흡 확인 및 119 신고/자동심장충격기 요청",
     "explanation": "반응·호흡 확인 → 즉시 119 신고 및 AED 요청 → 필요 시 CPR 시작."},
]

# ===================== 상태 =====================
if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0
    st.session_state.score = 0
    st.session_state.revealed = False
    st.session_state.selected = None

step = st.session_state.quiz_step
score = st.session_state.score
total = len(quizzes)
progress_ratio = step / total

# 상단 메트릭 & 진행바
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("진행률", f"{int(progress_ratio*100)}%")
with c2:
    st.metric("점수", f"{score} / {total}")
with c3:
    remain = total - step
    st.metric("남은 문제", remain)

st.progress(progress_ratio)

# ===================== 본문 =====================
if step < total:
    q = quizzes[step]
    st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
    st.subheader(f"문제 {step+1}. {q['question']}")

    choices = q["choices"][:]
    if randomize:
        random.shuffle(choices)

    st.session_state.selected = st.radio("답을 선택하세요:", choices, index=None, key=f"radio_{step}")

    b1, b2 = st.columns([1,1])
    with b1:
        if st.button("제출하기", type="primary", use_container_width=True, disabled=st.session_state.revealed or st.session_state.selected is None):
            st.session_state.revealed = True
            if st.session_state.selected == q["answer"]:
                st.session_state.score += 1
    with b2:
        if st.button("건너뛰기", use_container_width=True, disabled=st.session_state.revealed):
            st.session_state.revealed = True

    if st.session_state.revealed:
        if st.session_state.selected == q["answer"]:
            st.success("✅ 정답입니다! 멋져요.")
        elif st.session_state.selected is None:
            st.warning("⚠️ 건너뛰었습니다.")
        else:
            st.error("❌ 오답입니다.")
        if show_tips:
            st.info(f"해설: {q['explanation']}")

        if st.button("다음 문제 ▶", type="secondary"):
            st.session_state.quiz_step += 1
            st.session_state.revealed = False
            st.session_state.selected = None
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.balloons()
    st.success(f"퀴즈 완료! 최종 점수: {score} / {total}")
    pct = int((score/total)*100)
    st.metric("정답률", f"{pct}%")

    if pct == 100:
        fireworks()

    b1, b2 = st.columns(2)
    with b1:
        if st.button("🔄 다시 시작하기", type="primary", use_container_width=True):
            st.session_state.quiz_step = 0
            st.session_state.score = 0
            st.session_state.revealed = False
            st.session_state.selected = None
            st.rerun()
    with b2:
        st.caption("❄️ 눈송이, 🎆 불꽃놀이, 🎶 축하 사운드 효과가 활성화되었습니다.")
