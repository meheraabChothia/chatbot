from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from observer import get_callbacks

rephrase_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful assistant whose job is to reinterpret user questions in the context of the document titled:

"Seven Habits of Effective Text Editing" by Bram Moolenaar.

Reframe or rephrase the user's question so that it fits within the topic of the document. If no relation is possible, return: "UNRELATED".

User Question: {question}
Reframed Query:"""
)

llm = ChatOpenAI(temperature=0, callbacks=get_callbacks())

rephraser_chain = LLMChain(llm=llm, prompt=rephrase_prompt)

def rephrase_query(query: str) -> str:
    return rephraser_chain.run(query).strip()
