import pandas as pd

from app.forecasting.feature_engineering import FEATURE_COLUMNS


class Explainability:

    @staticmethod
    def feature_importance(model):
        """
        Return feature importance for tree-based models.
        """

        importance = pd.DataFrame(
            {
                "Feature": FEATURE_COLUMNS,
                "Importance": model.feature_importances_,
            }
        )

        importance = importance.sort_values(
            by="Importance",
            ascending=False
        ).reset_index(drop=True)

        return importance