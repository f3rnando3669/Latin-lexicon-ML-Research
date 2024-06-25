from typing import List
import re
import openai

class Client:
    """
    model object
    """
    def __init__(self, model="gpt-4o") -> None:
        self._key = "sk-proj-zhneKzEWaF5adbdJPBPmT3BlbkFJk8yS2iJVC501GP79GVwx"
        self._client = openai.OpenAI(api_key=self._key)
        self._model = model
        self._messages = []

    def is_prompt(self, prompts) -> bool:
        """
        check the validity of each prompt in prompts\n
        prevents submission of empty prompts
        """
        # print(prompts.unwrap_copy(), "unwrap")
        for message, flag in prompts.unwrap_copy():
            # print(message, flag, "wrapped")
            if message:
                # print(message, flag, "btuhrhrhh")
                if re.match(r"[a-zA-Z0-9]+", message):
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
    
    def generate_using_prompts(self, prompts) -> str:
        """
        have a conversation with the model using pre-made prompts\n
        N/B: clears all previous prompts
        """
        self.clear()
        if self.is_prompt(prompts):
            # print(self._messages)
            return self._generate(self._messages)
        else:
            ValueError("Use an actual prompt\nAPI requests are expensive")
            exit(-1)
    
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
        # print(messages)
        for pair in messages:
            message, flag =  pair
            # print(message, flag)
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
        # exit()
        return refined_messages
    
    def clear(self) -> None:
        """
        remove all prompts for the client
        """
        self._messages.clear()