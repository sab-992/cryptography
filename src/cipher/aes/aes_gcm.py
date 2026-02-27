import secrets
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES256
from cryptography.hazmat.primitives.ciphers.modes import GCM
from src.cipher.detail.algorithm import Algorithm, SALT_SIZE


IV_SIZE: int = 12
ENCODING: str = "utf-8"
TAG_SIZE: int = 16
TOTAL_ADDED_SIZE = TAG_SIZE + IV_SIZE + SALT_SIZE
class AESGCM(Algorithm):
    name: str = "AES - 256 bits"
    mode: str = "GCM"

    def __init__(self):
        super().__init__()

    def get_plain(self, password: str, cipher_hex: str) -> str:
        iv_start, iv_end = -(IV_SIZE + SALT_SIZE), -SALT_SIZE
        tag_start, tag_end = -TOTAL_ADDED_SIZE, -(TOTAL_ADDED_SIZE - TAG_SIZE)

        cipher: bytes = bytes.fromhex(cipher_hex)
        salt = cipher[-SALT_SIZE:]
        key_dict = self.get_key(password, salt)
        iv = cipher[iv_start:iv_end]
        tag = cipher[tag_start:tag_end]
        encrypted_data = cipher[:-TOTAL_ADDED_SIZE]

        decryptor = Cipher(AES256(key_dict["key"]), GCM(initialization_vector=iv, tag=tag)).decryptor()
        decrypted_bytes = decryptor.update(encrypted_data) + decryptor.finalize()
        return decrypted_bytes.decode(ENCODING)

    def get_cipher(self, password: str, decrypted: str) -> str:
        key_dict = self.get_key(password)
        iv = secrets.token_bytes(IV_SIZE)
        encryptor = Cipher(AES256(key_dict["key"]), GCM(initialization_vector=iv)).encryptor()
        encrypted_bytes = encryptor.update(decrypted.encode(ENCODING)) + encryptor.finalize()
        cipher = bytes.fromhex((encrypted_bytes + encryptor.tag + iv + key_dict["salt"]).hex())

        return cipher.hex()