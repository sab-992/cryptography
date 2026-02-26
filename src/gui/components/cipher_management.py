from pathlib import Path
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Slot
from src.cipher.detail.type import CipherDict
from src.gui.builder.label_builder import LabelBuilder
from src.gui.builder.push_button_builder import PushButtonBuilder
from src.gui.detail.component import Component
from src.gui.signals.cipher_management import CipherManagementSignalsSingleton
from src.gui.detail.settings import BUTTON_DEFAULT_HEIGHT, BUTTON_DEFAULT_WIDTH, DIMENSION_UNIT_SIZE, LABEL_DEFAULT_SIZE
from src.gui.detail.styles import get_button_hover_effect
from src.utils.file_strategy.file_strategy_factory import FileStrategyFactory
from src.utils.file_system import FileSystem
from src.utils.logger import Logger, Level_en


class CipherManagementComponent(Component):
    def __init__(self):
        self.cipher_management_signals_s: CipherManagementSignalsSingleton = CipherManagementSignalsSingleton()
        self.previous_save_path: str = FileSystem.get_root()
        self.previous_upload_path: str = FileSystem.get_root()

        super().__init__(row=0, col=2, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

    def connect_to_signals(self) -> None:
        self.cipher_management_signals_s.connect("payload_prepared", self.on_payload_prepared)

    def initialize_ui(self) -> None:
        SPACING = 10
        label_builder = (LabelBuilder().set_height(DIMENSION_UNIT_SIZE))
        push_button_builder = PushButtonBuilder().set_height(BUTTON_DEFAULT_HEIGHT)

        management_box = QtWidgets.QHBoxLayout(self)
        management_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        management_box.setSpacing(SPACING)

        management_box.addWidget(label_builder.set_text("Encrypted (Cipher): ").build())
        upload_btn: QtWidgets.QPushButton = (push_button_builder.set_text("Upload")
                                                                .set_width(BUTTON_DEFAULT_WIDTH)
                                                                .set_style(f"QPushButton {"{ border: none; background: #F44336; border-radius: 10px; padding: 8px; }"}{get_button_hover_effect("#F44336")}").build())
        upload_btn.clicked.connect(self.on_upload_btn_clicked)

        save_btn: QtWidgets.QPushButton = (push_button_builder.set_text("Save")
                                                              .set_width(BUTTON_DEFAULT_WIDTH)
                                                              .set_style(f"QPushButton {"{ border: none; background: #2196F3; border-radius: 10px; padding: 8px; }"}{get_button_hover_effect("#2196F3")}").build())
        save_btn.clicked.connect(self.on_save_btn_clicked)

        management_box.addWidget(upload_btn)
        management_box.addWidget(save_btn)

    @Slot(CipherDict)
    def on_payload_prepared(self, payload: CipherDict) -> None:
        file_path_info = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", self.previous_save_path, f"Files: (*{" *".join(FileStrategyFactory.supported())});;All Files (*)")

        if not file_path_info or self.path_is_empty(file_path_info[0]):
            return
        
        self.previous_save_path = str(Path(file_path_info[0]).parent.resolve())
        
        FileStrategyFactory.get(Path(file_path_info[0]).suffix).save(file_path_info[0], payload)

    @Slot()
    def on_save_btn_clicked(self) -> None:
        self.cipher_management_signals_s.emit("save_requested")

    @Slot()
    def on_upload_btn_clicked(self) -> None:
        file_path_info = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", self.previous_upload_path, f"Files: (*{" *".join(FileStrategyFactory.supported())})")

        if not file_path_info or self.path_is_empty(file_path_info[0]):
            return
        
        self.previous_upload_path = str(Path(file_path_info[0]).parent.resolve())
        
        file = FileStrategyFactory.get(Path(file_path_info[0]).suffix).read(file_path_info[0])
        if not file:
            Logger.log(message="File is ill-formed. Make sure it is written correctly", level=Level_en.WARNING, to_std_out=True)
        elif len(file) <= 0:
            Logger.log(message="File is empty", level=Level_en.WARNING, to_std_out=True)
        else:
            self.cipher_management_signals_s.emit("cipher_text_overwrite_requested", file)

    def path_is_empty(self, path: str):
        return not path or len(path) <= 0