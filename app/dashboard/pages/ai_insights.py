import streamlit as st

from app.dashboard.services.ai_service import DashboardAIService
from app.dashboard.services.dashboard_session import DashboardSession


class AIInsightsPage:

    @staticmethod
    def render():

        st.title("🧠 RetailPulse AI Copilot")

        st.caption(
            "Ask questions about your uploaded retail dataset and receive "
            "AI-powered business insights."
        )

        if st.button("🗑️ Clear Analysis History"):
            DashboardSession.clear_ai_history()
            DashboardSession.clear_latest_ai_response()
            st.rerun()

        st.divider()

        st.subheader("💬 Ask a Business Question")

        question = st.text_area(
            "Enter your question",
            height=120,
            placeholder=(
                "Example:\n"
                "• Why did revenue decrease in February?\n"
                "• Which products generate the most revenue?\n"
                "• Which customers are at risk?\n"
                "• Summarize my business performance.\n"
                "• What actions should I take next month?"
            ),
        )

        if st.button(
            "Generate Insights",
            use_container_width=True,
            type="primary",
            disabled=not question.strip(),
        ):

            with st.spinner("Analyzing your business data..."):

                DashboardAIService.ask(question)
        latest = DashboardSession.get_latest_ai_response()

        if latest:

            st.divider()

            st.subheader("✨ Latest Analysis")

            with st.container(border=True):
                st.markdown(
                    f"**Question:** {latest['question']}"
                )

                st.markdown("---")

                st.markdown(
                    latest["response"]
                )

        st.divider()

        st.subheader("📋 Analysis History")

        history = DashboardAIService.history()

        if not history:
            st.info(
                "No AI analyses yet. Ask a business question to get started."
            )

        for item in history:

            with st.expander(
                f"❓ {item['question']}",
                expanded=False,
            ):
                st.markdown(item["response"])