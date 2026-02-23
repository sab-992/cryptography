from PySide6 import QtWidgets
from src.cipher.cipher_algorithm_factory import CipherAlgorithm_en
from src.gui.builder.combo_box_builder import ComboBoxBuilder
from src.gui.builder.text_edit_builder import TextEditBuilder
from src.gui.detail.component import Component
from src.gui.detail.settings import COMBO_BOX_DEFAULT_WIDTH, DIMENSION_UNIT_SIZE, MAIN_COMPONENT_DEFAULT_WIDTH, TEXT_EDIT_DEFAULT_HEIGHT


class PlainComponent(Component):
    def __init__(self):
        super().__init__(row=0, col=0)
        self.initialize_ui()

    def initialize_ui(self) -> None:
        self.setMaximumWidth(MAIN_COMPONENT_DEFAULT_WIDTH)

        text_edit_builder = (TextEditBuilder().set_height(TEXT_EDIT_DEFAULT_HEIGHT))
        combo_box_builder = (ComboBoxBuilder().set_width(COMBO_BOX_DEFAULT_WIDTH)
                                              .set_height(DIMENSION_UNIT_SIZE // 1.5))

        plain_box = QtWidgets.QVBoxLayout(self)
        plain_box.addWidget(text_edit_builder.build())
        plain_box.addWidget(combo_box_builder.set_values(self.get_cipher_algorithms()).build())

    def get_cipher_algorithms(self):
        return [f"{cipher_alg.value.name}, mode: {cipher_alg.value.mode}" for cipher_alg in CipherAlgorithm_en]