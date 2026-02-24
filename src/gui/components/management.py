from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Slot
from src.cipher.detail.type import CipherDict
from src.gui.builder.combo_box_builder import ComboBoxBuilder
from src.gui.builder.push_button_builder import PushButtonBuilder
from src.gui.detail.component import Component
from src.gui.signals.management import ManagementSignalsSingleton
from src.gui.detail.settings import BUTTON_DEFAULT_HEIGHT, BUTTON_DEFAULT_WIDTH, COMBO_BOX_DEFAULT_WIDTH, DIMENSION_UNIT_SIZE
from src.gui.detail.styles import get_button_hover_effect
from src.utils.file_strategy.file_strategy_factory import FileStrategy, FileStrategy_en, FileStrategyFactory
from src.utils.logger import Logger, Level_en


class ManagementComponent(Component):
    def __init__(self):
        self.management_signals_s: ManagementSignalsSingleton = ManagementSignalsSingleton()
        self.file_strategy_combo_box = None
        self.current_file_strategy: FileStrategy = None

        super().__init__(row=1, col=2, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

    def connect_to_signals(self) -> None:
        self.management_signals_s.connect("payload_prepared", self.on_payload_prepared)

    def get_file_strategies(self) -> list[str]:
        return [strategy.value.name for strategy in FileStrategy_en]

    def initialize_ui(self) -> None:
        SPACING = 10

        combo_box_builder = (ComboBoxBuilder().set_width(COMBO_BOX_DEFAULT_WIDTH)
                                              .set_height(DIMENSION_UNIT_SIZE // 1.5))
        push_button_builder = PushButtonBuilder().set_height(BUTTON_DEFAULT_HEIGHT)

        management_box = QtWidgets.QHBoxLayout(self)
        management_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        management_box.setSpacing(SPACING)

        self.file_strategy_combo_box: QtWidgets.QComboBox = combo_box_builder.set_values(self.get_file_strategies()).build()
        self.current_file_strategy = FileStrategyFactory.get(self.file_strategy_combo_box.currentText())
        self.file_strategy_combo_box.currentIndexChanged.connect(self.on_file_strategy_changed)
        management_box.addWidget(self.file_strategy_combo_box)

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

    @Slot(int)
    def on_file_strategy_changed(self, index: int) -> None:
        if not self.file_strategy_combo_box:
            raise Exception(Logger.log(message=f"File strategy combo box is not defined", level=Level_en.ERROR))

        self.current_file_strategy = FileStrategyFactory.get(self.file_strategy_combo_box.itemText(index))

    @Slot(CipherDict)
    def on_payload_prepared(self, payload: CipherDict) -> None:
        # TODO: Allow file browsing to get file path
        file_path: str = ""
        # self.current_file_strategy.save(file_path, payload)
        print("Payload to save received !")

    @Slot()
    def on_save_btn_clicked(self) -> None:
        self.management_signals_s.emit("save_requested")

    @Slot()
    def on_upload_btn_clicked(self) -> None:
        # TODO: Allow file browsing to get file path
        file_path = ""
        # self.management_signals_s.emit("text_overwrite_requested", self.current_file_strategy.read(file_path))
        print("Read payload to send !")