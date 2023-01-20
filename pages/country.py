import streamlit as st
from src.data import get_data


def main():
    st.title("Country Page")

    coffee_reviews = get_data()

    origin_tab, roaster_tab = st.tabs([
        "Origin Country of coffee beans", "County of Roaster"
    ])

    with origin_tab:
        origin_country = st.selectbox(label="Select origin country of coffee beans:",
                                      options=coffee_reviews['origin_1'].unique())

        origin_country_df = coffee_reviews.loc[coffee_reviews['origin_1'] == origin_country]
        st.dataframe(origin_country_df)

    with roaster_tab:
        roaster_country = st.selectbox(label="Select country of roaster:",
                                       options=coffee_reviews["loc_country"].unique())

        roaster_country_df = coffee_reviews.loc[coffee_reviews['loc_country'] == roaster_country]
        st.dataframe(roaster_country_df)


if __name__ == "__main__":
    main()
