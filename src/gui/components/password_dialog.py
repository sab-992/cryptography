from PySide6 import QtWidgets
from src.gui.builder.dialog_builder import QDialogBuilder
from src.gui.builder.label_builder import LabelBuilder
from src.gui.builder.line_edit_builder import LineEditBuilder
from src.gui.builder.push_button_builder import PushButtonBuilder
from src.gui.detail.component import Component
from src.gui.detail.settings import BUTTON_DEFAULT_HEIGHT, DIMENSION_UNIT_SIZE


PASSWORD_DIALOG_TITLE = "Enter a password"
PASSWORD_DIALOG_PROMPT = "Please enter your password:"
PASSWORD_DIALOG_WIDTH = 640
PASSWORD_DIALOG_HEIGHT = 360


class PasswordDialogComponent(Component):
    def __init__(self):
        self.dialog: QtWidgets.QDialog = None

        super().__init__(row=1, col=1)

    def initialize_ui(self) -> None:
        self.dialog: QtWidgets.QDialog = (QDialogBuilder().set_window_title(PASSWORD_DIALOG_TITLE)
                                                     .set_width(PASSWORD_DIALOG_WIDTH)
                                                     .set_height(PASSWORD_DIALOG_HEIGHT)
                                                     .set_modal(True).build())
        label_builder = (LabelBuilder().set_height(DIMENSION_UNIT_SIZE))
        line_edit_builder = (LineEditBuilder().set_height(DIMENSION_UNIT_SIZE))
        push_button_builder = PushButtonBuilder().set_height(BUTTON_DEFAULT_HEIGHT)

        layout = QtWidgets.QVBoxLayout()
        label: QtWidgets.QLabel = label_builder.set_text(PASSWORD_DIALOG_PROMPT).build()
        self.password_input: QtWidgets.QLineEdit = line_edit_builder.set_echo_mode(QtWidgets.QLineEdit.EchoMode.Password).build()
        self.password_input.returnPressed.connect(self.dialog.accept)

        button_layout = QtWidgets.QVBoxLayout()
        ok_button: QtWidgets.QPushButton = push_button_builder.set_text("Ok").build()
        ok_button.clicked.connect(self.dialog.accept)
        cancel_button: QtWidgets.QPushButton = push_button_builder.set_text("Cancel").build()
        cancel_button.clicked.connect(self.dialog.reject)

        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addWidget(label)
        layout.addWidget(self.password_input)
        layout.addLayout(button_layout)

        self.dialog.setLayout(layout)
        self.password_input.setFocus()

    def open(self) -> str:
        if not self.dialog:
            return ""

        if self.dialog.exec() != QtWidgets.QDialog.DialogCode.Accepted:
            return ""

        return self.password_input.text()