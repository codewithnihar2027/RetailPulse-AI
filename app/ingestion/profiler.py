import pandas as pd


class DataProfiler:
    """
    Responsible for profiling datasets.
    """

    @staticmethod
    def generate_profile(df: pd.DataFrame) -> dict:

        profile = {

            "rows": len(df),

            "columns": len(df.columns),

            "missing_values": df.isnull().sum().to_dict(),

            "total_missing_values": int(df.isnull().sum().sum()),

            "duplicate_rows": int(df.duplicated().sum()),

            "memory_usage_mb": round(
                df.memory_usage(deep=True).sum() / (1024 * 1024), 2
            ),

            "numeric_columns": df.select_dtypes(
                include="number"
            ).columns.tolist(),

            "categorical_columns": df.select_dtypes(
                include="object"
            ).columns.tolist(),

        }

        return profile