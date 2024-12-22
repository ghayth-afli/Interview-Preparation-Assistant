import os
from dotenv import load_dotenv
import streamlit as st
from app.upload import upload_and_process_file
from app.agents.interview_agent import get_interview_agent

st.title("AI Interview Preparation Assistant")
load_dotenv()

# Initialize agent
agent = get_interview_agent()

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

    # Use agent to generate a question
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

        # Submit answer
        if st.button("Submit Answer"):
            if user_answer.strip():
                st.session_state.feedback = agent.run(
                    f"Provide feedback on this answer: {user_answer}"
                )
            else:
                st.warning("Please type an answer before submitting.")

        # Display feedback
        if st.session_state.feedback:
            st.write("Feedback:", st.session_state.feedback)
