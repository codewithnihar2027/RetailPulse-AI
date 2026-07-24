from app.forecasting.models.linear_regression import LinearRegressionForecast
from app.forecasting.models.random_forest import RandomForestForecast
from app.forecasting.forecasting_engine import ForecastingEngine
from app.forecasting.models.xgboost_model import XGBoostForecast

class ForecastModelManager:

    MODELS = {
        "Linear Regression": LinearRegressionForecast,
        "Random Forest": RandomForestForecast,
        "XGBoost": XGBoostForecast,
    }

    @classmethod
    def compare_models(cls, train_df, test_df):
        """
        Train, evaluate, and compare all registered forecasting models.
        """

        results = {}

        for model_name, model_class in cls.MODELS.items():

            output = model_class.train_and_predict(
            train_df,
            test_df
            )

            if isinstance(output, dict):

                forecast_df = output["forecast"]

                model = output.get("model")

            else:

                forecast_df = output

                model = None

            metrics = ForecastingEngine.evaluate_forecast(
                forecast_df
            )

            results[model_name] = {
                "metrics": metrics,
                "forecast": forecast_df,
                "model": model,
            }

        return results