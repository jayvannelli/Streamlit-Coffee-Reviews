import streamlit as st
from src.data import get_data


def main():
    st.title("Roaster Page")

    coffee_reviews = get_data()

    roaster_selection = st.selectbox("Select roaster:", options=coffee_reviews["roaster"].unique())

    st.write(roaster_selection)
    st.dataframe(coffee_reviews)


if __name__ == "__main__":
    main()
