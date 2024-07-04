from abc import ABC, abstractmethod
from Prompts.Utilities.StringValidation import emptyString
# from Utilities.StringValidation import emptyString

class Prompt(ABC):
    @abstractmethod
    def __init__(self, prompt) -> None:
        pass

    @abstractmethod
    def setprompt(self, *args) -> None:
        pass
    
    @abstractmethod
    def getprompt(self) -> str:
        pass
    
    @abstractmethod
    def isprompt(self, prompt) -> bool:
        return not emptyString(prompt)
    
    @abstractmethod
    def __str__(self) -> str:
        return self.getprompt()