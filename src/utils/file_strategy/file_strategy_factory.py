from dataclasses import dataclass
from enum import Enum
from src.utils.file_strategy.file_strategy import FileStrategy
from src.utils.file_strategy.json import JsonFS


@dataclass
class FileStrategyInfo():
    name: str
    obj_type: FileStrategy

class FileStrategy_en(Enum):
    JSON = FileStrategyInfo("JSON", JsonFS)

class FileStrategyFactory:
    def __init__(self):
        pass

    @staticmethod
    def get(strategy: FileStrategy_en) -> FileStrategy:
        return strategy.value.obj_type()