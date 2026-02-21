from PySide6.QtWidgets import QComboBox
from src.gui.detail.widget_builder import WidgetBuilder
from typing import Self


class ComboBox(WidgetBuilder):
    def __init__(self):
        super().__init__(QComboBox())
        self.__values: list[str] = []

    def get(self) -> QComboBox:
        if len(self.__values) <= 0:
            self.error("No values given")

        if not isinstance(self.widget, QComboBox):
            self.error("Cannot create components other than QComboBox")

        for value in self.__values:
            self.widget.addItem(value)

        return self.widget

    def set_values(self, values: list[str]) -> Self:
        self.__values = values
        return self