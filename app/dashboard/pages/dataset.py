import streamlit as st

from app.dashboard.services.pipeline_service import PipelineService
from app.dashboard.services.dashboard_session import DashboardSession
from app.dashboard.services.dashboard_data_service import DashboardDataService


class DatasetPage:

    @staticmethod
    def render():

        st.title("📂 Dataset")

        st.markdown(
            """
Upload a retail CSV dataset to begin analysis.

Supported datasets include:

- Online Retail
- Superstore Sales
- Retail Transactions
"""
        )

        # ==========================================
        # Success Message After Processing
        # ==========================================

        if st.session_state.pop("dataset_processed", False):

            st.success("✅ Dataset processed successfully!")

        # ==========================================
        # Upload Dataset
        # ==========================================

        uploaded_file = st.file_uploader(
            "Upload CSV",
            type=["csv"],
        )

        if uploaded_file is not None:

            st.success(
                f"Selected: **{uploaded_file.name}**"
            )

            if st.button(
                "🚀 Process Dataset",
                use_container_width=True,
            ):

                with st.spinner(
                    "Processing dataset..."
                ):

                    result = PipelineService.process_uploaded_file(
                        uploaded_file
                    )

                    DashboardSession.set_pipeline_result(result)

                    DashboardSession.clear_ai_history()

                    DashboardSession.clear_latest_ai_response()

                    st.session_state["dataset_processed"] = True

                st.rerun()

        # ==========================================
        # Dataset Overview
        # ==========================================

        if not DashboardSession.has_dataset():

            return

        df = DashboardDataService.get_dataframe()

        st.divider()

        st.subheader("📊 Dataset Overview")

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

            memory_mb = (
                df.memory_usage(deep=True).sum()
                / 1024
                / 1024
            )

            st.metric(
                "Memory",
                f"{memory_mb:.2f} MB"
            )

        st.divider()

        # ==========================================
        # Column Information
        # ==========================================

        st.subheader("🧾 Column Information")

        column_info = df.dtypes.astype(str).reset_index()

        column_info.columns = [
            "Column",
            "Data Type",
        ]

        column_info["Missing Values"] = df.isna().sum().values

        st.dataframe(
            column_info,
            use_container_width=True,
            hide_index=True,
        )

        # ==========================================
        # Dataset Preview
        # ==========================================

        st.divider()

        st.subheader("👀 Dataset Preview")

        st.dataframe(
            df.head(20),
            use_container_width=True,
        )

        # ==========================================
        # Numeric Summary
        # ==========================================

        st.divider()

        st.subheader("📈 Statistical Summary")

        st.dataframe(
            df.describe(),
            use_container_width=True,
        )