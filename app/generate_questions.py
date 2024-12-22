# app/generate_questions.py
import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.runnables import RunnablePassthrough

def generate_question(context_instruction="Generate a behavioral interview question"):
    """Generates a question based on the uploaded content."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    llm = GoogleGenerativeAI(
        temperature=0.7,
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

    vectorstore = PineconeVectorStore(index_name=os.environ["INDEX_NAME"], embedding=embeddings)

    # Define the prompt for generating interview questions
    template = """Use the following context to generate an interview question.
    The question should be behavioral, situational, and focused on personal experiences and skills.

    {context_instruction}

    Interview Question:"""

    custom_question_prompt = PromptTemplate.from_template(template)

    # Fix the chain by ensuring `RunnablePassthrough` wraps the input properly
    rag_chain = (
        {
            "context_instruction": RunnablePassthrough()
        }
        | custom_question_prompt
        | llm
    )

    question = rag_chain.invoke({"context_instruction": context_instruction})
    return question
