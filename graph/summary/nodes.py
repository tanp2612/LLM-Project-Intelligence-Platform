from agents.summary_agent import SummaryAgent

from rag.retriever import retrieve_context


def retrieve_node(state):

    documents = retrieve_context(
        query=state["question"],
        k=10,
    )

    state["documents"] = documents

    return state


def summary_node(state):

    agent = SummaryAgent()

    result = agent.run(
        docs=state["documents"]
    )

    state["summary"] = result.response

    return state