from PySide6.QtWidgets import QDialog
from src.gui.detail.widget_builder import WidgetBuilder
from typing import Self


class QDialogBuilder(WidgetBuilder):
    def __init__(self):
        super().__init__(QDialog)

        self.modal: bool = False
        self.w_title: str = "Dialog"


    def initialize_instance(self) -> QDialog:
        dialog = QDialog()
        dialog.setWindowTitle(self.w_title)
        dialog.setModal(self.modal)

        return dialog
    
    def set_modal(self, modal: bool) -> Self:
        self.modal = modal
        return self

    def set_window_title(self, title: str) -> Self:
        self.w_title = title
        return self
