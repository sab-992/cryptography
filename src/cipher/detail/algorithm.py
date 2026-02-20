from abc import ABC, abstractmethod
from src.cipher.detail.type import CipherDict
from src.utils.file_strategy.file_strategy import FileStrategy


class Algorithm(ABC):
    def __init__(self, strategy: FileStrategy):
        self.__strategy: FileStrategy = strategy

    @abstractmethod
    def decrypt(self, password: str, cipher_dict: CipherDict) -> str:
        pass

    @abstractmethod
    def encrypt(self, password: str, decrypted: str) -> CipherDict:
        pass

    def read(self, path: str) -> CipherDict:
        return self.__strategy.read(path)

    def save(self, file_name: str, cipher_dict: CipherDict) -> None:
        self.__strategy.save(file_name, cipher_dict)

    def set_strategy(self, file_strategy: FileStrategy) -> None:
        self.__strategy = file_strategy
