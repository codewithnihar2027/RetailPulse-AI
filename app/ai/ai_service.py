from app.ai.context_builder import ContextBuilder
from app.ai.prompt_builder import PromptBuilder
from app.ai.llm_provider import LLMProvider


class AIService:
    """
    Core AI service that coordinates the
    AI Business Copilot workflow.
    """

    @staticmethod
    def ask(question: str):

        context = ContextBuilder.build()

        if context is None:
            return "No dataset has been uploaded."

        prompt = PromptBuilder.build(
            context=context,
            question=question
        )

        response = LLMProvider.generate(prompt)

        return response