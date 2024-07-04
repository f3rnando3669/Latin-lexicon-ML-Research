import Clients.AbstractClient as AbstractClient
from Prompts.PromptList import PromptList
from openai import OpenAI
from Clients.Utilities.FileUtilities import write_tofile_indir, write_tojson
from Clients.Utilities.StringValidation import emptyString

class ContextFreeClient(AbstractClient.ABsClient):
    def __init__(self, client: OpenAI, model: str) -> None:
        self._client = client
        self._model = model
    
    def generate(self, prompts: PromptList, savepath: str="", json_savepath:str = "") -> str:
        if len(prompts) == 0:
            raise Exception("Empty Prompt List...")
            
        messages = prompts.unpack()
        generated = self._client.chat.completions.create(
            messages=messages,
            model=self._model
        )
        response = generated.choices[0].message.content

        if not emptyString(savepath):
            self._txtsave(savepath, response)
        
        if not emptyString(json_savepath):
            jsonbuild = [response]
            self._jsonsave(json_savepath, jsonbuild)

        return response

    def _txtsave(self, path, data) -> None:
        write_tofile_indir(path, data)
    
    def _jsonsave(self, path, data):
        write_tojson(path, data)