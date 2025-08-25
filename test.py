import streamlit as st

st.title("BMI 건강 체크 & 퀴즈 🩺")

# BMI 계산
height = st.number_input("키(cm):", 50, 250)
weight = st.number_input("몸무게(kg):", 10, 200)

if st.button("BMI 계산"):
    bmi = weight / ((height/100)**2)
    st.write(f"당신의 BMI: {bmi:.2f}")
    if bmi < 18.5:
        st.warning("저체중입니다")
    elif bmi < 24.9:
        st.success("정상 체중입니다")
    elif bmi < 29.9:
        st.warning("과체중입니다")
    else:
        st.error("비만입니다")

    # 간단한 의료 퀴즈
    st.subheader("건강 퀴즈 🎯")
    answer = st.radio("BMI가 25 이상이면 어떤 상태일까요?", 
                      ["저체중", "정상", "과체중", "비만"])
    if st.button("정답 확인"):
        if answer == "과체중" or answer == "비만":
            st.success("정답! BMI가 높으면 건강 위험이 증가할 수 있어요.")
        else:
            st.error("틀렸어요. BMI 25 이상은 과체중 혹은 비만에 해당합니다.")
