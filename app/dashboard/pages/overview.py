import streamlit as st

from app.dashboard.services.dashboard_session import DashboardSession
from app.dashboard.components.kpi_card import KPICard

class OverviewPage:

    @staticmethod
    def render():

        st.title("🏠 Executive Overview")

        if not DashboardSession.has_dataset():

            st.warning("Please upload a dataset first.")

            return

        result = DashboardSession.get_pipeline_result()

        analytics = result["analytics"]

        kpis = analytics["kpis"]

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

        monthly_sales = analytics["monthly_sales"]

        
        from app.dashboard.components.charts.line_chart import LineChart

        LineChart.render(
            monthly_sales,
            "Monthly Revenue"
        )

        st.divider()

        st.subheader("📊 Monthly Growth (%)")

        monthly_growth = analytics["monthly_growth"]

        from app.dashboard.components.charts.bar_chart import BarChart

        BarChart.render(
            monthly_growth,
            "Monthly Growth"
        )

        st.divider()

        st.subheader("🏆 Business Highlights")

        sales_summary = analytics["sales_summary"]

        daily_summary = analytics["daily_summary"]

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