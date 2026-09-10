from typing import List
from typing_extensions import TypedDict

from langchain_core.documents import Document

from schemas.risk import RiskOutput


class RiskState(TypedDict):

    question: str

    documents: List[Document]

    risk: RiskOutput