"""
GUI гллавного экрана. На нем мы выбираем файлы для проверки и рисуем кнопки
Также тут описаны главные параметры экрана и действия нажатия кнопок.
"""
import ctypes
import logging
import os
import sys
import tkinter as tk
from threading import Thread
from tkinter import PhotoImage

from gui.settings_window import SettingsWindow
from gui.components.frames import Frame
from gui.components.buttons import LangButton
from logic.get_xlsx import GetXlsx
from logic.settings_handler import SettingsHandler
from settings import settings as set

from .app_helper import AppHelper


class App:
    def __init__(self, root, save_path, lang_settings):
        self.root = root
        self.save_path = save_path
        self.lang_settings = lang_settings
        self.lang_code = lang_settings[set.DEFAULT_LANG_CODE_KEY]
        self.helper = AppHelper(root, self.lang_code)
        self.settings = SettingsWindow(root, self.lang_code)
        self.lang_button = LangButton(root, self.lang_settings)
        self.settings_handler = SettingsHandler()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title(set.START_WINDOW_TITLE)
        self.root.geometry(f"{set.WINDOW_WIDTH}x{set.WINDOW_HEIGHT}")
        self.set_window_icon()
        self.helper.center_window(
            self.root,
            set.WINDOW_WIDTH,
            set.WINDOW_HEIGHT
        )
        self.file_paths = []
        self.threads = []
        self.stop_threads = False

        buttons_args = {
            set.go_button_name[self.lang_code]: [],
            set.clean_button_name[self.lang_code]: [],
            set.settings_button_name[self.lang_code]: []
        }

        frame = Frame(root, self)

        # Создание фреймов с полем для ввода и кнопкой "Обзор"
        for label_text in set.labels[self.lang_code]:
            entry = frame.create_entry_frame(label_text)
            self.file_paths.append(entry)

        # Кнопки "Погнали", "Забей" и "Настройки"
        frame.create_button_frame(
            set.start_buttons_name_to_process[self.lang_code],
            buttons_args
        )

        label = tk.Label(root, text=set.AUTHOR_LABEL_TEXT,)
        label.place(
            relx=set.AUTHOR_RELX,
            rely=set.AUTHOR_RELY,
            anchor=set.AUTHOR_ANCHOR,
            y=set.AUTHOR_PADY,
        )

        # Кнопка смены языка
        self.lang_button.create_lang_button()

    def start_process(self):
        """Запускает процесс обработки и отображает информационное окно."""
        logging.info(set.LOG_DIVIDER)
        logging.info(set.log_start[self.lang_code])
        logging.info(
            f"Выбранные файлы: VMC: {self.file_paths[0].get()}, "
            f"RC: {self.file_paths[1].get()}, ST: {self.file_paths[2].get()},"
            f"CD: {self.file_paths[3].get()}, HB: {self.file_paths[4].get()}"
        )
        logging.info(f"{set.log_save_path_is[self.lang_code]}{self.save_path}")
        self.helper.show_info_window()
        logging.info(set.log_calculate_dates_call[self.lang_code])
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

        self.save_path = self.settings_handler.file_read(
            set.DEFAULT_SAVE_PATH_KEY
        )

        # Вызываем функцию из get_xlsx с нашим словарем
        logging.info(set.log_handle_request_call[self.lang_code])
        get_xlsx = GetXlsx(
            vmc_paths,
            hb_paths,
            rc_paths,
            st_paths,
            cd_paths,
            self.save_path,
            self.lang_code
        )
        if not get_xlsx.handle_request():
            logging.error(set.log_error_msg[self.lang_code])
            self.on_closing()

        # Закрываем информационное окно по завершении работы
        if self.helper.info_window:
            self.helper.info_window.destroy()

    def clear_entries(self):
        """Очищает все текстовые поля."""
        for entry in self.file_paths:
            entry.delete(set.FIRST_ELEMENT, tk.END)

    def open_settings(self):
        """Открывает окно настроек."""
        self.settings.create_window()
        self.save_path = self.settings_handler.file_read(
            set.DEFAULT_SAVE_PATH_KEY
        )

    def set_window_icon(self):
        """Устанавливает иконку для окна."""
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            'Weld Control'
        )

        if getattr(sys, 'frozen', False):
            # Если запущено как исполняемое приложение
            icon_path_png = os.path.join(
                sys._MEIPASS,
                set.ICONS_FOLDER_NAME,
                set.PNG_ICON_FILENAME
            )
            icon_path_ico = os.path.join(
                sys._MEIPASS,
                set.ICONS_FOLDER_NAME,
                set.ICO_ICON_FILENAME
            )
        else:
            # Если запущено из исходников
            icon_path_png = set.PNG_ICON_FILEPATH
            icon_path_ico = set.ICO_ICON_FILEPATH

        self.icon = PhotoImage(file=icon_path_png)
        self.root.iconphoto(True, self.icon)
        self.root.iconbitmap(icon_path_ico)

    def on_closing(self):
        """Обработчик закрытия окна."""
        self.stop_threads = True
        if self.helper.info_window:
            self.helper.info_window.destroy()
        self.root.quit()
