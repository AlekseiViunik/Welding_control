import ctypes
import os
import sys
import tkinter as tk
from tkinter import PhotoImage

from gui.app_helper import AppHelper
from gui.weld_control_window import WeldControlWindow
from settings import gui_settings as gs


class App:
    def __init__(self, root):
        self.root = root
        self.helper = AppHelper(self.root)
        self.root.title(gs.MAIN_WINDOW_TITLE)
        self.root.geometry(f"{gs.WINDOW_WIDTH}x{gs.WINDOW_HEIGHT}")
        self.set_window_icon()
        self.helper.center_window(
            self.root,
            gs.WINDOW_WIDTH,
            gs.WINDOW_HEIGHT
        )

        # Создаем выпадающий список
        self.selected_option = tk.StringVar(value=gs.CHOSE_HINT)
        options = gs.CHOSE_START_OPTIONS.keys()
        self.dropdown = tk.OptionMenu(
            self.root,
            self.selected_option,
            *options
        )
        self.dropdown.pack(pady=20)
        self.start_button = tk.Button(
            self.root,
            text="Погнали",
            command=self.start_process
        )
        self.start_button.pack(pady=10)
        label = tk.Label(self.root, text=gs.AUTHOR_LABEL_TEXT)
        label.place(
            relx=gs.AUTHOR_RELX,
            rely=gs.AUTHOR_RELY,
            anchor=gs.AUTHOR_ANCHOR,
            y=-gs.AUTHOR_PADY
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
                gs.ICONS_FOLDER_NAME,
                gs.PNG_ICON_FILENAME
            )
            icon_path_ico = os.path.join(
                sys._MEIPASS,
                gs.ICONS_FOLDER_NAME,
                gs.ICO_ICON_FILENAME
            )
        else:
            # Если запущено из исходников
            icon_path_png = gs.PNG_ICON_FILEPATH
            icon_path_ico = gs.ICO_ICON_FILEPATH

        self.icon = PhotoImage(file=icon_path_png)
        self.root.iconphoto(True, self.icon)
        self.root.iconbitmap(icon_path_ico)

    def start_process(self):
        self.root.destroy()
        selected_option = gs.CHOSE_START_OPTIONS[self.selected_option.get()]
        if selected_option == '01':
            self.weld_cotrol = WeldControlWindow()
