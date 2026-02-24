from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from src.cipher.cipher_algorithm_factory import Algorithm, CipherAlgorithmFactory
from src.cipher.detail.type import CipherDict, PlainDict
from src.gui.builder.label_builder import LabelBuilder
from src.gui.builder.line_edit_builder import LineEditBuilder
from src.gui.builder.text_edit_builder import TextEditBuilder
from src.gui.detail.component import Component
from src.gui.detail.settings import DIMENSION_UNIT_SIZE, LABEL_DEFAULT_SIZE, MAIN_COMPONENT_DEFAULT_WIDTH, TEXT_EDIT_DEFAULT_HEIGHT
from src.gui.signals.action import ActionSignalsSingleton
from src.gui.signals.cipher import CipherSignalsSingleton
from src.gui.signals.management import ManagementSignalsSingleton
from src.gui.signals.plain import PlainSignalsSingleton


class CipherComponent(Component):
    def __init__(self):
        self.action_signals_s = ActionSignalsSingleton()
        self.cipher_signals_s = CipherSignalsSingleton()
        self.management_signals_s = ManagementSignalsSingleton()
        self.plain_signals_s = PlainSignalsSingleton()

        super().__init__(row=0, col=2)

    def connect_to_signals(self) -> None:
        self.action_signals_s.connect("decryption_requested", self.on_decryption_requested)
        self.management_signals_s.connect("save_requested", self.on_save_requested)
        self.management_signals_s.connect("text_overwrite_requested", self.on_text_overwrite_requested)
        self.plain_signals_s.connect("cipher_algorithm_changed", self.cipher_algorithm_changed)
        self.plain_signals_s.connect("plain_changed", self.on_plain_changed)
        self.plain_signals_s.connect("plain_payload_prepared", self.on_plain_payload_prepared)

    def get_cipher(self) -> CipherDict:
        return { "cipher": self.cipher_text_edit.toPlainText(), "nonce": self.none_line_edit.text(), "salt": self.salt_line_edit.text(), "cipher_algorithm_used": self.cipher_algorithm }

    def initialize_ui(self) -> None:
        self.setMaximumWidth(MAIN_COMPONENT_DEFAULT_WIDTH)

        text_edit_builder = (TextEditBuilder().set_height(TEXT_EDIT_DEFAULT_HEIGHT - 2 * DIMENSION_UNIT_SIZE)) # We take off 2 times the DIMENSION_UNIT_SIZE so that the cipher 
                                                                                                               # component (1 QTextEdit and 2 QLineEdit) is the same size as the 
                                                                                                               # plain component.
        line_edit_builder = (LineEditBuilder().set_height(DIMENSION_UNIT_SIZE))
        label_builder = (LabelBuilder().set_width(LABEL_DEFAULT_SIZE)
                                       .set_height(DIMENSION_UNIT_SIZE))

        cipher_box = QtWidgets.QVBoxLayout(self)
        self.cipher_text_edit: QtWidgets.QTextEdit = text_edit_builder.build()
        self.cipher_text_edit.textChanged.connect(self.on_cipher_component_changed)
        cipher_box.addWidget(self.cipher_text_edit) 

        nonce_box = QtWidgets.QHBoxLayout()
        nonce_box.addWidget(label_builder.set_text("Nonce:").build())
        self.none_line_edit: QtWidgets.QLineEdit = line_edit_builder.build()
        self.none_line_edit.textChanged.connect(self.on_cipher_component_changed)
        nonce_box.addWidget(self.none_line_edit)

        salt_box = QtWidgets.QHBoxLayout()
        salt_box.addWidget(label_builder.set_text("Salt:").build())
        self.salt_line_edit: QtWidgets.QLineEdit = line_edit_builder.build()
        self.salt_line_edit.textChanged.connect(self.on_cipher_component_changed)
        salt_box.addWidget(self.salt_line_edit)

        cipher_box.addLayout(nonce_box)
        cipher_box.addLayout(salt_box)

    @Slot(str)
    def cipher_algorithm_changed(self, algorithm: str) -> None:
        self.cipher_algorithm: Algorithm = CipherAlgorithmFactory.get(algorithm)

    @Slot(str)
    def on_cipher_component_changed(self) -> None:
        self.cipher_signals_s.emit("cipher_changed")

    @Slot()
    def on_decryption_requested(self) -> None:
        self.cipher_signals_s.emit("cipher_payload_prepared", self.get_cipher())

    @Slot()
    def on_plain_changed(self) -> None:
        # TODO: Clear text edit, nonce and salt components
        print("Plain changed !")

    @Slot(PlainDict)
    def on_plain_payload_prepared(self, plain: PlainDict) -> None:
        # TODO: Encrypt and place new CipherDict inside text edit, nonce and salt components
        print("Plain payload to encrypt received !")

    @Slot()
    def on_save_requested(self) -> None:
        self.management_signals_s.emit("payload_prepared", self.get_cipher())

    @Slot(CipherDict)
    def on_text_overwrite_requested(self, cipher_dict: CipherDict) -> None:
        # TODO: Place CipherDict inside text edit, nonce and salt components
        print("Text overwrite requested !")