import sys
from PySide6 import QtWidgets
from src.utils.logger import Logger, Level_en
from src.gui.detail.ui_component import UIComponent, QtComponent


WINDOW_NAME: str = "Cryptography"
WINDOW_SIZE: tuple[int] = (1920, 1080)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.__app = QtWidgets.QApplication([]) # Keep this before the super() call because: must construct a QApplication before a QWidget
        super().__init__()
        
        self.set_window_settings()
        self.initialize_ui()

        Logger.log(message="Main window ready", level=Level_en.INFO, to_std_out=True)

    def add_component(self, qt_component: QtComponent, row: int, col: int, row_span: int = 1, col_span: int = 1):
        """
        row: starts at 0 (left side).

        col: starts at 0 (top).
        """
        self.__ui_components.append(UIComponent(qt_component, row, col, row_span, col_span))

    def create_ui_components(self):
        pass

    def initialize_ui(self):
        # Main layout
        main_layout_grid = QtWidgets.QGridLayout(self.centralWidget())

        # Create UI components.
        self.create_ui_components()

        # Add components to the main layout.
        for component in self.__ui_components:
            if isinstance(component.qt_component, QtWidgets.QWidget):
                main_layout_grid.addWidget(*component.get_tuple())
            elif isinstance(component.qt_component, QtWidgets.QLayout):
                main_layout_grid.addLayout(*component.get_tuple())
            else:
                raise Exception(Logger.log(message=f"Component type: '{component.type}' is not handled", level=Level_en.ERROR))

    def set_window_settings(self) -> None:
        self.setWindowTitle(WINDOW_NAME)
        self.resize(*WINDOW_SIZE)
        self.setCentralWidget(QtWidgets.QWidget())
        self.__ui_components: list[UIComponent] = []

    def start(self) -> None:
        self.show()
        sys.exit(self.__app.exec())