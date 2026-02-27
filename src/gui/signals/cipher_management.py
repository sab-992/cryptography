from PySide6.QtCore import QObject, Signal
from src.gui.signals.detail.signal import SignalSingleton

class CipherManagementSignalsSingleton(SignalSingleton):
    class CipherManagementSignals(QObject):
        payload_prepared = Signal(str)
        save_requested = Signal()
        cipher_text_overwrite_requested = Signal(str)

    def __init__(self):
        super().__init__(self.CipherManagementSignals())