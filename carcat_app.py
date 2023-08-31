import streamlit as st
import pandas as pd

name = 'Catalogue_Carrick_20230831.xlsx'

df = pd.read_excel('./data/'+name, index_col=0)

number = st.number_input('Insérer le code article', step=1, format="%i")
st.write('La code article est ', number)
st.write('Nombre total d articles : ', len(df))
