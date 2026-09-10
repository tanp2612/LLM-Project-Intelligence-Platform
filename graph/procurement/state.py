from typing import List
from typing_extensions import TypedDict

from langchain_core.documents import Document

from schemas.procurement import ProcurementOutput


class ProcurementState(TypedDict):

    question: str

    documents: List[Document]

    procurement: ProcurementOutput