from dataclasses import dataclass
from enum import Enum
from src.cipher.aes.aes_gcm import AESGCM
from src.cipher.detail.algorithm import Algorithm
from src.utils.logger import Logger, Level_en
from typing import Any, Type


@dataclass
class CipherAlgorithmInfo():
    name: str
    mode: str
    obj_type: Type[Algorithm]

    def __str__(self):
        return f"{self.name}, mode: {self.mode}"

class CipherAlgorithm_en(Enum):
    AES_GCM = CipherAlgorithmInfo("AES", "GCM", AESGCM)



class CipherAlgorithmFactory:
    factory: dict[str, Type[Algorithm]] = { str(cipher_algo_info.value): cipher_algo_info.value.obj_type for cipher_algo_info in CipherAlgorithm_en}

    @classmethod
    def get(cls, strategy: Any) -> Algorithm:
        if isinstance(strategy, CipherAlgorithm_en):
            return strategy.value.obj_type()

        obj_type = cls.factory.get(strategy, None)

        if not obj_type:
            raise Exception(Logger.log(message=f"File strategy {strategy} is not handled", level=Level_en.ERROR))
        
        return obj_type()