import streamlit as st

from app.dashboard.services.dashboard_session import DashboardSession

from app.dashboard.components.charts.line_chart import LineChart
from app.dashboard.components.charts.bar_chart import BarChart


class SalesPage:

    @staticmethod
    def render():

        st.title("📈 Sales Analytics")

        if not DashboardSession.has_dataset():

            st.warning("Please upload a dataset first.")

            return

        result = DashboardSession.get_pipeline_result()

        analytics = result["analytics"]

        monthly_sales = analytics["monthly_sales"]

        weekly_sales = analytics["weekly_sales"]

        quarterly_sales = analytics["quarterly_sales"]

        top_revenue = analytics["top_products_by_revenue"]

        top_quantity = analytics["top_products_by_quantity"]

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

        st.subheader("🏆 Top Product By revenue")

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