from typing import List
import openai
from ContextFreeClient import ContextFreeClient

class Client:
    """
    model object
    """
    def __init__(self, model="gpt-4o", client=ContextFreeClient) -> None:
        self._key = "sk-proj-zhneKzEWaF5adbdJPBPmT3BlbkFJk8yS2iJVC501GP79GVwx"
        self._model = model
        self._client = client(openai.OpenAI(api_key=self._key), model)