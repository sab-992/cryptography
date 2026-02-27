import secrets
from cryptography.hazmat.primitives.hashes import SHA512
from cryptography.exceptions import InvalidTag, InvalidSignature
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES256
from cryptography.hazmat.primitives.ciphers.modes import CTR
from src.cipher.detail.algorithm import Algorithm


IV_SIZE: int = 16
ENCODING: str = "utf-8"
TAG_SIZE: int = 64

class AESCTR(Algorithm):
    name: str = "AES - 256 bits"
    mode: str = "CTR + HMAC"

    def __init__(self):
        super().__init__()

    def get_plain(self, password: str, cipher_hex: str) -> str:
        decryption_info  = self.get_decryption_information(cipher_hex, TAG_SIZE, IV_SIZE)
        key_dict = self.get_key(password, decryption_info["salt"])
        decryptor = Cipher(AES256(key_dict["key"]), CTR(decryption_info["iv"])).decryptor()
        decrypted_bytes = decryptor.update(decryption_info["encrypted_data"]) + decryptor.finalize()
        decrypted = decrypted_bytes.decode(ENCODING)

        try:
            self.validate_tag(decrypted_bytes, key_dict["key"], SHA512(), decryption_info["tag"])
        except InvalidSignature:
            raise InvalidTag()

        return decrypted

    def get_cipher(self, password: str, decrypted: str) -> str:
        key_dict = self.get_key(password)
        iv = secrets.token_bytes(IV_SIZE)
        encryptor = Cipher(AES256(key_dict["key"]), CTR(iv)).encryptor()
        decrypted_bytes = decrypted.encode(ENCODING)
        encrypted_bytes = encryptor.update(decrypted_bytes) + encryptor.finalize()
        tag = self.create_tag(decrypted_bytes, key_dict["key"], SHA512())
        cipher = bytes.fromhex((encrypted_bytes + tag + iv + key_dict["salt"]).hex())

        return cipher.hex()