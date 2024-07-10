from typing import List
import openai
from Clients.ContextFreeClient import ContextFreeClient

class ClientInterface:
    """
    Client Interface\n
    Pass in the type of client you want to use\n
    By default this is set to ContextFreeClient\n
    You may also specify a model\n
    BY default this is set to gpt-4o\n
    """
    def __init__(self, client, model="gpt-4o") -> None:
        self._key = "sk-proj-zhneKzEWaF5adbdJPBPmT3BlbkFJk8yS2iJVC501GP79GVwx"
        self._model = model
        self._client = client(openai.OpenAI(api_key=self._key), model)