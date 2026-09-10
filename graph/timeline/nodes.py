from agents.timeline_agent import TimelineAgent

from rag.retriever import retrieve_context


def retrieve_node(state):

    documents = retrieve_context(
        query=state["question"],
        k=10,
    )

    state["documents"] = documents

    return state


def timeline_node(state):

    agent = TimelineAgent()

    result = agent.run(
        docs=state["documents"]
    )

    state["timeline"] = result.response

    return state