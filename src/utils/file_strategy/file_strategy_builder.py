from enum import Enum
from src.utils.file_strategy.file_strategy import FileStrategy
from src.utils.file_strategy.json import JsonFS
from src.utils.logger import Logger, Level_en


class FileStrategy_en(Enum):
    JSON = "JSON"

class FileStrategyBuilder:
    def __init__(self):
        pass

    @staticmethod
    def build(strategy: FileStrategy_en) -> FileStrategy:
        match strategy:
            case FileStrategy_en.JSON:
                return JsonFS()
            case _:
                raise Exception(Logger.log(message=f"Strategy: {strategy} does not exist !", level=Level_en.ERROR))