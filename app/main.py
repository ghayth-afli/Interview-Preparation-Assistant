# app/main.py
import streamlit as st
from upload import upload_and_process_file
from generate_questions import generate_question
from feedback import provide_feedback

# Streamlit UI elements
st.title("Interview Preparation Assistant")

# Use session state to track the generated question and feedback
if "generated_question" not in st.session_state:
    st.session_state.generated_question = None
if "feedback" not in st.session_state:
    st.session_state.feedback = None

# File uploader
uploaded_file = st.file_uploader("Upload your interview documents", type=["pdf", "docx"])

if uploaded_file is not None:
    # Upload and process the file
    num_chunks, texts = upload_and_process_file(uploaded_file)
    st.write(f"Created {num_chunks} chunks from the document.")

    # Generate a question
    if st.button("Generate a Question"):
        st.session_state.generated_question = generate_question(
            "Generate a challenging interview question based on the uploaded content."
        )
        st.session_state.feedback = None  # Reset feedback when a new question is generated

    # Display the generated question (if any)
    if st.session_state.generated_question:
        st.write("Generated Question:", st.session_state.generated_question)

        # Text area for user to type their answer
        user_answer = st.text_area("Your Answer", placeholder="Type your answer here...")

        # Submit button to provide feedback
        if st.button("Submit Answer"):
            if user_answer.strip():
                st.session_state.feedback = provide_feedback(user_answer)
            else:
                st.warning("Please type an answer before submitting.")

        # Display feedback (if any)
        if st.session_state.feedback:
            st.write("Feedback on your answer:", st.session_state.feedback)
