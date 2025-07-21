from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from loader import load_and_split_pdf

def build_vectorstore():
    splits = load_and_split_pdf()
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(splits, embeddings)
    return vectorstore
