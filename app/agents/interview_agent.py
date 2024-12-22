import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_google_genai import GoogleGenerativeAI
from app.tools.generate_interview_question import generate_interview_question_tool
from app.tools.provide_feedback import provide_feedback_tool

load_dotenv()
# Initialize LLM
llm = GoogleGenerativeAI(
    temperature=0.7,
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

# Define tools
tools = [
    Tool(
        name="Generate Interview Question",
        func=generate_interview_question_tool,
        description="Generate interview questions based on content.",
    ),
    Tool(
        name="Provide Feedback",
        func=provide_feedback_tool,
        description="Provide feedback on user's answers.",
    ),
]

# Initialize the agent
def get_interview_agent():
    return initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True,
    )
