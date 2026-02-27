from PySide6.QtCore import QObject, Signal
from src.cipher.detail.utils import EncryptionRequest
from src.gui.signals.detail.signal import SignalSingleton


class PlainSignalsSingleton(SignalSingleton):
    class PlainSignals(QObject):
        plain_changed = Signal()
        plain_payload_prepared = Signal(EncryptionRequest)

    def __init__(self):
        super().__init__(self.PlainSignals())