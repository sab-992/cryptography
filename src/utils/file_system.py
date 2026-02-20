import os
from enum import Enum
from pathlib import Path
from src.utils.logger import Logger, Level_en


ROOT_FOLDER_NAME: str = "encryption"

class WritingMode_en(Enum):
    APPEND = "a"
    OVERWRITE = "w"

class FileSystem():
    def __init__(self):
        pass

    @staticmethod
    def read(path: str) -> str:
        if(not os.path.exists(path)):
            raise Exception(Logger.log(message=f"File: '{path}' does not exist", level=Level_en.ERROR))

        with open(path, mode="r") as f:
            return f.read()

    @staticmethod
    def write(path: str, content: str, mode: WritingMode_en = "w") -> None:
        folder_path = os.path.basename(os.path.dirname(path))

        if(not os.path.exists(folder_path)):
            raise Exception(Logger.log(message=f"Folder: '{folder_path}' does not exist", level=Level_en.ERROR))

        with open(f"{FileSystem.get_root()}/{path}", mode=mode.value) as f:
            f.write(content)

    @staticmethod
    def get_root():
        current_path = Path.cwd()
        root_name = ROOT_FOLDER_NAME

        for parent in [current_path] + list(current_path.parents):
            current_path = parent / root_name
            if current_path.exists():
                return current_path
            
        raise Exception(Logger.log(message=f"Root folder not found", level=Level_en.ERROR))