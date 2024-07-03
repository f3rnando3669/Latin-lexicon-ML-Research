import Clients.AbstractClient as AbstractClient
from Prompts.PromptList import PromptList
from openai import OpenAI
from Utilities.FileUtilities import write_tofile_indir
from Utilities.StringValidation import emptyString

class ContextTightClient(AbstractClient.ABsClient):
    def __init__(self, client: OpenAI, model: str) -> None:
        self._client = client
        self._model = model
    
    def generate(self, context: PromptList, prompts: PromptList, savepath: str="") -> str:
        unpacked_context = context.unpack()
        messages = prompts.unpack()
        composite = unpacked_context + messages

        generated = self._client.chat.completions.create(
            messages=composite,
            model=self._model
        )
        response = generated.choices[0].message.content

        if not emptyString(savepath):
            prior = ""

            for prompt in unpacked_context:
                # prior += 
            self._save(savepath, prompt+"\n"+response)

        return response

    def _save(self, path, data) -> None:
        write_tofile_indir(path, data)
        # also write to csv