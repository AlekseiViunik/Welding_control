"""
GUI гллавного экрана. На нем мы выбираем файлы для проверки и рисуем кнопки
Также тут описаны главные параметры экрана и действия нажатия кнопок.
"""
import ctypes
import json
import logging
import os
import sys
import tkinter as tk
from threading import Thread
from tkinter import PhotoImage

from gui.settings_window import SettingsWindow
from logic.get_xlsx import GetXlsx
from settings import logging_settings as log
from settings import user_settings as us
from settings.gui.components import (
    buttons as btn,
    labels as lbl
)
from settings.gui.windows import windows as win
from gui.components.frames import Frame
from .app_helper import AppHelper


class App:
    def __init__(self, root, save_path):
        self.root = root
        self.save_path = save_path
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.helper = AppHelper(root)
        self.settings = SettingsWindow(root)
        self.root.title(win.START_WINDOW_TITLE)
        self.root.geometry(f"{win.WINDOW_WIDTH}x{win.WINDOW_HEIGHT}")
        self.set_window_icon()
        self.helper.center_window(
            self.root,
            win.WINDOW_WIDTH,
            win.WINDOW_HEIGHT
        )
        self.file_paths = []
        self.threads = []
        self.stop_threads = False

        buttons_args = {
            btn.GO_BUTTON_NAME: [],
            btn.CLEAN_BUTTON_NAME: [],
            btn.SETTINGS_BUTTON_NAME: []
        }

        frame = Frame(root, self)

        # Создание фреймов с полем для ввода и кнопкой "Обзор"
        for label_text in lbl.LABELS:
            entry = frame.create_entry_frame(label_text)
            self.file_paths.append(entry)

        # Кнопки "Погнали", "Забей" и "Настройки"
        frame.create_button_frame(
            btn.start_buttons_name_to_process,
            buttons_args
        )

        label = tk.Label(root, text=lbl.AUTHOR_LABEL_TEXT,)
        label.place(
            relx=lbl.AUTHOR_RELX,
            rely=lbl.AUTHOR_RELY,
            anchor=lbl.AUTHOR_ANCHOR,
            y=lbl.AUTHOR_PADY,
        )

    def start_process(self):
        """Запускает процесс обработки и отображает информационное окно."""
        logging.info(log.LOG_DIVIDER)
        logging.info(log.LOG_START)
        logging.info(
            f"Выбранные файлы: VMC: {self.file_paths[0].get()}, "
            f"RC: {self.file_paths[1].get()}, ST: {self.file_paths[2].get()},"
            f"CD: {self.file_paths[3].get()}, HB: {self.file_paths[4].get()}"
        )
        logging.info(f"Путь для сохранения итогового файла: {self.save_path}")
        self.helper.show_info_window()
        logging.info(log.LOG_CALCULATE_DATES_CALL)
        thread = Thread(target=self.calculate_dates)
        thread.daemon = True
        thread.start()
        self.threads.append(thread)

    def calculate_dates(self):
        """Запускает логику обработки процесса."""
        if self.stop_threads:
            return

        vmc_paths = self.file_paths[0].get()
        rc_paths = self.file_paths[1].get()
        st_paths = self.file_paths[2].get()
        cd_paths = self.file_paths[3].get()
        hb_paths = self.file_paths[4].get()

        self.get_save_path()

        # Вызываем функцию из get_xlsx с нашим словарем
        logging.info(log.LOG_HANDLE_REQUEST_CALL)
        get_xlsx = GetXlsx(
            vmc_paths,
            hb_paths,
            rc_paths,
            st_paths,
            cd_paths,
            self.save_path
        )
        if not get_xlsx.handle_request():
            logging.error(log.LOG_ERROR_MSG)
            self.on_closing()

        # Закрываем информационное окно по завершении работы
        if self.helper.info_window:
            self.helper.info_window.destroy()

    def get_save_path(self):
        with open(us.SETTINGS_FILE_NAME, 'r') as f:
            settings = json.load(f)
            self.save_path = settings[us.DEFAULT_SAVE_PATH_KEY]

    def clear_entries(self):
        """Очищает все текстовые поля."""
        for entry in self.file_paths:
            entry.delete(win.FIRST_ELEMENT, tk.END)

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
                win.ICONS_FOLDER_NAME,
                win.PNG_ICON_FILENAME
            )
            icon_path_ico = os.path.join(
                sys._MEIPASS,
                win.ICONS_FOLDER_NAME,
                win.ICO_ICON_FILENAME
            )
        else:
            # Если запущено из исходников
            icon_path_png = win.PNG_ICON_FILEPATH
            icon_path_ico = win.ICO_ICON_FILEPATH

        self.icon = PhotoImage(file=icon_path_png)
        self.root.iconphoto(True, self.icon)
        self.root.iconbitmap(icon_path_ico)

    def on_closing(self):
        """Обработчик закрытия окна."""
        self.stop_threads = True
        if self.helper.info_window:
            self.helper.info_window.destroy()
        self.root.quit()
