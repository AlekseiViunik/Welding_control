"""
Главный файл. С него начинается работа программы. Он по сути делает только
одно: запускает главный экран приложения.
"""
import json
import logging
import os
import sys

from gui.start_window import App
from settings import user_settings as us
from logging_files.limited_size_file_handler import LimitedSizeFileHandler

# Настройка логирования
log_file_path = 'logging_files/app.log'
handler = LimitedSizeFileHandler(log_file_path, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

default_settings = {
    us.SAVE_PATH_KEY: us.DEFAULT_SAVE_PATH
}

if not os.path.exists(us.SETTINGS_FILE_NAME):
    with open(us.SETTINGS_FILE_NAME, 'w') as f:
        json.dump(default_settings, f)
else:
    with open(us.SETTINGS_FILE_NAME, 'r') as f:
        settings = json.load(f)

    if not settings.get(us.SAVE_PATH_KEY):
        summary_file_path = (
            default_settings[us.SAVE_PATH_KEY] +
            "/" +
            us.SAVE_FILE_NAME
        )
        settings[us.SAVE_PATH_KEY] = summary_file_path
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
        save_path = settings[us.SAVE_PATH_KEY]
    root = tk.Tk()
    app = App(root, save_path)
    root.mainloop()
