import streamlit as st

from app.auth.auth_service import AuthService
from app.auth.session import SessionManager


class LoginPage:

    @staticmethod
    def render():

        with st.form("login_form"):

            email = st.text_input(
                "Email",
                placeholder="Enter your email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            submitted = st.form_submit_button(
                "🔐 Login",
                use_container_width=True
            )

        if submitted:

            success, result = AuthService.login(
                email,
                password
            )

            if success:

                SessionManager.login(result)

                st.success("Login successful!")

                st.rerun()

            else:

                st.error(result)