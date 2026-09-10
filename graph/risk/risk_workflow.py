from langgraph.graph import (
    StateGraph,
    START,
    END,
)
from memory.checkpointer import checkpointer

from graph.risk.risk_state import RiskState

from graph.risk.risk_nodes import (
    retrieve_node,
    risk_node,
)

builder = StateGraph(RiskState)

builder.add_node("retrieve", retrieve_node)
builder.add_node("risk", risk_node)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "risk")
builder.add_edge("risk", END)

risk_graph = builder.compile(
    checkpointer=checkpointer
)