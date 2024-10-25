import tkinter as tk
from tkinter import messagebox

def show_error(message: str):
    """Отображает всплывающее окно с сообщением об ошибке."""
    root = tk.Tk()
    root.withdraw()  # Скрыть основное окно
    messagebox.showerror("Ошибка", message)
    root.destroy()