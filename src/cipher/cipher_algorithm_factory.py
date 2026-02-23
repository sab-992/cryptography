from dataclasses import dataclass
from enum import Enum
from src.cipher.aes.aes_gcm import AESGCM
from src.cipher.detail.algorithm import Algorithm


@dataclass
class CipherAlgorithmDict():
    name: str
    mode: str
    obj_type: Algorithm

class CipherAlgorithm_en(Enum):
    AES_GCM = CipherAlgorithmDict("AES", "GCM", AESGCM)

class CipherAlgorithmFactory:
    def __init__(self):
        pass

    @staticmethod
    def get(strategy: CipherAlgorithm_en) -> Algorithm:
        return strategy.value.obj_type()