from src.utils.logger import Logger, Level_en
from tkinter import Misc
from tkinter.ttk import Combobox
from typing import Self

class ComboBoxBuilder():
    def __init__(self):
        self.__parent: Misc = None
        self.__width: int = -1
        self.__height: int = -1
        self.__values: tuple[str] = None

    def build(self):
        if not self.__parent:
            raise Exception(Logger.log(message=f"{__class__.__name__} - No parent given", level=Level_en.ERROR))
        
        if not self.__values or\
           len(self.__values) <= 0:
            raise Exception(Logger.log(message=f"{__class__.__name__} - No values given", level=Level_en.ERROR))
    
        if self.__width < 0 or \
           self.__height < 0:
            raise Exception(Logger.log(message=f"{__class__.__name__}: Missing dimensions", level=Level_en.ERROR))
        
        combo_box: Combobox = Combobox(self.__parent, height=self.__height, width=self.__width)

        combo_box["values"] = self.__values
        return combo_box

    def set_height(self, height: int) -> Self:
        self.__height = height
        return self
    
    def set_parent(self, parent: Misc) -> Self:
        self.__parent = parent
        return self
    
    def set_values(self, values: tuple[str]) -> Self:
        self.__values = values
        return self

    def set_width(self, width: int) -> Self:
        self.__width = width
        return self