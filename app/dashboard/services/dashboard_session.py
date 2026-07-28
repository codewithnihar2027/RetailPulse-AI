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