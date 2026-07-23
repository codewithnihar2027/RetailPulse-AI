import pandas as pd
class DataCleaner:
    """
    Performs data cleaning operations on the standardized dataset.
    """

    @staticmethod
    def clean(df):
        """
        Execute all cleaning steps.
        """
        df = df.copy()

        df = DataCleaner.remove_duplicates(df)

        df = DataCleaner.standardize_data_types(df)

        df = DataCleaner.handle_missing_values(df)

        return df

    @staticmethod
    def remove_duplicates(df):
        """
        Remove Duplicate Rows.
        """

        return df.drop_duplicates().copy()

    @staticmethod
    def standardize_data_types(df):
        """
        Convert important columns to appropriate data types.
        """

        if "InvoiceDate" in df.columns:
            df["InvoiceDate"] = (
                pd.to_datetime(
                    df["InvoiceDate"],
                    errors = "coerce"
                )
            )

        if "Quantity" in df.columns:
            df["Quantity"] = (
                pd.to_numeric(
                    df["Quantity"],
                    errors="coerce"
                )
            )

        if "Price" in df.columns:
            df["Price"] = (
                pd.to_numeric(
                    df["Price"],
                    errors="coerce"
                )
            )
        return df

    @staticmethod
    def handle_missing_values(df):
        """
        Handle missing values in important columns.
        """

        df = df.dropna(
            subset=[
                "Invoice",
                "InvoiceDate",
                "Quantity",
                "Price",
                "Product"
            ]
        )

        return df