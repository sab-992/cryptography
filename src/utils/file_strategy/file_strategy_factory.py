from enum import Enum
from src.utils.file_strategy.file_strategy import FileStrategy
from src.utils.file_strategy import json, text
from src.utils.logger import Logger, Level_en
from typing import Any, Type


class FileStrategy_en(Enum):
    TEXT = text.TextFS
    JSON = json.JsonFS

class FileStrategyFactory:
    supported_strategies: dict[str, Type[FileStrategy]] = {  file_strategy.value.extension: file_strategy.value for file_strategy in FileStrategy_en }

    @classmethod
    def get(cls, strategy: Any) -> FileStrategy:
        # Get using Enum
        if isinstance(strategy, FileStrategy_en):
            return strategy.value()

        obj_type = None
        # Get using extension ex: .json
        if strategy in cls.supported_strategies:
            obj_type = cls.supported_strategies.get(strategy)
        else:
            # Get using displayed name (FileStrategy.as_string()) ex: JSON
            extension = f".{str.lower(strategy)}"

            if extension in cls.supported_strategies:
                obj_type = cls.supported_strategies.get(extension)

        if not obj_type:
            raise Exception(Logger.log(message=f"File strategy {strategy} is not handled", level=Level_en.ERROR))
        
        return obj_type()

    @classmethod
    def supported(cls):
        return cls.supported_strategies.keys()

    @staticmethod
    def file_strategies() -> list[FileStrategy]:
        return [file_strategy.value for file_strategy in FileStrategy_en]
            