from langgraph.graph import StateGraph, START, END
from memory.checkpointer import checkpointer

from graph.summary.state import SummaryState
from graph.summary.nodes import (
    retrieve_node,
    summary_node,
)

builder = StateGraph(SummaryState)

builder.add_node("retrieve", retrieve_node)
builder.add_node("summary", summary_node)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "summary")
builder.add_edge("summary", END)

summary_graph = builder.compile(
    checkpointer=checkpointer
)