import streamlit as st
from src.data import get_data
from src.utils import remove_extra_rows


def main():
    st.title("Roast Page")

    coffee_reviews = get_data()
    roast_selection = st.selectbox("Select roast:", options=coffee_reviews["roast"].unique())

    st.write(roast_selection)

    cleaned_coffee_reviews = remove_extra_rows(coffee_reviews)

    low_rating, high_rating = st.select_slider(label="Select rating:",
                                               options=cleaned_coffee_reviews['rating'].sort_values().unique(),
                                               value=(
                                                   cleaned_coffee_reviews['rating'].min(),
                                                   cleaned_coffee_reviews['rating'].max()
                                               ))

    st.write(low_rating, high_rating)
    st.dataframe(cleaned_coffee_reviews)


if __name__ == "__main__":
    main()
