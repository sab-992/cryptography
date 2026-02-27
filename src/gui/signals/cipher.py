from PySide6.QtCore import QObject, Signal
from src.gui.signals.detail.signal import SignalSingleton


class CipherSignalsSingleton(SignalSingleton):
    class CipherSignals(QObject):
        cipher_changed = Signal()
        cipher_payload_prepared = Signal(str)

    def __init__(self):
        super().__init__(self.CipherSignals())