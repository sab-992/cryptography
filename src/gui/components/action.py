from PySide6 import QtWidgets
from src.gui.builder.push_button_builder import PushButtonBuilder
from src.gui.detail.component import Component
from src.gui.detail.settings import ACTION_BUTTON_SIZE, DIMENSION_UNIT_SIZE


class ActionComponent(Component):
    def __init__(self):
        super().__init__(row=0, col=1)
        self.initialize_ui()

    def initialize_ui(self) -> None:
        self.setFixedWidth(ACTION_BUTTON_SIZE + DIMENSION_UNIT_SIZE // 2)
        PUSH_BUTTON_STYLE = """\
QPushButton {
    border: none;
    background: transparent;
    border-radius: 50px;
}
QPushButton:hover {
    background: rgba(255, 255, 255, 30);
}
QPushButton:pressed {
    background: rgba(255, 255, 255, 60);
}
"""
        encrypt_decrypt_push_button_builder = (PushButtonBuilder().set_width(ACTION_BUTTON_SIZE)
                                                                  .set_height(ACTION_BUTTON_SIZE)
                                                                  .set_image_size(ACTION_BUTTON_SIZE, ACTION_BUTTON_SIZE)
                                                                  .set_style(PUSH_BUTTON_STYLE))

        action_box = QtWidgets.QVBoxLayout(self)
        action_box.addWidget(encrypt_decrypt_push_button_builder.set_image("decrypt-arrow.png").build())
        action_box.addWidget(encrypt_decrypt_push_button_builder.set_image("encrypt-arrow.png").build())