import streamlit as st


class SessionManager:

    @staticmethod
    def login(user: dict):
        st.session_state["authenticated"] = True
        st.session_state["user"] = user

    @staticmethod
    def logout():
        st.session_state["authenticated"] = False
        st.session_state["user"] = None

    @staticmethod
    def is_authenticated():
        return st.session_state.get("authenticated", False)

    @staticmethod
    def current_user():
        return st.session_state.get("user", None)