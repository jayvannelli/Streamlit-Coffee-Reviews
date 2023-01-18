import streamlit as st
from src.data import get_data


def main():
    st.title("Country Page")

    coffee_reviews = get_data()
    country_selection = st.selectbox("Select country:", options=coffee_reviews["loc_country"].unique())

    st.write(country_selection)
    st.dataframe(coffee_reviews)


if __name__ == "__main__":
    main()
