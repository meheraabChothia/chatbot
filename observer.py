from langfuse.langchain import CallbackHandler
from langchain.callbacks import StdOutCallbackHandler

def get_callbacks():
    return [
        CallbackHandler(),
        StdOutCallbackHandler()
    ]