from agents.procurement_agent import ProcurementAgent

from rag.retriever import retrieve_context


def retrieve_node(state):

    documents = retrieve_context(
        query=state["question"],
        k=10,
    )

    state["documents"] = documents

    return state


def procurement_node(state):

    agent = ProcurementAgent()

    result = agent.run(
        docs=state["documents"]
    )

    state["procurement"] = result.response

    return state