from PySide6 import QtWidgets, QtCore


# Cannot be an abstract class due to the fact that it already inherits QtWidgets.QWidget.
class Component(QtWidgets.QWidget):
    def __init__(self, row: int, col: int, row_span: int=1, col_span: int=1, alignment:QtCore.Qt.AlignmentFlag=None):
        super().__init__()
        self.row: int = row
        self.col: int = col
        self.row_span: int = row_span
        self.col_span: int = col_span
        self.alignment: QtCore.Qt.AlignmentFlag = alignment

    def get_tuple(self) -> tuple[QtWidgets.QWidget, int, int, int, int, QtCore.Qt.AlignmentFlag]:
        return (self, self.row, self.col, self.row_span, self.col_span)
    
    def initialize_ui() -> None:
        pass