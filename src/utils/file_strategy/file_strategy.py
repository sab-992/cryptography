from abc import ABC, abstractmethod


class FileStrategy(ABC):
    name: str = None

    def __init__(self):
        pass

    @classmethod
    def as_string(cls):
        return cls.name

    @abstractmethod
    def read(self, path: str) -> str:
        pass

    @abstractmethod
    def save(self, path: str, cipher: str) -> None:
        pass

    def __str__(self):
        return self.as_string()