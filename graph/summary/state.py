from typing import List
from typing_extensions import TypedDict

from langchain_core.documents import Document

from schemas.summary import SummaryOutput


class SummaryState(TypedDict):

    question: str

    documents: List[Document]

    summary: SummaryOutput