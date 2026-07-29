from app.config.settings import Config

from app.ai.providers.gemini_provider import GeminiProvider
from app.ai.providers.openrouter_provider import OpenRouterProvider


class LLMFactory:

    @staticmethod
    def get_provider():

        provider = Config.LLM_PROVIDER.lower()

        if provider == "gemini":
            return GeminiProvider()

        if provider == "openrouter":
            return OpenRouterProvider()

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )