import os
import tkinter as tk

from gui.app_helper import AppHelper
from settings import user_settings, gui_settings as gs


class SettingsWindow:
    def __init__(self, root):
        self.root = root
        self.helper = AppHelper(root)

    def create_window(self):
        """Открывает окно настроек."""
        settings_window = tk.Toplevel(self.root)
        settings_window.title(gs.SETTINGS_WINDOW_TITLE)
        settings_window.geometry(f"{gs.WINDOW_WIDTH}x{gs.WINDOW_HEIGHT}")

        # Текстовое поле с текущим путем сохранения
        # Устанавливаем текущее значение по умолчанию
        current_path = tk.StringVar(
            value=os.path.dirname(user_settings.DEFAULT_SAVE_PATH)
        )
        self.helper.create_label_entry_frame(
            settings_window,
            gs.WHERE_TO_SAVE,
            current_path
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
