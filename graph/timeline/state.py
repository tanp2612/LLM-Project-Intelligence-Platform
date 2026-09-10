from typing import List
from typing_extensions import TypedDict

from langchain_core.documents import Document

from schemas.timeline import TimelineOutput


class TimelineState(TypedDict):

    question: str

    documents: List[Document]

    timeline: TimelineOutput