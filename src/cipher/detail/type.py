from typing import TypedDict


type Cipher = bytes
type Salt = bytes
type Nonce = bytes

class CipherDict(TypedDict):
    cipher: Cipher
    nonce: Nonce
    salt: Salt

def cipher_dict_to_str_dict(cd: CipherDict) -> dict[str, str]:
    return { k: v.hex() for k, v in cd.items() }

def str_dict_to_cipher_dict(cs: dict[str, str]) -> CipherDict:
    return { k: bytes.fromhex(v) for k, v in cs.items() }

def is_cipher_dict(cd: dict) -> bool:
    return cd.get("cipher", None) and \
           cd.get("nonce", None) and \
           cd.get("salt", None)