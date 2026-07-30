import streamlit as st
import pandas as pd

from app.auth.session import SessionManager
from app.config.settings import Config
from app.dashboard.services.dashboard_session import DashboardSession
from app.dashboard.services.dashboard_data_service import DashboardDataService


class SettingsPage:

    @staticmethod
    def render():

        st.title("⚙ RetailPulse AI Settings")

        st.caption(
            "Application information, AI configuration, and system status."
        )

        # ==========================================
        # Application Status
        # ==========================================

        st.subheader("🟢 Application Status")

        dataset_loaded = DashboardSession.has_dataset()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Authentication",
                "✅ Logged In"
                if SessionManager.is_authenticated()
                else "❌ Logged Out"
            )

            st.metric(
                "Dataset",
                "✅ Loaded"
                if dataset_loaded
                else "❌ Not Loaded"
            )

            st.metric(
                "Analytics",
                "✅ Ready"
                if dataset_loaded
                else "⏳ Waiting"
            )

        with col2:

            st.metric(
                "Forecasting",
                "✅ Ready"
                if dataset_loaded
                else "⏳ Waiting"
            )

            st.metric(
                "AI Copilot",
                "✅ Ready"
                if dataset_loaded
                else "⏳ Waiting"
            )

            st.metric(
                "Session",
                "✅ Active"
            )

        # ==========================================
        # AI Configuration
        # ==========================================

        st.divider()

        st.subheader("🤖 AI Configuration")

        col1, col2 = st.columns(2)

        with col1:

            st.text_input(
                "Provider",
                value=Config.LLM_PROVIDER,
                disabled=True,
            )

        with col2:

            if Config.LLM_PROVIDER.lower() == "openrouter":

                model = Config.OPENROUTER_MODEL

            elif Config.LLM_PROVIDER.lower() == "gemini":

                model = Config.GEMINI_MODEL

            else:

                model = "Unknown"

            st.text_input(
                "Model",
                value=model,
                disabled=True,
            )

        # ==========================================
        # Dataset Information
        # ==========================================

        if dataset_loaded:

            df = DashboardDataService.get_dataframe()

            st.divider()

            st.subheader("📂 Dataset Information")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Rows",
                    f"{len(df):,}"
                )

            with col2:

                st.metric(
                    "Columns",
                    len(df.columns)
                )

            with col3:

                st.metric(
                    "Missing Values",
                    f"{df.isna().sum().sum():,}"
                )

        # ==========================================
        # Application Information
        # ==========================================

        st.divider()

        st.subheader("ℹ Application")

        info = {
            "Application": "RetailPulse AI",
            "Version": "v1.0.0",
            "Framework": "Streamlit",
            "Machine Learning": "Scikit-learn",
            "Database": "SQLite",
            "Language": "Python",
            "Developer": "Nihar Suman",
        }

        info_df = pd.DataFrame(
            info.items(),
            columns=["Property", "Value"]
        )

        st.dataframe(
            info_df,
            hide_index=True,
            use_container_width=True,
        )