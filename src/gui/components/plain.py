from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from src.cipher.detail.type import CipherDict, PlainDict
from src.cipher.cipher_algorithm_factory import CipherAlgorithm_en, CipherAlgorithmFactory
from src.gui.builder.combo_box_builder import ComboBoxBuilder
from src.gui.builder.text_edit_builder import TextEditBuilder
from src.gui.detail.component import Component
from src.gui.detail.settings import COMBO_BOX_DEFAULT_WIDTH, DIMENSION_UNIT_SIZE, MAIN_COMPONENT_DEFAULT_WIDTH, TEXT_EDIT_DEFAULT_HEIGHT
from src.gui.signals.action import ActionSignalsSingleton
from src.gui.signals.cipher import CipherSignalsSingleton
from src.gui.signals.plain import PlainSignalsSingleton


class PlainComponent(Component):
    def __init__(self):
        self.action_signals_s = ActionSignalsSingleton()
        self.cipher_signals_s = CipherSignalsSingleton()
        self.plain_signals_s = PlainSignalsSingleton()

        super().__init__(row=0, col=0)

    def connect_to_signals(self) -> None:
        self.action_signals_s.connect("encryption_requested", self.on_encryption_requested)
        self.cipher_signals_s.connect("cipher_changed", self.on_cipher_changed)
        self.cipher_signals_s.connect("cipher_payload_prepared", self.on_cipher_payload_prepared)

    def get_plain(self) -> PlainDict:
        return {"text": self.plain_text_edit.toPlainText(), "cipher_algorithm_to_use": self.cipher_algorithm_combo_box.currentText() }

    def get_cipher_algorithms(self):
        return [cipher_algo.value.as_string() for cipher_algo in CipherAlgorithm_en]

    def initialize_ui(self) -> None:
        self.setMaximumWidth(MAIN_COMPONENT_DEFAULT_WIDTH)

        text_edit_builder = (TextEditBuilder().set_height(TEXT_EDIT_DEFAULT_HEIGHT))
        combo_box_builder = (ComboBoxBuilder().set_width(COMBO_BOX_DEFAULT_WIDTH)
                                              .set_height(DIMENSION_UNIT_SIZE // 1.5))

        plain_box = QtWidgets.QVBoxLayout(self)

        self.plain_text_edit: QtWidgets.QTextEdit = text_edit_builder.build()
        self.plain_text_edit.textChanged.connect(self.on_plain_component_changed)

        self.cipher_algorithm_combo_box: QtWidgets.QComboBox = combo_box_builder.set_values(self.get_cipher_algorithms()).build()
        self.cipher_algorithm_combo_box.currentIndexChanged.connect(self.on_cipher_algorithm_changed)

        plain_box.addWidget(self.plain_text_edit)
        plain_box.addWidget(self.cipher_algorithm_combo_box)

        self.send_algorithm()
        self.elements_to_clear.add(self.plain_text_edit)

    @Slot()
    def on_cipher_changed(self) -> None:
        self.clear()

    @Slot()
    def on_cipher_algorithm_changed(self) -> None:
        self.send_algorithm()

    @Slot(CipherDict)
    def on_cipher_payload_prepared(self, cipher_dict: CipherDict) -> None:
        # TODO: Decrypt and place new plain text inside text edit component
        # TODO: Open modal window, with an line edit in password mode to input password
        password = ""
        self.overwrite(CipherAlgorithmFactory.get(cipher_dict["cipher_algorithm_used"]).decrypt(password, cipher_dict))

    @Slot()
    def on_encryption_requested(self) -> None:
        self.plain_signals_s.emit("plain_payload_prepared", self.get_plain())

    @Slot(str)
    def on_plain_component_changed(self) -> None:
        self.plain_signals_s.emit("plain_changed")

    def overwrite(self, plain: str) -> None:
        self.plain_text_edit.setText(plain)

    def send_algorithm(self) -> None:
        self.plain_signals_s.emit("cipher_algorithm_changed", self.cipher_algorithm_combo_box.currentText())