import streamlit as st
import pandas as pd

name = 'Catalogue_Carrick_20230831.xlsx'
df = pd.read_excel('./data/'+name, index_col=0)
st.write('Nombre total d articles est ', len(df))

number = st.number_input('Insérer le code article', step=1, format="%i")
if st.button('Find'):
    filtered_df = df.loc[df['code-article']==str(number)]
    st.table(filtered_df.T)
else:
    st.write('Press find button')





