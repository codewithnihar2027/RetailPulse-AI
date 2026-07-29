import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "gemini"
    )

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY"
    )

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.0-flash"
    )

    OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
    )

    OPENROUTER_MODEL = os.getenv(
        "OPENROUTER_MODEL",
        "deepseek/deepseek-chat"
    )