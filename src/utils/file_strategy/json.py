import json
from src.utils.file_strategy.file_strategy import FileStrategy
from src.utils.file_system import FileSystem, WritingMode_en
from src.utils.logger import Logger, Level_en


class JsonFS(FileStrategy):
    name: str = "JSON"

    def __init__(self):
        pass

    def read(self, path: str) -> str:
        try:
            cipher: dict = json.loads(FileSystem.read(path)).get("cipher", None)

            if not cipher:
                raise Exception(Logger.log(message="Cipher JSON object ill-formed", level=Level_en.ERROR))

            return cipher
        except json.JSONDecodeError as e:
            Logger.log(message=f"Error while reading JSON file: {e}, JSON file might be ill-formed", level=Level_en.ERROR)
            return None

    def save(self, path: str, cipher: str) -> None:
        FileSystem.write(path, content=json.dumps({ "cipher": cipher }), mode=WritingMode_en.OVERWRITE)