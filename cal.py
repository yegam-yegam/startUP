import streamlit as st

st.title("BMI 계산기")
l = st.number_input("키(cm)", value=0)
w = st.number_input("몸무게(kg)", value=0)
if st.button("계산하기"):
    try:
        l /= 100
        l *= l
        r = w/l
        st.write(f"BMI: {r}")
    except Exception as e:
        st.error("오류 발생")

      

