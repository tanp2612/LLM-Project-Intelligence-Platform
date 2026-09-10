from pydantic import BaseModel
from typing import List


class SummaryOutput(BaseModel):
    executive_summary: str

    key_objectives: List[str]

    major_highlights: List[str]

    current_status: str

    conclusion: str