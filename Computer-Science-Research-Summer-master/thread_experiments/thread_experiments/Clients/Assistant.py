from typing import List
from ClientUtils.StringValidation import emptyString
from ClientUtils.Tools import Tools

class Assistant:

    def __init__(self, client, model="gpt-4o") -> None:
        self._client = client
        self._instruction = ""
        self._name = ""
        self._tools: Tools = []
        self._model = model
        self._assistant = self._client.beta.assistants.create(model=self._model)

    # probably would automate this for scalability purposes
        if not emptyString(self._instruction) and not emptyString(self._name) and self._tools:
            self._client.beta.assistants.create(model=self._model, instruction=self._instruction, name=self._name, tools=self._tools)
        elif emptyString(self._instruction) and not emptyString(self._name) and self._tools:
            self._client.beta.assistants.create(model=self._model, name=self._name, tools=self._tools)
        elif emptyString(self._instruction) and emptyString(self._name) and self._tools:
            self._client.beta.assistants.create(model=self._model, name=self._name, tools=self._tools)
        elif emptyString(self._instruction) and emptyString(self._name) and not self._tools:
            self._client.beta.assistants.create(model=self._model, name=self._name, tools=self._tools)
        elif not emptyString(self._instruction) and emptyString(self._name) and self._tools:
            self._client.beta.assistants.create(model=self._model, instruction=self._instruction, tools=self._tools)
        elif not emptyString(self._instruction) and emptyString(self._name) and not self._tools:
            self._client.beta.assistants.create(model=self._model, instruction=self._instruction, tools=self._tools)
        elif emptyString(self._instruction) and emptyString(self._name) and not self._tools:
            self._client.beta.assistants.create(model=self._model, instruction=self._instruction, tools=self._tools)
        elif not emptyString(self._instruction) and not emptyString(self._name) and not self._tools:
            self._client.beta.assistants.create(model=self._model, instruction=self._instruction, name=self._name)
    
    def getId(self):
        return self._assistant.id

    def setinstruction(self, instruction) -> None:
        validated = emptyString(instruction)

        if validated:
            self._instruction = instruction
        else:
            Exception("Empty Instruction")
        
    def getinstruction(self) -> str:
        return self._instruction

    def setname(self, name) -> None:
        self._name = name
    
    def getname(self) -> str:
        return self._name

    def setmodel(self, model) -> None:
        self._model = model

    def getmodel(self) -> str:
        return self._model
    
    def settools(self, tools: Tools):
        self._tools = tools.unwrap()
    
    def addtools(self, tools: Tools):
        self._tools.extend(tools.unwrap())

    def gettools(self):
        return self._tools
