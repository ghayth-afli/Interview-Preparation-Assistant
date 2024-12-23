import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

def generate_question(context_instruction="Generate a behavioral interview question"):
    """Generates a question based on the uploaded content."""
    # Initialize embeddings and language model
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    llm = GoogleGenerativeAI(
        temperature=0.7,
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

    # Load the vectorstore to retrieve relevant context
    vectorstore = PineconeVectorStore(index_name=os.environ["INDEX_NAME"], embedding=embeddings)

    # Define the prompt for generating interview questions
    template = """As an HR expert, Use the following pieces of context to generate an interview question.
    The question should be behavioral, situational, and focused on personal experiences and skills.
    If there's no relevant context, use the instruction to craft the question.

    Context:
    {context}
    """

    custom_question_prompt = PromptTemplate.from_template(template)

    # Retrieve relevant context from vectorstore (simulate a general query for now)
    retrieved_context = vectorstore.as_retriever().get_relevant_documents("Commonly Asked Interview Questions")

    # Combine the retrieved context into a single string
    formatted_context = "\n\n".join([doc.page_content for doc in retrieved_context])

    # Fix the chain by properly passing both context and the instruction
    rag_chain = (
            {
                "context": lambda x: formatted_context
            }
            | custom_question_prompt
            | llm
    )

    # Invoke the chain with the provided instruction
    question = rag_chain.invoke({
        "context": formatted_context
    })
    return question
