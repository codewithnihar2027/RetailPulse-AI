import streamlit as st


class FilterManager:

    @staticmethod
    def render(df):

        st.sidebar.header("🔍 Filters")

        countries = sorted(df["Country"].dropna().unique())

        selected_countries = st.sidebar.multiselect(
            "Country",
            countries,
            default=countries,
        )

        years = sorted(df["Year"].unique())

        selected_years = st.sidebar.multiselect(
            "Year",
            years,
            default=years,
        )

        filtered_df = df[
            df["Country"].isin(selected_countries)
            &
            df["Year"].isin(selected_years)
        ]

        return filtered_df