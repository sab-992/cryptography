from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from src.cipher.cipher_algorithm_factory import CipherAlgorithmFactory
from src.cipher.detail.utils import EncryptionRequest, is_string_empty
from src.gui.components.password_dialog import PasswordDialogComponent
from src.gui.builder.text_edit_builder import TextEditBuilder
from src.gui.detail.component import Component
from src.gui.detail.settings import DIMENSION_UNIT_SIZE, MAIN_COMPONENT_DEFAULT_WIDTH, TEXT_EDIT_DEFAULT_HEIGHT
from src.gui.signals.action import ActionSignalsSingleton
from src.gui.signals.cipher import CipherSignalsSingleton
from src.gui.signals.cipher_management import CipherManagementSignalsSingleton
from src.gui.signals.plain import PlainSignalsSingleton
from src.utils.logger import Logger, Level_en


class CipherComponent(Component):
    def __init__(self):
        self.action_signals_s = ActionSignalsSingleton()
        self.cipher_signals_s = CipherSignalsSingleton()
        self.cipher_management_signals_s = CipherManagementSignalsSingleton()
        self.plain_signals_s = PlainSignalsSingleton()

        super().__init__(row=1, col=2)

    def connect_to_signals(self) -> None:
        self.action_signals_s.connect("decryption_requested", self.on_decryption_requested)
        self.cipher_management_signals_s.connect("save_requested", self.on_save_requested)
        self.cipher_management_signals_s.connect("cipher_text_overwrite_requested", self.on_cipher_text_overwrite_requested)
        self.plain_signals_s.connect("plain_changed", self.on_plain_changed)
        self.plain_signals_s.connect("plain_payload_prepared", self.on_plain_payload_prepared)

    def get_cipher(self) -> str:
        return self.cipher_text_edit.toPlainText()

    def initialize_ui(self) -> None:
        self.setMaximumWidth(MAIN_COMPONENT_DEFAULT_WIDTH)

        text_edit_builder = (TextEditBuilder().set_height(TEXT_EDIT_DEFAULT_HEIGHT - 2 * DIMENSION_UNIT_SIZE)) # We take off 2 times the DIMENSION_UNIT_SIZE so that the cipher 
                                                                                                               # component (1 QTextEdit and 2 QLineEdit) is the same size as the 
                                                                                                               # plain component.

        cipher_box = QtWidgets.QVBoxLayout(self)
        self.cipher_text_edit: QtWidgets.QTextEdit = text_edit_builder.build()
        self.cipher_text_edit.textChanged.connect(self.on_cipher_component_changed)
        cipher_box.addWidget(self.cipher_text_edit) 

        self.elements_to_clear.add(self.cipher_text_edit)

    def is_empty(self) -> bool:
        return  len(self.cipher_text_edit.toPlainText()) <= 0

    @Slot(str)
    def on_cipher_component_changed(self) -> None:
        self.cipher_signals_s.emit("cipher_changed")

    @Slot()
    def on_decryption_requested(self) -> None:
        if not self.is_empty():
            self.cipher_signals_s.emit("cipher_payload_prepared", self.get_cipher())

    @Slot()
    def on_plain_changed(self) -> None:
        self.clear()

    @Slot(EncryptionRequest)
    def on_plain_payload_prepared(self, request: EncryptionRequest) -> None:
        password = PasswordDialogComponent().open()

        if not password or len(password) <= 0:
            Logger.log(message="No password entered", level=Level_en.ERROR, to_std_out=True)
        else:
            self.overwrite(CipherAlgorithmFactory.get(request["cipher_algorithm_to_use"]).encrypt(password, request["text"]))

    @Slot()
    def on_save_requested(self) -> None:
        if self.is_empty():
            Logger.log(message="Nothing to save", level=Level_en.WARNING, to_std_out=True)
            return

        self.cipher_management_signals_s.emit("payload_prepared", self.get_cipher())

    @Slot(str)
    def on_cipher_text_overwrite_requested(self, cipher: str) -> None:
        self.overwrite(cipher)

    def overwrite(self, cipher: str) -> None:
        if is_string_empty(cipher):
            return

        self.cipher_text_edit.setText(cipher)