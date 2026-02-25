from abc import ABC, abstractmethod
from src.cipher.detail.type import CipherDict


class FileStrategy(ABC):
    name: str = None

    def __init__(self):
        pass

    @classmethod
    def as_string(cls):
        return cls.name

    @abstractmethod
    def read(self, path: str) -> CipherDict:
        pass

    @abstractmethod
    def save(self, path: str, cipher_dict: CipherDict) -> None:
        pass

    def __str__(self):
        return self.as_string()