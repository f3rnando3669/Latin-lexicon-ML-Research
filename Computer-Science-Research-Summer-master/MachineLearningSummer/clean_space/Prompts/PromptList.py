from typing import Any, List
from Prompts.Prompt import Prompt

class PromptList:
    def __init__(self) -> None:
        self._promptlist: List[dict[str]] = []

    def add_userprompt(self, prompt: Prompt) -> None:
        self._promptlist.append(
            {
                "role": "user",
                "content": prompt.getprompt()
            }
        )
    
    def add_userprompts(self, prompts: List[Prompt]) -> None:
        for prompt in prompts:
            self.add_userprompt(prompt)
    
    def add_systemprompt(self, prompt: Prompt) -> None:
        self._promptlist.append(
            {
                "role": "system",
                "content": prompt.getprompt()
            }
        )
    
    def add_systemprompts(self, prompts: Prompt) -> None:
        for prompt in prompts:
            self.add_systemprompt(prompt)
    
    def __len__(self) -> int:
        return self._promptlist.__len__()
    
    def __getitem__(self, index):
        return self._promptlist[index]
    
    def pop(self, index):
        return self._promptlist.pop(index)

    def clear(self):
        self._promptlist.clear()
        
    def unpack(self) -> List[dict[str]]:
        return self._promptlist
    
    def __str__(self) -> str:
        return self._promptlist.__str__()
    
# example = PromptList()
# prompt = SimplePrompt()
# prompt.setprompt("Hello")
# example.add_userprompt(prompt)
# print(example.unpack())