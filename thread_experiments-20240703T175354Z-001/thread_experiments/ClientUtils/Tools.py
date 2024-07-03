from StringValidation import emptyString

class Tools:
    def __init__(self) -> None:
        self._tools = []
    
    def addTool(self, toolstring) -> None:
        if emptyString(toolstring):
            Exception("Empty string!")
        else:
            self._tools.append({"type": toolstring})
        
    def addTools(self, toolstrings) -> None:
        for toolstring in toolstrings:
            if emptyString(toolstring):
                Exception("Empty string!")
            else:
                self._tools.append({"type": toolstring})
    
    def clear(self):
        self._tools.clear()
    
    def unwrap(self):
        return self._tools