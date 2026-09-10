from agents.risk_agent import RiskAgent

from rag.retriever import retrieve_context


def retrieve_node(state):

    documents = retrieve_context(
        query=state["question"],
        k=10,
    )

    state["documents"] = documents

    return state


def risk_node(state):

    agent = RiskAgent()

    result = agent.run(
        docs=state["documents"]
    )

    state["risk"] = result.response

    return state