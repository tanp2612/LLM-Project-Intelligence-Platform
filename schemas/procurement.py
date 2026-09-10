from pydantic import BaseModel
from typing import List


class ProcurementItem(BaseModel):
    package: str

    status: str

    remarks: str


class ProcurementOutput(BaseModel):
    procurement_summary: str

    packages: List[ProcurementItem]

    issues: List[str]

    recommendations: List[str]