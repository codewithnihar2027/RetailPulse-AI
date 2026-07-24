from sklearn.linear_model import LinearRegression

from app.forecasting.feature_engineering import FEATURE_COLUMNS


class LinearRegressionForecast:

    @staticmethod
    def train_and_predict(train_df, test_df):
        """
        Train a Linear Regression model and predict on the test set.
        """

        model = LinearRegression()

        X_train = train_df[FEATURE_COLUMNS]
        y_train = train_df["Revenue"]

        X_test = test_df[FEATURE_COLUMNS]

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        forecast_df = test_df.copy()

        forecast_df["Prediction"] = predictions

        return forecast_df