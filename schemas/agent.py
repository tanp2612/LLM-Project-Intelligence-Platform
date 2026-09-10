from typing import Any, List

from langchain_core.documents import Document
from pydantic import BaseModel


class AgentResult(BaseModel):
    response: Any
    sources: List[Document]