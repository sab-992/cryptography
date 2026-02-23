from abc import ABC, abstractmethod
from dataclasses import dataclass
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget
from src.utils.logger import Logger, Level_en
from src.gui.detail.settings import DEFAULT_FONT_FAMILY, DEFAULT_FONT_SIZE
from typing import Self, Type, TypeVar, Any
from types import FunctionType


T = TypeVar('T')

@dataclass
class Attribute():
    value: Any
    fct: FunctionType

class WidgetBuilder(ABC):
    def __init__(self, cls: Type[T]):
        if not issubclass(cls, QWidget):
            self.error(f"Type {cls.__name__} is not a Qt widget")

        self.attributes: dict[str, Attribute] = { "font":   Attribute(QFont(DEFAULT_FONT_FAMILY, DEFAULT_FONT_SIZE), QWidget.setFont),
                                                  "height": Attribute(None, QWidget.setFixedHeight),
                                                  "style":  Attribute(None, QWidget.setStyleSheet),
                                                  "width":  Attribute(None, QWidget.setFixedWidth) }

    def build(self) -> T:
        widget: QWidget = self.initialize_instance()

        for _, attribute in self.attributes.items():
            if attribute.value:
                attribute.fct(widget, attribute.value)

        return widget
    
    def error(self, reason: str) -> None:
        raise Exception(Logger.log(message=f"{__class__.__name__} - {reason}", level=Level_en.ERROR))

    @abstractmethod
    def initialize_instance(self) -> T:
        pass

    def set_font(self, family: str, size: int, weight: int = QFont.Weight.Normal, italic: bool = False) -> Self:
        self.attributes["font"].value = QFont(family, size, weight, italic)
        return self

    def set_height(self, height: int) -> Self:
        self.attributes["height"].value = height
        return self
    
    def set_style(self, style: str) -> Self:
        self.attributes["style"].value = style
        return self

    def set_width(self, width: int) -> Self:
        self.attributes["width"].value = width
        return self