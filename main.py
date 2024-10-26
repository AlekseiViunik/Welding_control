"""
Главный файл. С него начинается работа программы. Он по сути делает только
одно: запускает главный экран приложения. 
"""

import os
import sys

# Добавляем пути к папкам logic и gui
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'gui')))

# Импортируем приложение из gui
from gui.start_window import App

if __name__ == "__main__":
    import tkinter as tk
    
    root = tk.Tk()
    app = App(root)
    root.mainloop()