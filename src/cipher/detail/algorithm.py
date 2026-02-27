import secrets
from abc import ABC, abstractmethod
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.hashes import HashAlgorithm
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from src.cipher.detail.utils import is_string_empty
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

class DecryptionInformation(TypedDict):
    encrypted_data: bytes
    tag: bytes
    iv: bytes
    salt: bytes

class Algorithm(ABC):
    name: str = None
    mode: str = None

    def __init__(self):
        pass

    @classmethod
    def as_string(cls) -> str:
        return f"{cls.name}, mode: {cls.mode}"

    def create_tag(self, decrypted: bytes, key: bytes, hash_algorithm: HashAlgorithm) -> bytes:
        hmac = HMAC(key, hash_algorithm)
        hmac.update(decrypted)
        return hmac.finalize()

    def decrypt(self, password: str, cipher: str) -> str:
        if  is_string_empty(password) or is_string_empty(cipher):
            return ""
        
        try:
            return self.get_plain(password, cipher)
        except InvalidTag:
            Logger.log(message="Invalid password or the encrypted data has been tampered with", level=Level_en.ERROR, to_std_out=True)
        

    def encrypt(self, password: str, decrypted: str) -> str:
        if is_string_empty(password) or is_string_empty(decrypted):
            return ""

        return self.get_cipher(password, decrypted)

    @abstractmethod
    def get_cipher(self, password: str, decrypted: str) -> str:
        pass

    def get_key(self, password: str, salt: bytes=secrets.token_bytes(SALT_SIZE)) -> KeyDict:
        return { "key": Argon2id(salt=salt,
                                 length=KEY_LENGTH_BYTES,
                                 iterations=ARGON2_KDF_ITERATIONS,
                                 lanes=ARGON2_LANES,
                                 memory_cost=ARGON2_MEMORY).derive(password.encode()),
                 "salt": salt }

    def get_decryption_information(self, cipher_hex: str, tag_size: int, iv_size: int) -> DecryptionInformation:
        cipher: bytes = bytes.fromhex(cipher_hex)
        iv_start = -(iv_size + SALT_SIZE)
        tag_start = -(tag_size + iv_size + SALT_SIZE)

        return { "encrypted_data": cipher[:tag_start], "tag": cipher[tag_start:tag_start + tag_size], "iv": cipher[iv_start:iv_start + iv_size], "salt": cipher[-SALT_SIZE:] }

    @abstractmethod
    def get_plain(self, password: str, cipher: str) -> str:
        pass

    def validate_tag(self, decrypted: bytes, key: bytes, hash_algorithm: HashAlgorithm, tag: bytes) -> bytes:
        hmac = HMAC(key, hash_algorithm)
        hmac.update(decrypted)
        hmac.verify(tag)

    def __str__(self) -> str:
        return self.as_string()