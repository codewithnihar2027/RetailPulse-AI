class PromptBuilder:
    """
    Converts business context and the user's question
    into a structured prompt for the LLM.
    """

    @staticmethod
    def build(context: dict, question: str) -> str:

        prompt = f"""
You are RetailPulse AI, an expert Retail Business Analyst.

Use ONLY the provided business context to answer.
Do not make assumptions.
If the information is unavailable, clearly say so.

========================
BUSINESS CONTEXT
========================

KPIs:
{context.get("kpis")}

Sales Summary:
{context.get("sales_summary")}

Daily Summary:
{context.get("daily_summary")}

Monthly Growth:
{context.get("monthly_growth")}

Customer Segments:
{context.get("rfm_summary")}

Top Products:
{context.get("top_products")}

Top Customers:
{context.get("top_customers")}

========================

User Question:
{question}

========================

Provide your response in the following format:

Summary:
...

Key Findings:
- ...

Recommendations:
- ...

Keep the answer concise, professional, and data-driven.
"""

        return prompt