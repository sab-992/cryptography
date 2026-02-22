from PySide6.QtWidgets import QLineEdit
from src.gui.detail.widget_builder import WidgetBuilder


class LineEditBuilder(WidgetBuilder):
    def __init__(self):
        super().__init__(QLineEdit)

    def initialize_instance(self) -> QLineEdit:
        return QLineEdit()