from typing import TypedDict


class CipherDict(TypedDict):
    cipher: str
    cipher_algorithm_used: str

class PlainDict(TypedDict):
    text: str
    cipher_algorithm_to_use: str

def is_cipher_dict(cd: dict) -> bool:
    return cd.get("cipher", None)

def get_empty_cipher_dict(algorithm: str) -> bool:
    return { "cipher": "", "cipher_algorithm_used": algorithm }

def is_string_empty(string: str) -> bool:
    return not string or len(string) <= 0

def is_cipher_dict_empty(cipher_dict: CipherDict) -> bool:
    return is_string_empty(cipher_dict["cipher"])