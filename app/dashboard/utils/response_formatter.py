import re


class ResponseFormatter:

    @staticmethod
    def format(response: str) -> str:
        """
        Convert common AI headings into richer markdown.
        """

        if not response:
            return response

        response = re.sub(
            r"^Summary:",
            "## 📊 Executive Summary",
            response,
            flags=re.MULTILINE,
        )

        response = re.sub(
            r"^Key Findings:",
            "## 📈 Key Findings",
            response,
            flags=re.MULTILINE,
        )

        response = re.sub(
            r"^Recommendations:",
            "## 🎯 Recommendations",
            response,
            flags=re.MULTILINE,
        )

        return response