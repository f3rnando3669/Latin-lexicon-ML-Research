import Clients.AbstractClient as AbstractClient
from Prompts.PromptList import PromptList
from openai import OpenAI
from Clients.Utilities.FileUtilities import write_to_file_in_dir, write_tojson
from Clients.Utilities.StringValidation import emptyString

class ContextFreeClient(AbstractClient.ABsClient):
    """
    This Client cannot make use of context
    """
    def __init__(self, client: OpenAI, model: str) -> None:
        self._client = client
        self._model = model
    
    def generate(self, prompts: PromptList, txt_savepath: str="", json_savepath:str = "") -> str:
        """
        Enter a list of prompts\n
        You may also specify a savepath for a txt file\n
        Or a savepath for a json file
        """
        if len(prompts) == 0:
            raise Exception("Empty Prompt List...")
            
        messages = prompts.unpack()
        # print(messages)
        generated = self._client.chat.completions.create(
            messages=messages,
            model=self._model
        )
        response = generated.choices[0].message.content

        if not emptyString(txt_savepath):
            self._txtsave(txt_savepath, response)
        
        if not emptyString(json_savepath):
            jsonbuild = [response]
            self._jsonsave(json_savepath, jsonbuild)

        return response

    def _txtsave(self, path, data) -> None:
        write_to_file_in_dir(path, data)
    
    def _jsonsave(self, path, data):
        write_tojson(path, data)