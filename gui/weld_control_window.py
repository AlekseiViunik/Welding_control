"""
GUI гллавного экрана. На нем мы выбираем файлы для проверки и рисуем кнопки
Также тут описаны главные параметры экрана и действия нажатия кнопок.
"""
import json
import logging
import tkinter as tk

from gui.settings_window import SettingsWindow
from gui.app_helper import AppHelper
from logic.get_xlsx import GetXlsx
from settings import gui_settings as gs
from settings import logging_settings as log
from settings import user_settings as us


class WeldControlWindow:
    def __init__(self):
        self.root = tk.Tk()

        self.helper = AppHelper(self.root)
        self.settings = SettingsWindow(self.root)
        self.root.title(gs.WELD_CONTROL_WINDOW_TITLE)
        self.root.geometry(f"{gs.WINDOW_WIDTH}x{gs.WINDOW_HEIGHT}")
        self.helper.center_window(
            self.root,
            gs.WINDOW_WIDTH,
            gs.WINDOW_HEIGHT
        )
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.file_paths = []
        self.threads = []
        self.stop_threads = False
        self.save_path = self.get_save_path()

        for label_text in gs.LABELS:
            entry = self.helper.create_label_entry_frame(self.root, label_text)
            self.file_paths.append(entry)

        # Кнопки
        button_frame = tk.Frame(self.root)
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

            label = tk.Label(self.root, text=gs.AUTHOR_LABEL_TEXT)
            label.place(
                relx=gs.AUTHOR_RELX,
                rely=gs.AUTHOR_RELY,
                anchor=gs.AUTHOR_ANCHOR,
                y=-gs.AUTHOR_PADY
            )

    def start(self):
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
        self.root.after(0, self.calculate_dates)

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
            self.save_path = settings[us.SAVE_PATH_KEY]

    def clear_entries(self):
        """Очищает все текстовые поля."""
        for entry in self.file_paths:
            entry.delete(gs.FIRST_ELEMENT, tk.END)

    def open_settings(self):
        """Открывает окно настроек."""
        self.settings.create_window()
        self.get_save_path()

    def on_closing(self):
        """Обработчик закрытия окна."""
        self.stop_threads = True
        if self.helper.info_window:
            self.helper.info_window.destroy()
