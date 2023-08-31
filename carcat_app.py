import streamlit as st

number = st.number_input('Insérer le code article', format="%i")
st.write('La code article est ', number)
