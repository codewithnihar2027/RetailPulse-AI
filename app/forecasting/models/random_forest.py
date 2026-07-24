from sklearn.ensemble import RandomForestRegressor

from app.forecasting.feature_engineering import FEATURE_COLUMNS


class RandomForestForecast:

    @staticmethod
    def train_and_predict(train_df, test_df):
        """
        Train a Random Forest model and predict on the test set.
        """

        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        )

        X_train = train_df[FEATURE_COLUMNS]
        y_train = train_df["Revenue"]

        X_test = test_df[FEATURE_COLUMNS]

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        forecast_df = test_df.copy()

        forecast_df["Prediction"] = predictions

        return {
            "model": model,
            "forecast": forecast_df
        }