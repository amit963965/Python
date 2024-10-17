import streamlit as st
st.title('Loan Application App')
l=st.number_input('enter your ammount loan')
s=st.number_input('enter your salary')
c=st.number_input('enter your credit score')
if s>=40000 and c>=500:
    st.write('congrats')
else:
    st.write("we are sorry")
