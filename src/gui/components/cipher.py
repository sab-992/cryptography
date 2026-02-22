from PySide6 import QtWidgets
from src.gui.builder.label_builder import LabelBuilder
from src.gui.builder.line_edit_builder import LineEditBuilder
from src.gui.builder.text_edit_builder import TextEditBuilder
from src.gui.detail.component import Component
from src.gui.detail.settings import DIMENSION_UNIT_SIZE, LABEL_DEFAULT_SIZE, MAIN_COMPONENT_DEFAULT_WIDTH, TEXT_EDIT_DEFAULT_HEIGHT


class CipherComponent(Component):
    def __init__(self):
        super().__init__(row=0, col=2)
        self.initialize_ui()

    def initialize_ui(self) -> None:
        self.setMaximumWidth(MAIN_COMPONENT_DEFAULT_WIDTH)

        text_edit_builder = (TextEditBuilder().set_height(TEXT_EDIT_DEFAULT_HEIGHT - 2 * DIMENSION_UNIT_SIZE)) # We take off 2 times the DIMENSION_UNIT_SIZE so that the cipher 
                                                                                                               # component (1 QTextEdit and 2 QLineEdit) is the same size as the 
                                                                                                               # plain component.
        line_edit_builder = (LineEditBuilder().set_height(DIMENSION_UNIT_SIZE))
        label_builder = (LabelBuilder().set_width(LABEL_DEFAULT_SIZE)
                                       .set_height(DIMENSION_UNIT_SIZE))

        cipher_box = QtWidgets.QVBoxLayout(self)
        cipher_box.addWidget(text_edit_builder.build()) 

        nonce_box = QtWidgets.QHBoxLayout()
        nonce_box.addWidget(label_builder.set_text("Nonce:").build())
        nonce_box.addWidget(line_edit_builder.build())

        salt_box = QtWidgets.QHBoxLayout()
        salt_box.addWidget(label_builder.set_text("Salt:").build())
        salt_box.addWidget(line_edit_builder.build())

        cipher_box.addLayout(nonce_box)
        cipher_box.addLayout(salt_box)