from PySide6.QtCore import QObject, Signal
from src.gui.signals.detail.signal import SignalSingleton

class PlainManagementSignalsSingleton(SignalSingleton):
    class PlainManagementSignals(QObject):
        plain_text_overwrite_requested = Signal(str)

    def __init__(self):
        super().__init__(self.PlainManagementSignals())