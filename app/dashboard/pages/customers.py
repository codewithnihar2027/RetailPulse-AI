import streamlit as st

from app.dashboard.services.dashboard_session import DashboardSession

from app.dashboard.components.charts.bar_chart import BarChart

from app.dashboard.components.charts.horizontal_bar import HorizontalBarChart
from app.dashboard.services.dashboard_data_service import DashboardDataService
from app.dashboard.components.empty_state import EmptyState
class CustomerPage:

    @staticmethod
    def render():

        st.title("👥 Customer Analytics")

        if not DashboardSession.has_dataset():

            EmptyState.render(
                "📂 No Dataset Loaded",
                "Upload and process a retail dataset from the Dataset page to begin using RetailPulse AI."
            )

            return

        analytics = DashboardDataService.get_analytics()

        top_customers_revenue = analytics["top_customers_by_revenue"]

        top_customers_orders = analytics["top_customers_by_orders"]

        rfm_summary = analytics["rfm_summary"]

        segment_summary = rfm_summary["segment_summary"]

        rfm_table = rfm_summary["rfm_table"]

        st.divider()

        st.subheader("🏆 Top Customers by Revenue")

        HorizontalBarChart.render(
            top_customers_revenue,
            "Top Customers by Revenue"
        )

        st.divider()

        st.subheader("🛒 Top Customers by Orders")

        HorizontalBarChart.render(
            top_customers_orders,
            "Top Customers by Order"
        )

        st.divider()

        st.subheader("📊 Customer Segments")

        BarChart.render(
            segment_summary,
            "Customer Segments"
        )

        st.divider()

        st.subheader("📋 RFM Analysis")

        st.dataframe(
            rfm_table.sort_values(
                by="Monetary",
                ascending=False
            ),
            use_container_width=True
        )
