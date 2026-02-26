from PySide6.QtWidgets import QLineEdit
from src.gui.detail.widget_builder import WidgetBuilder
from typing import Self


class LineEditBuilder(WidgetBuilder):
    def __init__(self):
        super().__init__(QLineEdit)
        self.echo_mode: QLineEdit.EchoMode = QLineEdit.EchoMode.Normal

    def initialize_instance(self) -> QLineEdit:
        line_edit = QLineEdit()
        line_edit.setEchoMode(self.echo_mode)
        return line_edit

    def set_echo_mode(self, echo_mode: QLineEdit.EchoMode) -> Self:
        self.echo_mode = echo_mode
        return self