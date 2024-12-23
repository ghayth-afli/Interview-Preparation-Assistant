import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
load_dotenv()

def provide_feedback(user_answer):
    llm = GoogleGenerativeAI(
        temperature=0,
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

    feedback_prompt = f"As an HR expert with deep knowledge of behavioral and situational interviewing techniques, critically evaluate the following response. Provide detailed feedback on its strengths and weaknesses, suggest specific areas for improvement, and recommend a revised version to better align with best practices for effective communication and showcasing skills: {user_answer}"
    feedback_response = llm.invoke(feedback_prompt)

    return feedback_response
