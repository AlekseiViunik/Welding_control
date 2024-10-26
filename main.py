"""
Главный файл. С него начинается работа программы. Он по сути делает только
одно: запускает главный экран приложения.
"""
from gui.start_window import App

import os
import sys

# Добавляем пути к папкам logic и gui
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic'))
    )
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'gui'))
    )

if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    app = App(root)
    root.mainloop()
