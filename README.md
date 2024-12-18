# Interview Preparation Assistant

The **Interview Preparation Assistant** is a tool designed to help users prepare for job interviews by generating personalized questions based on uploaded documents and providing feedback on their answers. This project uses **LangChain**, **Pinecone**, and **Google Generative AI** to implement Retrieval-Augmented Generation (RAG) for interview preparation.

## Features

- **Document Upload**: Users can upload PDFs or Word documents with interview-related content.
- **Question Generation**: The tool generates personalized behavioral and situational interview questions based on the uploaded documents.
- **Answer Submission**: Users can submit their answers to the generated questions.
- **Feedback**: The system provides feedback on the user's answers and suggestions for improvement.

## Tech Stack

- **LangChain**: For natural language processing and integration with external tools.
- **Pinecone**: For storing and querying document embeddings.
- **Google Generative AI**: To generate embeddings and assist in generating interview questions.
- **Streamlit**: For the web interface to interact with users.
- **Python**: For backend logic and integration.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/interview-prep-assistant.git
2. **Navigate to the project directory:**:
   ```bash
   cd interview-prep-assistant
3. **Install Pipenv (if you don't have it installed already):**:
   ```bash
   pip install pipenv
4. **Install the dependencies using Pipenv:**:
   ```bash
   pipenv install
5. **Activate the virtual environment:**:
   ```bash
   pipenv shell
6. **Set up environment variables: Create a .env file in the root directory and add your environment variables:**:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   INDEX_NAME=your_pinecone_index_name
## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app/main.py
2. **Upload a document** (PDF or Word) containing interview-related content.
  
3. **Generate a Question**: Click the "Generate a Question" button to receive a personalized interview question based on the uploaded document.
  
4. **Submit an Answer**: Type your response in the text area and click "Submit Answer" to get feedback.

# Project Structure

```bash
interview-prep-assistant/
├── app/
│   ├── __init__.py
│   ├── main.py              # Streamlit UI and logic
│   ├── generate_questions.py # Logic for generating interview questions
│   ├── upload.py            # File upload and processing logic
│   ├── feedback.py          # Logic for providing feedback on answers
├── .env                     # Environment variables
├── Pipfile                  # Pipenv dependency file
├── Pipfile.lock             # Pipenv lock file
├── README.md                # Project overview
└── .gitignore               # Git ignore file
```

## Future Improvements

- **Add More Question Types**: Expand question generation to cover more types of interview questions (technical, situational, etc.).
- **Multilingual Support**: Enable the system to support multiple languages for a more diverse user base.
- **Analytics Dashboard**: Provide analytics to track progress over time in interview preparation.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

