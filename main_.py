from pprint import pprint

from app.pipeline import RetailPipeline
from app.forecasting.forecasting_engine import ForecastingEngine
from app.forecasting.feature_engineering import ForecastFeatureEngineering
from app.forecasting.model_manager import ForecastModelManager
from app.forecasting.explainability import Explainability

def main():

    # ======================================================
    # RUN PIPELINE
    # ======================================================

    pipeline = RetailPipeline()

    result = pipeline.run(
        "data/raw/online_retail_II.csv"
    )

    # ======================================================
    # PREPARE DAILY SALES
    # ======================================================

    daily_sales = ForecastingEngine.prepare_daily_sales(
        result["dataframe"]
    )

    # ======================================================
    # NAIVE FORECAST (Baseline)
    # ======================================================

    train_df, test_df = ForecastingEngine.train_test_split(
        daily_sales
    )

    naive_forecast = ForecastingEngine.naive_forecast(
        train_df,
        test_df
    )

    naive_metrics = ForecastingEngine.evaluate_forecast(
        naive_forecast
    )

    print("\n========== NAIVE FORECAST ==========\n")
    pprint(naive_metrics)

    # ======================================================
    # FEATURE ENGINEERING
    # ======================================================

    daily_sales = ForecastFeatureEngineering.create_features(
        daily_sales
    )

    print("\n========== FEATURE DATA ==========\n")

    print(daily_sales.info())
    print()
    print(daily_sales.head())

    # ======================================================
    # TRAIN / TEST SPLIT (Feature Engineered Data)
    # ======================================================

    train_df, test_df = ForecastingEngine.train_test_split(
        daily_sales
    )

    # ======================================================
    # MODEL COMPARISON
    # ======================================================

    results = ForecastModelManager.compare_models(
        train_df,
        test_df
    )

    print("\n========== MODEL COMPARISON ==========\n")

    for model_name, result in results.items():

        print(f"{model_name}")

        pprint(result["metrics"])

        print()

    # ======================================================
# FEATURE IMPORTANCE
# ======================================================

    for model_name in ["Random Forest", "XGBoost"]:

        if model_name not in results:
            continue

        model = results[model_name]["model"]

        if model is None:
            continue

        importance = Explainability.feature_importance(model)

        print(f"\n========== {model_name.upper()} FEATURE IMPORTANCE ==========\n")

        print(importance)

    # ======================================================
    # FUTURE FORECAST
    # ======================================================

    # Disabled for now.
    # We'll redesign this after implementing recursive forecasting.

    # future_forecast = ForecastingEngine.predict_next_days(
    #     daily_sales,
    #     days=30
    # )


if __name__ == "__main__":
    main()