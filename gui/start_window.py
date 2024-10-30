"""
GUI гллавного экрана. На нем мы выбираем файлы для проверки и рисуем кнопки
Также тут описаны главные параметры экрана и действия нажатия кнопок.
"""
import os
import sys
import ctypes
import json
import tkinter as tk
from tkinter import PhotoImage
from threading import Thread

from gui.settings_window import SettingsWindow
from settings import gui_settings as gs, user_settings as us
from logic import get_xlsx
from .app_helper import AppHelper


class App:
    def __init__(self, root, save_path):
        self.root = root
        self.save_path = save_path
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

        self.get_save_path()
        # Вызываем функцию из get_xlsx с нашим словарем
        get_xlsx.handle_request(
            vmc_paths,
            hb_paths,
            rc_paths,
            st_paths,
            cd_paths,
            self.save_path
            )

        # Закрываем информационное окно по завершении работы
        if self.helper.info_window:
            self.helper.info_window.destroy()

    def get_save_path(self):
        with open(us.SETTINGS_FILE_NAME, 'r') as f:
            settings = json.load(f)
            self.save_path = settings[us.SAVE_PATH_KEY]

    def clear_entries(self):
        """Очищает все текстовые поля."""
        for entry in self.file_paths:
            entry.delete(gs.FIRST_ELEMENT, tk.END)

    def open_settings(self):
        """Открывает окно настроек."""
        self.settings.create_window()
        self.get_save_path()

    def set_window_icon(self):
        """Устанавливает иконку для окна."""
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            'Weld Control'
        )

        if getattr(sys, 'frozen', False):
            # Если запущено как исполняемое приложение
            icon_path_png = os.path.join(
                sys._MEIPASS,
                "icons",
                "mark32x32.png"
            )
            icon_path_ico = os.path.join(
                sys._MEIPASS,
                "icons",
                "mark32x32.ico"
            )
        else:
            # Если запущено из исходников
            icon_path_png = "icons/mark32x32.png"
            icon_path_ico = "icons/mark32x32.ico"

        self.icon = PhotoImage(file=icon_path_png)
        self.root.iconphoto(True, self.icon)
        self.root.iconbitmap(icon_path_ico)
