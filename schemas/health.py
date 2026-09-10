from pydantic import BaseModel
from typing import List

from schemas.common import HealthStatus


class HealthMetric(BaseModel):
    score: int

    status: HealthStatus

    explanation: str


class HealthOutput(BaseModel):
    cost: HealthMetric

    schedule: HealthMetric

    scope: HealthMetric

    risks: HealthMetric

    compliance: HealthMetric

    overall_score: int

    overall_status: HealthStatus

    overall_summary: str

    recommendations: List[str]