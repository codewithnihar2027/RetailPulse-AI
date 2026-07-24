import streamlit as st

from app.dashboard.auth.login import LoginPage
from app.dashboard.auth.signup import SignupPage


class AuthPage:

    @staticmethod
    def render():

        st.title("📊 RetailPulse AI")

        st.subheader("AI-Powered Retail Analytics Platform")

        login_tab, signup_tab = st.tabs(
            ["🔐 Login", "📝 Create Account"]
        )

        with login_tab:
            LoginPage.render()

        with signup_tab:
            SignupPage.render()