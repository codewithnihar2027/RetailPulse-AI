from app.dashboard.services.dashboard_session import DashboardSession
from app.dashboard.services.dashboard_data_service import DashboardDataService


class ContextBuilder:
    """
    Builds structured business context for the AI Copilot.
    """

    @staticmethod
    def _to_markdown(df, limit=10):
        """
        Convert DataFrame to Markdown table.
        """

        if df is None:
            return "No data available."

        try:

            if df.empty:
                return "No data available."

            return df.head(limit).to_markdown(index=False)

        except Exception:

            return str(df)

    @staticmethod
    def build():

        if not DashboardSession.has_dataset():
            return None

        analytics = DashboardDataService.get_analytics()

        context = {

            # ======================================
            # KPIs
            # ======================================

            "kpis": analytics.get("kpis"),

            # ======================================
            # Sales Analytics
            # ======================================

            "sales_summary": analytics.get("sales_summary"),

            "daily_summary": analytics.get("daily_summary"),

            "monthly_growth": analytics.get("monthly_growth"),

            "monthly_sales": ContextBuilder._to_markdown(
                analytics.get("monthly_sales"),
                limit=24,
            ),

            "weekly_sales": ContextBuilder._to_markdown(
                analytics.get("weekly_sales"),
                limit=52,
            ),

            "quarterly_sales": ContextBuilder._to_markdown(
                analytics.get("quarterly_sales"),
                limit=8,
            ),

            "country_sales": ContextBuilder._to_markdown(
                analytics.get("country_sales"),
                limit=25,
            ),

            # ======================================
            # Product Analytics
            # ======================================

            "top_products_by_revenue": ContextBuilder._to_markdown(
                analytics.get("top_products_by_revenue"),
                limit=20,
            ),

            "top_products_by_quantity": ContextBuilder._to_markdown(
                analytics.get("top_products_by_quantity"),
                limit=20,
            ),

            # ======================================
            # Customer Analytics
            # ======================================

            "rfm_summary": analytics.get("rfm_summary"),

            "top_customers_by_revenue": ContextBuilder._to_markdown(
                analytics.get("top_customers_by_revenue"),
                limit=20,
            ),

            "top_customers_by_orders": ContextBuilder._to_markdown(
                analytics.get("top_customers_by_orders"),
                limit=20,
            ),
        }

        return context