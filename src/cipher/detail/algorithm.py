import secrets
from abc import ABC, abstractmethod
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from src.cipher.detail.utils import CipherDict, get_empty_cipher_dict, is_string_empty, is_cipher_dict_empty
from src.utils.file_strategy.file_strategy import FileStrategy
from src.utils.logger import Logger, Level_en
from typing import TypedDict


MB: int = 1024
ARGON2_KDF_ITERATIONS: int = 5
ARGON2_LANES: int = 4
ARGON2_MEMORY: int = 64 * MB
KEY_LENGTH_BYTES: int = 32
SALT_SIZE: int = 16

class KeyDict(TypedDict):
    key: bytes
    salt: bytes

class Algorithm(ABC):
    name: str = None
    mode: str = None

    def __init__(self, strategy: FileStrategy):
        self.__strategy: FileStrategy = strategy

    @classmethod
    def as_string(cls) -> str:
        return f"{cls.name}, mode: {cls.mode}"

    def decrypt(self, password: str, cipher_dict: CipherDict) -> str:
        if  is_string_empty(password) or is_cipher_dict_empty(cipher_dict):
            return ""
        
        try:
            return self.get_plain(password, cipher_dict)
        except InvalidTag:
            Logger.log(message="Invalid password or the encrypted data has been tampered with", level=Level_en.ERROR, to_std_out=True)
        

    def encrypt(self, password: str, decrypted: str) -> CipherDict:
        if is_string_empty(password) or is_string_empty(decrypted):
            return get_empty_cipher_dict(str(self))

        return self.get_cipher_dict(password, decrypted)

    @abstractmethod
    def get_cipher_dict(self, password: str, decrypted: str) -> CipherDict:
        pass

    def get_key(self, password: str, salt: bytes=secrets.token_bytes(SALT_SIZE)) -> KeyDict:
        return { "key": Argon2id(salt=salt,
                                 length=KEY_LENGTH_BYTES,
                                 iterations=ARGON2_KDF_ITERATIONS,
                                 lanes=ARGON2_LANES,
                                 memory_cost=ARGON2_MEMORY).derive(password.encode()),
                 "salt": salt }

    @abstractmethod
    def get_plain(self, password: str, cipher_dict: CipherDict) -> str:
        pass

    def read(self, path: str) -> CipherDict:
        return self.__strategy.read(path)

    def save(self, file_name: str, cipher_dict: CipherDict) -> None:
        self.__strategy.save(file_name, cipher_dict)

    def set_strategy(self, file_strategy: FileStrategy) -> None:
        self.__strategy = file_strategy

    def __str__(self) -> str:
        return self.as_string()