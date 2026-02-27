import secrets
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES256
from cryptography.hazmat.primitives.ciphers.modes import GCM
from src.cipher.detail.algorithm import Algorithm
from src.cipher.detail.utils import CipherDict
from src.utils.file_strategy.file_strategy_factory import FileStrategy, FileStrategy_en, FileStrategyFactory


IV_SIZE: int = 12
ENCODING: str = "utf-8"
TAG_SIZE: int = 16

class AESGCM(Algorithm):
    name: str = "AES"
    mode: str = "GCM"

    def __init__(self, strategy: FileStrategy = FileStrategyFactory.get(FileStrategy_en.JSON)):
        super().__init__(strategy)

    def get_plain(self, password: str, cipher_dict: CipherDict) -> str:
        salt = bytes.fromhex(cipher_dict["salt"])
        key_dict = self.get_key(password, salt)
        cipher = bytes.fromhex(cipher_dict["cipher"])[:-TAG_SIZE]
        nonce = bytes.fromhex(cipher_dict["nonce"])
        tag = bytes.fromhex(cipher_dict["cipher"])[-TAG_SIZE:]

        decryptor = Cipher(AES256(key_dict["key"]), GCM(initialization_vector=nonce, tag=tag)).decryptor()
        decrypted_bytes = decryptor.update(cipher) + decryptor.finalize()
        return decrypted_bytes.decode(ENCODING)

    def get_cipher_dict(self, password: str, decrypted: str) -> CipherDict:
        key_dict = self.get_key(password)
        nonce = secrets.token_bytes(IV_SIZE)
        encryptor = Cipher(AES256(key_dict["key"]), GCM(initialization_vector=nonce)).encryptor()
        encrypted_bytes = encryptor.update(decrypted.encode(ENCODING)) + encryptor.finalize()
        return { "cipher": (encrypted_bytes + encryptor.tag).hex(), "nonce": nonce.hex(), "salt": key_dict["salt"].hex(), "cipher_algorithm_used": str(self) }