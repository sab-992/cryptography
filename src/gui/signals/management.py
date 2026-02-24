from PySide6.QtCore import QObject, Signal
from src.cipher.detail.type import CipherDict
from src.gui.signals.detail.signal import SignalSingleton

class ManagementSignalsSingleton(SignalSingleton):
    class ManagementSignals(QObject):
        payload_prepared = Signal(CipherDict)
        save_requested = Signal()
        text_overwrite_requested = Signal(CipherDict)

    def __init__(self):
        super().__init__(self.ManagementSignals())