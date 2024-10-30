import tkinter as tk
from tkinter import messagebox

from settings.gui_settings import ERROR_MESSAGE_TITLE


def show_error(message: str):
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
