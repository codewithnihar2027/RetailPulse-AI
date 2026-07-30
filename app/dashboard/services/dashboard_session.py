import streamlit as st
from datetime import datetime
from app.config.settings import Config



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

    # ==============================
    # AI Analysis History
    # ==============================

    @staticmethod
    def initialize_ai_history():

        import streamlit as st

        if "ai_history" not in st.session_state:
            st.session_state.ai_history = []


    @staticmethod
    def add_ai_history(question, response):

        import streamlit as st

        DashboardSession.initialize_ai_history()

        st.session_state.ai_history.insert(
            0,
            {
                "question": question,
                "response": response
            }
        )


    @staticmethod
    def get_ai_history():

        import streamlit as st

        DashboardSession.initialize_ai_history()

        return st.session_state.ai_history


    @staticmethod
    def clear_ai_history():

        import streamlit as st

        st.session_state.ai_history = []

        # ==============================
    # Latest AI Response
    # ==============================

    @staticmethod
    def set_latest_ai_response(question, response):

        st.session_state["latest_ai_response"] = {
            "question": question,
            "response": response,
            "model": Config.OPENROUTER_MODEL,
            "generated_at": datetime.now().strftime(
                "%d %b %Y, %I:%M %p"
            )
        }

    @staticmethod
    def get_latest_ai_response():

        return st.session_state.get(
            "latest_ai_response"
        )


    @staticmethod
    def clear_latest_ai_response():

        st.session_state.pop(
            "latest_ai_response",
            None
        )