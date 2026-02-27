from typing import TypedDict


class EncryptionRequest(TypedDict):
    text: str
    cipher_algorithm_to_use: str

def is_string_empty(string: str) -> bool:
    return not string or len(string) <= 0