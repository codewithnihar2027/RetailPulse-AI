from google import genai

from app.config.settings import Config
from app.ai.providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    def generate(self, prompt: str) -> str:

        if not Config.GEMINI_API_KEY:
            return (
                "❌ Gemini API key not configured."
            )

        try:

            client = genai.Client(
                api_key=Config.GEMINI_API_KEY
            )

            response = client.models.generate_content(
                model=Config.GEMINI_MODEL,
                contents=prompt,
            )

            return response.text

        except Exception as e:

            return f"❌ Gemini Error:\n\n{str(e)}"