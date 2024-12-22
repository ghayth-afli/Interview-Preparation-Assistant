import os
from dotenv import load_dotenv
from app.generate_questions import generate_question

load_dotenv()
def generate_interview_question_tool(context: str) -> str:
    """Tool to generate interview questions based on context."""
    return generate_question(context)
