"""
Главный файл. С него начинается работа программы. Он по сути делает только
одно: запускает главный экран приложения.
"""
import json
import logging
import os
import sys

from gui.start_window import App
from logging_files.limited_size_file_handler import LimitedSizeFileHandler
from settings import user_settings as us, logging_settings as ls

# Настройка логирования
if not os.path.exists(ls.LOG_FOLDER):
    os.makedirs(ls.LOG_FOLDER)
if getattr(sys, 'frozen', False):
    log_file_path = os.path.join(
        os.path.dirname(sys.executable),
        ls.LOG_FOLDER,
        ls.LOG_FILENAME
    )
else:
    log_file_path = os.path.join(
        os.path.abspath(ls.LOG_FOLDER),
        ls.LOG_FILENAME
    )
handler = LimitedSizeFileHandler(log_file_path, encoding=ls.ENCODING)
formatter = logging.Formatter(ls.LOG_FORMAT)
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)

default_settings = {
    us.DEFAULT_SAVE_PATH_KEY: us.DEFAULT_SAVE_PATH,
    us.DEFAULT_LANG_KEY: {
        us.DEFAULT_LANG_CODE_KEY: us.DEFAULT_LANG_CODE,
        us.DEFAULT_LANG_ICON_PATH_KEY: us.DEFAULT_LANG_ICON_PATH
    }
}

if not os.path.exists(us.SETTINGS_FILE_NAME):
    with open(us.SETTINGS_FILE_NAME, 'w') as f:
        json.dump(default_settings, f)
else:
    with open(us.SETTINGS_FILE_NAME, 'r') as f:
        settings = json.load(f)

    if not settings.get(us.DEFAULT_SAVE_PATH_KEY):
        summary_file_path = (
            default_settings[us.DEFAULT_SAVE_PATH_KEY] +
            "/" +
            us.SAVE_FILE_NAME
        )
        settings[us.DEFAULT_SAVE_PATH_KEY] = summary_file_path
        with open(us.SETTINGS_FILE_NAME, 'w') as f:
            json.dump(settings, f, indent=us.JSON_INDENT)

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), us.LOGIC_PATH))
)
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), us.GUI_PATH))
)

if __name__ == "__main__":
    import tkinter as tk

    with open(us.SETTINGS_FILE_NAME, 'r') as f:
        settings = json.load(f)
        save_path = settings[us.DEFAULT_SAVE_PATH_KEY]
        lang_settings = settings[us.DEFAULT_LANG_KEY]
    root = tk.Tk()
    app = App(root, save_path)
    root.mainloop()
