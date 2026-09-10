from langgraph.graph import StateGraph, START, END
from memory.checkpointer import checkpointer

from graph.procurement.state import ProcurementState
from graph.procurement.nodes import (
    retrieve_node,
    procurement_node,
)

builder = StateGraph(ProcurementState)

builder.add_node("retrieve", retrieve_node)
builder.add_node("procurement", procurement_node)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "procurement")
builder.add_edge("procurement", END)

procurement_graph = builder.compile(
    checkpointer=checkpointer
)