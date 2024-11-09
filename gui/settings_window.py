import json
import tkinter as tk

from gui.app_helper import AppHelper
from gui.messagebox import MessageBox
from gui.components.frames import Frame
from settings import user_settings as us
from settings.gui.components import (
    buttons as btn,
    labels as lbl,
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
        save_path = settings[us.DEFAULT_SAVE_PATH_KEY]

        frame = Frame(settings_window, self)
        current_path = tk.StringVar(
            value=save_path
        )

        # Фрейм с лейблом, текстовым полем для ввода и кнопкой "Обзор"
        frame.create_entry_frame(lbl.WHERE_TO_SAVE, current_path, True)

        # Фрейм с кнопками "Сохранить" и "Отмена"
        buttons_args = {
            btn.SAVE_BUTTON_NAME: [current_path, settings_window],
            btn.CANCEL_BUTTON_NAME: [settings_window]
        }
        frame.create_button_frame(
            btn.settings_buttons_name_to_process,
            buttons_args
        )

    def save_settings(self, path, window):
        """Сохраняет настройки в JSON файл."""
        settings = self.load_settings(us.SETTINGS_FILE_NAME)
        settings[us.DEFAULT_SAVE_PATH_KEY] = path.get()

        with open(us.SETTINGS_FILE_NAME, 'w') as f:
            json.dump(settings, f, indent=us.JSON_INDENT)

        self.message_box.show_message(
            info.SUCCESS_TITLE,
            info.SAVED_SETTINGS_SUCCESS_MESSAGE,
        )
        window.destroy()

    def load_settings(self, settings_file):
        with open(settings_file, 'r') as f:
            return json.load(f)

    def destroy(self, instance):
        instance.destroy()
