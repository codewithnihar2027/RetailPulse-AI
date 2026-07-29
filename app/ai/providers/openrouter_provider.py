import requests

from app.ai.providers.base_provider import BaseProvider
from app.config.settings import Config


class OpenRouterProvider(BaseProvider):

    URL = "https://openrouter.ai/api/v1/chat/completions"

    def generate(self, prompt: str) -> str:

        if not Config.OPENROUTER_API_KEY:
            return (
                "❌ OpenRouter API key not configured.\n\n"
                "Please configure OPENROUTER_API_KEY in your .env file."
            )

        headers = {
            "Authorization": f"Bearer {Config.OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": Config.OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "reasoning": {
                "exclude": True
            }
        }

        try:

            print("Using Model:", Config.OPENROUTER_MODEL)

            response = requests.post(
                self.URL,
                headers=headers,
                json=payload,
                timeout=60
            )

            data = response.json()

            print("OpenRouter Response:")
            print(data)

            # Handle API errors gracefully
            if not response.ok:

                message = (
                    data.get("error", {})
                    .get("message", response.text)
                )

                return (
                    f"❌ OpenRouter Error\n\n"
                    f"{message}"
                )

            choices = data.get("choices", [])

            if not choices:
                return (
                    "❌ OpenRouter returned an empty response."
                )

            return (
                choices[0]
                .get("message", {})
                .get("content", "No response generated.")
            )

        except requests.exceptions.Timeout:

            return (
                "❌ Request timed out.\n\n"
                "Please try again."
            )

        except requests.exceptions.ConnectionError:

            return (
                "❌ Unable to connect to OpenRouter.\n\n"
                "Please check your internet connection."
            )

        except Exception as e:

            return (
                f"❌ Unexpected OpenRouter Error\n\n{str(e)}"
            )