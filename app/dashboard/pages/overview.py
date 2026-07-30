import streamlit as st

from app.dashboard.services.dashboard_session import DashboardSession
from app.dashboard.services.dashboard_data_service import DashboardDataService

from app.dashboard.components.kpi_card import KPICard
from app.dashboard.components.charts.line_chart import LineChart
from app.dashboard.components.charts.bar_chart import BarChart
from app.dashboard.components.empty_state import EmptyState

class OverviewPage:

    @staticmethod
    def render():

        st.title("🏠 Executive Overview")

        if not DashboardSession.has_dataset():

            EmptyState.render(
                "📂 No Dataset Loaded",
                "Upload and process a retail dataset from the Dataset page to begin using RetailPulse AI."
            )


            return

        kpis = DashboardDataService.get_kpis()

        monthly_sales = DashboardDataService.get_monthly_sales()

        analytics = DashboardDataService.get_analytics()

        monthly_growth = DashboardDataService.get_monthly_growth()

        sales_summary = DashboardDataService.get_sales_summary()

        daily_summary = DashboardDataService.get_daily_summary()

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            KPICard.render(
                "Revenue",
                f"${kpis['total_revenue']:,.2f}"
            )

        with col2:

            KPICard.render(
                "Orders",
                f"{kpis['total_orders']:,}"
            )

        with col3:

            KPICard.render(
                "Customers",
                f"{kpis['total_customers']:,}"
            )

        with col4:

            KPICard.render(
                "Avg Order Value",
                f"${kpis['average_order_value']:,.2f}"
            )

        st.divider()

        st.subheader("📈 Monthly Revenue Trend")

        LineChart.render(
            monthly_sales,
            "Monthly Revenue"
        )

        st.divider()

        st.subheader("📊 Monthly Growth (%)")

        BarChart.render(
            monthly_growth,
            "Monthly Growth"
        )

        st.divider()

        st.subheader("🏆 Business Highlights")

        col1, col2 = st.columns(2)

        with col1:

            st.info(
                f"""
**Best Month:** {sales_summary['best_month']}

**Revenue:** ${sales_summary['best_month_revenue']:,.2f}
"""
            )

        with col2:

            st.info(
                f"""
**Best Day:** {daily_summary['best_day']}

**Revenue:** ${daily_summary['best_day_revenue']:,.2f}
"""
            )