import streamlit as st

st.title("BMI 계산기")
l = st.number_input("키(cm)", value=1)
w = st.number_input("몸무게(kg)", value=1)
l /= 100
l *= l
r = w/l
st.write(f"BMI: {r}")
      

