from langgraph.graph import StateGraph, START, END
from memory.checkpointer import checkpointer

from graph.chat.chat_state import ChatState
from graph.chat.chat_nodes import (
    retrieve_node,
    chat_node,
)


builder = StateGraph(ChatState)

builder.add_node("retrieve", retrieve_node)
builder.add_node("chat", chat_node)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "chat")
builder.add_edge("chat", END)

chat_graph = builder.compile(
    checkpointer=checkpointer
)