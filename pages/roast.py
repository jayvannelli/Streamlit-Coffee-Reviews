import streamlit as st
from src.data import get_data


def main():
    st.title("Roast Page")

    coffee_reviews = get_data()

    roast_selection = st.selectbox("Select roast:", options=coffee_reviews['roast'].unique())
    st.write(roast_selection)
    st.dataframe(coffee_reviews)


if __name__ == "__main__":
    main()