import sys
from PySide6 import QtCore, QtWidgets
from src.gui.builder.combo_box_builder import ComboBoxBuilder
from src.gui.builder.label_builder import LabelBuilder
from src.gui.builder.line_edit_builder import LineEditBuilder
from src.gui.builder.push_button_builder import PushButtonBuilder
from src.gui.builder.text_edit_builder import TextEditBuilder
from src.gui.detail.ui_component import QtComponent, UIComponent
from src.utils.logger import Logger, Level_en

# Main window settings
WINDOW_NAME: str = "Cryptography"
WINDOW_SIZE: tuple[int] = (1920, 1080)

# UI
DIMENSION_UNIT_SIZE: int = 50
ACTION_BUTTON_SIZE: int = 100
BUTTON_DEFAULT_WIDTH: int = DIMENSION_UNIT_SIZE * 3
BUTTON_DEFAULT_HEIGHT: int = DIMENSION_UNIT_SIZE * 1.5
COMBO_BOX_DEFAULT_WIDTH: int = DIMENSION_UNIT_SIZE * 5
LABEL_DEFAULT_SIZE: int = DIMENSION_UNIT_SIZE * 2
MAIN_COMPONENT_DEFAULT_WIDTH: int = DIMENSION_UNIT_SIZE * 12 + LABEL_DEFAULT_SIZE
TEXT_EDIT_DEFAULT_HEIGHT: int = DIMENSION_UNIT_SIZE * 16

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.__app = QtWidgets.QApplication([]) # Keep this before the super() call because: must construct a QApplication before a QWidget
        super().__init__()
        
        self.set_window_settings()
        self.initialize_ui()

        Logger.log(message="Main window ready", level=Level_en.INFO, to_std_out=True)

    def add_component(self, qt_component: QtComponent, row: int, col: int, row_span: int = 1, col_span: int = 1, alignment: QtCore.Qt.AlignmentFlag = None):
        """
        row: starts at 0 (left side).

        col: starts at 0 (top).
        """
        self.__ui_components.append(UIComponent(qt_component, row, col, row_span, col_span, alignment))

    def create_ui_components(self):
        self.add_component(self.get_plain_section(), row=0, col=0)
        self.add_component(self.get_action_section(), row=0, col=1, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.add_component(self.get_cipher_section(), row=0, col=2)
        self.add_component(self.get_management_section(), row=1, col=2, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

    def initialize_ui(self):
        main_layout_grid = QtWidgets.QGridLayout(self.centralWidget())

        self.create_ui_components()

        for component in self.__ui_components:
            params = component.get_tuple()
            if component.alignment:
                params += (component.alignment,)

            if isinstance(component.qt_component, QtWidgets.QWidget):
                main_layout_grid.addWidget(*component.get_tuple())
            elif isinstance(component.qt_component, QtWidgets.QLayout):
                main_layout_grid.addLayout(*component.get_tuple())
            else:
                raise Exception(Logger.log(message=f"Component type: '{type(component.qt_component)}' is not handled", level=Level_en.ERROR))

    def set_window_settings(self) -> None:
        self.setWindowTitle(WINDOW_NAME)
        self.resize(*WINDOW_SIZE)
        self.setCentralWidget(QtWidgets.QWidget())
        self.__ui_components: list[UIComponent] = []

    def start(self) -> None:
        self.show()
        sys.exit(self.__app.exec())

    # TODO: Separate all section functions into their own classes.
    def get_action_section(self) -> QtWidgets.QWidget:
        encrypt_decrypt_push_button_builder = (PushButtonBuilder().set_width(ACTION_BUTTON_SIZE)
                                                                  .set_height(ACTION_BUTTON_SIZE)
                                                                  .set_image_size(ACTION_BUTTON_SIZE, ACTION_BUTTON_SIZE))

        action_container = QtWidgets.QWidget()
        action_container.setFixedWidth(ACTION_BUTTON_SIZE + DIMENSION_UNIT_SIZE // 2)

        action_box = QtWidgets.QVBoxLayout(action_container)
        action_box.addWidget(encrypt_decrypt_push_button_builder.set_image("decrypt-arrow.png").build())
        action_box.addWidget(encrypt_decrypt_push_button_builder.set_image("encrypt-arrow.png").build())

        return action_container

    def get_cipher_section(self) -> QtWidgets.QWidget:
        text_edit_builder = (TextEditBuilder().set_height(TEXT_EDIT_DEFAULT_HEIGHT - 2 * DIMENSION_UNIT_SIZE)) # We take off 2 times the DIMENSION_UNIT_SIZE so that the cipher 
                                                                                                               # section (1 QTextEdit and 2 QLineEdit) is the same size as the 
                                                                                                               # plain section.
        line_edit_builder = (LineEditBuilder().set_height(DIMENSION_UNIT_SIZE))
        label_builder = (LabelBuilder().set_width(LABEL_DEFAULT_SIZE)
                                       .set_height(DIMENSION_UNIT_SIZE))

        cipher_container = QtWidgets.QWidget()
        cipher_container.setMaximumWidth(MAIN_COMPONENT_DEFAULT_WIDTH)

        cipher_box = QtWidgets.QVBoxLayout(cipher_container)
        cipher_box.addWidget(text_edit_builder.build()) 

        nonce_box = QtWidgets.QHBoxLayout()
        nonce_box.addWidget(label_builder.set_text("Nonce:").build())
        nonce_box.addWidget(line_edit_builder.build())

        salt_box = QtWidgets.QHBoxLayout()
        salt_box.addWidget(label_builder.set_text("Salt:").build())
        salt_box.addWidget(line_edit_builder.build())

        cipher_box.addLayout(nonce_box)
        cipher_box.addLayout(salt_box)

        return cipher_container

    def get_management_section(self) -> QtWidgets.QWidget:
        combo_box_builder = (ComboBoxBuilder().set_width(COMBO_BOX_DEFAULT_WIDTH)
                                              .set_height(DIMENSION_UNIT_SIZE // 1.5))
        push_button_builder = PushButtonBuilder().set_height(BUTTON_DEFAULT_HEIGHT)

        management_container = QtWidgets.QWidget()

        management_box = QtWidgets.QHBoxLayout(management_container)
        management_box.setAlignment(QtCore.Qt.AlignRight)
        management_box.setSpacing(5)

        management_box.addWidget(combo_box_builder.set_values(["File strategy"]).build())
        management_box.addWidget(push_button_builder.set_text("Upload").set_width(BUTTON_DEFAULT_WIDTH).build())
        management_box.addWidget(push_button_builder.set_text("Save").set_width(BUTTON_DEFAULT_WIDTH).build())

        return management_container

    def get_plain_section(self) -> QtWidgets.QWidget:
        text_edit_builder = (TextEditBuilder().set_height(TEXT_EDIT_DEFAULT_HEIGHT))
        combo_box_builder = (ComboBoxBuilder().set_width(COMBO_BOX_DEFAULT_WIDTH)
                                              .set_height(DIMENSION_UNIT_SIZE // 1.5))

        plain_container = QtWidgets.QWidget()
        plain_container.setMaximumWidth(MAIN_COMPONENT_DEFAULT_WIDTH)

        plain_box = QtWidgets.QVBoxLayout(plain_container)
        plain_box.addWidget(text_edit_builder.build())
        plain_box.addWidget(combo_box_builder.set_values(["Cipher Algorithm"]).build())

        return plain_container