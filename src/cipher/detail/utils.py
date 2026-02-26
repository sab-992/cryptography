from typing import TypedDict


type Cipher = str
type Salt = str
type Nonce = str

class CipherDict(TypedDict):
    cipher: Cipher
    nonce: Nonce
    salt: Salt # Used to make an encryption key by combining it with user's password
    cipher_algorithm_used: str

class PlainDict(TypedDict):
    text: Cipher
    cipher_algorithm_to_use: str

def is_cipher_dict(cd: dict) -> bool:
    return cd.get("cipher", None) and \
           cd.get("nonce", None) and \
           cd.get("salt", None)

def get_empty_cipher_dict(algorithm: str) -> bool:
    return { "cipher": "", "nonce": "", "salt": "", "cipher_algorithm_used": algorithm }

def is_string_empty(string: str) -> bool:
    return not string or len(string) <= 0

def is_cipher_dict_empty(cipher_dict: CipherDict) -> bool:
    return is_string_empty(cipher_dict["cipher"]) or\
           is_string_empty(cipher_dict["nonce"]) or\
           is_string_empty(cipher_dict["salt"])