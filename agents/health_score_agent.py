from langchain_core.prompts import ChatPromptTemplate

from rag.llm import get_structured_llm

from schemas.health import HealthOutput


class HealthScoreAgent:

    def __init__(self):

        self.llm = get_structured_llm(HealthOutput)

        self.prompt = ChatPromptTemplate.from_template(
            """
You are a Senior World Bank Project Management Expert.

You have access to two sources of information.

1. Specialist AI analyses
2. Original Project Evidence

Use the specialist analyses as the PRIMARY source.

Use the Original Project Evidence only to validate findings
or extract additional information not present in the analyses.

--------------------------------------------------

Executive Summary

{summary}

--------------------------------------------------

Timeline Analysis

{timeline}

--------------------------------------------------

Risk Analysis

{risk}

--------------------------------------------------

Procurement Analysis

{procurement}

--------------------------------------------------

Original Project Evidence

{raw_context}

--------------------------------------------------

Generate a comprehensive AI Project Health Report.

Evaluate:

1. Cost
2. Schedule
3. Scope
4. Risks
5. Compliance

For each category provide:

- Score (0-100)
- Status
- Explanation

Finally provide:

- Overall Project Health Score
- Overall Project Status
- Overall Summary
- Recommendations

Return the response using the required structured output.
"""
        )

    def generate_health_score(
        self,
        summary,
        timeline,
        risk,
        procurement,
        documents,
    ):

        raw_context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        messages = self.prompt.format_messages(
            summary=summary.model_dump_json(indent=2),
            timeline=timeline.model_dump_json(indent=2),
            risk=risk.model_dump_json(indent=2),
            procurement=procurement.model_dump_json(indent=2),
            raw_context=raw_context,
        )

        response = self.llm.invoke(messages)

        return response