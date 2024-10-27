"""
GUI гллавного экрана. На нем мы выбираем файлы для проверки и рисуем кнопки
Также тут описаны главные параметры экрана и действия нажатия кнопок.
"""

import tkinter as tk
from threading import Thread

from gui.settings_window import SettingsWindow
from settings.gui_settings import (
    TITLE, LABELS, BUTTONS_WIDTH,
    FRAME_BUTTONS_PADX, FRAME_BUTTONS_SIDE, BUTTONS_FRAME_PADY, BUTTON_TEXTS,
    FIRST_ELEMENT, MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT,
    AUTHOR_PADY, AUTHOR_LABEL_TEXT, AUTHOR_ANCHOR
)
from logic import get_xlsx
from .app_helper import AppHelper


class App:
    def __init__(self, root):
        self.root = root
        self.helper = AppHelper(root)
        self.settings = SettingsWindow(root)
        self.root.title(TITLE)
        self.root.geometry(f"{MAIN_WINDOW_WIDTH}x{MAIN_WINDOW_HEIGHT}")
        self.helper.center_window(
            self.root,
            MAIN_WINDOW_WIDTH,
            MAIN_WINDOW_HEIGHT
        )

        self.file_paths = []

        for label_text in LABELS:
            entry = self.helper.create_label_entry_frame(root, label_text)
            self.file_paths.append(entry)

        # Кнопки
        button_frame = tk.Frame(root)
        button_frame.pack(pady=BUTTONS_FRAME_PADY)

        for text, command_name in BUTTON_TEXTS.items():
            command = getattr(self, command_name)
            button = tk.Button(
                button_frame,
                text=text,
                command=command,
                width=BUTTONS_WIDTH
                )
            button.pack(side=FRAME_BUTTONS_SIDE, padx=FRAME_BUTTONS_PADX)

        label = tk.Label(root, text=AUTHOR_LABEL_TEXT)
        label.place(relx=0.5, rely=1.0, anchor=AUTHOR_ANCHOR, y=-AUTHOR_PADY)

    def start_process(self):
        """Запускает процесс обработки и отображает информационное окно."""
        self.helper.show_info_window()
        Thread(target=self.calculate_dates).start()

    def calculate_dates(self):
        """Запускает логику обработки процесса."""
        vmc_paths = self.file_paths[0].get()
        rc_paths = self.file_paths[1].get()
        st_paths = self.file_paths[2].get()
        cd_paths = self.file_paths[3].get()
        hb_paths = self.file_paths[4].get()

        # Вызываем функцию из get_xlsx с нашим словарем
        get_xlsx.handle_request(
            vmc_paths,
            hb_paths,
            rc_paths,
            st_paths,
            cd_paths
            )

        # Закрываем информационное окно по завершении работы
        if self.helper.info_window:
            self.helper.info_window.destroy()

    def clear_entries(self):
        """Очищает все текстовые поля."""
        for entry in self.file_paths:
            entry.delete(FIRST_ELEMENT, tk.END)

    def open_settings(self):
        """Открывает окно настроек."""
        self.settings.create_window()
