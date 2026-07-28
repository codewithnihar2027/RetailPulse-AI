from app.dashboard.services.dashboard_session import DashboardSession


class ContextBuilder:
    """
    Builds structured business context for the AI Copilot.
    """

    @staticmethod
    def _to_records(df, limit=10):
        """
        Convert DataFrame to a list of dictionaries.
        """
        if df is None:
            return []

        try:
            return df.head(limit).to_dict(orient="records")
        except Exception:
            return df

    @staticmethod
    def build():

        if not DashboardSession.has_dataset():
            return None

        result = DashboardSession.get_pipeline_result()

        analytics = result["analytics"]

        context = {
            "kpis": analytics.get("kpis"),
            "sales_summary": analytics.get("sales_summary"),
            "daily_summary": analytics.get("daily_summary"),
            "monthly_growth": analytics.get("monthly_growth"),
            "rfm_summary": analytics.get("rfm_summary"),

            "top_products": ContextBuilder._to_records(
                analytics.get("top_products_by_revenue")
            ),

            "top_customers": ContextBuilder._to_records(
                analytics.get("top_customers_by_revenue")
            ),

            "country_sales": ContextBuilder._to_records(
                analytics.get("country_sales")
            ),

            "monthly_sales": ContextBuilder._to_records(
                analytics.get("monthly_sales")
            )
        }

        return context