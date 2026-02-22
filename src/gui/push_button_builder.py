import os
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton
from src.gui.detail.widget_builder import WidgetBuilder
from src.utils.settings import ASSETS_FOLDER_PATH
from typing import Self


class PushButtonBuilder(WidgetBuilder):
    def __init__(self):
        super().__init__(QPushButton)
        self.__image_path: str = None
        self.__image_size: QSize = None
        self.__text: str = None

    def initialize_instance(self) -> QPushButton:
        push_button = QPushButton()

        has_text: bool = self.__text and len(self.__text) > 0
        has_image_path: bool = self.__image_path and len(self.__image_path) > 0

        if has_text and has_image_path:
            self.error("Cannot have text and icon at the same time")

        if has_image_path:
            if not self.__image_size:
                self.error("No size given for the icon")

            if not os.path.exists(self.__image_path):
                self.error(f"Icon at: {self.__image_path} does not exist")

            push_button.setIcon(QIcon(self.__image_path))
            push_button.setIconSize(self.__image_size)

        if has_text:
            push_button.setText(self.__text)

        if not has_text and not has_image_path:
            self.error("No text or icon given")

        return push_button
    
    def set_text(self, text: str) -> Self:
        self.__text = text
        return self

    def set_image(self, path: str) -> Self:
        """
        path: Image's path relative to asset/. 
        """
        self.__image_path = f"{ASSETS_FOLDER_PATH}/{path}"
        return self
    
    def set_image_size(self, w: int, h: int) -> Self:
        self.__image_size = QSize(w, h)
        return self