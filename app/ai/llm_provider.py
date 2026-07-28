from google import genai

from app.config.settings import Config


class LLMProvider:
    """
    Gemini LLM Provider.

    This class is responsible only for
    communicating with the language model.
    """

    @staticmethod
    def generate(prompt: str) -> str:

        if not Config.GEMINI_API_KEY:
            return (
                "❌ Gemini API key not found.\n\n"
                "Please configure GEMINI_API_KEY in your .env file."
            )

        try:
            client = genai.Client(
                api_key=Config.GEMINI_API_KEY
            )

            print("Loaded model:", repr(Config.GEMINI_MODEL))

            response = client.models.generate_content(
                model="models/gemini-2.5-pro",
                contents="Reply with exactly: OK"
            )

            print(response)

            return response.text

        except Exception as e:
            message = str(e)

            if "RESOURCE_EXHAUSTED" in message or "429" in message:
                return (
                    "⚠️ Gemini API quota exceeded.\n\n"
                    "Please try again later or use a different Gemini model/API key."
                )

            return f"❌ Gemini Error:\n\n{message}"