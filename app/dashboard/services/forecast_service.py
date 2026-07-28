from app.dashboard.services.dashboard_session import DashboardSession
from app.forecasting.forecasting_engine import ForecastingEngine
from app.forecasting.model_manager import ForecastModelManager
from app.forecasting.feature_engineering import ForecastFeatureEngineering

class ForecastService:
    """
    Service layer between the dashboard and forecasting module.
    """

    @staticmethod
    def get_forecast_results():

        if not DashboardSession.has_dataset():
            return None

        result = DashboardSession.get_pipeline_result()

        df = result["dataframe"]

        daily_sales = ForecastingEngine.prepare_daily_sales(df)

        daily_sales = ForecastFeatureEngineering.create_features(
            daily_sales
        )

        train_df, test_df = (
            ForecastingEngine.train_test_split(
                daily_sales
            )
        )

        model_results = (
            ForecastModelManager.compare_models(
                train_df,
                test_df
            )
        )

        future_forecast = None

        return {
            "daily_sales": daily_sales,
            "train_df": train_df,
            "test_df": test_df,
            "models": model_results,
            "future_forecast": future_forecast
        }