import streamlit as st
from src.data import get_data


def main():
    st.title("Country Page")

    coffee_reviews = get_data()

    left_column, right_column = st.columns(2)
    with left_column:
        origin_country = st.selectbox(label="Select origin country of beans:",
                                      options=coffee_reviews['origin_1'].unique())
    with right_column:
        roaster_country = st.selectbox(label="Select country of roaster:",
                                       options=coffee_reviews["loc_country"].unique())

    origin_country_df = coffee_reviews.loc[coffee_reviews['origin_1'] == origin_country]
    roaster_country_df = coffee_reviews.loc[coffee_reviews['loc_country'] == roaster_country]

    st.write(origin_country_df)
    st.write(roaster_country_df)


if __name__ == "__main__":
    main()
