import pandas as pd
FEATURE_COLUMNS = [
    "DayOfWeek",
    "Month",
    "Quarter",
    "Weekend",
    "Lag_1",
    "Lag_7",
    "Lag_30",
    "Rolling_Mean_7",
    "Rolling_Mean_30",
]

class ForecastFeatureEngineering:

    @staticmethod
    def create_features(df):
        """
        Create forecasting features.
        """

        data = df.copy()

        # ------------------------
        # Calendar Features
        # ------------------------

        data["DayOfWeek"] = data["Date"].dt.dayofweek

        data["Month"] = data["Date"].dt.month

        data["Quarter"] = data["Date"].dt.quarter

        data["Weekend"] = (
            data["DayOfWeek"] >= 5
        ).astype(int)

        # ------------------------
        # Lag Features
        # ------------------------

        data["Lag_1"] = data["Revenue"].shift(1)

        data["Lag_7"] = data["Revenue"].shift(7)

        data["Lag_30"] = data["Revenue"].shift(30)

        # ------------------------
        # Rolling Features
        # ------------------------

        data["Rolling_Mean_7"] = (
            data["Revenue"]
            .rolling(7)
            .mean()
        )

        data["Rolling_Mean_30"] = (
            data["Revenue"]
            .rolling(30)
            .mean()
        )

        # Remove rows with missing lag/rolling values
        data = data.dropna().reset_index(drop=True)

        return data