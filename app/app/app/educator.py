from fastapi import APIRouter
from schemas.educator import LessonRequest, LessonResponse

router = APIRouter()

@router.post("/generate_lesson", response_model=LessonResponse)
def generate_lesson(request: LessonRequest):
    # Mocked lesson generation
    return LessonResponse(
        lesson_title=f"Lesson aligned to {request.standard}",
        activities=[
            "Warm-up discussion",
            "Hands-on experiment",
            "Group reflection"
        ],
        assessment="Quiz on key concepts"
    )
