from langgraph.graph import StateGraph, START, END
from memory.checkpointer import checkpointer

from graph.timeline.state import TimelineState
from graph.timeline.nodes import (
    retrieve_node,
    timeline_node,
)

builder = StateGraph(TimelineState)

builder.add_node("retrieve", retrieve_node)
builder.add_node("timeline", timeline_node)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "timeline")
builder.add_edge("timeline", END)

timeline_graph = builder.compile(
    checkpointer=checkpointer
)