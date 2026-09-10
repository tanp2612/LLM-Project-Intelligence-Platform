from langgraph.graph import StateGraph, START, END
from memory.checkpointer import checkpointer

from graph.health.state import HealthState

from graph.health.nodes import (
    retrieve_node,
    summary_node,
    risk_node,
    timeline_node,
    procurement_node,
    health_node,
)


builder = StateGraph(HealthState)

# Nodes
builder.add_node("retrieve", retrieve_node)
builder.add_node("summary", summary_node)
builder.add_node("risk", risk_node)
builder.add_node("timeline", timeline_node)
builder.add_node("procurement", procurement_node)
builder.add_node("health", health_node)

# Workflow
builder.add_edge(START, "retrieve")

builder.add_edge("retrieve", "summary")
builder.add_edge("summary", "risk")
builder.add_edge("risk", "timeline")
builder.add_edge("timeline", "procurement")
builder.add_edge("procurement", "health")

builder.add_edge("health", END)

# Compile graph
health_graph = builder.compile(
    checkpointer=checkpointer
)