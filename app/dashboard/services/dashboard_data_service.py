from app.dashboard.services.dashboard_session import DashboardSession


class DashboardDataService:

    @staticmethod
    def get_result():
        return DashboardSession.get_pipeline_result()

    @staticmethod
    def get_cleaned_data():
        return DashboardDataService.get_result()["dataframe"]

    @staticmethod
    def get_analytics():
        return DashboardDataService.get_result()["analytics"]

    # ==============================
    # KPI
    # ==============================

    @staticmethod
    def get_kpis():
        return DashboardDataService.get_analytics()["kpis"]

    # ==============================
    # Sales Analytics
    # ==============================

    @staticmethod
    def get_monthly_sales():
        return DashboardDataService.get_analytics()["monthly_sales"]

    @staticmethod
    def get_weekly_sales():
        return DashboardDataService.get_analytics()["weekly_sales"]

    @staticmethod
    def get_quarterly_sales():
        return DashboardDataService.get_analytics()["quarterly_sales"]

    @staticmethod
    def get_monthly_growth():
        return DashboardDataService.get_analytics()["monthly_growth"]

    @staticmethod
    def get_sales_summary():
        return DashboardDataService.get_analytics()["sales_summary"]

    @staticmethod
    def get_daily_summary():
        return DashboardDataService.get_analytics()["daily_summary"]

    @staticmethod
    def get_country_sales():
        return DashboardDataService.get_analytics()["country_sales"]

    @staticmethod
    def get_top_products_by_revenue():
        return DashboardDataService.get_analytics()["top_products_by_revenue"]

    @staticmethod
    def get_top_products_by_quantity():
        return DashboardDataService.get_analytics()["top_products_by_quantity"]

    # ==============================
    # Customer Analytics
    # ==============================

    @staticmethod
    def get_top_customers_by_revenue():
        return DashboardDataService.get_analytics()["top_customers_by_revenue"]

    @staticmethod
    def get_top_customers_by_orders():
        return DashboardDataService.get_analytics()["top_customers_by_orders"]

    @staticmethod
    def get_rfm():
        return DashboardDataService.get_analytics()["rfm_summary"]

    # ==============================
    # Forecasting
    # ==============================

    @staticmethod
    def get_forecast():
        return DashboardDataService.get_result()["forecast"]

    @staticmethod
    def get_dataset_info():

        df = DashboardDataService.get_dataframe()

        return {
            "rows": len(df),
            "columns": len(df.columns),
            "missing_values": int(df.isna().sum().sum()),
            "memory_mb": df.memory_usage(deep=True).sum() / 1024 / 1024
        }

    @staticmethod
    def get_dataframe():
        return DashboardDataService.get_cleaned_data()