import re
import unicodedata


class ResponseFormatter:

    @staticmethod
    def format(response: str):

        if not response:
            return response

        response = unicodedata.normalize("NFKC", response)

        response = re.sub(r"\n{3,}", "\n\n", response)

        response = re.sub(
            r"^Summary:",
            "## 📊 Executive Summary",
            response,
            flags=re.MULTILINE | re.IGNORECASE,
        )

        response = re.sub(
            r"^Key Findings:",
            "## 📈 Key Findings",
            response,
            flags=re.MULTILINE | re.IGNORECASE,
        )

        response = re.sub(
            r"^Recommendations:",
            "## 🎯 Recommendations",
            response,
            flags=re.MULTILINE | re.IGNORECASE,
        )

        return response