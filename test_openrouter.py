import os
import requests
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "model": os.getenv("OPENROUTER_MODEL"),
        "messages": [
            {
                "role": "user",
                "content": "Reply with exactly: OpenRouter Working"
            }
        ]
    },
    timeout=60
)

print(response.status_code)
print(response.json())