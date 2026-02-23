from abc import ABC, abstractmethod
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget
from src.utils.logger import Logger, Level_en
from src.gui.detail.settings import DEFAULT_FONT_SIZE
from typing import Self, Type, TypeVar

T = TypeVar('T')

class WidgetBuilder(ABC):
    def __init__(self, cls: Type[T]):
        if not issubclass(cls, QWidget):
            self.error(f"Type {cls.__name__} is not a Qt widget")
        self.width: int = None
        self.height: int = None
        self.font: QFont = None

    def build(self) -> T:
        widget: QWidget = self.initialize_instance()

        if self.width:
            widget.setFixedWidth(self.width)

        if self.height:
            widget.setFixedHeight(self.height)

        if not self.font:
            default_font = widget.font()
            self.set_font(default_font.family(), DEFAULT_FONT_SIZE)

        widget.setFont(self.font)

        return widget

    @abstractmethod
    def initialize_instance(self) -> T:
        pass

    def set_font(self, family: str, size: int, weight: int = QFont.Weight.Normal, italic: bool = False) -> Self:
        self.font = QFont(family, size, weight, italic)
        return self

    def set_height(self, height: int) -> Self:
        self.height = height
        return self

    def set_width(self, width: int) -> Self:
        self.width = width
        return self

    def error(self, reason: str) -> None:
        raise Exception(Logger.log(message=f"{__class__.__name__} - {reason}", level=Level_en.ERROR))
