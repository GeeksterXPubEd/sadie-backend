from pydantic import BaseModel

class BadgeRequest(BaseModel):
    student_id: str
    badge_name: str

class BadgeResponse(BaseModel):
    badge_awarded: str
    message: str
