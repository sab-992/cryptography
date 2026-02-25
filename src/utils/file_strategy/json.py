import json
from src.cipher.detail.type import CipherDict, is_cipher_dict
from src.utils.file_strategy.file_strategy import FileStrategy
from src.utils.file_system import FileSystem, WritingMode_en
from src.utils.logger import Logger, Level_en


class JsonFS(FileStrategy):
    name: str = "JSON"

    def __init__(self):
        pass

    def read(self, path: str) -> CipherDict:
        try:
            json_obj: dict = json.loads(FileSystem.read(path))

            if not is_cipher_dict(json_obj):
                raise Exception(Logger.log(message="Cipher JSON object ill-formed", level=Level_en.ERROR))

            return json_obj
        except json.JSONDecodeError as e:
            Logger.log(message=f"Error while reading JSON file: {e}, JSON file might be ill-formed", level=Level_en.ERROR)
            return None

    def save(self, path: str, cipher_dict: CipherDict) -> None:
        FileSystem.write(path, content=json.dumps(cipher_dict), mode=WritingMode_en.OVERWRITE)