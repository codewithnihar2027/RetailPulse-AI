import streamlit as st


class DashboardSession:

    @staticmethod
    def set_pipeline_result(result):

        st.session_state["pipeline_result"] = result

    @staticmethod
    def get_pipeline_result():

        return st.session_state.get(
            "pipeline_result"
        )

    @staticmethod
    def has_dataset():

        return "pipeline_result" in st.session_state

    @staticmethod
    def clear():

        st.session_state.pop(
            "pipeline_result",
            None
        )