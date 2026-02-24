from dataclasses import dataclass
from enum import Enum
from src.utils.file_strategy.file_strategy import FileStrategy
from src.utils.file_strategy.json import JsonFS
from src.utils.logger import Logger, Level_en
from typing import Any, Type


@dataclass
class FileStrategyInfo():
    name: str
    obj_type: FileStrategy

class FileStrategy_en(Enum):
    JSON = FileStrategyInfo("JSON", JsonFS)

class FileStrategyFactory:
    factory: dict[str, Type[FileStrategy]] = { fs_info.value.name: fs_info.value.obj_type for fs_info in FileStrategy_en}

    @classmethod
    def get(cls, strategy: Any) -> FileStrategy:
        if isinstance(strategy, FileStrategy_en):
            return strategy.value.obj_type()

        obj_type = cls.factory.get(strategy, None)

        if not obj_type:
            raise Exception(Logger.log(message=f"File strategy {strategy} is not handled", level=Level_en.ERROR))
        
        return obj_type()