import streamlit as st

from app.dashboard.services.dashboard_session import DashboardSession
from app.dashboard.services.dashboard_data_service import DashboardDataService

from app.dashboard.components.charts.line_chart import LineChart
from app.dashboard.components.charts.bar_chart import BarChart
from app.dashboard.components.empty_state import EmptyState

class SalesPage:

    @staticmethod
    def render():

        st.title("📈 Sales Analytics")

        if not DashboardSession.has_dataset():

            EmptyState.render(
                "📂 No Dataset Loaded",
                "Upload and process a retail dataset from the Dataset page to begin using RetailPulse AI."
            )


            return

        analytics = DashboardDataService.get_analytics()

        monthly_sales = DashboardDataService.get_monthly_sales()

        weekly_sales = analytics["weekly_sales"]

        quarterly_sales = DashboardDataService.get_quarterly_sales()

        top_revenue = DashboardDataService.get_top_products_by_revenue()

        top_quantity = DashboardDataService.get_top_products_by_quantity()

        st.divider()

        st.subheader("📅 Monthly Sales")

        LineChart.render(
            monthly_sales,
            "Monthly Sales"
        )

        st.divider()

        st.subheader("📆 Weekly Sales")

        LineChart.render(
            weekly_sales,
            "Weekly Sales"
        )

        st.divider()

        st.subheader("📊 Quarterly Sales")

        BarChart.render(
            quarterly_sales,
            "Quarterly Sales"
        )

        st.divider()

        st.subheader("🏆 Top Products by Revenue")

        BarChart.render(
            top_revenue,
            "Top Revenue Products"
        )

        st.divider()

        st.subheader("📦 Top Products by Quantity")

        BarChart.render(
            top_quantity,
            "Top Quantity Products"
        )