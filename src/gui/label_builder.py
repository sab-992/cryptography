from PySide6.QtWidgets import QLabel
from src.gui.detail.widget_builder import WidgetBuilder
from typing import Self


class LabelBuilder(WidgetBuilder):
    def __init__(self):
        super().__init__(QLabel)
        self.__text = None

    def initialize_instance(self) -> QLabel:
        if not self.__text or len(self.__text) <= 0:
            self.error("No text given")

        return QLabel(text=self.__text)

    def set_text(self, text: str) -> Self:
        self.__text = text
        return self