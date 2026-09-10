from langchain_core.messages import HumanMessage, AIMessage

from graph.chat.chat_agent import ChatAgent
from rag.retriever import retrieve_context


def retrieve_node(state):

    documents = retrieve_context(
        query=state["question"],
        k=10,
    )

    return {
        "documents": documents
    }


def chat_node(state):

    agent = ChatAgent()

    messages = state.get("messages", [])

    response = agent.run(
        messages=messages + [HumanMessage(content=state["question"])],
        docs=state["documents"],
    )

    return {
        "messages": [
            HumanMessage(content=state["question"]),
            AIMessage(content=response.content),
        ],
        "response": response.content,
    }