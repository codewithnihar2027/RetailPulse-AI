from app.ai.ai_service import AIService
from app.dashboard.services.dashboard_session import DashboardSession


class DashboardAIService:

    @staticmethod
    def ask(question: str):

        if not question.strip():
            return "Please enter a business question."

        response = AIService.ask(question)

        DashboardSession.set_latest_ai_response(
            question,
            response
        )

        DashboardSession.add_ai_history(
            question,
            response
        )

        return response

    @staticmethod
    def history():

        return DashboardSession.get_ai_history()