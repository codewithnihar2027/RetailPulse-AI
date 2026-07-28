import streamlit as st

from app.dashboard.services.forecast_service import ForecastService
from app.dashboard.components.charts.comparison_chart import ComparisonChart


class ForecastPage:

    @staticmethod
    def render():

        st.title("📊 Forecasting")

        result = ForecastService.get_forecast_results()

        if result is None:
            st.warning("Please upload a dataset first.")
            return


        models = result["models"]

        st.divider()

        st.subheader("📊 Model Performance")

        for model_name, output in models.items():
            metrics = output["metrics"]

            st.write(f"### {model_name}")

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

        best_model = min(
            models.items(),
            key=lambda x: x[1]["metrics"]["RMSE"]
        )
        best_name = best_model[0]
        best_output = best_model[1]

        st.divider()

        st.subheader("🏆 Best Forecasting Model")

        st.success(
            f"🏆 {best_name} achieved the lowest RMSE and is selected as the best forecasting model."
        )

        forecast_df = best_output["forecast"]

        actual = forecast_df["Revenue"]

        predicted = forecast_df["Prediction"]


        st.divider()

        st.subheader("📈 Actual vs Predicted")

        ComparisonChart.render(
            actual,
            predicted,
            "Forecast Comparison"
        )