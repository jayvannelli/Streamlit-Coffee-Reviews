import streamlit as st
import pandas as pd


@st.cache(allow_output_mutation=True)
def get_analysis_df():
    return pd.read_csv("data/coffee_analysis.csv")
