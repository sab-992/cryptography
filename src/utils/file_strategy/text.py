from src.utils.file_strategy.file_strategy import FileStrategy
from src.utils.file_system import FileSystem, WritingMode_en
from src.utils.logger import Logger, Level_en


class TextFS(FileStrategy):
    name: str = "TEXT"
    extension: str = ".txt"

    def __init__(self):
        pass

    def read(self, path: str) -> str:
        try:
            if FileSystem.get_extension(path) != self.extension:
                raise Exception(Logger.log(message=f"File is not a {self.name} file", level=Level_en.ERROR))

            cipher: dict = FileSystem.read(path)

            if not cipher or len(cipher) <= 0:
                raise Exception(Logger.log(message=f"Missing cipher in {self.name} file", level=Level_en.ERROR, to_std_out=True))

            return cipher
        except Exception:
            return None

    def save(self, path: str, cipher: str) -> None:
        FileSystem.write(path, content=cipher, mode=WritingMode_en.OVERWRITE)