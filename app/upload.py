import os
import fitz
from docx import Document
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
load_dotenv()
def extract_pdf_text(file_path):
    """Extracts text from a PDF file."""
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def extract_word_text(file_path):
    """Extracts text from a Word (.docx) file."""
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def upload_and_process_file(uploaded_file):
    """Processes uploaded PDF or Word files and ingests content into Pinecone."""
    # Save the uploaded file to a temporary location
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(uploaded_file.getbuffer())

    # Extract content based on file type
    if uploaded_file.type == "application/pdf":
        document_content = extract_pdf_text(temp_file_path)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        document_content = extract_word_text(temp_file_path)
    else:
        raise ValueError("Unsupported file type")

    # Clean up temporary file
    os.remove(temp_file_path)

    # Split the content into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1913, chunk_overlap=0)
    texts = text_splitter.split_text(document_content)

    # Generate embeddings and ingest into Pinecone
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    PineconeVectorStore.from_texts(texts, embeddings, index_name=os.environ.get("INDEX_NAME"))

    return len(texts), texts
