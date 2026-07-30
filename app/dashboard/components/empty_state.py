import streamlit as st


class EmptyState:

    @staticmethod
    def render(title: str, message: str):

        st.info(
            f"""
### {title}

{message}
"""
        )