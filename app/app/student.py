from fastapi import APIRouter
from schemas.student import StudentAskRequest, StudentAskResponse, EssayFeedbackRequest, EssayFeedbackResponse

router = APIRouter()

@router.post("/ask", response_model=StudentAskResponse)
def ask_student(request: StudentAskRequest):
    # Mocked Socratic response
    return StudentAskResponse(
        response=f"Let's break it down: {request.question} (Grade {request.grade_level}). What do you already know about this topic?"
    )

@router.post("/essay_feedback", response_model=EssayFeedbackResponse)
def essay_feedback(request: EssayFeedbackRequest):
    # Mocked cognitive feedback
    return EssayFeedbackResponse(
        feedback="Your essay shows strong analytic thinking but could use more creative connections. Try relating the topic to real-world experiences."
    )
