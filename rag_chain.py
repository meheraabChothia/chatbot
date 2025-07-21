from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from observer import get_callbacks
from retriever import build_vectorstore

def build_qa_chain():
    llm = ChatOpenAI(temperature=0, callbacks=get_callbacks())

    vectorstore = build_vectorstore()
    retriever = vectorstore.as_retriever()

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a helpful assistant who ONLY answers questions based on the document:

"Seven Habits of Effective Text Editing" by Bram Moolenaar.

Always try to relate the user question to the document. If absolutely nothing is relevant, say:

"I'm sorry, but that information is not covered in the document."

Context:
{context}

Question:
{question}

Answer:"""
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt_template},
        callbacks=get_callbacks()
    )

    return qa_chain, vectorstore
