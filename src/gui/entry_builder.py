from src.utils.logger import Logger, Level_en
from tkinter import Misc, Entry
from typing import Self

class EntryBuilder():
    def __init__(self):
        self.__parent: Misc = None
        self.__width: int = -1

    def build(self):
        if not self.__parent:
            raise Exception(Logger.log(message=f"{__class__.__name__} - No parent given", level=Level_en.ERROR))

        if self.__width < 0:
            raise Exception(Logger.log(message=f"{__class__.__name__} - Missing width", level=Level_en.ERROR))

        return Entry(self.__parent, width=self.__width)

    def set_parent(self, parent: Misc) -> Self:
        self.__parent = parent
        return self
    
    def set_width(self, width: int) -> Self:
        self.__width = width
        return self