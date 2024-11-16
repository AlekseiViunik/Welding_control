import ctypes
import logging
import os
import sys
import tkinter as tk
from threading import Thread
from tkinter import PhotoImage

from gui.settings_window import SettingsWindow
from gui.components.frames import BrowseFrame, ButtonsFrame
from gui.components.buttons import LangButton
from logic.get_xlsx import GetXlsx
from logic.settings_handler import SettingsHandler
from settings import settings as set

from .app_helper import AppHelper


class App:
    def __init__(self, root):
        self.root = root
        self.save_path = ''
        self.lang_code = ''
        self.lang_settings = {}
        self.helper = None
        self.settings = None
        self.main_frame = None
        self.lang_button = None
        self.settings_handler = SettingsHandler()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title(set.START_WINDOW_TITLE)
        self.root.geometry(f"{set.WINDOW_WIDTH}x{set.WINDOW_HEIGHT}")
        self.threads = []
        self.stop_threads = False

        self.set_window_icon()
        self.render_main_frame()

    def render_main_frame(self):
        """
        Renders main frame that includes:
            - "Browse" frames:
                textfield, describing label and "Browse" button;
            - "Buttons" frame:
                buttons "Go", "Cancel" and "Settings";
            - Language choice button
            - "Created by" label
        """
        if hasattr(self, 'main_frame') and self.main_frame:
            self.main_frame.destroy()
        settings = self.settings_handler.file_read()
        self.lang_settings = settings[set.DEFAULT_LANG_KEY]
        self.lang_code = self.lang_settings[set.DEFAULT_LANG_CODE_KEY]
        self.save_path = settings[set.DEFAULT_SAVE_PATH_KEY]

        self.settings = SettingsWindow(self.root, self.lang_code)
        self.helper = AppHelper(self.root, self.lang_code)

        self.helper.center_window(
            self.root,
            set.WINDOW_WIDTH,
            set.WINDOW_HEIGHT
        )

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.file_paths = []
        # frame = Frame(self.main_frame, self)
        browse_frame = BrowseFrame(self.main_frame, self)
        buttons_frame = ButtonsFrame(self.main_frame, self)

        self.lang_button = LangButton(
            self.main_frame,
            self.lang_settings,
            self
        )

        # Browse frame creation
        for label_text in set.labels[self.lang_code]:
            entry = browse_frame.create_frame(label_text)
            self.file_paths.append(entry)

        buttons_args = {
            set.go_button_name[self.lang_code]: [],
            set.clear_button_name[self.lang_code]: [],
            set.settings_button_name[self.lang_code]: []
        }

        # Buttons "Go", "Clear" and "Settings"
        buttons_frame.create_frame(
            set.start_buttons_name_to_process[self.lang_code],
            buttons_args
        )

        label = tk.Label(self.main_frame, text=set.AUTHOR_LABEL_TEXT,)
        label.place(
            relx=set.AUTHOR_RELX,
            rely=set.AUTHOR_RELY,
            anchor=tk.S,
            y=set.AUTHOR_PADY,
        )

        # Change lang button
        self.lang_button.create_lang_button()

    def start_process(self):
        """
        Starts thread for the logic process and shows an info window about
        the process start. Starts logging.
        """
        logging.info(set.LOG_DIVIDER)
        logging.info(set.log_start[self.lang_code])
        log_message = (
            set.log_chosen_files[self.lang_code].format(
                self.file_paths[0].get(),
                self.file_paths[1].get(),
                self.file_paths[2].get(),
                self.file_paths[3].get(),
                self.file_paths[4].get()
            )
        )
        logging.info(log_message)
        logging.info(f"{set.log_save_path_is[self.lang_code]}{self.save_path}")
        self.helper.show_info_window()

        logging.info(set.log_calculate_dates_call[self.lang_code])
        thread = Thread(target=self.calculate_dates)
        thread.daemon = True
        thread.start()
        self.threads.append(thread)

    def calculate_dates(self):
        """
        The method for the thread running.
        """
        if self.stop_threads:
            return

        vmc_paths = self.file_paths[0].get()
        rc_paths = self.file_paths[1].get()
        st_paths = self.file_paths[2].get()
        cd_paths = self.file_paths[3].get()
        hb_paths = self.file_paths[4].get()

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

        # Close info window when job is finished
        if self.helper.info_window:
            self.helper.info_window.destroy()

    def clear_entries(self):
        """Clears all textfields."""
        for entry in self.file_paths:
            entry.delete(set.FIRST_ELEMENT, tk.END)

    def open_settings(self):
        """Opens settings window."""
        self.settings.create_window()

    def set_window_icon(self):
        """Sets up the window icons"""
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            'Weld Control'
        )

        if getattr(sys, 'frozen', False):
            # If it run as an executable file
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
            # If it runs as a python app
            icon_path_png = set.PNG_ICON_FILEPATH
            icon_path_ico = set.ICO_ICON_FILEPATH

        self.icon = PhotoImage(file=icon_path_png)
        self.root.iconphoto(True, self.icon)
        self.root.iconbitmap(icon_path_ico)

    def on_closing(self):
        """Window closing handler."""
        self.stop_threads = True
        if self.helper.info_window:
            self.helper.info_window.destroy()
        self.root.quit()
