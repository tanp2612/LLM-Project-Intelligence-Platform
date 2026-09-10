from enum import Enum
from pydantic import BaseModel


class HealthStatus(str, Enum):
    GOOD = "Good"
    MODERATE = "Moderate"
    CRITICAL = "Critical"


class Severity(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Recommendation(BaseModel):
    title: str
    description: str