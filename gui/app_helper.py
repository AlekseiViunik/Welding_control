import tkinter as tk
from tkinter import filedialog

from settings.gui_settings import (
    FIRST_ELEMENT, PATH_DIVIDER, INFO_WINDOW_TITLE, INFO_WINDOW_WIDTH,
    INFO_WINDOW_HEIGHT, INFO_LABEL_TEXT, INFO_LABEL_PADX, INFO_LABEL_PADY,
)


class AppHelper:
    def __init__(self, root):
        self.root = root

    def center_window(self, window, width, height):
        """Центрирует главное окно на экране."""

        # Получаем размеры экрана
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Вычисляем координаты для центрирования окна
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        window_position = f"{width}x{height}+{x}+{y}"
        # Устанавливаем позицию окна
        window.geometry(window_position)

    def browse_file(self, entry):
        """Открывает диалог выбора файлов."""
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            entry.delete(FIRST_ELEMENT, tk.END)
            entry.insert(FIRST_ELEMENT, PATH_DIVIDER.join(file_paths))

    def show_info_window(self):
        """Показывает информационное окно о начале работы."""
        self.info_window = tk.Toplevel(self.root)
        self.info_window.title(INFO_WINDOW_TITLE)
        self.info_window.geometry(f"{INFO_WINDOW_WIDTH}x{INFO_WINDOW_HEIGHT}")
        self.center_window(
            self.info_window,
            INFO_WINDOW_WIDTH,
            INFO_WINDOW_HEIGHT
        )

        label = tk.Label(
            self.info_window,
            text=INFO_LABEL_TEXT,
            padx=INFO_LABEL_PADX,
            pady=INFO_LABEL_PADY
        )
        label.pack()
