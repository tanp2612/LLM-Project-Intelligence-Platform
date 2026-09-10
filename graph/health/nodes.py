from agents.summary_agent import SummaryAgent
from agents.risk_agent import RiskAgent
from agents.timeline_agent import TimelineAgent
from agents.procurement_agent import ProcurementAgent
from agents.health_score_agent import HealthScoreAgent

from rag.retriever import retrieve_context


def retrieve_node(state):

    docs = retrieve_context(
        state["question"],
        k=10,
    )

    state["documents"] = docs

    return state


def summary_node(state):

    agent = SummaryAgent()

    result = agent.run(
        docs=state["documents"]
    )

    state["summary"] = result.response

    return state


def risk_node(state):

    agent = RiskAgent()

    result = agent.run(
        docs=state["documents"]
    )

    state["risk"] = result.response

    return state


def timeline_node(state):

    agent = TimelineAgent()

    result = agent.run(
        docs=state["documents"]
    )

    state["timeline"] = result.response

    return state


def procurement_node(state):

    agent = ProcurementAgent()

    result = agent.run(
        docs=state["documents"]
    )

    state["procurement"] = result.response

    return state


def health_node(state):

    agent = HealthScoreAgent()

    result = agent.generate_health_score(
        summary=state["summary"],
        timeline=state["timeline"],
        risk=state["risk"],
        procurement=state["procurement"],
        documents=state["documents"],
    )

    state["health_score"] = result

    return state