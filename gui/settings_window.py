import os
import tkinter as tk

from gui.app_helper import AppHelper
from settings import user_settings


class SettingsWindow:
    def __init__(self, root):
        self.root = root
        self.helper = AppHelper(root)

    def create_window(self):
        """Открывает окно настроек."""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Настройки")
        settings_window.geometry("600x400")

        # Текстовое поле с текущим путем сохранения
        # Устанавливаем текущее значение по умолчанию
        current_path = tk.StringVar(
            value=os.path.dirname(user_settings.DEFAULT_SAVE_PATH)
        )
        self.helper.create_label_entry_frame(
            settings_window,
            'Куда сохранять итоговый файл?',
            current_path
        )

        # Кнопки Сохранить и Отмена
        button_frame = tk.Frame(settings_window)
        button_frame.pack(pady=20)

        save_button = tk.Button(
            button_frame,
            text="Сохранить",
            command=lambda: self.save_settings(
                current_path.get(),
                settings_window
            )
        )
        save_button.pack(side='left', padx=5)

        cancel_button = tk.Button(
            button_frame,
            text="Отмена",
            command=settings_window.destroy
        )
        cancel_button.pack(side='left', padx=5)
