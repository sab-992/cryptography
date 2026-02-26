from PySide6.QtCore import QObject, Signal
from src.cipher.detail.utils import PlainDict
from src.gui.signals.detail.signal import SignalSingleton


class PlainSignalsSingleton(SignalSingleton):
    class PlainSignals(QObject):
        cipher_algorithm_changed = Signal(str)
        plain_changed = Signal()
        plain_payload_prepared = Signal(PlainDict)

    def __init__(self):
        super().__init__(self.PlainSignals())