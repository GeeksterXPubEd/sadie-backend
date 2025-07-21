from pydantic import BaseModel
from typing import List

class ProgressUpdateRequest(BaseModel):
    student_id: str
    task: str
    score: int
    time_spent_minutes: int
    badges_earned: List[str]

class ProgressUpdateResponse(BaseModel):
    status: str
    badges: List[str]
    total_score: int
