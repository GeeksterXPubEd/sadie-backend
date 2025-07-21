from fastapi import FastAPI
from app import student, educator, progress, feedback, gamification

app = FastAPI(title="Sadie Backpack")

app.include_router(student.router, prefix="/student", tags=["Student"])
app.include_router(educator.router, prefix="/educator", tags=["Educator"])
app.include_router(progress.router, prefix="/student", tags=["Progress"])
app.include_router(feedback.router, prefix="/student", tags=["Feedback"])
app.include_router(gamification.router, prefix="/gamification", tags=["Gamification"])
