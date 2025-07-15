import streamlit as st

st.title("BMI 계산기")
l = st.number_input("키(cm)", value=0)
w = st.number_input("몸무게(kg)", value=0)

if st.button("계산하기"):
    try:
        r = round(w/((l/100)**2), 2)
        st.write(f"BMI: {r}")
        st.write("\n    저체중            정상        과체중        비만                고도비만")
        st.write("             18.5               23      25                  30")
        st.write("              !                 !       !                   !                   ")
        st.write("="*80)
        i = round((r-15)*4, 0)
        if i > 80:
            i = 78
        st.write(" "*i,"^")

        if bmi <= 18:
            st.write("저체중 입니다.")
        if bmi > 18 and bmi <= 23:
            st.write("정상 입니다.")       
        if bmi > 23 and bmi <= 25:
            st.write("과체중 입니다.")       
        if bmi > 25 and bmi <= 30:
            st.write("비만 입니다.")
        if bmi > 30:
            st.write("고도비만 입니다.")
    except Exception as e:
        st.error("오류 발생")

      

