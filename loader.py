from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from config import PDF_PATH, CHUNK_SIZE, CHUNK_OVERLAP

def load_and_split_pdf():
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    return splitter.split_documents(docs)
