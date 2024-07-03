import Prompt

class SimplePrompt(Prompt.Prompt):

    def __init__(self) -> None:
        self._prompt = ""

    def setprompt(self, arg) -> None:
        if self.isprompt(arg):
            self._prompt = arg
        else:
            raise Exception(f"Invalid Prompt detected!")

    def getprompt(self) -> str:
        return self._prompt

    def isprompt(self, prompt) -> bool:
        return super().isprompt(prompt)
    
    def __str__(self) -> str:
        return super().__str__()
        
# example = SimplePrompt()
# example.setprompt("Hello World!")
# print(example.getprompt())