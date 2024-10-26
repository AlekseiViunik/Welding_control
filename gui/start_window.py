"""
GUI гллавного экрана. На нем мы выбираем файлы для проверки и рисуем кнопки
Также тут описаны главные параметры экрана и действия нажатия кнопок.
"""

import tkinter as tk
from tkinter import filedialog

from default_settings.gui_settings import (
    TITLE, GEOMETRY, LABELS, LABEL_PADX, LABEL_ANCHOR, FRAME_FILL_AXIS,
    FRAME_PADX, ENTRY_WIDTH, ENTRY_EXPAND, ENTRY_FILL_AXIS, ENTRY_FRAME_SIDE,
    FRAME_BUTTON_TEXT, FRAME_BUTTON_LEFT_PADX, FRAME_BUTTON_RIGHT_PADX,
    FRAME_BUTTON_SIDE, DIVIDER_HEIGHT, DIVIDER_FILL_AXIS, BUTTONS_WIDTH,
    FRAME_BUTTONS_PADX, FRAME_BUTTONS_SIDE, BUTTONS_FRAME_PADY, BUTTON_TEXTS,
    FIRST_ELEMENT, PATH_DIVIDER
    )
from logic import get_xlsx

class App:
    def __init__(self, root):
        self.root = root
        self.root.title(TITLE)
        self.root.geometry(GEOMETRY)

        self.file_paths = []

        for label_text in LABELS:
            
            # Текст-подсказка для текстового поля
            label = tk.Label(root, text=label_text)
            label.pack(anchor=LABEL_ANCHOR, padx=LABEL_PADX)

            # Фрейм с текстовым полем для ввода и кнопкой
            frame = tk.Frame(root)
            frame.pack(fill=FRAME_FILL_AXIS, padx=FRAME_PADX)

            # Текстовое поле фрейма
            entry = tk.Entry(frame, width=ENTRY_WIDTH)
            entry.pack(
                side=ENTRY_FRAME_SIDE,
                fill=ENTRY_FILL_AXIS,
                expand=ENTRY_EXPAND
                )

            # Кнопка фрейма
            button = tk.Button(
                frame,
                text=FRAME_BUTTON_TEXT,
                command=lambda e=entry: self.browse_file(e)
                )
            button.pack(
                side=FRAME_BUTTON_SIDE,
                padx=(FRAME_BUTTON_LEFT_PADX, FRAME_BUTTON_RIGHT_PADX)
                )

            self.file_paths.append(entry)

            # Разделительная строка
            tk.Frame(root, height=DIVIDER_HEIGHT).pack(fill=DIVIDER_FILL_AXIS)

        # Кнопки
        button_frame = tk.Frame(root)
        button_frame.pack(pady=BUTTONS_FRAME_PADY)

        for text in BUTTON_TEXTS.keys():
            command = getattr(self, BUTTON_TEXTS[text])
            button = tk.Button(
                button_frame,
                text=text,
                command=command,
                width=BUTTONS_WIDTH
                )
            button.pack(side=FRAME_BUTTONS_SIDE, padx=FRAME_BUTTONS_PADX)

    def browse_file(self, entry):
        """Открывает диалог выбора файлов."""
        file_paths = filedialog.askopenfilenames()  # Позволяем выбирать несколько файлов
        if file_paths:
            entry.delete(FIRST_ELEMENT, tk.END)  # Очищаем текущее значение
            entry.insert(FIRST_ELEMENT, PATH_DIVIDER.join(file_paths))  # Вставляем выбранные пути через точку с запятой

    def start_process(self):
        """Запускает процесс обработки."""
        vmc_paths = self.file_paths[0].get()  # Путь из первого текстового поля
        rc_paths = self.file_paths[1].get()   # Путь из второго текстового поля
        st_paths = self.file_paths[2].get()   # Путь из третьего текстового поля
        cd_paths = self.file_paths[3].get()   # Путь из четвертого текстового поля
        hb_paths = self.file_paths[4].get()  # Путь из пятого текстового поля, если несколько

        # Вызываем функцию из get_xlsx с нашим словарем
        get_xlsx.handle_request(vmc_paths, hb_paths, rc_paths, st_paths, cd_paths)  # Преобразуем строки в списки

        print("Запуск обработки...")

    def clear_entries(self):
        """Очищает все текстовые поля."""
        for entry in self.file_paths:
            entry.delete(FIRST_ELEMENT, tk.END)
    
    def open_settings(self):
        """Открывает окно настроек."""
        # TODO реализовать метод
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()