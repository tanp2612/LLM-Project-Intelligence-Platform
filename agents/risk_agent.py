from langchain_core.prompts import ChatPromptTemplate

from agents.base_agent import BaseAgent
from schemas.risk import RiskOutput


class RiskAgent(BaseAgent):

    QUERY = (
        "Identify project implementation risks, environmental risks, "
        "financial risks, governance risks and mitigation strategies."
    )

    PROMPT = ChatPromptTemplate.from_template(
        """
You are a World Bank Risk Assessment Specialist.

Use ONLY the provided project documents.

Identify:

- Overall Project Risk
- Individual Risks
- Severity of each Risk
- Mitigation Strategy
- Recommendations

If information is unavailable, explicitly state that.

Context:
{context}
"""
    )

    @property
    def OUTPUT_SCHEMA(self):
        return RiskOutput