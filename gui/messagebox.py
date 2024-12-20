import tkinter as tk
from tkinter import messagebox

from settings import settings as set


class MessageBox:

    def __init__(self):
        pass

    def show_error(self, message: str, lang_code):
        """Creates a pop up error window."""
        root = tk.Tk()
        root.withdraw()
        title = set.error_message_title[lang_code]
        messagebox.showerror(title, message)
        root.destroy()

    def show_message(self, title, message):
        """Creates a pop up info window."""
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(
            title,
            message
        )
