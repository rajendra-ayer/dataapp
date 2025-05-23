import streamlit as st
import pandas as pd

st.set_page_config(page_title="sewak app")


file=pd.read_csv("data/amazon.csv")

st.write("Hello All")

st.write(file)