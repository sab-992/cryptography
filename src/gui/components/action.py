from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from src.gui.builder.push_button_builder import PushButtonBuilder
from src.gui.detail.component import Component
from src.gui.detail.settings import ACTION_BUTTON_SIZE, DIMENSION_UNIT_SIZE
from src.gui.detail.styles import get_button_hover_effect
from src.gui.signals.action import ActionSignalsSingleton


class ActionComponent(Component):
    def __init__(self):
        self.action_signal_s = ActionSignalsSingleton()

        super().__init__(row=0, col=1)

    def initialize_ui(self) -> None:
        self.setFixedWidth(ACTION_BUTTON_SIZE + DIMENSION_UNIT_SIZE // 2)
        push_button_builder = (PushButtonBuilder().set_width(ACTION_BUTTON_SIZE)
                                                  .set_height(ACTION_BUTTON_SIZE)
                                                  .set_image_size(ACTION_BUTTON_SIZE, ACTION_BUTTON_SIZE)
                                                  .set_style(f"QPushButton {"{border: none; background: transparent; border-radius: 50px;}"}{get_button_hover_effect("transparent")}"))

        action_box = QtWidgets.QVBoxLayout(self)

        decrypt_btn: QtWidgets.QPushButton = push_button_builder.set_image("decrypt-arrow.png").build()
        decrypt_btn.clicked.connect(self.on_decrypt_btn_clicked)

        encrypt_btn: QtWidgets.QPushButton = push_button_builder.set_image("encrypt-arrow.png").build()
        encrypt_btn.clicked.connect(self.on_encrypt_btn_clicked)

        action_box.addWidget(decrypt_btn)
        action_box.addWidget(encrypt_btn)

    @Slot()
    def on_decrypt_btn_clicked(self):
        self.action_signal_s.emit("decryption_requested")

    @Slot()
    def on_encrypt_btn_clicked(self):
        self.action_signal_s.emit("encryption_requested")