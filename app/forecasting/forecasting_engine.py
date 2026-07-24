import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error
)
import numpy as np
from sklearn.linear_model import LinearRegression
from app.forecasting.feature_engineering import FEATURE_COLUMNS

class ForecastingEngine:
    """
    Handles sales forecasting models.
    """

    @staticmethod
    def prepare_daily_sales(df):
        """
        Prepare a continuous daily sales time series.
        Missing dates are filled with zero revenue.
        """

        daily_sales = (
            df.groupby(df["InvoiceDate"].dt.date)["Revenue"]
            .sum()
            .reset_index()
        )

        daily_sales.columns = ["Date", "Revenue"]

        daily_sales["Date"] = pd.to_datetime(daily_sales["Date"])

        # Create continuous daily index
        full_dates = pd.date_range(
            start=daily_sales["Date"].min(),
            end=daily_sales["Date"].max(),
            freq="D"
        )

        daily_sales = (
            daily_sales
            .set_index("Date")
            .reindex(full_dates, fill_value=0)
            .rename_axis("Date")
            .reset_index()
        )

        return daily_sales

    @staticmethod
    def train_test_split(daily_sales, test_size=30):
        """
        Split the daily sales time series into
        training and testing datasets.

        Parameters
        ----------
        daily_sales : pd.DataFrame
            DataFrame with Date and Revenue columns.

        test_size : int
            Number of days reserved for testing.

        Returns
        -------
        train_df, test_df
        """

        train_df = daily_sales.iloc[:-test_size].copy()

        test_df = daily_sales.iloc[-test_size:].copy()

        return train_df, test_df

    @staticmethod
    def naive_forecast(train_df, test_df):
        """
        Generate naive forecast.

        Prediction for each day is the previous day's actual revenue.
        """

        predictions = []

        # Last known value from training
        previous_value = train_df["Revenue"].iloc[-1]

        for actual in test_df["Revenue"]:

            predictions.append(previous_value)

            previous_value = actual

        forecast_df = test_df.copy()

        forecast_df["Prediction"] = predictions

        return forecast_df

    @staticmethod
    def evaluate_forecast(forecast_df):
        """
        Evaluate forecasting performance.
        """

        actual = forecast_df["Revenue"]

        predicted = forecast_df["Prediction"]

        mae = mean_absolute_error(
            actual,
            predicted
        )

        rmse = root_mean_squared_error(
            actual,
            predicted
        )

        return {

            "MAE": float(round(mae, 2)),

            "RMSE": float(round(rmse, 2))

        }

    @staticmethod
    def create_features(daily_sales):
        """
        Create numerical features for forecasting.
        """

        df = daily_sales.copy()

        df["Day"] = np.arange(len(df))

        return df

    # @staticmethod
    # def linear_regression_forecast(train_df, test_df):
    #     """
    #     Train a Linear Regression model and forecast the test period.
    #     """

    #     model = LinearRegression()

    #     X_train = train_df[FEATURE_COLUMNS]
    #     y_train = train_df["Revenue"]

    #     X_test = test_df[FEATURE_COLUMNS]

    #     model.fit(X_train, y_train)

    #     predictions = model.predict(X_test)

    #     forecast_df = test_df.copy()

    #     forecast_df["Prediction"] = predictions

    #     return forecast_df

    @staticmethod
    def predict_next_days(daily_sales, days=30):
        """
        Train Linear Regression on the complete dataset
        and predict future revenue.
        """

        model = LinearRegression()

        X = daily_sales[["Day"]]

        y = daily_sales["Revenue"]

        model.fit(X, y)

        last_day = daily_sales["Day"].max()

        future_days = np.arange(
            last_day + 1,
            last_day + days + 1
        )

        predictions = model.predict(
            future_days.reshape(-1, 1)
        )

        last_date = daily_sales["Date"].max()

        future_dates = pd.date_range(
            start=last_date + pd.Timedelta(days=1),
            periods=days,
            freq="D"
        )

        future_forecast = pd.DataFrame({

            "Date": future_dates,

            "Prediction": predictions

        })

        return future_forecast