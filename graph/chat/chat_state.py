from typing import Annotated, List

from typing_extensions import TypedDict

from langchain_core.documents import Document
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class ChatState(TypedDict):

    question: str

    messages: Annotated[List[BaseMessage], add_messages]

    documents: List[Document]

    response: str