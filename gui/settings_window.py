import json
import tkinter as tk

from gui.app_helper import AppHelper
from gui.messagebox import show_message
from settings import gui_settings as gs
from settings import user_settings as us


class SettingsWindow:
    def __init__(self, root):
        self.root = root
        self.helper = AppHelper(root)

    def create_window(self):
        """Открывает окно настроек."""
        settings_window = tk.Toplevel(self.root)
        settings_window.title(gs.SETTINGS_WINDOW_TITLE)
        settings_window.geometry(f"{gs.WINDOW_WIDTH}x{gs.WINDOW_HEIGHT}")
        settings = self.load_settings(us.SETTINGS_FILE_NAME)
        save_path = settings[us.SAVE_PATH_KEY]
        # Текстовое поле с текущим путем сохранения
        # Устанавливаем текущее значение по умолчанию
        current_path = tk.StringVar(
            value=save_path
        )
        self.helper.create_label_entry_frame(
            settings_window,
            gs.WHERE_TO_SAVE,
            current_path,
            True
        )

        # Кнопки Сохранить и Отмена
        button_frame = tk.Frame(settings_window)
        button_frame.pack(pady=gs.SETTINGS_BUTTONS_FRAME_PADY)

        # Кнопка Сохранить
        save_button = tk.Button(
            button_frame,
            text=gs.SAVE_BUTTON_NAME,
            command=lambda: self.save_settings(
                current_path.get(),
                settings_window
            )
        )
        save_button.pack(
            side=gs.SETTINGS_BUTTONS_PACK_SIDE,
            padx=gs.SETTINGS_BUTTONS_PADX
        )

        # Кнопка Отмена
        cancel_button = tk.Button(
            button_frame,
            text=gs.CANCEL_BUTTON_NAME,
            command=settings_window.destroy
        )
        cancel_button.pack(
            side=gs.SETTINGS_BUTTONS_PACK_SIDE,
            padx=gs.SETTINGS_BUTTONS_PADX
        )

    def save_settings(self, path, window):
        """Сохраняет настройки в JSON файл."""
        settings = self.load_settings(us.SETTINGS_FILE_NAME)
        settings[us.SAVE_PATH_KEY] = path

        with open(us.SETTINGS_FILE_NAME, 'w') as f:
            json.dump(settings, f, indent=us.JSON_INDENT)

        show_message(
            gs.SUCCESS_TITLE,
            gs.SAVED_SETTINGS_SUCCESS_MESSAGE,
        )
        window.destroy()  # Закрываем окно настроек после сохранения

    def load_settings(self, settings_file):
        with open(settings_file, 'r') as f:
            return json.load(f)
