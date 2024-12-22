import os
from dotenv import load_dotenv
from app.feedback import provide_feedback

load_dotenv()
def provide_feedback_tool(answer: str) -> str:
    """Tool to provide feedback on user's answer."""
    return provide_feedback(answer)
