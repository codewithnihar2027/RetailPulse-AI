class ForecastComparison:

    @staticmethod
    def compare(models):

        print("\n========== MODEL COMPARISON ==========\n")

        print(
            f"{'Model':<20}"
            f"{'MAE':>12}"
            f"{'RMSE':>12}"
        )

        print("-" * 44)

        for name, metric in models.items():

            print(
                f"{name:<20}"
                f"{metric['MAE']:>12.2f}"
                f"{metric['RMSE']:>12.2f}"
            )