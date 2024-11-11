"""
Главный файл. С него начинается работа программы. Он по сути делает только
одно: запускает главный экран приложения.
"""
import logging
import os
import sys

from gui.start_window import App
from logging_files.limited_size_file_handler import LimitedSizeFileHandler
from logic.settings_handler import SettingsHandler
from settings import settings as set

# Настройка логирования
if not os.path.exists(set.LOG_FOLDER):
    os.makedirs(set.LOG_FOLDER)
if getattr(sys, 'frozen', False):
    log_file_path = os.path.join(
        os.path.dirname(sys.executable),
        set.LOG_FOLDER,
        set.LOG_FILENAME
    )
else:
    log_file_path = os.path.join(
        os.path.abspath(set.LOG_FOLDER),
        set.LOG_FILENAME
    )
handler = LimitedSizeFileHandler(log_file_path, encoding=set.ENCODING)
formatter = logging.Formatter(set.LOG_FORMAT)
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)

settings_handler = SettingsHandler()
default_settings = {
    set.DEFAULT_SAVE_PATH_KEY: set.DEFAULT_SAVE_PATH,
    set.DEFAULT_LANG_KEY: {
        set.DEFAULT_LANG_CODE_KEY: set.RU_CODE,
        set.DEFAULT_LANG_ICON_PATH_KEY: set.RU_ICON_PATH
    }
}

# TODO create file handler to open files and get data
if not os.path.exists(set.SETTINGS_FILE_NAME):
    settings_handler.file_write(default_settings)
else:
    settings = settings_handler.file_read()

    if not settings.get(set.DEFAULT_SAVE_PATH_KEY):
        settings[set.DEFAULT_SAVE_PATH_KEY] = (
            default_settings[set.DEFAULT_SAVE_PATH_KEY]
        )
        settings_handler.file_write(settings)

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), set.LOGIC_PATH))
)
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), set.GUI_PATH))
)

if __name__ == "__main__":
    import tkinter as tk

    settings = settings_handler.file_read()
    save_path = settings[set.DEFAULT_SAVE_PATH_KEY]
    lang_settings = settings[set.DEFAULT_LANG_KEY]
    root = tk.Tk()
    app = App(root, save_path, lang_settings)
    root.mainloop()
