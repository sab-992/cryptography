from PySide6.QtCore import QObject, Signal
from src.cipher.detail.type import CipherDict
from src.gui.signals.detail.signal import SignalSingleton

class CipherManagementSignalsSingleton(SignalSingleton):
    class CipherManagementSignals(QObject):
        payload_prepared = Signal(CipherDict)
        save_requested = Signal()
        cipher_text_overwrite_requested = Signal(CipherDict)

    def __init__(self):
        super().__init__(self.CipherManagementSignals())