from abc import ABC, abstractmethod


class FileStrategy(ABC):
    name: str = None
    extension: str = None

    def __init__(self):
        pass

    @abstractmethod
    def read(self, path: str) -> str:
        pass

    @abstractmethod
    def save(self, path: str, cipher: str) -> None:
        pass