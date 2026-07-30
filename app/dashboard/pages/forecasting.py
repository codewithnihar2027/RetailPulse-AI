import streamlit as st

from app.dashboard.services.forecast_service import ForecastService
from app.dashboard.components.charts.comparison_chart import ComparisonChart
from app.dashboard.components.empty_state import EmptyState

class ForecastPage:

    @staticmethod
    def render():

        st.title("📊 Sales Forecasting")

        st.caption(
            "Evaluate forecasting models and compare predicted sales "
            "against actual historical revenue."
        )

        result = ForecastService.get_forecast_results()

        if result is None:

            EmptyState.render(
                "📂 No Dataset Loaded",
                "Upload and process a retail dataset from the Dataset page to begin using RetailPulse AI."
            )

            return

        models = result["models"]

        # ==========================================
        # Model Performance
        # ==========================================

        st.divider()

        st.subheader("🤖 Forecast Model Performance")

        for model_name, output in models.items():

            metrics = output["metrics"]

            with st.container(border=True):

                st.markdown(
                    f"### {model_name}"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "MAE",
                        f"{metrics['MAE']:,.2f}"
                    )

                with col2:

                    st.metric(
                        "RMSE",
                        f"{metrics['RMSE']:,.2f}"
                    )

        # ==========================================
        # Best Model
        # ==========================================

        best_name, best_output = min(
            models.items(),
            key=lambda x: x[1]["metrics"]["RMSE"]
        )

        st.divider()

        st.subheader("🏆 Best Performing Model")

        st.success(
            f"""
**{best_name}** achieved the lowest RMSE and has been
selected as the best forecasting model for this dataset.
"""
        )

        # ==========================================
        # Forecast Comparison
        # ==========================================

        forecast_df = best_output["forecast"]

        actual = forecast_df["Revenue"]

        predicted = forecast_df["Prediction"]

        st.divider()

        st.subheader("📈 Actual vs Predicted Revenue")

        ComparisonChart.render(
            actual,
            predicted,
            "Actual vs Predicted Revenue"
        )

        # ==========================================
        # Model Interpretation
        # ==========================================

        metrics = best_output["metrics"]

        st.divider()

        st.subheader("📝 Model Interpretation")

        st.info(
            f"""
**Selected Model:** {best_name}

**MAE:** {metrics['MAE']:,.2f}

**RMSE:** {metrics['RMSE']:,.2f}

The selected model produced the lowest prediction error
among all evaluated forecasting models.

Lower MAE indicates better average prediction accuracy,
while lower RMSE indicates fewer large prediction errors.
"""
        )

        # ==========================================
        # Download Forecast
        # ==========================================

        st.divider()

        st.download_button(
            label="📥 Download Forecast (.csv)",
            data=forecast_df.to_csv(index=False),
            file_name="forecast_results.csv",
            mime="text/csv",
            use_container_width=True,
        )