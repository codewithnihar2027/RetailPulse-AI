import pandas as pd

from .exceptions import DatasetValidationError

class DatasetValidator:

    @staticmethod
    def validate_not_empty(df: pd.DataFrame):

        if df.empty:
            raise DatasetValidationError(
                "The uploaded dataset is empty."
            )

        return True