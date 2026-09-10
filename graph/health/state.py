from typing import Any, List
from typing_extensions import TypedDict

from schemas.summary import SummaryOutput
from schemas.risk import RiskOutput
from schemas.timeline import TimelineOutput
from schemas.procurement import ProcurementOutput
from schemas.health import HealthOutput


class HealthState(TypedDict):

    question: str

    documents: List[Any]

    summary: SummaryOutput

    risk: RiskOutput

    timeline: TimelineOutput

    procurement: ProcurementOutput

    health_score: HealthOutput