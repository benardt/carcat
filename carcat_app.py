import streamlit as st
import pandas as pd

name = 'Catalogue_Carrick_20230831.xlsx'
df = pd.read_excel('./data/'+name, index_col=0)
st.write('Nombre total d articles est ', len(df))

number = st.number_input('Insérer le code article', step=1, format="%i")
if st.button('Find'):
    filtered_df = df.loc[df['code-article']==str(number)]
    st.write('La code article est ', number)
    st.table(filtered_df.T)
    st.write('La prix article est ', filtered_df['prix'].values[0])
    st.write('Le nom  article est ', filtered_df['title'].values[0])
    st.write('Le variant      est ', filtered_df['variant-name'].values[0] + " " + filtered_df['variant-option'].values[0])
else:
    st.write('Press find button')





