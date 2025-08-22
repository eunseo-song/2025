import streamlit as st
import random

st.set_page_config(page_title="간호사 하루 체험", page_icon="👩‍⚕️", layout="centered")

st.markdown("""
# 👩‍⚕️ 간호사 하루 체험 시뮬레이션

당신은 병동에서 근무하는 간호사입니다. 올바른 판단을 내려 **환자들을 안전하게 돌볼 수 있을까요?** 🏥
""")

# 세션 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = 0

# 시뮬레이션 단계별 스토리
scenarios = [
    {
        "text": "아침 7시, 병동 근무가 시작됐습니다. 첫 번째로 무엇을 할까요?",
        "choices": {
            "환자들의 바이탈 사인(혈압, 맥박 등) 체크": 1,
            "의사 지시사항부터 확인": 2,
        },
    },
    {
        "text": "환자들의 바이탈을 체크했습니다. 한 환자의 혈압이 매우 높습니다. 어떻게 할까요?",
        "choices": {
            "즉시 담당 의사에게 보고": 3,
            "환자에게 물 한 잔 드리기": 4,
        },
    },
    {
        "text": "의사 지시사항을 확인했습니다. 오전 9시에 약물 투여가 필요하다고 적혀 있습니다. 지금 무엇을 할까요?",
        "choices": {
            "약물 준비를 미리 한다": 5,
            "잠시 쉬었다가 나중에 준비한다": 4,
        },
    },
    {
        "text": "적절하지 않은 선택으로 문제가 생겼습니다 😢. 하지만 경험을 통해 배우는 것도 중요하죠!",
        "choices": {},
    },
    {
        "text": "정확한 판단으로 환자를 잘 돌보았습니다! 👏 오늘 하루가 순조롭게 흘러갑니다.",
        "choices": {},
    },
    {
        "text": "약물을 준비하던 중, 갑자기 한 환자가 호흡곤란을 호소합니다! 응급상황입니다 🚨. 어떻게 할까요?",
        "choices": {
            "응급벨을 누르고 도움을 요청": 6,
            "혼자 해결하려고 시도": 3,
        },
    },
    {
        "text": "빠르게 응급벨을 눌러 의료팀이 도착했습니다. 환자는 무사히 안정을 찾았습니다 🙌. 이제 약물을 안전하게 투여합니다.",
        "choices": {
            "약물 투여를 신중하게 진행": 7,
        },
    },
    {
        "text": "약물을 정확히 투여했습니다 💉 환자는 안정을 찾고, 오늘 하루도 무사히 지나갑니다. 수고하셨습니다! 🎉",
        "choices": {},
    },
]

# 현재 단계 출력
scenario = scenarios[st.session_state.step]

st.markdown(f"""
<div style='padding:20px; background-color:#f0f9ff; border-radius:15px; border:1px solid #cce7ff;'>
<h3>{scenario['text']}</h3>
</div>
""", unsafe_allow_html=True)

# 선택지 버튼 생성
for choice, next_step in scenario["choices"].items():
    if st.button(choice, use_container_width=True):
        st.session_state.step = next_step
        st.rerun()

# 처음부터 다시 시작하기 버튼
if st.session_state.step > 0:
    if st.button("🔄 처음부터 다시 하기", type="primary"):
        st.session_state.step = 0
        st.rerun()

