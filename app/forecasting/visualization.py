import matplotlib.pyplot as plt


class ForecastVisualizer:

    @staticmethod
    def plot_forecast(forecast_df, title="Forecast"):

        plt.figure(figsize=(12, 6))

        plt.plot(
            forecast_df["Date"],
            forecast_df["Revenue"],
            label="Actual"
        )

        plt.plot(
            forecast_df["Date"],
            forecast_df["Prediction"],
            label="Prediction"
        )

        plt.title(title)

        plt.xlabel("Date")

        plt.ylabel("Revenue")

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        plt.show()

    @staticmethod
    def plot_future_forecast(future_forecast):

        plt.figure(figsize=(12, 6))

        plt.plot(
            future_forecast["Date"],
            future_forecast["Prediction"],
            marker="o"
        )

        plt.title("Next 30 Days Revenue Forecast")

        plt.xlabel("Date")

        plt.ylabel("Predicted Revenue")

        plt.grid(True)

        plt.tight_layout()

        plt.show()