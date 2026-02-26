from pathlib import Path
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Slot
from src.gui.builder.label_builder import LabelBuilder
from src.gui.builder.push_button_builder import PushButtonBuilder
from src.gui.detail.component import Component
from src.gui.signals.plain_management import PlainManagementSignalsSingleton
from src.gui.detail.settings import BUTTON_DEFAULT_HEIGHT, BUTTON_DEFAULT_WIDTH, DIMENSION_UNIT_SIZE, LABEL_DEFAULT_SIZE
from src.gui.detail.styles import get_button_hover_effect
from src.utils.file_system import FileSystem
from src.utils.logger import Logger, Level_en


class PlainManagementComponent(Component):
    def __init__(self):
        self.plain_management_signals_s: PlainManagementSignalsSingleton = PlainManagementSignalsSingleton()
        self.previous_upload_path: str = FileSystem.get_root()

        super().__init__(row=0, col=0, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

    def connect_to_signals(self) -> None:
        pass

    def initialize_ui(self) -> None:
        SPACING = 10
        label_builder = (LabelBuilder().set_width(LABEL_DEFAULT_SIZE * 1.5)
                                       .set_height(DIMENSION_UNIT_SIZE))
        push_button_builder = PushButtonBuilder().set_height(BUTTON_DEFAULT_HEIGHT)

        management_box = QtWidgets.QHBoxLayout(self)
        management_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        management_box.setSpacing(SPACING)

        management_box.addWidget(label_builder.set_text("Decrypted (Plain): ").build())
        upload_btn: QtWidgets.QPushButton = (push_button_builder.set_text("Upload")
                                                                .set_width(BUTTON_DEFAULT_WIDTH)
                                                                .set_style(f"QPushButton {"{ border: none; background: #F44336; border-radius: 10px; padding: 8px; }"}{get_button_hover_effect("#F44336")}").build())
        upload_btn.clicked.connect(self.on_upload_btn_clicked)
        management_box.addWidget(upload_btn)

    @Slot()
    def on_upload_btn_clicked(self) -> None:
        file_path_info = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", self.previous_upload_path, f"All Files (*)")

        if not file_path_info or self.path_is_empty(file_path_info[0]):
            return
        
        self.previous_upload_path = str(Path(file_path_info[0]).parent.resolve())

        try:
            file = FileSystem.read(file_path_info[0])

            if len(file) <= 0:
                Logger.log(message="File is empty", level=Level_en.WARNING, to_std_out=True)

            self.plain_management_signals_s.emit("plain_text_overwrite_requested", file)
        except Exception as e:
            Logger.log(message=e, level=Level_en.WARNING, to_std_out=True)

    def path_is_empty(self, path: str):
        return not path or len(path) <= 0