import tkinter as tk
from tkinter import messagebox

from settings.gui_settings import ERROR_MESSAGE_TITLE


class MessageBox:

    def __init__(self):
        pass

    def show_error(self, message: str):
        """Отображает всплывающее окно с сообщением об ошибке."""
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(ERROR_MESSAGE_TITLE, message)
        root.destroy()

    def show_message(title, message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(
            title,
            message
        )
