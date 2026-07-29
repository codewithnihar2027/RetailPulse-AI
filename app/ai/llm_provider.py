from app.ai.providers.llm_factory import LLMFactory


class LLMProvider:

    @staticmethod
    def generate(prompt: str) -> str:

        provider = LLMFactory.get_provider()

        return provider.generate(prompt)