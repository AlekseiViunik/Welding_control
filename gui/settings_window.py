import tkinter as tk

from gui.app_helper import AppHelper
from gui.messagebox import MessageBox
from gui.components.frames import Frame
from logic.settings_handler import SettingsHandler
from settings import settings as set


class SettingsWindow:
    def __init__(self, root, lang_code):
        self.root = root
        self.helper = AppHelper(root, lang_code)
        self.message_box = MessageBox()
        self.settings_handler = SettingsHandler()
        self.lang_code = lang_code

    def create_window(self):
        """Открывает окно настроек."""
        settings_window = tk.Toplevel(self.root)
        settings_window.title(set.settings_window_title[self.lang_code])
        settings_window.geometry(f"{set.WINDOW_WIDTH}x{set.WINDOW_HEIGHT}")
        settings = self.settings_handler.file_read()
        save_path = settings[set.DEFAULT_SAVE_PATH_KEY]

        frame = Frame(settings_window, self)
        current_path = tk.StringVar(
            value=save_path
        )

        # Фрейм с лейблом, текстовым полем для ввода и кнопкой "Обзор"
        frame.create_entry_frame(
            set.where_to_save[self.lang_code],
            current_path,
            True
        )

        # Фрейм с кнопками "Сохранить" и "Отмена"
        buttons_args = {
            set.save_button_name[self.lang_code]: [
                current_path, settings_window
            ],
            set.cancel_button_name[self.lang_code]: [
                settings_window
            ]
        }
        frame.create_button_frame(
            set.settings_buttons_name_to_process[self.lang_code],
            buttons_args
        )

    def save_settings(self, path, window):
        """Сохраняет настройки в JSON файл."""
        settings = self.settings_handler.file_read()
        settings[set.DEFAULT_SAVE_PATH_KEY] = path.get()

        self.settings_handler.file_write(settings)

        self.message_box.show_message(
            set.success_title[self.lang_code],
            set.saved_settings_success_message[self.lang_code],
        )
        window.destroy()

    def destroy(self, instance):
        instance.destroy()
