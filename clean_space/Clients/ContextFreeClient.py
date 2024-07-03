import Clients.AbstractClient as AbstractClient
from Prompts.PromptList import PromptList
from openai import OpenAI
from Utilities.FileUtilities import write_tofile_indir
from Utilities.StringValidation import emptyString

class ContextFreeClient(AbstractClient.ABsClient):
    def __init__(self, client: OpenAI, model: str) -> None:
        self._client = client
        self._model = model
    
    def generate(self, prompts: PromptList, savepath: str="") -> str:
        messages = prompts.unpack()
        generated = self._client.chat.completions.create(
            messages=messages,
            model=self._model
        )
        response = generated.choices[0].message.content

        if not emptyString(savepath):
            self._save(savepath, response)

        return response

    def _save(self, path, data) -> None:
        write_tofile_indir(path, data)