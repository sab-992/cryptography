import json
from src.cipher.detail.type import CipherDict, is_cipher_dict, cipher_dict_to_str_dict, str_dict_to_cipher_dict
from src.utils.file_strategy.file_strategy import FileStrategy
from src.utils.file_system import FileSystem, WritingMode_en
from src.utils.logger import Logger, Level_en
from src.utils.settings import OUTPUT_FOLDER_PATH


class JsonFS(FileStrategy):
    name: str = "JSON"

    def __init__(self):
        pass

    def read(self, path: str) -> CipherDict:
        json_obj: dict = json.loads(FileSystem.read(path))

        if not is_cipher_dict(json_obj):
            raise Exception(Logger.log(message="Cipher JSON object ill-formed", level=Level_en.ERROR))

        return str_dict_to_cipher_dict(json_obj)

    def save(self, name: str, cipher_dict: CipherDict) -> None:
        FileSystem.write(f"{OUTPUT_FOLDER_PATH}/{name}.json", content=json.dumps(cipher_dict_to_str_dict(cipher_dict)), mode=WritingMode_en.OVERWRITE)