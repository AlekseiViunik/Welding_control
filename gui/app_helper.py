import tkinter as tk
from tkinter import filedialog

from settings.gui_settings import (
    FIRST_ELEMENT, PATH_DIVIDER, INFO_WINDOW_TITLE, INFO_WINDOW_WIDTH,
    INFO_WINDOW_HEIGHT, INFO_LABEL_TEXT, INFO_LABEL_PADX, INFO_LABEL_PADY,
    FRAME_BUTTON_LEFT_PADX, FRAME_BUTTON_RIGHT_PADX, FRAME_BUTTON_SIDE,
    FRAME_BUTTON_TEXT, FRAME_FILL_AXIS, FRAME_PADX, LABEL_ANCHOR, ENTRY_WIDTH,
    ENTRY_FRAME_SIDE, ENTRY_FILL_AXIS, ENTRY_EXPAND
)


class AppHelper:
    def __init__(self, root):
        self.root = root

    def center_window(self, window, width, height):
        """Центрирует окно на экране."""

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

    def create_label_entry_frame(self, parent, label_text, hint=''):
        """Создает фрейм с лейблом и текстовым полем."""
        frame = tk.Frame(parent)
        frame.pack(fill=FRAME_FILL_AXIS, padx=FRAME_PADX)

        label = tk.Label(frame, text=label_text)
        label.pack(anchor=LABEL_ANCHOR)

        entry = tk.Entry(
            frame,
            textvariable=hint,
            width=ENTRY_WIDTH
        )
        entry.pack(
            side=ENTRY_FRAME_SIDE,
            fill=ENTRY_FILL_AXIS,
            expand=ENTRY_EXPAND
        )

        button = tk.Button(
            frame,
            text=FRAME_BUTTON_TEXT,
            command=lambda e=entry: self.browse_file(e)
        )
        button.pack(
            side=FRAME_BUTTON_SIDE,
            padx=(FRAME_BUTTON_LEFT_PADX, FRAME_BUTTON_RIGHT_PADX)
        )

        return entry
