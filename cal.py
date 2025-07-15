import streamlit as st

st.title("BMI 계산기")
l = st.number_input("키(cm)", value=0)
w = st.number_input("몸무게(kg)", value=0)

if st.button("계산하기"):
    try:
        l /= 100
        l *= l
        r = round(w/l, 2)
        st.write(f"BMI: {r}")
        print("\n    저체중            정상        과체중        비만                고도비만")
        print("             18.5               23      25                  30")
        print("              !                 !       !                   !                   ")
        print("="*80)
        print(" "*i,"^")

        if bmi <= 18:
            print("저체중 입니다.")
        
        if bmi > 18 and bmi <= 23:
            print("정상 입니다.")
            
        if bmi > 23 and bmi <= 25:
            print("과체중 입니다.")
            
        if bmi > 25 and bmi <= 30:
            print("비만 입니다.")
        
        if bmi > 30:
            print("고도비만 입니다.")
    except Exception as e:
        st.error("오류 발생")

      

