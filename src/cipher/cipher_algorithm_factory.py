from dataclasses import dataclass
from enum import Enum
from src.cipher.aes.aes_gcm import AESGCM
from src.cipher.detail.algorithm import Algorithm
from src.utils.logger import Logger, Level_en
from typing import Any


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
    def get(strategy: Any) -> CipherAlgorithm_en:
        if isinstance(CipherAlgorithm_en):
            return strategy.value.obj_type()

        match strategy:
            case CipherAlgorithm_en.AES_GCM.name:
                return CipherAlgorithm_en.AES_GCM.value.obj_type()
            case _:
                raise Exception(Logger.log(message=f"File strategy {strategy} is not handled", level=Level_en.ERROR))