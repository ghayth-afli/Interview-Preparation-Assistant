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

    feedback_prompt = f"Evaluate the following answer and provide suggestions for improvement: {user_answer}"
    feedback_response = llm.invoke(feedback_prompt)

    return feedback_response
