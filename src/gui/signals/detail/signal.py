from PySide6.QtCore import QObject, Signal
from src.utils.singleton import SingletonMeta
from types import FunctionType
from typing import Any

class SignalSingleton(metaclass=SingletonMeta):
    def __init__(self, signals: QObject):
        self.signals: QObject = signals

    def connect(self, name: str, fct: FunctionType) -> None:
        getattr(self.signals, name).connect(fct)

    def emit(self, name: str, value: Any = None) -> None:
        signal: Signal = getattr(self.signals, name)

        if value == None:
            signal.emit()
        else:
            signal.emit(value)