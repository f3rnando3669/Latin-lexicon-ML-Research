from typing import List
from Prompts.PromptList import PromptList
from Utilities.FileUtilities import readfile

class ContextHandler:
    def __init__(self) -> None:
        self._context: PromptList = []

    def load(path: str) -> None:
        pass

    def getcontext(self) -> PromptList:
        return self._context