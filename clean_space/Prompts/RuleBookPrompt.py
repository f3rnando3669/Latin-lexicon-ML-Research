import Prompt

class RuleBookPrompt(Prompt.Prompt):
        
    def __init__(self) -> None:
        self._prompt = ""

    def setprompt(self, *args) -> None:
        for index, arg in enumerate(args):
            if self.isprompt(arg):
                continue
            raise Exception(f"Invalid Prompt detected at index: {index}")
        self._prompt = f"Create a rulebook for types of defective arguments according to <{arg[0]}> with the following template: \"* <Rule 1>: <name of Rule 1>, <explanation of Rule 1>, e.g, <example of Rule 1>\""

    def getprompt(self) -> str:
        return self._prompt

    def isprompt(self, prompt) -> bool:
        return super().isprompt(prompt)
    
    def __str__(self) -> str:
        return super().__str__()
        
# example = RuleBookPrompt()
# example.setprompt("Hello World!")
# print(example.getprompt())