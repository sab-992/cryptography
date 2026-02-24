from PySide6.QtCore import QObject, Signal
from src.gui.signals.detail.signal import SignalSingleton


class ActionSignalsSingleton(SignalSingleton):
    class ActionSignals(QObject):
        encryption_requested = Signal()
        decryption_requested = Signal()

    def __init__(self):
        super().__init__(self.ActionSignals())