from abc import ABC, abstractmethod
from src.cipher.detail.type import CipherDict


class FileStrategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read(self, path: str) -> CipherDict:
        pass

    @abstractmethod
    def save(self, name: str, cipher_dict: CipherDict) -> None:
        pass