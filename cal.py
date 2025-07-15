import streamlit as st

st.title("Calculator")

n1 = 0
n2 = 0

if st.button("1"):
  n1 = n1*10+1
if st.button("2"):
  n1 = n1*10+2
if st.button("3"):
  n1 = n1*10+3
if st.button("4"):
  n1 = n1*10+4
if st.button("5"):
  n1 = n1*10+5
if st.button("6"):
  n1 = n1*10+6
if st.button("7"):
  n1 = n1*10+7
if st.button("8"):
  n1 = n1*10+8
if st.button("9"):
  n1 = n1*10+9
if st.button("+"):
  o = 1
if st.button("-"):
  o = 2
if st.button("*"):
  o = 3
if st.button("/"):
  o = 4


if o == 1:
  r=n1+n2
if o == 2:
  r=n1-n2
if o == 3:
  r=n1*n2
if o == 4:
  r=n1/n2
  
st.write(f"Result: {r}")
      

