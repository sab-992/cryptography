import os
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from src.cipher.detail.algorithm import Algorithm
from src.cipher.detail.type import CipherDict, Salt, Nonce
from src.utils.file_strategy.file_strategy_builder import FileStrategy, FileStrategy_en, FileStrategyBuilder


SALT_SIZE: int = 16
NONCE_SIZE: int = 12
KDF_ITERATIONS: int = 100_000

class AESGCM(Algorithm):
    def __init__(self, strategy: FileStrategy = FileStrategyBuilder.build(FileStrategy_en.JSON)):
        super().__init__(strategy)

    def decrypt(self, password: str, cipher_dict: CipherDict) -> str:
        return AESGCM(self.__get_key(password, cipher_dict["salt"])).decrypt(nonce=cipher_dict["nonce"], data=cipher_dict["cipher"], associated_data=None).decode("utf-8")

    def encrypt(self, password: str, decrypted: str) -> CipherDict:
        salt: Salt = os.urandom(SALT_SIZE)
        nonce: Nonce = os.urandom(NONCE_SIZE)
        return { "cipher": AESGCM(self.__get_key(password, salt)).encrypt(nonce, decrypted.encode("utf-8"), None), "nonce": nonce, "salt": salt }

    def __get_key(self, password: str, salt: bytes) -> bytes:
        return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, KDF_ITERATIONS)