from typing import List
import openai
from ClientUtils.StringValidation import emptyString
from utilities import write_tocsv, read_fromcsv

class Client:
    """
    model object
    """
    def __init__(self, model="gpt-4o") -> None:
        self._key = ""
        self._client = openai.OpenAI(api_key=self._key)
        self._model = model
        self._messages = []

    def is_prompt(self, prompts) -> bool:
        """
        check the validity of each prompt in prompts\n
        prevents submission of empty prompts
        """
        for message, flag in prompts.unwrap_copy():
            if not emptyString(message):
                self._messages.append([message, flag])
            else:
                return False
        return True

    def quick(self) -> str:
        """
        have a quick conversation with the model\n
        would require user input when called\n
        N/B: clears all previous prompts
        """
        self.clear()
        message = input("Prompt: ")
        if self.is_prompt([message]):
            return self._generate(self._messages)
        else:
            ValueError("Use an actual prompt\nAPI requests are expensive")
            exit(-1)
    
    def generate_using_prompts(self, savepath, prompts) -> str:
        """
        have a conversation with the model using pre-made prompts\n
        N/B: clears all previous prompts
        """
        self.clear()
        if self.is_prompt(prompts):
            generated = self._generate(self._messages)
            self._save(savepath, generated)
            return generated
        else:
            ValueError("Use an actual prompt\nAPI requests are expensive")
            exit(-1)
    
    def _save(path, text) -> None:
        write_tocsv(path, text)
    
    def load(path) -> List[List[str]]:
        return read_fromcsv(path)

    def _generate(self, messages) -> str:
        """
        send request to model api for conversation
        """
        refined_messages = self.quick_refine(messages)
        
        chat_completion = self._client.chat.completions.create(
            messages=refined_messages,
            model= self._model
        )

        return chat_completion.choices[0].message.content
    
    def quick_refine(self, messages) -> List[str]:
        """
        create template from model conversation
        """
        refined_messages = []
        for pair in messages:
            message, flag =  pair
            if flag == 0:
                refined_messages.append(
                    {
                        "role": "user",
                        "content": message
                    }
                )
            elif flag == 1:
                refined_messages.append(
                    {
                        "role": "system",
                        "content": message
                    }
                )
        return refined_messages
    
    def clear(self) -> None:
        """
        remove all prompts for the client
        """
        self._messages.clear()