import json
import tkinter as tk

from gui.app_helper import AppHelper
from gui.messagebox import MessageBox
from settings import user_settings as us
from settings.gui.components import (
    buttons as btn,
    labels as lbl,
    frames as fr
)
from settings.gui.windows import (
    windows as win,
    info_windows as info
)


class SettingsWindow:
    def __init__(self, root):
        self.root = root
        self.helper = AppHelper(root)
        self.message_box = MessageBox()

    def create_window(self):
        """Открывает окно настроек."""
        settings_window = tk.Toplevel(self.root)
        settings_window.title(win.SETTINGS_WINDOW_TITLE)
        settings_window.geometry(f"{win.WINDOW_WIDTH}x{win.WINDOW_HEIGHT}")
        settings = self.load_settings(us.SETTINGS_FILE_NAME)
        save_path = settings[us.SAVE_PATH_KEY]
        # Текстовое поле с текущим путем сохранения
        # Устанавливаем текущее значение по умолчанию
        current_path = tk.StringVar(
            value=save_path
        )
        self.helper.create_label_entry_frame(
            settings_window,
            lbl.WHERE_TO_SAVE,
            current_path,
            True
        )

        # Кнопки Сохранить и Отмена
        button_frame = tk.Frame(settings_window)
        button_frame.pack(pady=fr.SETTINGS_BUTTONS_FRAME_PADY)

        # Кнопка Сохранить
        save_button = tk.Button(
            button_frame,
            text=btn.SAVE_BUTTON_NAME,
            command=lambda: self.save_settings(
                current_path.get(),
                settings_window
            )
        )
        save_button.pack(
            side=btn.SETTINGS_BUTTONS_PACK_SIDE,
            padx=btn.SETTINGS_BUTTONS_PADX
        )

        # Кнопка Отмена
        cancel_button = tk.Button(
            button_frame,
            text=btn.CANCEL_BUTTON_NAME,
            command=settings_window.destroy
        )
        cancel_button.pack(
            side=btn.SETTINGS_BUTTONS_PACK_SIDE,
            padx=btn.SETTINGS_BUTTONS_PADX
        )

    def save_settings(self, path, window):
        """Сохраняет настройки в JSON файл."""
        settings = self.load_settings(us.SETTINGS_FILE_NAME)
        settings[us.SAVE_PATH_KEY] = path

        with open(us.SETTINGS_FILE_NAME, 'w') as f:
            json.dump(settings, f, indent=us.JSON_INDENT)

        self.message_box.show_message(
            info.SUCCESS_TITLE,
            info.SAVED_SETTINGS_SUCCESS_MESSAGE,
        )
        window.destroy()  # Закрываем окно настроек после сохранения

    def load_settings(self, settings_file):
        with open(settings_file, 'r') as f:
            return json.load(f)
