from dataclasses import dataclass
from PySide6 import QtWidgets, QtCore


type QtComponent = QtWidgets.QWidget | QtWidgets.QLayout

@dataclass
class UIComponent:
    qt_component: QtComponent
    row: int
    col: int
    row_span: int
    col_span: int
    alignment: QtCore.Qt.AlignmentFlag

    def get_tuple(self) -> tuple[QtComponent, int, int, int, int, QtCore.Qt.AlignmentFlag]:
        return (self.qt_component, self.row, self.col, self.row_span, self.col_span)