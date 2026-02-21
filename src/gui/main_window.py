import sys
from PySide6 import QtWidgets
from src.utils.logger import Logger, Level_en
from typing import Literal, Self

WINDOW_NAME: str = "Cryptography"
WINDOW_SIZE: tuple[int] = (1920, 1080)

WidgetType = Literal["QWidget", "QLayout"]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.__app = QtWidgets.QApplication([]) # Keep this before the super() call because: must construct a QApplication before a QWidget
        super().__init__()
        
        self.set_window_settings()
        self.initialize_ui()

        Logger.log(message="Main window ready", level=Level_en.INFO, to_std_out=True)

    # X and Y starts from the top left corner.
    def add_layout(self, component: QtWidgets.QWidget, x: int, y: int):
        self.__ui_components.append((component, x, y, "QLayout"))

    # X and Y starts from the top left corner.
    def add_widget(self, component: QtWidgets.QWidget, x: int, y: int):
        self.__ui_components.append((component, x, y, "QWidget"))

    def create_ui_components(self):
        pass

    def initialize_ui(self):
        # Main layout
        main_layout_grid = QtWidgets.QGridLayout(self.centralWidget())

        # Create UI components.
        self.create_ui_components()

        # Add components to the main layout.
        for component_info in self.__ui_components:
            match component_info[3]:
                case "QWidget":
                    main_layout_grid.addWidget(component_info[0], component_info[1], component_info[2])
                case "QLayout":
                    main_layout_grid.addLayout(component_info[0], component_info[1], component_info[2])
                case _:
                    raise Exception(Logger.log(message=f"Component type is not handled", level=Level_en.ERROR))

    def set_window_settings(self) -> None:
        self.setWindowTitle(WINDOW_NAME)
        self.resize(*WINDOW_SIZE)
        self.setCentralWidget(QtWidgets.QWidget())
        self.__ui_components: list[tuple[QtWidgets.QWidget, int, int, WidgetType]] = []

    def start(self) -> Self:
        self.show()
        sys.exit(self.__app.exec())