from abc import ABC, abstractmethod
from PySide6.QtWidgets import QWidget
from src.utils.logger import Logger, Level_en
from typing import Self, Type, TypeVar

T = TypeVar('T')

class WidgetBuilder(ABC):
    def __init__(self, cls: Type[T]):
        if not issubclass(cls, QWidget):
            self.error(f"Type {cls.__name__} is not a Qt widget")
        self.width = -1
        self.height = -1

    def build(self) -> T:
        if self.width <= 0 or\
           self.height <= 0:
            self.error(f"Missing dimensions ! w={self.width}, h={self.height}")

        widget: QWidget = self.initialize_instance()
        widget.setFixedWidth(self.width)
        widget.setFixedHeight(self.height)

        return widget

    @abstractmethod
    def initialize_instance(self) -> T:
        pass

    def set_height(self, height: int) -> Self:
        self.height = height
        return self

    def set_width(self, width: int) -> Self:
        self.width = width
        return self

    def error(self, reason: str) -> None:
        raise Exception(Logger.log(message=f"{__class__.__name__} - {reason}", level=Level_en.ERROR))
