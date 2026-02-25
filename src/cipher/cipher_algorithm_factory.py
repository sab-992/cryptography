from enum import Enum
from src.cipher.aes.aes_gcm import AESGCM
from src.cipher.detail.algorithm import Algorithm
from src.utils.logger import Logger, Level_en
from typing import Any, Type


class CipherAlgorithm_en(Enum):
    AES_GCM = AESGCM

class CipherAlgorithmFactory:
    factory: dict[str, Type[Algorithm]] = { cipher_algo.value.as_string(): cipher_algo.value for cipher_algo in CipherAlgorithm_en}

    @classmethod
    def get(cls, algorithm: Any) -> Algorithm:
        if isinstance(algorithm, CipherAlgorithm_en):
            return algorithm.value()
        
        obj_type = cls.factory.get(algorithm, None)

        if not obj_type:
            raise Exception(Logger.log(message=f"Algorithm: {algorithm} is not handled", level=Level_en.ERROR))
        
        return obj_type()