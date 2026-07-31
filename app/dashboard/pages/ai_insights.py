import streamlit as st

from app.dashboard.services.ai_service import DashboardAIService
from app.dashboard.services.dashboard_session import DashboardSession
from app.dashboard.utils.ai_suggestions import AISuggestions
from app.dashboard.utils.response_formatter import ResponseFormatter
from app.dashboard.utils.pdf_report import PDFReport

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

        # ==============================
        # Suggested Questions
        # ==============================

        if "ai_question" not in st.session_state:
            st.session_state.ai_question = ""

        st.caption("💡 Suggested Questions")

        labels = [
            "📈 Business Summary",
            "🏆 Top Products",
            "👥 Customer Segments",
            "🌍 Country Performance",
            "📉 Monthly Growth",
            "🎯 Recommendations",
        ]

        for i in range(0, len(labels), 2):

            col1, col2 = st.columns(2)

            with col1:
                if st.button(
                    labels[i],
                    use_container_width=True,
                ):
                    st.session_state.ai_question = (
                        AISuggestions.QUESTIONS[i]
                    )

            if i + 1 < len(labels):

                with col2:
                    if st.button(
                        labels[i + 1],
                        use_container_width=True,
                    ):
                        st.session_state.ai_question = (
                            AISuggestions.QUESTIONS[i + 1]
                        )

        question = st.text_area(
            "Enter your question",
            key="ai_question",
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

            with st.spinner(
                "Analyzing your business data..."
            ):

                DashboardAIService.ask(question)

                st.rerun()

        # ==============================
        # Latest Analysis
        # ==============================

        latest = DashboardSession.get_latest_ai_response()

        if latest:

            st.divider()

            st.subheader("✨ Latest Analysis")

            with st.container(border=True):

                st.markdown(
                    f"### ❓ Question\n\n{latest['question']}"
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.caption(
                        f"🤖 Model: {latest['model']}"
                    )

                with col2:
                    st.caption(
                        f"📅 {latest['generated_at']}"
                    )

                st.divider()

                st.markdown(
                    ResponseFormatter.format(
                        latest["response"]
                    ),
                    help=None,
                )
                # st.code(latest["response"])

                st.download_button(
                    label="📥 Download Report (.md)",
                    data=latest["response"],
                    file_name="retailpulse_ai_report.md",
                    mime="text/markdown",
                    width="stretch",
                )

                pdf = PDFReport.generate(latest)
                st.download_button(
                    label="📄 Download Report (.pdf)",
                    data=pdf,
                    file_name="retailpulse_ai_report.pdf",
                    mime="application/pdf",
                    width="stretch"
                )

        # ==============================
        # Analysis History
        # ==============================

        st.divider()

        st.subheader("📋 Analysis History")

        history = DashboardAIService.history()

        if not history:

            st.info(
                "No AI analyses yet. Ask a business question to get started."
            )

            return

        for item in history:

            with st.expander(
                f"❓ {item['question']}",
                expanded=False,
            ):

                st.markdown(
                    ResponseFormatter.format(
                        item["response"]
                    )
                )