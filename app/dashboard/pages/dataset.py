import streamlit as st
from app.dashboard.services.pipeline_service import PipelineService
from app.dashboard.services.dashboard_session import DashboardSession


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

        uploaded_file = st.file_uploader(
            "Upload CSV",
            type=["csv"]
        )

        if uploaded_file is not None:

            st.success(
                f"Selected: {uploaded_file.name}"
            )

            if st.button(
                "🚀 Process Dataset",
                use_container_width=True
            ):

                with st.spinner("Processing dataset..."):

                    result = PipelineService.process_uploaded_file(
                        uploaded_file
                    )

                    DashboardSession.set_pipeline_result(result)
                    DashboardSession.clear_ai_history()

                st.success("Dataset processed successfully!")

                st.rerun()