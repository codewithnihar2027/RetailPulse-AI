import pandas as pd


class SchemaDetector:

    @staticmethod
    def get_columns(df: pd.DataFrame):
        return list(df.columns)

    @staticmethod
    def get_shape(df: pd.DataFrame):
        return df.shape

    @staticmethod
    def get_dtypes(df: pd.DataFrame):
        return df.dtypes.astype(str).to_dict()

    @staticmethod
    def generate_report(df: pd.DataFrame):
        """
        Generate schema metadata for the uploaded dataset.
        """

        report = {

            "rows": df.shape[0],

            "columns": df.shape[1],

            "column_names": list(df.columns),

            "data_types": df.dtypes.astype(str).to_dict()

        }

        return report