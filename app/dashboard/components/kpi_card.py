import streamlit as st


class KPICard:

    @staticmethod
    def render(title, value):

        st.metric(
            label=title,
            value=value
        )