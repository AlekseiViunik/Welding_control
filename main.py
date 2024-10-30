"""
Главный файл. С него начинается работа программы. Он по сути делает только
одно: запускает главный экран приложения.
"""
from gui.start_window import App

import json
import os
import sys

from settings import user_settings as us

settings_file = us.SETTINGS_FILE_NAME

# Устанавливаем путь сохранения итогового файла по умолчанию
default_settings = {
    us.SAVE_PATH_KEY: us.DEFAULT_SAVE_PATH
}

if not os.path.exists(settings_file):
    with open(settings_file, 'w') as f:
        json.dump(default_settings, f)
else:
    # Если файл существует, проверяем значение DEFAULT_SAVE_PATH
    with open(settings_file, 'r') as f:
        settings = json.load(f)

    # Проверяем, пустое ли значение для ключа DEFAULT_SAVE_PATH
    if not settings.get(us.SAVE_PATH_KEY):
        settings[us.SAVE_PATH_KEY] = default_settings[us.SAVE_PATH_KEY]
        # Записываем обновленные настройки обратно в файл
        with open(settings_file, 'w') as f:
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

    root = tk.Tk()
    app = App(root)
    root.mainloop()
