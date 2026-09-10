from pydantic import BaseModel
from typing import List

from schemas.common import Severity


class RiskItem(BaseModel):
    risk: str

    severity: Severity

    mitigation: str


class RiskOutput(BaseModel):
    overall_risk: str

    risks: List[RiskItem]

    recommendations: List[str]