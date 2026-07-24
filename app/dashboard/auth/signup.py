import streamlit as st

from app.auth.auth_service import AuthService


class SignupPage:

    @staticmethod
    def render():

        with st.form("signup_form"):

            full_name = st.text_input(
                "Full Name",
                placeholder="Enter your full name"
            )

            email = st.text_input(
                "Email",
                placeholder="Enter your email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Create a password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                placeholder="Re-enter your password"
            )

            submitted = st.form_submit_button(
                "📝 Create Account",
                use_container_width=True
            )

        if submitted:

            if password != confirm_password:
                st.error("Passwords do not match.")
                return

            success, message = AuthService.register(
                full_name=full_name,
                email=email,
                password=password
            )

            if success:
                st.success(message)
                st.info("You can now log in using the Login tab.")
            else:
                st.error(message)