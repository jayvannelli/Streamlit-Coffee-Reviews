import streamlit as st
from src.data import get_analysis_df


def main():
    st.title("Coffee Reviews | Streamlit | Kaggle")

    analysis_df = get_analysis_df()

    st.dataframe(analysis_df)
    roast_selection = st.selectbox("Select roast:", options=analysis_df['roast'].unique())


if __name__ == "__main__":
    main()
