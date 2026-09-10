from langchain_core.prompts import ChatPromptTemplate

from agents.base_agent import BaseAgent
from schemas.timeline import TimelineOutput


class TimelineAgent(BaseAgent):

    QUERY = (
        "Extract project timeline, milestones, implementation progress "
        "and future activities."
    )

    PROMPT = ChatPromptTemplate.from_template(
        """
You are a World Bank Project Timeline Specialist.

Use ONLY the provided project documents.

Generate:

- Current Project Phase
- Major Milestones
- Upcoming Activities
- Schedule Status

If information is unavailable, explicitly state that.

Context:
{context}
"""
    )

    @property
    def OUTPUT_SCHEMA(self):
        return TimelineOutput