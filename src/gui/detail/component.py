from PySide6 import QtWidgets, QtCore


class Component(QtWidgets.QWidget):
    def __init__(self, row: int, col: int, row_span: int=1, col_span: int=1, alignment:QtCore.Qt.AlignmentFlag=None):
        super().__init__()

        self.row: int = row
        self.col: int = col
        self.row_span: int = row_span
        self.col_span: int = col_span
        self.alignment: QtCore.Qt.AlignmentFlag = alignment
        self.elements_to_clear: set[QtWidgets.QWidget] = set()

        self.connect_to_signals()
        self.initialize_ui()

    def clear(self) -> None:
        for element in self.elements_to_clear:
            element.blockSignals(True)
            if hasattr(element, 'clear'):
                element.clear()
            element.blockSignals(False)

    def connect_to_signals(self) -> None:
        pass

    def initialize_ui(self) -> None:
        pass

    def __iter__(self):
        elems = [self, self.row, self.col, self.row_span, self.col_span]

        if self.alignment:
            elems.append(self.alignment)
        return iter(elems)