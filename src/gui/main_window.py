import sys
from PySide6 import QtWidgets
from src.gui.detail.component import Component
from src.gui.components.action import ActionComponent
from src.gui.components.cipher import CipherComponent
from src.gui.components.management import ManagementComponent
from src.gui.components.plain import PlainComponent
from src.gui.detail.settings import WINDOW_NAME, WINDOW_SIZE
from src.utils.logger import Logger, Level_en


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.__app = QtWidgets.QApplication([]) # Keep this before the super() call because: must construct a QApplication before a QWidget
        super().__init__()
        
        self.set_window_settings()
        self.initialize_ui()

        Logger.log(message="Main window ready", level=Level_en.INFO, to_std_out=True)

    def initialize_ui(self):
        main_layout_grid = QtWidgets.QGridLayout(self.centralWidget())

        components: list[Component] = [ActionComponent(),
                                       CipherComponent(),
                                       ManagementComponent(),
                                       PlainComponent()]

        for component in components:
            parameters = component.get_tuple()
            if component.alignment:
                parameters += (component.alignment,)

            if not isinstance(component, QtWidgets.QWidget):
                raise Exception(Logger.log(message=f"Component type: '{type(component)}' is not handled", level=Level_en.ERROR))

            main_layout_grid.addWidget(*parameters)

    def set_window_settings(self) -> None:
        self.setWindowTitle(WINDOW_NAME)
        self.resize(*WINDOW_SIZE)
        self.setCentralWidget(QtWidgets.QWidget())

    def start(self) -> None:
        self.show()
        sys.exit(self.__app.exec())