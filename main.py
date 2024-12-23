import os
from dotenv import load_dotenv
import streamlit as st
from app.upload import upload_and_process_file
from app.agents.interview_agent import get_interview_agent

st.title("AI Interview Preparation Assistant")
load_dotenv()

# Initialize agent
agent = get_interview_agent()

# Initialize session state variables
if "generated_question" not in st.session_state:
    st.session_state.generated_question = None
if "feedback" not in st.session_state:
    st.session_state.feedback = None

# File uploader
uploaded_file = st.file_uploader("Upload your interview documents", type=["pdf", "docx"])

if uploaded_file:
    # Process the file
    num_chunks, texts = upload_and_process_file(uploaded_file)
    st.write(f"Document processed into {num_chunks} chunks.")

    # Generate a question
    if st.button("Generate a Question"):
        st.session_state.generated_question = agent.run(
            "Generate an interview question based on the uploaded content."
        )
        st.session_state.feedback = None

    # Display the generated question
    if st.session_state.generated_question:
        st.write("Generated Question:", st.session_state.generated_question)

        # Answer input
        user_answer = st.text_area("Your Answer", placeholder="Type your answer here...")

        # Submit the answer for feedback
        if st.button("Submit Answer"):
            if user_answer.strip():  # Ensure the answer is not empty
                # Include the question in the feedback prompt
                st.session_state.feedback = agent.run(
                    f"""
                    You are an expert HR evaluator specializing in assessing interview answers. Your role is to evaluate the provided response to an interview question based on the following criteria:

                    1. **Relevance:** Does the answer address the question directly and stay on topic?
                    2. **Clarity:** Is the answer well-structured, clear, and easy to understand?
                    3. **Detail:** Does the answer provide sufficient context, examples, or evidence to support claims?
                    4. **Professionalism:** Does the response reflect a positive attitude, emotional intelligence, and professionalism?
                    5. **Impact:** Does the answer demonstrate the candidate's skills, abilities, or experiences effectively?

                    Based on these criteria, classify the answer into one of the following categories:  
                    - **Good Answer:** Fully addresses the question with clear, detailed, and professional responses. Demonstrates strong communication and problem-solving skills.  
                    - **Needs Revision:** Partially addresses the question but lacks depth, clarity, or focus. Shows potential but requires improvement.  
                    - **Bad Answer:** Fails to address the question, lacks professionalism, or demonstrates poor communication and problem-solving skills.

                    After classifying the answer, provide a brief explanation justifying your evaluation and suggest improvements if necessary.

                    **Question:** '{st.session_state.generated_question}'  
                    **Answer to Evaluate:** '{user_answer}'  

                    **Your Evaluation:**
                    """
                )

            else:
                st.warning("Please type an answer before submitting.")

        # Display feedback
        if st.session_state.feedback:
            st.write("Feedback:", st.session_state.feedback)
