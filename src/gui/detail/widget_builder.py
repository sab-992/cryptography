from PySide6.QtWidgets import QWidget
from src.utils.logger import Logger, Level_en
from typing import Self


class WidgetBuilder():
    def __init__(self, widget: QWidget):
        self.widget: QWidget = widget

    def set_height(self, height: int) -> Self:
        self.widget.setFixedHeight(height)
        return self

    def set_width(self, width: int) -> Self:
        self.widget.setFixedWidth(width)
        return self

    def error(self, reason: str) -> None:
        raise Exception(Logger.log(message=f"{__class__.__name__} - {reason}", level=Level_en.ERROR))
