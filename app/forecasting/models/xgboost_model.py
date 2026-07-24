from xgboost import XGBRegressor

from app.forecasting.feature_engineering import FEATURE_COLUMNS


class XGBoostForecast:

    @staticmethod
    def train_and_predict(train_df, test_df):

        model = XGBRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            objective="reg:squarederror"
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