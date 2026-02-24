from dataclasses import dataclass
from enum import Enum
from src.utils.file_strategy.file_strategy import FileStrategy
from src.utils.file_strategy.json import JsonFS
from src.utils.logger import Logger, Level_en
from typing import Any


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
    def get(strategy: Any) -> FileStrategy:
        if isinstance(strategy, FileStrategy_en):
            return strategy.value.obj_type()

        match strategy:
            case FileStrategy_en.JSON.name:
                return FileStrategy_en.JSON.value.obj_type()
            case _:
                raise Exception(Logger.log(message=f"File strategy {strategy} is not handled", level=Level_en.ERROR))