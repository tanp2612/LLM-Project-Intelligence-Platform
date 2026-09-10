from graph.chat.chat_workflow import chat_graph

from graph.summary.workflow import summary_graph
from graph.risk.risk_workflow import risk_graph
from graph.timeline.workflow import timeline_graph
from graph.procurement.workflow import procurement_graph
from graph.health.workflow import health_graph


class ConversationManager:

    def handle_chat(
        self,
        question: str,
        thread_id: str = "demo"    
        ):

        state = {
                "question": question,
                "messages": [],
                "documents": [],
                "response": "",
                }

        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }

        result = chat_graph.invoke(
            state,
            config=config,
        )

        return result["response"]

    def handle_summary(
        self,
        thread_id: str,
    ):

        state = {
            "question": "Generate Executive Summary",
            "documents": [],
            "summary": None,
        }

        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }

        result = summary_graph.invoke(
            state,
            config=config,
        )

        return result["summary"]

    def handle_risk(
        self,
        thread_id: str,
    ):

        state = {
            "question": "Generate Risk Analysis",
            "documents": [],
            "risk": None,
        }

        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }

        result = risk_graph.invoke(
            state,
            config=config,
        )

        return result["risk"]

    def handle_timeline(
        self,
        thread_id: str,
    ):

        state = {
            "question": "Generate Timeline Analysis",
            "documents": [],
            "timeline": None,
        }

        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }

        result = timeline_graph.invoke(
            state,
            config=config,
        )

        return result["timeline"]

    def handle_procurement(
        self,
        thread_id: str,
    ):

        state = {
            "question": "Generate Procurement Analysis",
            "documents": [],
            "procurement": None,
        }

        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }

        result = procurement_graph.invoke(
            state,
            config=config,
        )

        return result["procurement"]

    def handle_health(
        self,
        thread_id: str,
    ):

        state = {
            "question": "Generate AI Project Health Report",
            "documents": [],
            "summary": None,
            "risk": None,
            "timeline": None,
            "procurement": None,
            "health_score": None,
        }

        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }

        result = health_graph.invoke(
            state,
            config=config,
        )

        return result["health_score"]