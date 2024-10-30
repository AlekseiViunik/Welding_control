"""
Главный файл. С него начинается работа программы. Он по сути делает только
одно: запускает главный экран приложения.
"""
from gui.start_window import App

import json
import os
import sys

from settings import user_settings as us


# Устанавливаем путь сохранения итогового файла по умолчанию
default_settings = {
    us.SAVE_PATH_KEY: us.DEFAULT_SAVE_PATH
}

if not os.path.exists(us.SETTINGS_FILE_NAME):
    with open(us.SETTINGS_FILE_NAME, 'w') as f:
        json.dump(default_settings, f)
else:
    # Если файл существует, проверяем значение DEFAULT_SAVE_PATH
    with open(us.SETTINGS_FILE_NAME, 'r') as f:
        settings = json.load(f)

    # Проверяем, пустое ли значение для ключа DEFAULT_SAVE_PATH
    if not settings.get(us.SAVE_PATH_KEY):
        summary_file_path = (
            default_settings[us.SAVE_PATH_KEY] +
            "/" +
            us.SAVE_FILE_NAME
        )
        settings[us.SAVE_PATH_KEY] = summary_file_path
        # Записываем обновленные настройки обратно в файл
        with open(us.SETTINGS_FILE_NAME, 'w') as f:
            json.dump(settings, f, indent=us.JSON_INDENT)

# Добавляем пути к папкам logic и gui
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
