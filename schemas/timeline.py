from pydantic import BaseModel
from typing import List


class Milestone(BaseModel):
    milestone: str

    status: str

    expected_date: str


class TimelineOutput(BaseModel):
    project_phase: str

    milestones: List[Milestone]

    upcoming_activities: List[str]

    schedule_status: str