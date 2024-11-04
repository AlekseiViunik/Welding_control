import tkinter as tk
from tkinter import messagebox

from settings.gui.windows import message_box as mb


class MessageBox:

    def __init__(self):
        pass

    def show_error(self, message: str):
        """Отображает всплывающее окно с сообщением об ошибке."""
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(mb.ERROR_MESSAGE_TITLE, message)
        root.destroy()

    def show_message(self, title, message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(
            title,
            message
        )
