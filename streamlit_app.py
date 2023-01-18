import streamlit as st
from src.data import get_data


def main():
    st.set_page_config(page_title="Coffee Reviews",
                       page_icon="⭐",
                       layout="wide")

    st.title("Coffee Reviews | Streamlit | Kaggle")

    coffee_reviews = get_data()

    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Kaggle image here")
    with right_column:
        st.write("Streamlit image here")

    st.write("Data source: https://www.kaggle.com/datasets/schmoyote/coffee-reviews-dataset")

    st.write("---")
    st.write("Data contained in this web app is from the simplified CSV")

    with st.expander("View CSV as pandas DataFrame"):
        st.dataframe(coffee_reviews)


if __name__ == "__main__":
    main()
