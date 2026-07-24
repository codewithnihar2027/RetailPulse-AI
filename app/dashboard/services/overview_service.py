from app.dashboard.services.dashboard_session import DashboardSession


class OverviewService:

    @staticmethod
    def get_summary():

        if not DashboardSession.has_dataset():
            return None

        result = DashboardSession.get_pipeline_result()

        return result["analytics"]