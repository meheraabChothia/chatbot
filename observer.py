from langfuse.langchain import LangfuseCallbackHandler
from langchain.callbacks import StdOutCallbackHandler

def get_callbacks():
    return [
        LangfuseCallbackHandler(),
        StdOutCallbackHandler()
    ]