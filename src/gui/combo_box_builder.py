from PySide6.QtWidgets import QComboBox
from src.gui.detail.widget_builder import WidgetBuilder
from typing import Self


class ComboBoxBuilder(WidgetBuilder):
    def __init__(self):
        super().__init__(QComboBox)
        self.__values: list[str] = []

    def initialize_instance(self) -> QComboBox:
        if len(self.__values) <= 0:
            self.error("No values given")

        widget = self.widget_type()

        for value in self.__values:
            widget.addItem(value)

        return widget

    def set_values(self, values: list[str]) -> Self:
        self.__values = values
        return self