import json
import tkinter as tk

from gui.app_helper import AppHelper
from gui.messagebox import MessageBox
# from gui.buttons import Buttons
from settings import user_settings as us
from settings.gui.windows import (
    message_box as mb,
    settings_window as set
)


class SettingsWindow:
    def __init__(self, root):
        self.root = root
        self.helper = AppHelper(root)
        self.message_box = MessageBox()
        self.current_path = ''

    def create_window(self):
        """Открывает окно настроек."""
        settings_window = tk.Toplevel(self.root)
        settings_window.title(set.SETTINGS_WINDOW_TITLE)
        settings_window.geometry(
            f"{set.SETTINGS_WINDOW_WIDTH}x{set.SETTINGS_WINDOW_HEIGHT}"
        )
        settings = self.load_settings(us.SETTINGS_FILE_NAME)
        save_path = settings[us.SAVE_PATH_KEY]
        # Текстовое поле с текущим путем сохранения
        # Устанавливаем текущее значение по умолчанию
        self.current_path = tk.StringVar(
            value=save_path
        )
        self.helper.create_label_entry_frame(
            settings_window,
            set.WHERE_TO_SAVE,
            self.current_path,
            True
        )

        # Кнопки Сохранить и Отмена
        # buttons = Buttons(self.root, self, settings_window)
        # buttons.create_buttons_frame(set.SETTINGS_BUTTONS_NAME_TO_PROCESS)

        button_frame = tk.Frame(settings_window)
        button_frame.pack(pady=set.SETTINGS_BUTTONS_FRAME_PADY)

        # Кнопка Сохранить
        save_button = tk.Button(
            button_frame,
            text=set.SAVE_BUTTON_NAME,
            command=lambda: self.save_settings(
                self.current_path.get(),
                settings_window
            )
        )
        save_button.pack(
            side=set.SETTINGS_BUTTONS_PACK_SIDE,
            padx=set.SETTINGS_BUTTONS_PADX
        )

        # Кнопка Отмена
        cancel_button = tk.Button(
            button_frame,
            text=set.CANCEL_BUTTON_NAME,
            command=settings_window.destroy
        )
        cancel_button.pack(
            side=set.SETTINGS_BUTTONS_PACK_SIDE,
            padx=set.SETTINGS_BUTTONS_PADX
        )

    def save_settings(self, path, window):
        """Сохраняет настройки в JSON файл."""
        settings = self.load_settings(us.SETTINGS_FILE_NAME)
        settings[us.SAVE_PATH_KEY] = path

        with open(us.SETTINGS_FILE_NAME, 'w') as f:
            json.dump(settings, f, indent=us.JSON_INDENT)

        self.message_box.show_message(
            mb.SUCCESS_TITLE,
            mb.SAVED_SETTINGS_SUCCESS_MESSAGE,
        )
        window.destroy()  # Закрываем окно настроек после сохранения

    def load_settings(self, settings_file):
        with open(settings_file, 'r') as f:
            return json.load(f)

    def destroy(self, parent):
        parent.destroy()
