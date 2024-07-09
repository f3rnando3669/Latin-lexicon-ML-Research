from abc import ABC, abstractmethod

class ABsClient(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def generate(self, prompts) -> str:
        pass
