"""
GUI гллавного экрана. На нем мы выбираем файлы для проверки и рисуем кнопки
Также тут описаны главные параметры экрана и действия нажатия кнопок.
"""
import ctypes
import tkinter as tk
from tkinter import PhotoImage
from threading import Thread

from gui.settings_window import SettingsWindow
import settings.gui_settings as gs
from logic import get_xlsx
from .app_helper import AppHelper


class App:
    def __init__(self, root):
        self.root = root
        self.helper = AppHelper(root)
        self.settings = SettingsWindow(root)
        self.root.title(gs.MAIN_WINDOW_TITLE)
        self.root.geometry(f"{gs.WINDOW_WIDTH}x{gs.WINDOW_HEIGHT}")
        self.set_window_icon()
        self.helper.center_window(
            self.root,
            gs.WINDOW_WIDTH,
            gs.WINDOW_HEIGHT
        )

        self.file_paths = []

        for label_text in gs.LABELS:
            entry = self.helper.create_label_entry_frame(root, label_text)
            self.file_paths.append(entry)

        # Кнопки
        button_frame = tk.Frame(root)
        button_frame.pack(pady=gs.BUTTONS_FRAME_PADY)

        for text, command_name in gs.BUTTON_TEXTS.items():
            command = getattr(self, command_name)
            button = tk.Button(
                button_frame,
                text=text,
                command=command,
                width=gs.BUTTONS_WIDTH
                )
            button.pack(side=gs.FRAME_BUTTONS_SIDE, padx=gs.FRAME_BUTTONS_PADX)

        label = tk.Label(root, text=gs.AUTHOR_LABEL_TEXT)
        label.place(
            relx=gs.AUTHOR_RELX,
            rely=gs.AUTHOR_RELY,
            anchor=gs.AUTHOR_ANCHOR,
            y=-gs.AUTHOR_PADY
        )

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
            entry.delete(gs.FIRST_ELEMENT, tk.END)

    def open_settings(self):
        """Открывает окно настроек."""
        self.settings.create_window()

    def set_window_icon(self):
        # Загружаем иконку для окна
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            'Dates control'
        )

        self.icon = PhotoImage(file="icons/mark32x32.png")
        self.root.iconphoto(True, self.icon)
        self.root.iconbitmap("icons/mark32x32.ico")
