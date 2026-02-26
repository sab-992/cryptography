import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM as AESGCM_c
from src.cipher.detail.algorithm import Algorithm
from src.cipher.detail.utils import CipherDict
from src.utils.file_strategy.file_strategy_factory import FileStrategy, FileStrategy_en, FileStrategyFactory


NONCE_SIZE: int = 12

class AESGCM(Algorithm):
    name: str = "AES"
    mode: str = "GCM"

    def __init__(self, strategy: FileStrategy = FileStrategyFactory.get(FileStrategy_en.JSON)):
        super().__init__(strategy)

    def get_plain(self, password: str, cipher_dict: CipherDict) -> str:
        key_dict = self.get_key(password, bytes.fromhex(cipher_dict["salt"]))
        return AESGCM_c(key_dict["key"]).decrypt(nonce=bytes.fromhex(cipher_dict["nonce"]), data=bytes.fromhex(cipher_dict["cipher"]), associated_data=None).decode("utf-8")

    def get_cipher_dict(self, password: str, decrypted: str) -> CipherDict:
        key_dict, nonce = self.get_key(password), secrets.token_bytes(NONCE_SIZE)
        return { "cipher": AESGCM_c(key_dict["key"]).encrypt(nonce, decrypted.encode("utf-8"), None).hex(), "nonce": nonce.hex(), "salt": key_dict["salt"].hex(), "cipher_algorithm_used": str(self) }