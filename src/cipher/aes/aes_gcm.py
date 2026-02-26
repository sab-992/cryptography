import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM as AESGCM_c
from src.cipher.detail.algorithm import Algorithm
from src.cipher.detail.type import CipherDict
from src.utils.file_strategy.file_strategy_factory import FileStrategy, FileStrategy_en, FileStrategyFactory


SALT_SIZE: int = 16
NONCE_SIZE: int = 12

class AESGCM(Algorithm):
    name: str = "AES"
    mode: str = "GCM"

    def __init__(self, strategy: FileStrategy = FileStrategyFactory.get(FileStrategy_en.JSON)):
        super().__init__(strategy)

    def decrypt(self, password: str, cipher_dict: CipherDict) -> str:
        if  self.is_string_empty(cipher_dict["cipher"]) or\
            self.is_string_empty(cipher_dict["nonce"]) or\
            self.is_string_empty(cipher_dict["salt"]):
            return

        return AESGCM_c(self.get_key(password, bytes.fromhex(cipher_dict["salt"]))).decrypt(nonce=bytes.fromhex(cipher_dict["nonce"]), data=bytes.fromhex(cipher_dict["cipher"]), associated_data=None).decode("utf-8")

    def encrypt(self, password: str, decrypted: str) -> CipherDict:
        if self.is_string_empty(decrypted):
            return { "cipher": "", "nonce": "", "salt": "", "cipher_algorithm_used": str(self) }

        salt: bytes = os.urandom(SALT_SIZE)
        nonce: bytes = os.urandom(NONCE_SIZE)
        return { "cipher": AESGCM_c(self.get_key(password, salt)).encrypt(nonce, decrypted.encode("utf-8"), None).hex(), "nonce": nonce.hex(), "salt": salt.hex(), "cipher_algorithm_used": str(self) }