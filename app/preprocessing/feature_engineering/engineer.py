class FeatureEngineer:
    """
    Responsible for creating business features
    from the cleaned retail dataset.
    """

    @staticmethod
    def engineer(df):

        df = df.copy()

        df = FeatureEngineer.create_revenue(df)

        df = FeatureEngineer.extract_date_features(df)

        return df

    @staticmethod
    def create_revenue(df):
        """
        Create Revenue column.
        """

        if {"Quantity", "Price"}.issubset(df.columns):
            df["Revenue"] = df["Quantity"] * df["Price"]

        return df

    @staticmethod
    def extract_date_features(df):
        """
        Extract useful time-based features.
        """

        if "InvoiceDate" not in df.columns:
            return df

        df["Year"] = df["InvoiceDate"].dt.year

        df["Month"] = df["InvoiceDate"].dt.month

        df["Quarter"] = df["InvoiceDate"].dt.quarter

        df["Day"] = df["InvoiceDate"].dt.day

        df["Weekday"] = df["InvoiceDate"].dt.day_name()

        df["Weekend"] = (
            df["InvoiceDate"]
            .dt.weekday
            .isin([5, 6])
        )

        return df