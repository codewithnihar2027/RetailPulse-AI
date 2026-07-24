import streamlit as st

from app.auth.session import SessionManager


class Sidebar:

    @staticmethod
    def render():

        user = SessionManager.current_user()

        st.sidebar.title("📊 RetailPulse AI")

        st.sidebar.markdown("---")

        st.sidebar.write(f"👤 **{user['full_name']}**")
        st.sidebar.caption(user["email"])

        st.sidebar.markdown("---")

        page = st.sidebar.radio(
            "Navigation",
            [
                "📂 Dataset",
                "🏠 Overview",
                "📈 Sales Analytics",
                "👥 Customer Analytics",
                "📊 Forecasting",
                "🤖 AI Insights",
                "⚙ Settings"
            ]
        )

        st.sidebar.markdown("---")

        if st.sidebar.button("🚪 Logout", use_container_width=True):
            SessionManager.logout()
            st.rerun()

        return page