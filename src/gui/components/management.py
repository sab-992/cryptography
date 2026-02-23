from PySide6 import QtCore, QtWidgets
from src.gui.builder.combo_box_builder import ComboBoxBuilder
from src.gui.builder.push_button_builder import PushButtonBuilder
from src.gui.detail.component import Component
from src.gui.detail.settings import BUTTON_DEFAULT_HEIGHT, BUTTON_DEFAULT_WIDTH, COMBO_BOX_DEFAULT_WIDTH, DIMENSION_UNIT_SIZE
from src.gui.detail.styles import get_button_hover_effect
from src.utils.file_strategy.file_strategy_factory import FileStrategy_en


class ManagementComponent(Component):
    def __init__(self):
        super().__init__(row=1, col=2, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        self.initialize_ui()

    def initialize_ui(self) -> None:
        SPACING = 10

        combo_box_builder = (ComboBoxBuilder().set_width(COMBO_BOX_DEFAULT_WIDTH)
                                              .set_height(DIMENSION_UNIT_SIZE // 1.5))
        push_button_builder = PushButtonBuilder().set_height(BUTTON_DEFAULT_HEIGHT)

        management_box = QtWidgets.QHBoxLayout(self)
        management_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        management_box.setSpacing(SPACING)
        management_box.addWidget(combo_box_builder.set_values(self.get_file_strategies()).build())
        management_box.addWidget(push_button_builder.set_text("Upload").set_width(BUTTON_DEFAULT_WIDTH).set_style(f"QPushButton {"{ border: none; background: #F44336; border-radius: 10px; padding: 8px; }"}{get_button_hover_effect("#F44336")}").build())
        management_box.addWidget(push_button_builder.set_text("Save").set_width(BUTTON_DEFAULT_WIDTH).set_style(f"QPushButton {"{ border: none; background: #2196F3; border-radius: 10px; padding: 8px; }"}{get_button_hover_effect("#2196F3")}").build())

    def get_file_strategies(self) -> list[str]:
        return [strategy.value.name for strategy in FileStrategy_en]          