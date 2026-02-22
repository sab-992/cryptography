from PySide6.QtWidgets import QTextEdit
from src.gui.detail.widget_builder import WidgetBuilder


class TextEditBuilder(WidgetBuilder):
    def __init__(self):
        super().__init__(QTextEdit)

    def initialize_instance(self) -> QTextEdit:
        return QTextEdit()