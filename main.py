import streamlit as st
import pandas as pd

st.set_page_config(page_title="sewak app")
file = st.file_uploader("Upload CSV", type="csv")

if file:
    df=pd.read_csv(file)
    st.write(df.head())
    st.bar_chart(df.iloc[8])
else:
    st.write("Please Upload file to see magic")
