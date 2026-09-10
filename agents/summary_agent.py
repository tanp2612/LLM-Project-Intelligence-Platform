from langchain_core.prompts import ChatPromptTemplate

from agents.base_agent import BaseAgent
from schemas.summary import SummaryOutput

class SummaryAgent(BaseAgent):

    QUERY = (
        "Provide an overall summary of the project including "
        "development objective, components, financing and outcomes."
    )

    PROMPT = ChatPromptTemplate.from_template(
        """
You are an AI Project Intelligence Assistant.

Use ONLY the provided project documents.

Generate an executive summary with the following sections:

1. Project Overview
2. Development Objective
3. Key Components
4. Financing
5. Expected Outcomes

If information is unavailable, explicitly state that.

Context:
{context}
"""
    )

    @property
    def OUTPUT_SCHEMA(self):
        return SummaryOutput