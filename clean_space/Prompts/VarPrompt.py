import Prompt

class VarPrompt(Prompt.Prompt):

    def __init__(self) -> None:
        self._prompt = ""

    def setprompt(self, *args) -> None:
        for index, arg in enumerate(args):
            if self.isprompt(arg):
                continue
            raise Exception(f"Invalid Prompt detected at index: {index}")
        self._prompt = f"Define <{args[0]}> to be {args[1]}"

    def getprompt(self) -> str:
        return self._prompt

    def isprompt(self, prompt) -> bool:
        return super().isprompt(prompt)
    
    def __str__(self) -> str:
        return super().__str__()
        
# example = VarPrompt()
# example.setprompt("H", "Hello World!")
# print(example.getprompt())