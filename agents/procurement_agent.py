from langchain_core.prompts import ChatPromptTemplate

from agents.base_agent import BaseAgent
from schemas.procurement import ProcurementOutput


class ProcurementAgent(BaseAgent):

    QUERY = (
        "Analyze procurement activities, contract packages, "
        "procurement issues and recommendations."
    )

    PROMPT = ChatPromptTemplate.from_template(
        """
You are a World Bank Procurement Specialist.

Use ONLY the provided project documents.

Generate:

- Procurement Summary
- Procurement Packages
- Procurement Issues
- Recommendations

If information is unavailable, explicitly state that.

Context:
{context}
"""
    )

    @property
    def OUTPUT_SCHEMA(self):
        return ProcurementOutput